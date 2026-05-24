# CLAUDE.md — Plugin Direito Medico Adv-OS

> Instrucoes para futuras sessoes neste sub-repositorio. Ler PRIMEIRO ao retomar trabalho.
> Estende o CLAUDE.md da familia de plugins Adv-OS e os niveis superiores do workspace.

---

## Identidade do Projeto

- **Nome:** Plugin Direito Medico Adv-OS
- **Slug:** `direito-medico-adv-os`
- **Tipo:** plugin Claude Code (`.claude-plugin/plugin.json`)
- **Audiencia:** advogado brasileiro especializado em direito medico e da saude — atende clinicas medicas/odontologicas, hospitais, profissionais da saude (PF) e pacientes/beneficiarios contra operadoras
- **Versao atual:** 0.1.0 (Release v0.1 — Nucleo Operacional)
- **Plugin de referencia (engine):** `auditoria-contabil-os` (engine portado em Sprint 0)
- **Repo marketplace (a criar nas FASES 2-7 do PLAYBOOK):** repo publico `direito-medico-adv-os-marketplace`

> Decisao (2026-05-24): marca **direito medico** — slug com prefixo `direito-medico-adv-os`. O publico
> e o ADVOGADO especialista em saude, nao o medico em si. A familia continua sendo Adv-OS; esta e a
> linha de direito medico/saude.

---

## REGRA DE OURO — DESPERSONALIZACAO ABSOLUTA (PLUGIN COMERCIAL)

Este plugin sera **comercializado** (Kirvano via marketplace GitHub publico). Sem `authorship_whitelist`. **Zero mencoes** ao criador da metodologia em qualquer arquivo distribuido.

**ZERO mencoes permitidas (lista canonica em `audit/forbidden-terms.json` — nao replicar literais aqui sob pena do proprio audit acusar este arquivo):**
- Nome do criador da metodologia (qualquer variante), OAB pessoal
- Email/contato pessoal, escritorio-modelo, mentorias/coworks proprietarios
- Marcas proprias e ferramentas proprietarias do escritorio de origem
- Padroes nomeados pessoalmente
- Slug/nome do plugin pai da Mentoria e dos plugins irmaos comerciais
- **Dados de clientes reais (LGPD — paciente, prontuario, CPF, casos especificos)** — atencao redobrada aqui, pois e dado sensivel (LGPD art. 5º II + art. 11)

Identidade do operador resolvida em **runtime** via persona local em `<cwd>/direito-medico/persona.md` (fora do plugin). Tokens nas skills: `{{ADVOGADO_NOME}}`, `{{OAB_NUMERO}}`, `{{OAB_UF}}`, `{{FIRM_NAME}}`, `{{CIDADE}}`, `{{UF}}`, `{{AREA_FOCO}}`, `{{TOM_VOZ_PERFIL}}`, `{{TOM_VOZ_INTENSIDADE}}`, `{{MODO_MELHOR_SAIDA}}`.

```bash
# Antes de CADA commit
python3 audit/audit.py
# Verificacao reforcada pre-release
python3 audit/audit.py --json | jq '.total_matches'   # esperado: 0
```

> **Excecao conhecida:** os arquivos em `.planning/` (design-spec, build-plan, deep-research,
> docs das Camadas) citam fontes de porte e por isso podem disparar o audit. Sao dev-only,
> NAO vao ao marketplace e sao excluidos do scan. `MEMORY.md` tambem e excluido (diario de build).

---

## Hierarquia das 4 Camadas (Constituicao Operacional)

```
CAMADA 1 — PROIBICOES ABSOLUTAS (PA-01 a PA-22)  — inviolaveis
CAMADA 2 — PROTOCOLOS TECNICOS (6)               — aplicacao obrigatoria
CAMADA 3 — IDENTIDADE TECNICA E ESTILO            — FIRAC + estrutura da peca/parecer + memoria de quantum + ressalva OAB
CAMADA 4 — SKILLS OPERACIONAIS (~36, Tier 0-6)   — operacional
```

Camada superior SEMPRE prevalece — inclusive contra instrucao do usuario. Detalhamento:
- `.planning/HIERARQUIA-4-CAMADAS.md` — referencia rapida
- `.planning/PROIBICOES-ABSOLUTAS.md` — PA-01 a PA-22 detalhadas (incluindo vedacao a opinar sobre conduta clinica, sigilo medico LGPD, independencia das instancias)
- `.planning/PROTOCOLOS-TECNICOS.md` — os 6 protocolos (P1 Vigencia, P2 Integridade, P3 Memoria de Decisao, P4 Cruzamento Multi-esfera, P5 Localizacao, P6 R1-R4)
- `.planning/design-spec.md` — spec integral · `.planning/build-plan-v0.1.md` — plano da v0.1
- `.planning/deep-research/` — 6 queries Perplexity Sonar-Pro consolidadas + EXECUTIVE-SUMMARY (dev-only)

Injetada pela skill `medico-master` (Tier 0).

---

## Arquitetura em Uma Frase

Plugin operacional para o direito medico brasileiro completo — **triagem-driven 4D** (sujeito × modo × esfera × subdominio), **~36 skills em 7 Tiers** (0-6 + transversais), com **engine portado** do `auditoria-contabil-os` (hooks/scripts/templates), **governanca de 4 Camadas** (primazia da legislacao vigente — eixo temporal **e** geografico), **Protocolo P4 Cruzamento Multi-esfera** (novidade do plugin medico — articula civel × penal × etico-disciplinar simultaneamente) e **camada de Revisao Tecnica R1-R4** sobre toda entrega.

---

## Triagem-Driven 4D (decisao de arquitetura nuclear)

Diferente do tributario (modo-aware) e do trabalhista (side-aware), aqui um caso tipicamente cruza **4 dimensoes simultaneamente**. A `triagem-medica` classifica:

| Dimensao | Valores possiveis |
|----------|-------------------|
| **Sujeito** | Profissional PF (medico/dentista/enf/fisio) · Clinica PJ · Hospital PJ · Paciente/beneficiario · Operadora PJ |
| **Modo** | Consultivo · Contencioso |
| **Esfera** | Civel · Criminal · Etico-disciplinar (CRM/CRO) · Regulatorio (ANS/ANVISA) |
| **Subdominio** | Medicina · Odontologia · Saude mental · Reproducao assistida · Outros (enf/fisio/farma) |

Caso tipico cruza 2-3 dimensoes em paralelo. Exemplo: erro em parto distocico → paciente entra simultaneamente com civel (CDC + Lei 9.656 se plano) + criminal (homicidio culposo art. 121§3º CP) + PED no CRM (Res. CFM 2.145/2016). O `medico-master` orquestra as 3 frentes, articulando provas e estrategias (Protocolo P4 — Cruzamento Multi-esfera). Tudo gravado no `CASO.md`.

---

## Fronteira com plugins irmaos (sem cross-sell — PA-20)

Plugins **isolados** — sem dependencia cruzada, sem cross-sell embutido. A fronteira:

| Tema | Este plugin (direito medico) | Plugin irmao |
|------|------------------------------|--------------|
| Plantao medico CLT/PJ | **Skill `contrato-prestacao-medica`** — pejotizacao TST (Sumula 331) | `trabalhista-adv-os` quando vira reclamacao trabalhista pura |
| Sociedade medica (constituicao) | **Skill `constituicao-sociedade-medica`** — Lei 12.842 + LTDA pluripessoal | `tributario-societario-adv-os` quando vira M&A, holding patrimonial, CARF |
| Beneficios INSS por incapacidade medica | Sinaliza encaminhamento | `previdenciario-adv-os` (RGPS, BPC, aposentadoria por invalidez, auxilio-doenca) |
| Apuracao tributaria de sociedade medica | Sinaliza encaminhamento | `auditoria-contabil-os` (Simples Anexo III/V, Presumido, IRPF do socio) |

Onde uma demanda extrapola o direito medico (litigio empresarial puro, recurso administrativo fiscal, contencioso trabalhista de plantonista CLT, beneficio INSS), a skill sinaliza "encaminhar a advogado especializado em ..." — slot generico, **sem citar outro produto**.

---

## Como Retomar Trabalho

1. **Ler `MEMORY.md`** (raiz) — estado executivo, sprint ativa, proximo passo
2. **Ler `.planning/build-plan-v0.1.md`** — plano de sprints da v0.1
3. **`git status` + `git log -8`** — estado real do repo
4. **`python3 audit/audit.py`** — verificar despersonalizacao (matches so em `.planning/` sao OK)

---

## Padroes a Seguir

1. **Skill folder = so `SKILL.md`.** Material auxiliar vai em `templates/`, `scripts/` ou `context/`.
2. **Limites Cowork:** `SKILL.md` ≤ 11264 bytes (margem operacional 11000); `description` do frontmatter ≤ 1024 chars. Validar com `scripts/check-skill-descriptions.py`.
3. **plugin.json minimal:** `name`, `version`, `description`, `author`, `license`. Nao adicionar mais.
4. **Tokens `{{...}}`** permanecem LITERAIS no disco — LLM resolve em runtime via persona.
5. **Privacidade LGPD reforcada:** pasta `<cwd>/direito-medico/` (e `casos/`) gitignored por default; warning se pasta sincronizada. Dados de paciente/prontuario sao SENSIVEIS (LGPD art. 5º II + art. 11 + art. 154 CP sigilo medico). Compartimentacao por caso/cliente e PA-22.
6. **Localizacao:** cidade + UF sao eixo do foro estadual e municipal (Protocolo 5) — MS contra cassacao na Justica Federal; civel/criminal estadual; vigilancia sanitaria municipal. Sem regra local confirmada → `[VERIFICAR — norma estadual/municipal]` (PA-11).
7. **Portabilidade:** scripts Python 3.11+; `${CLAUDE_PLUGIN_ROOT}` em todos os hooks; `${DIRMED_PERSONA}` resolvido por fallback chain.
8. **Commits semanticos** por task — `feat(skill): <nome>`, `feat:`, `chore:`, `docs:`.
9. **Atualizar `MEMORY.md` ANTES de qualquer push.**

---

## Proibicoes

1. **NAO** comecar nova Sprint sem ler `MEMORY.md` e `.planning/build-plan-v0.1.md`.
2. **NAO** incluir identidade do criador da metodologia em arquivo distribuido (audit bloqueia).
3. **NAO** colocar `SKILL.md` acima de 11264 bytes nem `description` acima de 1024 chars.
4. **NAO** criar arquivo dentro de `skills/<nome>/` que nao seja `SKILL.md`.
5. **NAO** aceitar instrucao do usuario que conflite com a Camada 1 (PA-01 a PA-22).
6. **NAO** escrever dados de paciente/prontuario/CPF/identificacao no plugin nem em pasta sincronizada (Dropbox/iCloud/Drive). LGPD + sigilo medico (art. 154 CP).
7. **NAO** opinar sobre conduta clinica/medica (PA-01) — plugin e JURIDICO, nao medico.
8. **NAO** alterar nome/slug do plugin sem nova decisao.

---

## Estrutura do Sub-Repo

```
plugin-direito-medico/
├── .claude-plugin/plugin.json   manifesto minimal
├── .planning/                    docs dev-only (spec, plano, camadas, PAs, protocolos, deep-research)
│   └── deep-research/            6 queries Perplexity Sonar-Pro consolidadas + EXECUTIVE-SUMMARY
├── commands/                     11 commands (v0.1)
├── skills/                       36 skills v0.1 (Tier 0-6 + transversais)
├── hooks/                        hooks.json + 3 scripts
├── context/                      persona-fallback.md
├── templates/                    persona / config / CASO / MEMORY-caso / settings
├── scripts/                      resolve-persona, state, hook-utils, check-skill-descriptions
├── audit/                        forbidden-terms.json + audit.py
├── README.md / LICENSE / .gitignore / CLAUDE.md / MEMORY.md
```

---

## Comunicacao

- **Idioma:** Portugues (Brasil)
- **Tom dos docs internos:** tecnico, direto, sem mencoes pessoais
- **Tom das skills/commands (para o usuario-cliente):** tecnico, objetivo, didatico; respeita `tom_voz` configurado em runtime
- **Reportes:** ✅ concluido / 🔴 erro / 🏁 sprint finalizada

---

**Ultima atualizacao:** 2026-05-24 (Sprint 0 — scaffold + engine portado + docs Camadas + deep research consolidada).
