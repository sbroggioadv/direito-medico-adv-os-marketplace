---
name: omissao-de-socorro-medico
description: >
  Defesa criminal em omissao de socorro praticada por profissional da saude (CP art. 135) e omissao impropria (CP art. 13§2o "a" — medico como garantidor). Aplica Lei 9.099/95 art. 89 (sursis), CP art. 24 (estado de necessidade), recusa esclarecida do paciente (Lei 15.378/2026 + Res. CFM 1.995/2012 DAV), triagem hospitalar (Res. CFM 2.077/2014). Distincao critica: dolo eventual (omissao consciente do risco aceito) x culpa consciente (acredita evitar desfecho). Casos tipicos: nao atendimento em PA, transferencia indevida, abandono pos-op, recusa por inadimplencia. Teses: ausencia do dever de agir, justa causa, atendimento prestado por terceiro, recusa documentada do paciente, perigo concreto inexistente. Aciona: omissao de socorro medico, omissao impropria, CP 135, garantidor, dolo eventual medico, culpa consciente, recusa atendimento PA, transferencia hospitalar, triagem Manchester, abandono pos-op.
---

# OMISSAO DE SOCORRO MEDICO

> Skill **Tier 3** — defesa criminal em omissao de socorro/omissao impropria praticada por profissional de saude. Implementa PA-02, PA-03, PA-12 (cruzamento), PA-13, PA-18 (saude mental — lembrete MP 72h quando aplicavel). Acionada por `medico-master`, `triagem-medica` (esfera criminal), `timeline-multiesfera`.

---

## 0. Escopo e acionamento

Defesa em (a) omissao de socorro (CP art. 135) — crime comum mas com majorante quando resulta lesao grave/morte; (b) omissao impropria (CP art. 13§2o "a") — medico como **garantidor** do paciente sob seu cuidado, resultado tipico (homicidio/lesao). Inclui: nao-atendimento em PA, demora injustificada, transferencia indevida (defluxo de paciente instavel), recusa por inadimplencia, abandono pos-op, alta precoce. Pre-requisito: Selo P1 + `analise-prontuario-medico`.

## 1. Posicao na orquestra

- **Chamada por:** `medico-master`, `triagem-medica` (esfera criminal), `timeline-multiesfera`.
- **Aciona:** `analise-prontuario-medico` (registro de plantao/PA), `analise-pericia-medica` (causa do desfecho), `defesa-ped-crm` (cruzamento P4), `revisao-final-medica`.
- **Entrega para:** resposta a acusacao (CPP 396-A), HC trancamento, alegacoes finais.

## 2. Marco normativo

| Norma | Conteudo |
|-------|----------|
| **CP art. 135** | Omissao de socorro — pena 1-6m + majorante: lesao grave (1/2), morte (3x) |
| **CP art. 13§2o "a"** | Omissao impropria — garantidor responde pelo resultado |
| CP art. 13§2o "b/c" | Garantidor por contrato ou risco precedente |
| CP art. 18 I/II | Dolo (eventual) x culpa (consciente) — divisor critico |
| CP art. 23-25 | Excludentes — estado de necessidade, exercicio regular |
| **CPP 396-A / 397** | Resposta acusacao / absolvicao sumaria |
| **Lei 9.099/95 89** | Sursis processual — omissao simples cabe; omissao com majorante depende |
| Res. CFM 2.077/2014 | Triagem em PA — classificacao Manchester (5 niveis) |
| Res. CFM 1.995/2012 | Diretivas Antecipadas de Vontade |
| **Lei 15.378/2026** | Estatuto dos Direitos do Paciente — direito a recusa esclarecida `[VERIFICAR vigencia/regulamentacao]` |
| Res. CFM 1.480/97 / 1.805/06 | Morte encefalica / cuidados paliativos (ortotanásia) |
| CDC art. 39 | Vedacao a condicionar atendimento a pagamento em urgencia |
| Lei 12.842/2013 art. 5o III | Ato medico — atendimento de emergencia |

**Jurisprudencia:** STJ HC 489.012 (omissao impropria de medico plantonista — requer dever especifico); STJ AgRg AREsp 1.245.566 (recusa de atendimento PA + tipicidade do art. 135); STF HC 137.888 (dolo eventual em conducao temeraria — parametro de transposicao critica).

## 3. Dever de agir do medico — fonte da garantia

| Fonte do dever | Norma | Aplicacao |
|----------------|-------|-----------|
| **Plantao em PA** | Codigo etica + Res. CFM 2.077/2014 | Atendimento de emergencia obrigatorio (PA-03 — nao opinar conduta) |
| **Vinculo contratual** | CP 13§2o "b" | Medico assistente; convenio firmado; alta nao formalizada |
| **Risco precedente** | CP 13§2o "c" | Cirurgia previa do mesmo medico; iniciou procedimento e abandonou |
| **Triagem hospitalar** | Res. CFM 2.077 | Recusa em triar = omissao; classificacao errada = culpa |
| **Acolhimento** | CDC 39 + Lei 12.842 5o III | PA privado nao pode recusar emergencia por falta de pagamento |

**Sem dever de agir = atipicidade (CP 13§2o pressupoe garantidor).**

## 4. Distincao dolo eventual x culpa consciente

| Categoria | Conteudo subjetivo | Tipica acusacao |
|-----------|-------------------|----------------|
| **Dolo eventual (CP 18 I)** | Previu o resultado + **assumiu o risco** | "Recusou atender ciente da gravidade" -> homicidio doloso (art. 121) — pena severa |
| **Culpa consciente (CP 18 II)** | Previu o risco + **acreditou evitar** | Pena culposa (121§3o ou 129§6o) — sursis cabivel |
| **Omissao simples (CP 135)** | Nao prestou socorro a perigo evidente | Pena 1-6m + majorante |

**Tese defensiva chave:** desclassificar dolo eventual -> culpa consciente -> omissao art. 135 simples (pena muito menor + sursis). Argumentos: ausencia de representacao do resultado; confianca em terceiro (colega chamado); avaliacao tecnica equivocada de gravidade (PA-03 — usar laudo pericial).

## 5. Teses defensivas

| Tese | Fundamento | Acionar quando |
|------|-----------|----------------|
| **Ausencia do dever de agir** | CP 13§2o (sem garantia) | Medico fora de plantao; sem vinculo; passante |
| **Atendimento prestado por terceiro** | CP 135 caput in fine | Colega assumiu; equipe atendeu; SAMU acionado |
| **Recusa esclarecida do paciente** | Lei 15.378/2026 + Res. CFM 1.995 (DAV) + CC 15 + autonomia | Paciente consciente recusa intervencao — registro em prontuario |
| **Estado de necessidade** | CP 24 | Triagem em situacao de emergencia coletiva (TARM, MCI) — priorizar mais graves |
| **Justa causa / exercicio regular** | CP 23 III | Encaminhamento por incompetencia tecnica (especialista nao disponivel) — registro |
| **Atipicidade — perigo concreto inexistente** | CP 135 exige perigo iminente | Paciente estavel; classificacao Manchester nao-urgente |
| **Desclassificacao dolo eventual -> culposo** | Veja item 4 | Acusacao por homicidio doloso por omissao |
| **Excludente de culpabilidade — erro inevitavel** | CP 21 | Diagnostico medico equivocado de gravidade |
| **Atipicidade — terceiro foi quem omitiu** | Quebra do nexo | Triagem fez classificacao errada; nao chegou ao denunciado |

## 6. Quesitos para a pericia (P2)

1. Qual era o quadro clinico do paciente no momento [hora] e como a literatura medica vigente em [ano fato — PA-09] classificava sua gravidade?
2. O atendimento prestado conforme prontuario [anexo] foi adequado a classificacao apresentada?
3. Se ha demora, em qual momento ela ocorreu e quem era o responsavel pela continuidade do atendimento?
4. A piora do quadro era previsivel pelo medico denunciado naquele momento?
5. Houve registro de recusa do paciente a intervencao indicada? Foi documentada?

## 7. Esqueleto FIRAC — Resposta a acusacao por omissao

```
RESPOSTA A ACUSACAO — CPP 396-A
EXMO. SR. JUIZ DE DIREITO DA ___ VARA CRIMINAL DE [Cidade/UF]

[ACUSADO], CRM/CRO [num/UF], por {{ADVOGADO_NOME}} OAB/{{OAB_UF}} {{OAB_NUMERO}},
nos autos n. ___, oferece RESPOSTA A ACUSACAO

I — FATOS [F] — narrativa datada do plantao/atendimento (referencia CASO.md)
II — ISSUE [I] — havia dever de agir? havia perigo concreto? houve omissao?
III — DIREITO [R]
  III.1 Tipicidade — CP 135 exige perigo iminente
        + CP 13§2o exige garantidor (PA-13)
  III.2 [Ausencia do dever / atendimento por terceiro / recusa esclarecida /
        estado de necessidade] — fundamentar com norma + prova
  III.3 Desclassificacao — se acusacao for doloso, pedir desclassificacao
        para 135 ou para culposo (CP 121§3o / 129§6o)
  III.4 Cruzamento P4 — civel (`responsabilidade-civil-medica`) e PED
        (`defesa-ped-crm`) em paralelo
IV — PEDIDOS [C]
  IV.1 Absolvicao sumaria (CPP 397 III — atipicidade)
  IV.2 Subsidiariamente: desclassificacao + sursis processual (Lei 9.099/95 89)
  IV.3 Diligencias: pericia complementar com quesitos; oitiva da equipe de plantao
  IV.4 Arrolamento de [N] testemunhas (max 8)

[Cidade, data] — {{ADVOGADO_NOME}} | OAB/{{OAB_UF}} {{OAB_NUMERO}}

RESSALVA (PA-05).
```

## 8. Casos tipicos

- **Recusa por inadimplencia (PA privado):** CDC 39 + Res. CFM 2.077 — atendimento obrigatorio. Defesa do medico PF: decisao administrativa; transferencia obrigada. Responsabilidade vai a PJ.
- **Transferencia indevida (defluxo):** instavel transferido sem recurso. Defesa: falta de leito UTI/equipamento; protocolo seguido; receptor confirmou; SAMU/regulacao registrados.
- **Abandono pos-op:** Defesa: alta formalizada; transferencia a hospitalista/intensivista; acessibilidade demonstrada.
- **Fadiga/sobrecarga de plantao:** atenuante de dosimetria, nao excludente.

## 9. Cruzamento P4 (PA-12)

| Esfera | Tese |
|--------|------|
| **Civel (CDC 14 + CC 951)** | Responsabilidade objetiva do hospital/PA; subjetiva do medico PF |
| **Criminal (CP 135 ou omissao impropria)** | Defesa nuclear desta skill |
| **PED CRM (Res. CFM 2.145/2016)** | `defesa-ped-crm` — articulacao paralela |
| **Saude mental** | Se involuntaria — PA-18 — comunicar MP 72h |

Absolvicao por CPP 386 I/III alcanca civel/PED (PA-12).

## 10. Vedacoes especificas

- **PA-02** — sem promessa de absolvicao. Probabilidade tecnica.
- **PA-03** — vedado opinar se a conduta clinica do medico foi correta — usar protocolo + pericia.
- **PA-06** — sem orientacao clinica direta ao paciente (a defesa e do medico).
- **PA-08** — sem critica pessoal a perito ou colega.
- **PA-13** — CP/CPP + jurisprudencia com identificacao precisa.

## 11. Protocolos acionados

- **P1** — Selo emitido.
- **P2** — `analise-prontuario-medico` (registro do atendimento/triagem) + `analise-pericia-medica`.
- **P3** — memoria de decisao (HC x sursis x absolvicao).
- **P4** — `timeline-multiesfera` quando ha civel/PED.
- **P6** — `revisao-final-medica` R1-R4.

## 12. Localizacao

JE comarca do local do fato (CPP 70). PA hospitalar privado -> JE; PA SUS -> JE Fazenda Publica. Hospital federal -> JF (CF 109 IV).

## 13. Integracao

**Chamada por:** `medico-master`, `triagem-medica` (esfera criminal), `timeline-multiesfera`.

**Entrega para:** resposta a acusacao / HC / alegacoes finais / pedido de sursis -> `revisao-final-medica` -> operador.

**Sem esta skill:** defesa generica de omissao sem articular dever de agir, dolo eventual x culpa, recusa esclarecida do paciente — exposicao a desclassificacao desfavoravel e perda de sursis.
