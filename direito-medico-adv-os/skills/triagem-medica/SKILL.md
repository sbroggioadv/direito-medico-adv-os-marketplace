---
name: triagem-medica
description: >
  Porta de entrada de todo caso de direito medico — executa a triagem 4D (sujeito x modo x esfera x subdominio), grava o CASO.md compartimentado (PA-22 LGPD) e aciona o validador-legislacao-vigente para emitir o Selo. Roteia ao Tier correto (2 RC, 3 criminal, 4 PED, 5 plano, 6 consultivo, transversais). Identifica casos multi-frente (Protocolo 4 — civel + criminal + etico + regulatorio simultaneos). Captura foro/competencia (Protocolo 5) e datacao do fato gerador (PA-09). Aciona: novo caso, triagem, classificar caso, sujeito do caso, abrir caso, retomar caso, qual Tier, multi-frente, multi-esfera, fato gerador, foro competente, parto distocico, erro medico, negativa cobertura, PED, MS conselho.
---

# TRIAGEM MEDICA

> Skill **Tier 1** — porta de entrada. Pre-requisito de toda producao (Tier 2-6). Implementa PA-09 (datacao), PA-22 (compartimentacao), P4 (multi-esfera) e P5 (localizacao). Acionada por `medico-master` ou diretamente pelo operador.

---

## 0. Escopo e acionamento

Acionada por `/triagem`, `/caso-medico` (abertura), pelo `medico-master` em prompt do dominio, ou pelo operador: "novo caso", "triagem", "classificar caso", "abrir caso de erro medico". Executa a **triagem 4D** + datacao + localizacao + identificacao multi-frente + grava `CASO.md` na pasta compartimentada do caso + aciona `validador-legislacao-vigente` para emitir o Selo (P1) + roteia ao(s) Tier(s) aplicavel(eis).

## 1. Posicao na orquestra

- **Chamada por:** `medico-master`, `/triagem`, `/caso-medico`, qualquer demanda nova.
- **Aciona em seguida:** `validador-legislacao-vigente` (P1 — Selo), `analise-prontuario-medico` ou `analise-tcle` ou `analise-pericia-medica` (P2 — quando ha documento), `timeline-multiesfera` (P4 — quando 2+ esferas), `memoria-de-caso-medico` (gestao do CASO.md), skills do Tier de producao aplicavel.
- **Entrega para:** `CASO.md` em `<cwd>/direito-medico/casos/<slug>/`, lido por todas as skills.

## 2. As 4 dimensoes da triagem

| Dimensao | Valores | Implicacao tecnica |
|----------|---------|--------------------|
| **Sujeito** | profissional-PF (medico/dentista/enf/fisio) · clinica-PJ · hospital-PJ · paciente/beneficiario · operadora-PJ | Profissional PF -> CC art. 951 subjetiva; PJ -> CDC art. 14 objetiva (Sum. 469 STJ); paciente -> autor em Tier 2/5; operadora -> consultivo Tier 6 ou re em Tier 5 |
| **Modo** | consultivo · contencioso | Consultivo -> Tier 6 (sociedade, contrato, credenciamento, LGPD, publicidade); contencioso -> Tier 2-5 |
| **Esfera** | civel · criminal · etico-disciplinar (CRM/CRO) · regulatorio (ANS/ANVISA) | 1+ simultaneamente -> P4 Cruzamento (CC art. 935 + independencia relativa, PA-12) |
| **Subdominio** | medicina (CFM) · odontologia (CFO) · saude mental (Lei 10.216 + 13.840) · reproducao (Res. CFM 2.320/2022) · outros (COFEN 564/2017 · COFFITO 424/2013 · CFF) | Define normativa profissional + HOF interconselhos (Res. CFM 2.337/2023) |

## 3. Casos cruzados (P4 — exemplos canonicos)

**Caso A — Parto distocico com lesao neonatal:**
- Sujeito: hospital-PJ + obstetra-PF (litisconsorcio passivo)
- Modo: contencioso
- Esfera: civel (CC art. 951 + CDC art. 14) + criminal (lesao corporal culposa art. 129§6o CP ou homicidio culposo art. 121§3o CP) + PED CRM (Res. CFM 2.145/2016)
- Subdominio: medicina (obstetricia)
- **Tiers acionados:** 1 (analise-prontuario + analise-pericia) + 2 (responsabilidade-civil-medica + perda-de-uma-chance se atraso) + 3 (defesa-culpa-medica-criminal) + 4 (defesa-ped-crm) + transversal `timeline-multiesfera`

**Caso B — Negativa de cobertura oncologica off-label:**
- Sujeito: paciente vs operadora-PJ
- Modo: contencioso
- Esfera: civel (CDC + Lei 9.656/1998 + Lei 14.454/2022) + regulatorio (representacao a ANS)
- Subdominio: medicina (oncologia)
- **Tiers acionados:** 1 (analise-prontuario do laudo medico) + 5 (acao-negativa-cobertura-oncologica + tutela-urgencia-plano-saude) + Selo P1 obrigatorio

**Caso C — Defesa em PED por publicidade irregular:**
- Sujeito: medico-PF (denunciado no CRM)
- Modo: contencioso administrativo
- Esfera: etico-disciplinar (Res. CFM 2.336/2023 publicidade); risco de criminal por falsa pratica se houver promessa de cura
- Subdominio: medicina
- **Tiers acionados:** 1 (timeline) + 4 (defesa-ped-crm) + 6 (compliance-publicidade-medica como insumo de defesa)

**Caso D — Constituicao de sociedade medica + contrato de PJ medico:**
- Sujeito: clinica/sociedade em formacao
- Modo: consultivo
- Esfera: nenhuma contenciosa
- Subdominio: medicina
- **Tiers acionados:** 6 (constituicao-sociedade-medica + contrato-prestacao-medica) — sem P1 obrigatorio (consulta conceitual nao demanda Selo, mas peca contratual demanda — PA-04)

## 4. Datacao do fato gerador (PA-09)

Primeiro campo obrigatorio. Capturar:

- **Data do ato medico controvertido** (cirurgia, parto, atendimento PA, alta, prescricao, publicidade publicada).
- **Data do contrato** (negativa de cobertura -> data da negativa; reajuste -> mes/ano do reajuste; rescisao -> data da denuncia).
- **Data da ciencia inequivoca** do dano (princípio actio nata — Sum. 278 STJ) — gatilho da prescricao (PA-19).

Se nao informado, perguntar especificamente: "Qual a data exata do fato? (DD/MM/AAAA)". A data trava: legislacao aplicavel (PA-09 — redacao do ano do fato gerador), prazo prescricional (PA-19), jurisprudencia viva no ano (PA-10).

## 5. Localizacao do caso (Protocolo 5)

Capturar:

- **UF de atuacao do operador** (default da persona) — eixo do escritorio.
- **UF de inscricao do profissional-cliente** no CRM/CRO — pode ser DIFERENTE da UF do operador; eixo do PED e do estatuto regional aplicavel.
- **Comarca/UF do fato medico controvertido** — eixo do foro civel/criminal estadual (CDC art. 101 I; CPP art. 70).
- **Telemedicina interestadual** — quando medico em UF-A atende paciente em UF-B: domicilio do paciente prevalece em demanda consumerista (CDC art. 101 I).

Sinalizar foro/competencia esperada:

| Esfera | Foro | Norma |
|--------|------|-------|
| MS contra cassacao/suspensao CRM/CRO | Justica Federal | Sum. 105 STJ + CF art. 109 I |
| Civel erro medico (vs PF, clinica, hospital, operadora) | JE comarca do domicilio do autor | CDC art. 101 I; CPC |
| Criminal medico | JE comarca do lugar da infracao | CPP art. 70 |
| PED CRM | CRM da UF de inscricao | Res. CFM 2.145/2016 |
| PED CRO | CRO da UF de inscricao | Res. CFO 71/2006 |
| Recurso CFM/CFO | Federal (CFM/CFO sede DF) | Res. CFM 2.145/2016 art. ~70; Res. CFO |
| Regulatorio ANS | Federal | Lei 9.961/2000 |
| Regulatorio ANVISA | Federal | Lei 9.782/1999 |
| Vigilancia sanitaria municipal | JE comarca municipal (apos defesa administrativa) | legislacao local |

`[VERIFICAR — estatuto CRM-UF / norma local]` (PA-11) quando regra local nao confirmada.

## 6. Estrutura do CASO.md gravado (template canonico)

Em `<cwd>/direito-medico/casos/<slug>/CASO.md` (slug nao expoe nome do paciente — usar `<UF>-<ano>-<seq>` ou hash):

```markdown
# CASO — <slug>

## Dimensoes (triagem 4D)
- Sujeito: <profissional-PF | clinica-PJ | hospital-PJ | paciente | operadora-PJ>
- Modo: <consultivo | contencioso>
- Esfera(s): <civel | criminal | etico-disciplinar | regulatorio> (lista)
- Subdominio: <medicina | odontologia | saude mental | reproducao | outros>

## Datacao
- Data do fato gerador: <DD/MM/AAAA>
- Data da ciencia inequivoca do dano: <DD/MM/AAAA>  # actio nata, Sum. 278 STJ
- Prazo prescricional aplicavel: <3 anos CC art. 206 §3o V | 5 anos CDC art. 27> [PA-19]

## Localizacao
- UF do operador: <UF>
- UF de inscricao do profissional-cliente: <UF>
- Comarca/UF do fato: <Cidade/UF>
- Foro/competencia esperada: <JF | JE comarca X | administrativo CRM-UF>

## Selo de Validacao Legal Previa
- (preenchido pelo validador-legislacao-vigente apos triagem)

## Documentos do caso (arquivos/ — gitignored, PA-16)
- prontuario.pdf | tcle.pdf | laudo-pericial.pdf | contrato.pdf | denuncia-ped.pdf | ...

## Timeline multi-esfera (P4 — quando 2+ esferas)
| Esfera | Marco | Data | Prazo | Prejudicialidade |

## Estrategia priorizada
- Prioridade 1: <esfera>
- Justificativa: <CC art. 935 + aproveitamento cruzado>

## Memoria de quantum (quando aplicavel — P3)
| Item | Base legal | Valor | Atualizacao |

## Skills acionadas
- triagem-medica, validador-legislacao-vigente, ...

## Status
- Ultima atualizacao: <DD/MM/AAAA>
```

## 7. Fluxo de triagem (roteiro do operador)

1. **Receber a demanda** — descricao do caso em linguagem natural.
2. **Coletar 4D** — perguntar especificamente cada dimensao se nao for evidente.
3. **Datar** (PA-09) — perguntar data do fato gerador.
4. **Localizar** (P5) — perguntar UF do operador, UF de inscricao do cliente-medico, comarca do fato.
5. **Identificar multi-frente** (P4) — se 2+ esferas, marcar timeline e priorizar.
6. **Compartimentar** (PA-22) — definir slug do caso (sem expor nome de paciente).
7. **Gravar CASO.md** — template acima.
8. **Acionar validador-legislacao-vigente** — emitir Selo.
9. **Rotear** — Tier(s) aplicavel(eis) com base no 4D.

## 8. Vedacoes especificas

- **PA-22** — vedada mistura de clientes/casos no mesmo prompt. Cada caso em pasta propria.
- **PA-16** — vedado persistir prontuario, TCLE, exame ou dado clinico do paciente no `CASO.md`; apenas referencias.
- **PA-09** — sem data do fato gerador -> nao prosseguir. Pedir explicitamente.
- **PA-11** — regra local nao confirmada -> `[VERIFICAR — estatuto CRM-UF / norma municipal]`.
- **PA-20** — demanda fora do dominio medico -> "encaminhar a especialista da area aplicavel" (slot generico).

## 9. Protocolos acionados

- **P1** — aciona `validador-legislacao-vigente` para emitir Selo apos triagem.
- **P2** — se ha documento, aciona `analise-prontuario-medico` / `analise-tcle` / `analise-pericia-medica`.
- **P4** — se 2+ esferas, aciona `timeline-multiesfera`.
- **P5** — captura a localizacao.

## 10. Localizacao

Ja detalhada na secao 5. Triagem **e** o ponto de captura da localizacao por caso — pode sobrescrever a default da persona quando o profissional-cliente esta inscrito em outra UF ou o fato medico ocorreu em outra comarca.

## 11. Integracao

**Chamada por:** `medico-master`, `/triagem`, `/caso-medico`, qualquer demanda nova.

**Entrega para:** `CASO.md` em `<cwd>/direito-medico/casos/<slug>/`; `validador-legislacao-vigente` (em seguida); Tier 2-6 conforme roteamento. Entrega final passa por `revisao-final-medica` (R1-R4).

**Sem esta skill:** nenhum caso ganha estrutura — Tier 2-6 ficam sem 4D, sem Selo, sem localizacao. Pre-requisito de toda producao.
