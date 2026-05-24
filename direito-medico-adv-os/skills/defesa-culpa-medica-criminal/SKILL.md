---
name: defesa-culpa-medica-criminal
description: >
  Defesa criminal do profissional da saude em homicidio culposo (CP art. 121§3o), lesao corporal culposa (CP art. 129§6o) e modalidades correlatas. Aplica CPP art. 158-159 (pericia oficial IML x assistente tecnico), CPP art. 386 (especies de absolvicao com efeito cruzado civel/PED — CC art. 935 + PA-12), CP art. 18 II (culpa: negligencia, imprudencia, impericia), CP art. 13§2o (relevancia da omissao por garantidor). Vias defensivas: HC trancamento, absolvicao sumaria CPP art. 397, sursis processual Lei 9.099/95 art. 89 (pena minima ate 1 ano), transacao penal art. 76. Teses: ausencia de nexo, ausencia de previsibilidade, observancia da lex artis, erro escusavel, culpa exclusiva do paciente, fato de terceiro. Aciona: homicidio culposo medico, lesao culposa medica, parto distocico criminal, anestesia letal, erro cirurgico criminal, IML, assistente tecnico, sursis processual, HC trancamento, absolvicao sumaria, CP art. 121, CP art. 129, lex artis, dolo eventual medico, culpa consciente.
---

# DEFESA CRIMINAL — CULPA MEDICA

> Skill **Tier 3** — defesa criminal do profissional de saude em ilicito culposo. Implementa PA-02 (vedada promessa), PA-03 (sem opinar tecnica clinica), PA-08 (sem critica pessoal a perito), PA-12 (independencia relativa civel/penal/PED), PA-13 (citacao precisa). Acionada por `medico-master`, `triagem-medica` (esfera criminal) ou `timeline-multiesfera` (caso multi-frente).

---

## 0. Escopo e acionamento

Defesa do profissional indiciado/denunciado por **homicidio culposo (CP art. 121§3o)** ou **lesao corporal culposa (CP art. 129§6o)** em contexto de atendimento medico/odontologico/saude. Inclui modalidades: omissao impropria (CP art. 13§2o "a" — garantidor), parto distocico, anestesia letal, erro cirurgico, complicacao em UTI, atendimento de urgencia. Pre-requisito: Selo P1 + `analise-prontuario-medico` + `analise-pericia-medica`.

## 1. Posicao na orquestra

- **Chamada por:** `medico-master`, `triagem-medica` (esfera criminal), `timeline-multiesfera` (caso multi-frente com civel/PED).
- **Aciona:** `analise-pericia-medica` (quesitos ao IML e assistente tecnico), `analise-prontuario-medico` (defensa probatoria), `responsabilidade-civil-medica` (cruzamento P4), `defesa-ped-crm` (cruzamento P4), `revisao-final-medica`.
- **Entrega para:** resposta a acusacao (CPP art. 396-A), pedido de HC, alegacoes finais, recurso, peticao de sursis processual.

## 2. Marco normativo

| Norma | Conteudo |
|-------|----------|
| **CP 18 II** | Culpa — negligencia, imprudencia, impericia |
| **CP 121§3o** | Homicidio culposo — pena 1-3a |
| CP 121§4o / 129§7o | Aumento — inobservancia regra tecnica |
| **CP 129§6o** | Lesao culposa — pena 2m-1a |
| CP 13§2o "a" | Omissao impropria — garantidor |
| CP 20 / 21 / 23 III / 24 | Erro tipo/proibicao; estado de necessidade |
| **CPP 158-159** | Pericia IML + assistente tecnico defesa |
| CPP 396-A / 397 | Resposta acusacao 10d / absolvicao sumaria |
| **CPP 386 I-VII** | Especies de absolvicao — efeito civel/PED varia (PA-12) |
| Lei 9.099/95 76 / **89** | Transacao penal / sursis processual (chave) |

**Jurisprudencia paradigma:** STJ HC 421.604/RS (atipicidade ausencia previsibilidade); STJ AgRg AREsp 1.671.123 (trancamento por inepcia); STF HC 89.395 (descricao individualizada); STJ Sum. 105 (JE competente; JF so hospital federal).

## 3. Especies de culpa — anatomia

| Modalidade | Aplicacao medica |
|------------|------------------|
| **Negligencia** | Nao acompanhar pos-op; nao examinar; nao realizar exame indicado |
| **Imprudencia** | Iniciar sem condicoes; operar fora da especialidade; tecnica nao indicada |
| **Impericia** | Operar sem qualificacao; desconhecer literatura basica vigente |

**PA-03:** advogado **nao opina** sobre culpa tecnica — articula sobre prova pericial (laudo + assistente tecnico) e literatura medica vigente no ano do fato (PA-09).

## 4. Vias defensivas (cardapio)

- **HC trancamento (CF 5o LXVIII + Lei 13.869/19):** atipicidade evidente; inepcia (STF HC 89.395); ausencia de justa causa. Foro: TJ (originario) ou STJ (decisao TJ).
- **Resposta a acusacao (CPP 396-A) — 10d:** arrolar ate 8 testemunhas, juntar parecer de assistente tecnico, requerer diligencias, pedir absolvicao sumaria (art. 397).
- **Absolvicao sumaria (CPP 397):** I excludente ilicitude; II excludente culpabilidade (erro inevitavel); III atipicidade (sem previsibilidade); IV extincao punibilidade (prescricao).
- **Sursis processual (Lei 9.099/95 art. 89) — CORACAO em culposo:** pena minima ate 1 ano — CP 121§3o (min 1a) e CP 129§6o (min 2m) cabem. Suspensao 2-4a com condicoes (proibicao de exercer no local; comparecimento mensal; reparacao civel). Cumprida -> extincao punibilidade sem reincidencia.
- **Transacao penal (Lei 9.099/95 art. 76):** lesao culposa cabe ate limite de 2a. Sem reincidencia mas registra.

## 5. Teses tecnicas

| Tese | Fundamento | Acionar |
|------|-----------|---------|
| **Ausencia previsibilidade** | CP 18 II + risco permitido | Complicacao rara documentada |
| **Lex artis observada** | Codigo etica + diretrizes especialidade | Conduta conforme `[VERIFICAR diretriz]` |
| **Ausencia de nexo** | CP 13 + imputacao objetiva | Doenca de base; concorrencia de causas |
| **Erro escusavel** | CP 20/21 | Quadro clinico atipico |
| **Culpa exclusiva paciente** | Quebra do nexo | Descumprir TCLE; pos-op |
| **Fato de terceiro** | Quebra do nexo | Erro de outro profissional/instituicao |
| **Estado de necessidade** | CP 23 III + 24 | Urgencia sem alternativa |
| **Inepcia da denuncia** | CPP 41 + STF HC 89.395 | Acusacao generica |
| **Prescricao** | CP 109-110 | Pena prevista x marcos |

## 6. Cruzamento P4 — efeito da absolvicao na civel/PED (PA-12 + CC 935)

| CPP 386 | Civel | PED |
|---------|-------|-----|
| **I — inexistencia do fato** | Alcanca | Alcanca |
| II — atipicidade (nao crime) | NAO (cabe ilicito civel/etico) | NAO |
| **III — sem autoria** | Alcanca | Alcanca |
| IV — sem culpa | Alcanca parcial | Discutivel |
| **V / VII — insuficiencia prova** | NAO | NAO |
| VI — excludente | Conforme natureza | Idem |

**Estrategia:** buscar absolvicao por **386 I ou III** — alcanca civel/PED. **V ou VII nao protege.** Coordenar com `timeline-multiesfera`.

## 7. Quesitos para pericia (P2 + `analise-pericia-medica`)

Ao IML: (1) causas medicas do desfecho; (2) conduta obedeceu literatura vigente em [ano fato — PA-09]?; (3) conduta correta evitaria desfecho com certeza ou apenas probabilidade?; (4) outras causas concorrentes; (5) complicacao descrita como **risco inerente** na literatura? Assistente tecnico de defesa (CPP 159§3o): quesitos suplementares + parecer paralelo.

## 8. Esqueleto FIRAC — Resposta a acusacao (CPP 396-A)

```
RESPOSTA A ACUSACAO — CPP art. 396-A
EXMO. SR. JUIZ DE DIREITO DA ___ VARA CRIMINAL DE [Cidade/UF]

[ACUSADO], qualificacao, CRM/CRO [num/UF], representado por {{ADVOGADO_NOME}}
OAB/{{OAB_UF}} {{OAB_NUMERO}}, nos autos n. ___, oferece RESPOSTA A ACUSACAO

I — FATOS [F] — narrativa defensiva datada (referencia CASO.md)
II — ISSUE [I] — atipicidade por ausencia de [previsibilidade/nexo/culpa]?
III — DIREITO [R]
  III.1 Regime — CP art. 18 II (culpa exige negligencia/imprudencia/impericia
        + previsibilidade + nexo)
  III.2 Lex artis observada — conforme literatura/diretriz vigente em [ano fato — PA-09]
        `[VERIFICAR — diretriz especifica]`
  III.3 Ausencia de [previsibilidade/nexo] — laudo do assistente tecnico anexo
  III.4 Quebra do nexo — [doenca de base / culpa exclusiva paciente / fato terceiro]
  III.5 Cruzamento P4 — eventual absolvicao por art. 386 I/III alcanca civel/PED
IV — PEDIDOS [C]
  IV.1 Absolvicao sumaria (CPP art. 397 III — atipicidade)
  IV.2 Subsidiariamente: realizacao de pericia complementar (CPP art. 159§3o)
        com quesitos abaixo
  IV.3 Subsidiariamente: sursis processual (Lei 9.099/95 art. 89) com
        condicoes proporcionais
  IV.4 Arrolamento de [N] testemunhas (max 8 — CPP art. 401)

[Cidade, data] — {{ADVOGADO_NOME}} | OAB/{{OAB_UF}} {{OAB_NUMERO}}

RESSALVA (PA-05): minuta tecnica — revisao + responsabilidade do advogado OAB ativo.
```

## 9. Casos tipicos

- **Parto distocico:** acusacao por homicidio culposo neonatal/lesao por paralisia cerebral. Defesa: CTG normal ate X; cesarea indicada em Y conforme `[VERIFICAR FEBRASGO]`. Perda de chance e tese **civel**; criminal exige causa-efeito direta ou atipicidade.
- **Anestesia letal:** CP §4o/§7o (regra tecnica). Defesa: avaliacao pre-anestesica completa; TCLE; monitorizacao registrada; anafilaxia idiopatica `[VERIFICAR SBA]`.
- **Erro cirurgico (corpo estranho/lado errado):** corpo estranho geralmente e **culpa institucional** (contagem) — civel ao hospital; criminal so se houver conduta individualizavel.

## 10. Vedacoes especificas

- **PA-02** — sem promessa de absolvicao. "Probabilidade tecnica" + pontos de risco.
- **PA-03** — vedado opinar se a conduta foi tecnicamente correta — usar laudo + diretriz.
- **PA-08** — sem critica pessoal a perito IML. Impugnacao tecnica (CPP art. 159§4o).
- **PA-12** — articular cruzamento esferas com precisao — nao prometer transbordo.
- **PA-13** — citar CP/CPP com artigo/inciso/paragrafo; jurisprudencia STJ/STF com numero/turma/data.
- **PA-21** — em pedido de quantum civel reflexo, conservadorismo.

## 11. Protocolos acionados

- **P1** — Selo emitido (`validador-legislacao-vigente`).
- **P2** — `analise-prontuario-medico` + `analise-pericia-medica` + `analise-tcle`.
- **P3** — memoria de decisao da estrategia (HC x sursis x absolvicao).
- **P4** — `timeline-multiesfera` se ha civel/PED paralelos.
- **P5** — foro JE (Sum. 105 STJ); JF excepcional (hospital federal).
- **P6** — `revisao-final-medica` R1-R4.

## 12. Localizacao

JE da comarca do local do fato (CPP art. 70). Hospital federal (HFC, INTO, etc.) -> JF (CF art. 109 IV). Vara especializada onde houver. PED no CRM/CRO da UF de inscricao corre em paralelo (P4).

## 13. Integracao

**Chamada por:** `medico-master`, `triagem-medica` (esfera criminal), `timeline-multiesfera`.

**Entrega para:** peca criminal (resposta a acusacao / HC / alegacoes finais / pedido sursis) -> `revisao-final-medica` (R1-R4) -> operador.

**Sem esta skill:** defesa sem articulacao das vias (HC x sursis x absolvicao sumaria), sem cruzamento P4 (perde efeito cruzado da absolvicao por art. 386 I/III), com risco de tese frouxa criminal.
