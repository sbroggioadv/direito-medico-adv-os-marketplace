#!/usr/bin/env python3
"""
Hook UserPromptSubmit do plugin Direito Medico Adv-OS.

Logica (ativacao automatica por contexto):
1. Le o prompt via stdin (JSON padrao Claude Code hooks).
2. Detecta bypass explicito: flags `--no-revisao`, `--quick`, `--no-r1r4`, `/revisao off`.
3. Detecta GATILHO MEDICO via keywords (3 niveis):
   - Gatilho 1: prompt contem palavras do dominio do direito medico/saude
   - Gatilho 2: keywords fortes do dominio (erro medico, CRM, CRO, PED, prontuario,
     TCLE, plano de saude, ANS, ANVISA, telemedicina, pericia, etc.)
   - Gatilho 3: comandos `/start-medico`, `/medico-master`, etc.
4. Se gatilho dispara:
   - Verifica se `direito-medico/cowork-state.json` existe no path atual
   - SIM: injeta protocolo Revisao Tecnica R1-R4 + aponta para skill `medico-master`
   - NAO: sugere `/start-medico` ao usuario (mas nao bloqueia)
5. Se ha bypass: reafirma em stdout que o bypass foi aceito (transparencia).
6. Se nao eh tarefa juridico-medica: silencio (exit 0 sem output).

Tambem respeita state.json: se `revisao_tecnica.enabled = false`, nunca injeta R1-R4.

Stdlib only.
"""

from __future__ import annotations

import io
import json
import os
import re
import sys
from pathlib import Path

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

SCRIPT_DIR = Path(__file__).resolve().parent
PLUGIN_ROOT = SCRIPT_DIR.parent.parent
sys.path.insert(0, str(PLUGIN_ROOT / "scripts"))

import importlib.util
spec = importlib.util.spec_from_file_location("hook_utils", PLUGIN_ROOT / "scripts" / "hook-utils.py")
hook_utils = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hook_utils)


# Gatilho 1: palavras genericas do dominio do direito medico/saude (case insensitive)
TRIGGER_MEDICO = [
    r"\bdireito\s+medico\b",
    r"\bdireito\s+m[ée]dico\b",
    r"\bdireito\s+da\s+saude\b",
    r"\bdireito\s+da\s+sa[úu]de\b",
    r"\bdireito\s+odontol[óo]gico\b",
    r"\bdireito\s+hospitalar\b",
    r"\bsaude\s+suplementar\b",
    r"\bsa[úu]de\s+suplementar\b",
    r"\bresponsabilidade\s+m[ée]dica\b",
    r"\bresponsabilidade\s+civil\s+m[ée]dica\b",
    r"\berro\s+m[ée]dico\b",
    r"\berro\s+odontol[óo]gico\b",
    r"\bm[áa]\s+pr[áa]tica\b",
    r"\bm[áa]\s+pr[áa]xis\b",
]

# Gatilho 2: keywords fortes do dominio juridico-medico brasileiro
DOMAIN_KEYWORDS = [
    # Conselhos profissionais
    r"\bCRM\b", r"\bCRO\b", r"\bCFM\b", r"\bCFO\b",
    r"\bCOFEN\b", r"\bCOREN\b", r"\bCOFFITO\b", r"\bCREFITO\b", r"\bCFF\b",
    r"\bPED\b", r"\bprocesso\s+[ée]tico-disciplinar\b", r"\bprocesso\s+[ée]tico-profissional\b",
    r"\bcassa[çc][ãa]o\b", r"\bcensura\s+confidencial\b", r"\bcensura\s+p[úu]blica\b",
    r"\bsindic[âa]ncia\b", r"\bsuspens[ãa]o\s+preventiva\b",
    # Reguladores
    r"\bANS\b", r"\bANVISA\b", r"\bMinist[ée]rio\s+da\s+Sa[úu]de\b", r"\bMS\b",
    r"\bvigil[âa]ncia\s+sanit[áa]ria\b", r"\bCNES\b", r"\bSUS\b",
    # Documentos clinicos
    r"\bprontu[áa]rio\b", r"\bTCLE\b", r"\btermo\s+de\s+consentimento\b",
    r"\blaudo\s+m[ée]dico\b", r"\blaudo\s+pericial\b", r"\bpericia\s+m[ée]dica\b", r"\bper[íi]cia\s+m[ée]dica\b",
    r"\bIML\b", r"\bassistente\s+t[ée]cnico\b",
    r"\bPEP\b", r"\bprontu[áa]rio\s+eletr[ôo]nico\b",
    r"\batestado\s+m[ée]dico\b", r"\breceitu[áa]rio\b",
    # Planos de saude
    r"\bplano\s+de\s+sa[úu]de\b", r"\bopera[çc][ãa]o\s+de\s+plano\b",
    r"\boperadora\b", r"\bcoopera(?:tiva|do)\b",
    r"\bnegativa\s+de\s+cobertura\b", r"\bnegativa\s+de\s+pl[áa]stica\b",
    r"\bcredenciamento\b", r"\bdescredenciamento\b", r"\bglosa\b",
    r"\bcar[êe]ncia\b", r"\bpreexist[êe]ncia\b", r"\breembolso\b",
    r"\brol\s+da\s+ANS\b", r"\brol\s+exemplificativo\b", r"\brol\s+taxativo\b",
    r"\bhome\s+care\b", r"\bOPME\b", r"\b[óo]rteses\b", r"\bpr[óo]teses\b",
    r"\boncol[óo]gic[ao]\b", r"\boff-?label\b", r"\bquimioterapia\b",
    r"\bTEA\b", r"\bautismo\b", r"\bABA\b",
    r"\breajuste\s+abusivo\b", r"\brescis[ãa]o\s+unilateral\b",
    # Telemedicina e digital
    r"\btelemedicina\b", r"\bteleconsulta\b", r"\bteleorienta[çc][ãa]o\b",
    r"\btelediagn[óo]stico\b", r"\btelemonitoramento\b", r"\bteleinterconsulta\b",
    r"\bteleodontologia\b",
    r"\bprescri[çc][ãa]o\s+eletr[ôo]nica\b",
    # Especialidades e procedimentos
    r"\bobstetr[íi]cia\b", r"\bgineco-obstetr[íi]cia\b",
    r"\bcesariana\b", r"\bparto\s+dist[óo]cico\b", r"\bparalisia\s+neonatal\b",
    r"\bcirurgia\s+est[ée]tica\b", r"\bcirurgia\s+pl[áa]stica\b", r"\bharmoniza[çc][ãa]o\s+orofacial\b", r"\bHOF\b",
    r"\bimplantodontia\b", r"\bortodontia\b", r"\bendodontia\b", r"\bperiodontia\b",
    r"\bbotox\b", r"\bpreenchedor\b", r"\b[áa]cido\s+hialur[ôo]nico\b",
    r"\banestesia\b", r"\banafilaxia\b",
    # Esferas
    r"\bresponsabilidade\s+civil\b", r"\bdano\s+moral\s+m[ée]dico\b",
    r"\bdano\s+est[ée]tico\b", r"\bperda\s+de\s+uma\s+chance\b",
    r"\blex\s+artis\b",
    r"\bculpa\s+m[ée]dica\b", r"\bhomic[íi]dio\s+culposo\b",
    r"\blesao\s+corporal\s+culposa\b", r"\bles[ãa]o\s+culposa\b",
    r"\bomiss[ãa]o\s+de\s+socorro\b", r"\bsigilo\s+m[ée]dico\b",
    r"\bfalsidade\s+ideol[óo]gica\b",
    # Saude mental, reproducao, idoso, crianca
    r"\binterna[çc][ãa]o\s+involunt[áa]ria\b", r"\binterna[çc][ãa]o\s+compuls[óo]ria\b",
    r"\bsa[úu]de\s+mental\b", r"\bpsiqui[áa]tric[ao]\b",
    r"\breprodu[çc][ãa]o\s+assistida\b", r"\bbarriga\s+solid[áa]ria\b", r"\bFIV\b",
    r"\bdiretivas\s+antecipadas\b", r"\bDAV\b", r"\bcuidados\s+paliativos\b",
    # LGPD aplicada e publicidade
    r"\bLGPD\b", r"\bdados\s+sens[íi]veis\b", r"\bANPD\b",
    r"\bpublicidade\s+m[ée]dica\b", r"\bpublicidade\s+odontol[óo]gica\b",
    r"\bPROAD\b",
    # Sociedade medica / consultivo
    r"\bsociedade\s+m[ée]dica\b", r"\bsociedade\s+odontol[óo]gica\b",
    r"\bsociedade\s+uniprofissional\b",
    r"\bpejotiza[çc][ãa]o\b", r"\bplant[ãa]o\s+m[ée]dico\b",
    r"\bcontrato\s+de\s+credenciamento\b",
    # Legislacao chave
    r"\bLei\s+9\.656\b", r"\bLei\s+14\.454\b", r"\bLei\s+14\.510\b",
    r"\bLei\s+12\.842\b", r"\bLei\s+10\.216\b", r"\bLei\s+13\.146\b",
    r"\bLei\s+15\.378\b", r"\bResolu[çc][ãa]o\s+CFM\b", r"\bResolu[çc][ãa]o\s+CFO\b",
    r"\bTema\s+952\b", r"\bTema\s+990\b", r"\bTema\s+1\.?069\b", r"\bTema\s+1\.?082\b",
]

# Gatilho 3: commands prefixados do plugin
PLUGIN_COMMANDS = [
    "/start-medico",
    "/medico-master",
    "/caso-medico",
    "/triagem",
    "/civil",
    "/criminal",
    "/ped",
    "/plano-saude",
    "/consultivo",
    "/revisao-final",
    "/status-medico",
]

# Keywords gerais (fallback — protocolo cauteloso quando casa generico)
DIRMED_KEYWORDS_GENERAL = [
    r"\badvocacia\s+m[ée]dica\b",
    r"\bcl[íi]nica\s+m[ée]dica\b", r"\bhospital\b",
    r"\bm[ée]dico\b", r"\bdentista\b", r"\bcirurgi[ãa]o\b",
    r"\benfermeir[ao]\b", r"\bfisioterapeuta\b", r"\bfarmac[êe]utico\b",
    r"\bpaciente\b", r"\bbeneficiari[oa]\b",
]

BYPASS_TOKENS = [
    "--no-revisao",
    "--no-r1r4",
    "--quick",
    "/revisao off",
    "/revisao-off",
]


def _load_input() -> dict:
    raw = sys.stdin.read().strip()
    if not raw:
        return {}
    try:
        return json.loads(raw)
    except Exception:
        return {}


def _matches_any(text: str, patterns: list[str]) -> bool:
    for pat in patterns:
        if re.search(pat, text, re.IGNORECASE):
            return True
    return False


def _is_medico(prompt: str) -> bool:
    """Detecta se o prompt e do dominio juridico-medico (gatilhos 1, 2 ou 3)."""
    if _matches_any(prompt, TRIGGER_MEDICO):
        return True
    if _matches_any(prompt, DOMAIN_KEYWORDS):
        return True
    low = prompt.lower()
    for cmd in PLUGIN_COMMANDS:
        if cmd.lower() in low:
            return True
    return False


def _is_medico_general(prompt: str) -> bool:
    """Detecta tarefa juridico-medica em geral (sem keyword forte)."""
    return _matches_any(prompt, DIRMED_KEYWORDS_GENERAL)


def _has_bypass(prompt: str) -> str | None:
    low = prompt.lower()
    for token in BYPASS_TOKENS:
        if token in low:
            return token
    return None


def _has_medico_state(cowork: Path | None) -> bool:
    """Verifica se existe `direito-medico/cowork-state.json` no path."""
    if cowork is None:
        return False
    return (cowork / "direito-medico" / "cowork-state.json").exists()


def _revisao_tecnica_enabled(cowork: Path | None) -> bool:
    """Le state.json e verifica revisao_tecnica.enabled. Default true se ausente."""
    if cowork is None:
        return True
    sf = cowork / "direito-medico" / "cowork-state.json"
    if not sf.exists():
        return True
    try:
        state = json.loads(sf.read_text(encoding="utf-8"))
        return bool(state.get("revisao_tecnica", {}).get("enabled", True))
    except Exception:
        return True


def _resolve_cowork() -> Path | None:
    """Resolve COWORK root via env DIRMED_COWORK_PATH ou cwd ancestral."""
    env = os.environ.get("DIRMED_COWORK_PATH") or os.environ.get("COWORK_PATH")
    if env:
        p = Path(env)
        if (p / "direito-medico" / "cowork-state.json").exists():
            return p
    return hook_utils.find_cowork(Path.cwd())


def main() -> int:
    payload = _load_input()
    prompt = payload.get("prompt") or payload.get("user_prompt") or ""
    if not isinstance(prompt, str) or not prompt.strip():
        return 0

    cowork = _resolve_cowork()
    bypass = _has_bypass(prompt)

    is_medico = _is_medico(prompt)
    is_medico_other = _is_medico_general(prompt) and not is_medico

    # Caso 1: bypass explicito
    if bypass and (is_medico or is_medico_other):
        sys.stdout.write(
            f"[direito-medico-adv-os] Bypass detectado ({bypass}). "
            "Pecas, pareceres e estrategias serao entregues SEM a "
            "Revisao Tecnica R1-R4. Use por sua conta e risco.\n"
        )
        return 0

    # Caso 2: tarefa juridico-medica + plugin configurado
    if is_medico and _has_medico_state(cowork):
        if not _revisao_tecnica_enabled(cowork):
            sys.stdout.write(
                "[direito-medico-adv-os] Demanda juridico-medica detectada. "
                "Revisao Tecnica DESATIVADA na configuracao. Aciono apenas a cadeia de skills.\n"
                "Acionar skill: medico-master.\n"
            )
        else:
            sys.stdout.write(
                "[direito-medico-adv-os] Demanda juridico-medica detectada. Plugin ativado.\n"
                "\n"
                "PROTOCOLO AUTOMATICO:\n"
                "1. Acionar skill `medico-master` (Tier 0 - sempre ativa)\n"
                "2. Aplicar Hierarquia das 4 Camadas (1-Proibicoes, 2-Protocolos, 3-Estilo, 4-Skills)\n"
                "3. Verificar as 22 Proibicoes Absolutas (PA-01 a PA-22), com atencao especial:\n"
                "   - PA-01: vedacao a opinar sobre conduta clinica (plugin e JURIDICO, nao medico)\n"
                "   - PA-04: Selo de Validacao Legal Previa antes de qualquer estrategia (P1)\n"
                "   - PA-03: datar parecer/peca pelo ano do fato gerador (norma vigente a epoca)\n"
                "   - PA-09: dados de paciente/prontuario NUNCA no plugin (LGPD; pasta caso local)\n"
                "   - PA-10: sigilo medico oponivel (art. 154 CP + Res. CFM 1.821/2007)\n"
                "   - PA-12: independencia relativa das instancias (civel != penal != etico)\n"
                "   - PA-14: subjetiva (medico) vs objetiva (clinica/hospital) - nao confundir\n"
                "   - PA-15: obrigacao de meio vs resultado (estetica, odonto) - separar com precisao\n"
                "   - PA-07: a saida e rascunho operacional - responsabilidade tecnica do advogado (OAB)\n"
                "4. Acionar os 6 Protocolos da Camada 2 conforme demanda\n"
                "   (P1 Vigencia, P2 Integridade, P3 Memoria de Decisao, P4 Cruzamento Multi-esfera,\n"
                "    P5 Localizacao, P6 Revisao R1-R4)\n"
                "5. Antes de entregar: Revisao Tecnica R1->R2->R3->R4 (skill `revisao-final-medica`)\n"
                "\n"
                "Bypass disponivel: `--no-revisao`, `--quick`, `/revisao off`.\n"
            )
        return 0

    # Caso 3: tarefa juridico-medica mas plugin NAO configurado
    if is_medico and not _has_medico_state(cowork):
        sys.stdout.write(
            "[direito-medico-adv-os] Detectei demanda juridico-medica, mas o plugin "
            "ainda nao foi configurado neste diretorio.\n"
            "\n"
            "RECOMENDACAO: rode /start-medico para configurar (~5 min).\n"
            "Vou criar uma pasta `direito-medico/` aqui com a identidade do "
            "advogado/escritorio, OAB, cidade/UF, area de foco (defesa profissional / plano de saude / consultivo / todos), "
            "tom de voz e configuracao das skills.\n"
            "\n"
            "Caso queira prosseguir SEM configurar, trabalho em modo fallback generico "
            "(persona neutra, qualidade reduzida). Apenas avise.\n"
        )
        return 0

    # Caso 4: tarefa juridico-medica geral - protocolo cauteloso
    if is_medico_other:
        sys.stdout.write(
            "[direito-medico-adv-os] Tarefa juridico-medica detectada (sem frente especifica). "
            "Aplique protocolo padrao:\n"
            "1. Questionamento previo (sem suposicoes silenciosas - exigir dado real do caso).\n"
            "2. Apresentar estrutura + premissas antes de redigir peca/parecer.\n"
            "3. Aguardar confirmacao do advogado-operador.\n"
            "4. Antes de entregar: executar Revisao Tecnica R1-R4 se aplicavel.\n"
            "Bypass: `--no-revisao`, `--quick`, `/revisao off`.\n"
        )
        return 0

    # Caso default: nao e tarefa juridico-medica - silencio
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
