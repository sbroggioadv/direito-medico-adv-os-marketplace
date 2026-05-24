---
name: onboarding-medico
description: >
  Wizard de configuracao inicial do plugin no ambiente do escritorio de advocacia medica. Coleta identidade do advogado (nome, OAB e UF), escritorio, cidade e UF de atuacao (eixo critico — Protocolo 5: CRM/CRO regional, foro estadual, JF para MS contra conselho), AREA_FOCO (defesa-profissional / plano-saude / consultivo / todos), frentes ativas, tom de voz e modo de melhor saida. Grava persona local em `<cwd>/direito-medico/persona.md` (fora do plugin distribuido). LGPD reforcada — alerta agressivo se pasta sincronizada (dados de paciente sao sensiveis, LGPD art. 11 + art. 154 CP). Aciona: configurar plugin, primeira vez, /start-medico, onboarding, instalar, comecar a usar, configurar escritorio, persona.
---

# ONBOARDING MEDICO

> Wizard de configuracao inicial **Tier 0**. Linguagem acolhedora, tom didatico. Conduz o operador a configurar o plugin ao perfil do escritorio de direito medico — com atencao especial a **localizacao** (cidade + UF — eixo do Protocolo 5), a **AREA_FOCO** (define prioridade de roteamento) e ao alerta LGPD agressivo (prontuario e dado sensivel — PA-16, PA-22).

---

## 0. Escopo e acionamento

Acionada por `/start-medico` ou quando o operador disser "configurar plugin", "primeira vez", "onboarding", "instalar", "configurar escritorio". Cria a pasta `direito-medico/` no diretorio de trabalho com identidade, localizacao, AREA_FOCO, frentes, tom e modo de melhor saida.

## 1. Posicao na orquestra

- **Chamada por:** `/start-medico` ou intencao de configuracao.
- **Entrega para:** os arquivos de runtime em `<cwd>/direito-medico/` — lidos por `medico-master`, `validador-legislacao-vigente`, `triagem-medica` e todas as demais skills via hook SessionStart.
- Roda uma vez na instalacao; idempotente nas execucoes seguintes.

## 2. Regras do wizard

1. Portugues (Brasil), tom acolhedor e direto.
2. Uma pergunta por vez para campos criticos; agrupar relacionados quando fizer sentido.
3. Defaults inteligentes — o operador aceita com Enter.
4. Validar em tempo real (OAB numerico/com pontos, UF com 2 letras maiusculas, email valido).
5. Confirmar antes de gravar (resumo + "confirma? s/n").
6. **Idempotencia** — se ja existe `direito-medico/cowork-state.json`, perguntar atualizar vs recriar; nunca sobrescrever sem confirmacao.
7. **Privacidade LGPD reforcada (PA-16, PA-22)** — NUNCA pedir nome de paciente, CPF/RG, prontuario, exame, foto clinica. NUNCA armazenar dados clinicos no estado.
8. A **localizacao** (cidade + UF) e campo critico — explicar por que importa (Protocolo 5: foro federal/estadual/administrativo CRM-UF/CRO-UF).
9. **AREA_FOCO** define prioridade de roteamento pelo `medico-master` — explicar com clareza.

## 3. Fluxo do wizard

### Bloco 0 — Abertura
> "Ola! Sou o assistente do **Plugin Direito Medico Adv-OS**. Vou te guiar na configuracao (~5 min). Ao final, as 36 skills estarao adaptadas ao seu escritorio (defesa profissional + acoes contra plano + consultivo + compliance). Pronto para comecar?"

### Bloco 1 — Diretorio (LGPD reforcada)
Detectar cwd. Mostrar:
> "Vou criar `direito-medico/` em `<cwd>`.
>
> **ALERTA LGPD (PA-16, PA-22):** plugin opera prontuario/TCLE/laudo — dados sensiveis (LGPD art. 11 + art. 154 CP). Pasta dentro de iCloud/OneDrive/Dropbox/Drive sincroniza dados clinicos para a nuvem = incidente LGPD com responsabilidade solidaria. Recomendo caminho local (ex.: `~/Dev/direito-medico/`). Confirma?"

Pasta sincronizada -> alertar 2x; so prosseguir com "confirmo o risco LGPD" expresso.

### Bloco 2 — Identidade do advogado
> "Sua identidade:
> 1. Nome completo do advogado responsavel? 2. Numero da OAB? 3. UF da OAB?
> 4. Nome do escritorio? 5. Email institucional (opcional)? 6. Telefone (opcional)?"

Validar OAB (digitos/pontos), UF (2 letras maiusculas), email. **OAB ativa sustenta responsabilidade tecnica (PA-05).**

### Bloco 3 — Localizacao (eixo do Protocolo 5)
> "Localizacao do escritorio: 1. Cidade-sede? 2. UF de atuacao predominante?
>
> Por que importa (P5): MS contra cassacao/suspensao -> JF (Sum. 105 STJ + CF art. 109 I); civel/criminal -> JE comarca (CDC art. 101 I; CPP art. 70); PED CRM/CRO -> Conselho da UF de inscricao do medico-cliente (Res. CFM 2.145/2016, Res. CFO 71/2006); vigilancia sanitaria -> municipal/estadual.
>
> `triagem-medica` confirma a localizacao por caso (UF de inscricao do cliente pode diferir)."

Gravar `cidade` e `uf`.

### Bloco 4 — AREA_FOCO (prioridade de roteamento)
> "Area predominante (define priorizacao do `medico-master`):
> 1. **defesa-profissional** — defesa medico/dentista (civel + criminal + PED). Tier 2-4. Ticket alto.
> 2. **plano-saude** — acoes do paciente vs operadora. Tier 5. Varejo, alto volume.
> 3. **consultivo** — clinica/sociedade/hospital. Tier 6.
> 4. **todos** *(default)* — 4 frentes.
>
> Toda demanda passa pela triagem 4D — `area_foco` so prioriza."

### Bloco 5 — Frentes ativas
> "Frentes atendidas (multi-select ou `todas`): defesa-profissional, responsabilidade-civil, criminal-medico, ped-conselho, acoes-plano-saude, consultivo-clinica, regulatorio-saude, saude-mental (v0.2), reproducao-assistida (v0.2)."

### Bloco 6 — Subdominios
> "Subdominios (multi-select ou `todos`): medicina (CFM); odontologia (CFO — HOF, Sum. 597 STJ, Res. CFO 196/2019); saude-mental (Lei 10.216 + Lei 13.840 — v0.2); reproducao-assistida (Res. CFM 2.320/2022 — v0.2); outros (COFEN/COFFITO/farmacia)."

### Bloco 7 — Tom de voz
> "Perfil: 1. **tecnico-objetivo** *(default)* — direto; 2. **tecnico-didatico** — explicativo; 3. **tecnico-cordial** — formal.
>
> Intensidade combativa 0-10 *(default 4)*: 0-3 didatico-cordial; 4-6 tecnico-direto; 7-10 maximo combativo (PA-08 sempre — sem critica pessoal)."

### Bloco 8 — Modo de melhor saida
> "Em comparacao de teses/estrategias: 1. **recomendar-e-listar** *(default)* — recomenda + lista alternativas; 2. **apenas-listar** — opcoes sem recomendar. Em ambos, saida e rascunho com ressalva OAB (PA-05). Vedada promessa de resultado (PA-02)."

### Bloco 9 — Revisao Tecnica R1-R4
> "**Revisao R1-R4** (P6) — auditoria de 4 rodadas (escopo/dados, tecnica juridica, conformidade + cruzamento P4, entrega/clareza) antes da entrega. Manter ATIVA? *(default s)*. Bypass: `--no-revisao` / `--quick` / `/revisao off`."

### Bloco 10 — Ferramentas (opcional)
> "Ferramentas (pode pular): sistema juridico de prazos/andamentos; plataforma de peticionamento (PJe/eproc/Projudi); CRM/leads; email/banco/PSP; assinatura digital; PEP/telemedicina do cliente medico."

### Bloco 11 — Geracao dos arquivos
Apresentar o resumo da configuracao e pedir "confirma? (s/n)". Confirmado, gerar:

1. **`direito-medico/cowork-state.json`** — via `python3 scripts/state.py init <cwd>` + `set` por campo (incluindo `advogado_nome`, `oab_numero`, `oab_uf`, `cidade`, `uf`, `area_foco`).
2. **`direito-medico/persona.md`** — de `templates/persona.md.tpl`, resolvendo tokens `{{ADVOGADO_NOME}}`, `{{OAB_NUMERO}}`, `{{OAB_UF}}`, `{{FIRM_NAME}}`, `{{CIDADE}}`, `{{UF}}`, `{{AREA_FOCO}}`, `{{TOM_VOZ_PERFIL}}`, `{{TOM_VOZ_INTENSIDADE}}`, `{{MODO_MELHOR_SAIDA}}`.
3. **`direito-medico/config.md`** — de `templates/config.md.tpl` (localizacao, AREA_FOCO, frentes, subdominios, tom, modo, ferramentas).
4. **`direito-medico/casos/`** — pasta gitignored onde cada caso/cliente sera compartimentado (PA-22 + LGPD).
5. **`.claude/settings.local.json`** — apontando `DIRMED_PERSONA`, `DIRMED_COWORK_PATH`, `DIRMED_STATE_FILE`.

### Bloco 12 — Encerramento
```
Plugin Direito Medico Adv-OS configurado.

Advogado: <nome> — OAB/<UF> <numero>
Escritorio: <firma>
Localizacao: <cidade>/<UF>   (eixo do Protocolo 5)
Area de foco: <area_foco>
Frentes ativas: <lista>
Subdominios: <lista>
Tom: <perfil> (intensidade <X>/10)
Modo de melhor saida: <recomendar-e-listar | apenas-listar>
Revisao Tecnica R1-R4: <ATIVA | DESATIVADA>

PROXIMOS PASSOS:
1. Reinicie a sessao (hook SessionStart injeta a sua persona)
2. Use /medico-master para ativar a cadeia completa
3. Use /caso-medico para abrir o primeiro caso (compartimentado por LGPD)
4. Ou faca uma pergunta de direito medico — o plugin desperta via hook
5. /status-medico para diagnostico do ambiente
```

## 4. Fluxo alternativo — state ja existente (idempotencia)

Se `direito-medico/cowork-state.json` ja existir:
> "Detectei configuracao existente. Advogado: <nome>. Localizacao: <cidade/UF>. AREA_FOCO: <area>. O que deseja?
> (a) Continuar usando — nada muda
> (b) Atualizar — refaco blocos especificos
> (c) Recriar do zero — **apaga configuracao atual** (os casos em `casos/` sao preservados)"

Se (c): confirmar duas vezes antes de prosseguir. **Casos existentes NUNCA sao apagados** (LGPD + EAOAB art. 34 IV).

## 5. Vedacoes especificas

- **PA-16 + PA-22** — NUNCA coletar nome/CPF/RG de paciente, prontuario, exame, dado clinico. So coletar identidade do advogado-operador.
- **PA-05** — OAB ativa e pre-requisito de toda entrega; sem OAB, plugin opera em modo limitado e avisa.
- LGPD reforcada — alerta agressivo em pasta sincronizada; confirmacao expressa por escrito.
- Nunca sobrescrever `cowork-state.json` existente sem dupla confirmacao.
- Tokens `{{...}}` permanecem literais no disco — LLM resolve em runtime via persona.
- Cidade + UF sao obrigatorios — sem eles, foro/competencia ficam sem eixo (PA-11 -> `[VERIFICAR — norma local]` em toda peca).

## 6. Protocolos acionados

- **P5 — Localizacao** — Bloco 3 captura cidade + UF (eixo do roteamento de foro).
- Nao executa P1-P4 nem P6 (skill de configuracao, nao de producao).

## 7. Localizacao

Esta skill **estabelece** a localizacao padrao do escritorio (cidade + UF), gravada na persona e no state. Ponto de origem do Protocolo 5: `validador-legislacao-vigente` sabe qual estatuto CRM/CRO regional consultar; `triagem-medica` confirma ou sobrescreve por caso (UF de inscricao do medico-cliente pode ser distinta).

## 8. Integracao

**Chamada por:** `/start-medico` ou intencao de configuracao inicial.

**Entrega para:** os arquivos de runtime em `<cwd>/direito-medico/` (`persona.md`, `config.md`, `cowork-state.json`, `casos/`) e `.claude/settings.local.json`. Lidos por todas as skills via hook SessionStart.

**Checklist final:**
- [ ] `direito-medico/cowork-state.json` valido no schema, com `cidade`, `uf`, `oab_numero`, `oab_uf`, `area_foco` preenchidos
- [ ] `direito-medico/persona.md` com tokens resolvidos
- [ ] `direito-medico/config.md` com localizacao, AREA_FOCO, frentes, subdominios, tom, modo
- [ ] `direito-medico/casos/` criada e gitignored
- [ ] `.claude/settings.local.json` com `DIRMED_PERSONA` e `DIRMED_COWORK_PATH`
