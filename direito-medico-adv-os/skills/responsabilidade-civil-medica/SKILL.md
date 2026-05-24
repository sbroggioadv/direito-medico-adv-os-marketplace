---
name: responsabilidade-civil-medica
description: >
  Nucleo civel do plugin — responsabilidade civil em erro medico/odontologico. Distincao critica subjetiva x objetiva (PA-15): medico PF autonomo CC art. 951 (subjetiva — provar culpa) vs clinica/hospital/operadora PJ CDC art. 14 (objetiva — basta nexo+dano). Aplica STJ Sum. 469 (CDC em planos), Sum. 608 (coletivos), Sum. 597 (odonto), Sum. 387 (cumulacao moral+estetico), Sum. 326 (sucumbencia). Inversao do onus CDC art. 6o VIII / Sum. 469 STJ vs distribuicao dinamica CC art. 373 §1o. Memoria de quantum (CC arts. 948-950 + parametros STJ por especialidade) conservadora (PA-21). Aciona: erro medico, responsabilidade civil medica, indenizacao por dano medico, danos morais medicos, danos materiais medicos, pensao por morte medica, REsp 1.708.628, Sumula 469 STJ, CDC art. 14, CC art. 951, inversao do onus, peticao inicial erro medico, contestacao erro medico.
---

# RESPONSABILIDADE CIVIL MEDICA

> Skill **Tier 2** — nucleo civel. Implementa PA-04 (Selo), PA-13 (citacao precisa), PA-14 (inversao fundamentada), PA-15 (subjetiva x objetiva), PA-19 (prescricao), PA-21 (conservadorismo quantum). Acionada por `medico-master`, `triagem-medica` (esfera civel) ou `timeline-multiesfera` (caso multi-frente).

---

## 0. Escopo e acionamento

Acionada em demanda civel — peticao inicial do paciente, contestacao do medico/clinica/hospital/operadora, parecer consultivo sobre tese e quantum. Cobre erro medico em sentido amplo (diagnostico, conduta, procedimento, omissao, comunicacao falha). Pre-requisito: Selo P1 emitido + analise-prontuario-medico + analise-pericia-medica + analise-tcle (P2).

## 1. Posicao na orquestra

- **Chamada por:** `medico-master`, `triagem-medica` (esfera civel), `timeline-multiesfera` (caso multi-frente), `perda-de-uma-chance`, `cirurgia-estetica-resultado`, `responsabilidade-odontologica` (irmaos).
- **Aciona:** `prescricao-erro-medico` (conferir prazo), `estilo-entrega-medica` (FIRAC + ressalva), `revisao-final-medica` (R1-R4).
- **Entrega para:** peca civel (petic. inicial, contestacao, parecer) + memoria de quantum -> revisao final.

## 2. Marco normativo

| Norma | Conteudo |
|-------|----------|
| CC art. 186 / 187 / 927 | Ato ilicito, abuso, obrigacao de indenizar (caput + obj. por risco) |
| CC art. 932 III / 933 | Empregador/comitente; obj. independente de culpa |
| **CC art. 951** | **Medico PF — subjetiva (culpa)** |
| CC arts. 948, 949, 950 | Quantum: morte, lesao, pensionamento |
| **CDC art. 14** | **Obj. do prestador (clinica/hospital/operadora)** |
| CDC art. 14 §4o | Profissional liberal subjetiva |
| CDC art. 6o VIII / 27 | Inversao do onus / prescricao 5 anos |
| CPC art. 373 §1o | Distribuicao dinamica (regime CC) |

**Sumulas STJ:** 469 (CDC em planos); 597 (CDC nao em autogestao; carencia > 24h emergencia; odonto CDC); 608 (CDC em coletivos); 387 (cumulacao moral+estetico); 326 (sucumbencia — quantum inferior nao gera reciproca); 278 (actio nata — ciencia inequivoca); 54 (juros desde evento extracontratual); 362 (correcao do moral desde a fixacao).

**REsp paradigma:** 1.708.628/RS (hospital privado obj. + medico autonomo subj. — distincao); 1.526.466/RS (estetica = resultado); 1.291.247/RS (perda de chance); EREsp 1.385.732 (prescricao consumerista x CC).

## 3. Distincao subjetiva x objetiva (PA-15 — coracao da tese)

| Sujeito | Regime | Norma | Onus probatorio |
|---------|--------|-------|-----------------|
| Medico PF autonomo | **Subjetiva** | CC art. 951 + CDC art. 14 §4o | Autor prova: conduta + culpa (negligencia, imprudencia, impericia) + nexo + dano |
| Clinica/hospital PJ | **Objetiva** (relacao consumerista) | CDC art. 14 | Autor prova: nexo + dano. Re prova excludente (caso fortuito, culpa exclusiva do consumidor, fato de terceiro) |
| Operadora de plano | **Objetiva** | CDC art. 14 + Sum. 469 | Idem |
| Autogestao (Geap, Cassi, etc.) | NAO consumerista (Sum. 608) | CC art. 927 + 951 | Autor prova culpa |
| Hospital publico/SUS | Objetiva (CF art. 37 §6o — Estado) | CF art. 37 §6o | Idem objetiva |
| SUS — entes federados | Responsabilidade solidaria | STF RE 855.178 | Acao contra qualquer ente |

**Litisconsorcio passivo tipico:** paciente -> medico PF (subjetiva) + clinica/hospital PJ (objetiva). Estrategia: provar nexo + dano para PJ; provar culpa do medico tambem (efeito vinculativo ampliado).

## 4. Inversao do onus probatorio (PA-14)

| Regime | Base legal | Pressupostos |
|--------|-----------|--------------|
| **Inversao CDC** | CDC art. 6o VIII + Sum. 469 STJ | Relacao de consumo + verossimilhanca OU hipossuficiencia do consumidor |
| **Distribuicao dinamica CPC** | CPC art. 373 §1o | Caso concreto sem relacao consumerista — onus a quem melhor possa produzir (clinica vs paciente) |

**Aplicacao pratica:** medico PF autonomo em relacao **nao-consumerista** -> CC art. 373 §1o (distribuicao dinamica). Clinica/hospital/operadora -> inversao CDC art. 6o VIII. **Fundamentar sempre** — inversao automatica nao existe; depende de pedido fundamentado.

## 5. Memoria de quantum (P3 — toda peca com valor)

Tabela canonica (insumo de `estilo-entrega-medica`):

| Item | Base legal | Fundamentacao | Valor | Atualizacao |
|------|-----------|---------------|-------|-------------|
| **Dano material** — despesas medicas, exames, fisioterapia, medicamentos | CC art. 949 | Comprovantes em nota fiscal; recibo de profissional inscrito | R$ X | Selic acumulada desde o desembolso (Sum. 54 STJ) |
| **Lucros cessantes** | CC art. 402 + 950 | Comprovacao de renda + tempo afastamento | R$ X | Selic |
| **Pensao por morte** | CC art. 948 II + 950 | Dependentes (Sum. 491 STF — companheira; idade base 25-65 anos) | R$ X x prazo Y | Selic; revisao salarial |
| **Pensao por incapacidade** | CC art. 950 | Percentual de incapacidade x renda | Idem | Idem |
| **Dano moral** | CC art. 186 + 927 + parametros STJ por gravidade/especialidade | Conservador (PA-21); ancorado em Tema 1.094/1.095 STJ | R$ X (parametro) | Sum. 362 STJ (desde a fixacao) |
| **Dano estetico** | CC art. 949 + Sum. 387 STJ | Cumulavel com moral | R$ Y | Selic |
| **Perda de uma chance** | CC art. 186 + 927 + REsp 1.291.247 | Percentual sobre prejuizo total | % x R$ Z | Selic |
| **Honorarios sucumbenciais** | CPC art. 85 §§2o-3o | 10-20% sobre condenacao | — | — |
| **TOTAL pleiteado** | — | — | **R$ TOTAL** | — |

**Conservadorismo (PA-21):** parametros por especialidade — consultar jurisprudencia STJ atual `[VERIFICAR — Tema 1.094/1.095]`. Valor inflado prejudica credibilidade da peca e pode gerar honorarios menores.

## 6. Esqueleto FIRAC — Peticao inicial (template)

```
PETICAO INICIAL — Civel — Erro Medico
EXMO. SR. JUIZ DE DIREITO DA ___ VARA CIVEL DE [Cidade/UF]

[PACIENTE/ESPOLIO], qualificacao, por {{ADVOGADO_NOME}} — OAB/{{OAB_UF}}
{{OAB_NUMERO}}, propoe ACAO DE INDENIZACAO em face de
[MEDICO PF + CRM + CLINICA/HOSPITAL PJ + CNPJ — litisconsorcio passivo]

I — FATOS [F] — narrativa cronologica datada do evento (referencia CASO.md)
II — ISSUE [I] — houve erro do Re X (CC art. 951) e falha do Re Y (CDC art. 14)?
III — DIREITO [R]
  III.1 Regime (PA-15): Re Y objetiva CDC art. 14 + Sum. 469 STJ + REsp 1.708.628;
        Re X subjetiva CC art. 951 + CDC art. 14 §4o
  III.2 Inversao do onus (PA-14): Re Y -> CDC art. 6o VIII + Sum. 469;
        Re X -> CPC art. 373 §1o (distribuicao dinamica fundamentada)
  III.3 Conduta culposa do Re X — negligencia/imprudencia/impericia
        (posicao juridica, NAO clinica — PA-03; conduta tecnica e do perito)
  III.4 Nexo + dano — prontuario, laudo, sequela
  III.5 Quantum (P3 — tabela abaixo)
IV — PEDIDOS [C]
  IV.1 Tutela de urgencia (se aplicavel) — CPC art. 300
  IV.2 Inversao do onus — CDC art. 6o VIII / CPC art. 373 §1o
  IV.3 Citacao + pericia medica (quesitos em `analise-pericia-medica`)
  IV.4 Procedencia solidaria:
        - R$ ___ dano material (CC art. 949)
        - R$ ___ pensao (CC art. 948/950)
        - R$ ___ dano moral (CC art. 186 + 927)
        - R$ ___ dano estetico (CC art. 949 + Sum. 387 STJ)
        - Atualizacao Selic + correcao (Sum. 54 e 362 STJ)
        - Honorarios (CPC art. 85)
  IV.5 Valor da causa: R$ ___ (CPC art. 292)

[Cidade, data] — {{ADVOGADO_NOME}} | OAB/{{OAB_UF}} {{OAB_NUMERO}}

RESSALVA (PA-05): minuta — revisao + responsabilidade tecnica do advogado
OAB ativo. Selo em [data] — CASO.md.
```

## 7. Esqueleto FIRAC — Contestacao (defesa)

Inverte: identificar regime (subjetiva se medico PF — onus do autor; objetiva se PJ — apontar excludentes); demolir nexo causal (caso fortuito, evolucao natural da doenca, condicao pre-existente, culpa exclusiva do paciente — descumprimento de TCLE); impugnar inversao do onus; impugnar quantum por excesso (Tema 1.094/1.095 STJ); arguir prescricao (PA-19 — `prescricao-erro-medico`).

## 8. Vedacoes especificas

- **PA-02** — vedada promessa de procedencia/improcedencia. Probabilidade tecnica + pontos de risco.
- **PA-03** — nao opinar sobre conduta clinica tecnica — usar o laudo pericial.
- **PA-15** — subjetiva x objetiva separadas com precisao.
- **PA-14** — inversao do onus fundamentada com norma certa.
- **PA-19** — prazo prescricional conferido (3 anos CC x 5 anos CDC) — acionar `prescricao-erro-medico`.
- **PA-21** — quantum conservador (Tema 1.094/1.095 STJ).
- **PA-05** — ressalva OAB obrigatoria.

## 9. Protocolos acionados

- **P1** — Selo emitido por `validador-legislacao-vigente`.
- **P2** — `analise-prontuario-medico` + `analise-tcle` + `analise-pericia-medica`.
- **P3** — memoria de quantum em tabela.
- **P4** — `timeline-multiesfera` se caso cruza com penal/PED.
- **P6** — `revisao-final-medica` R1-R4 antes de devolver.

## 10. Localizacao

Foro: JE comarca do domicilio do autor (CDC art. 101 I) ou foro de eleicao/local do fato (CPC art. 53 III "d"). Telemedicina interestadual -> domicilio do paciente prevalece em demanda consumerista. SUS -> JE Fazenda Publica.

## 11. Integracao

**Chamada por:** `medico-master`, `triagem-medica` (esfera civel), `timeline-multiesfera`. Dependencia upstream: `validador-legislacao-vigente`, `analise-prontuario-medico`, `analise-tcle`, `analise-pericia-medica`, `prescricao-erro-medico`.

**Entrega para:** peca civel (petic. inicial / contestacao / parecer) + memoria de quantum -> `revisao-final-medica` (R1-R4) -> operador.

**Sem esta skill:** caso civel sem nucleo tecnico — confusao subjetiva/objetiva, inversao do onus mal fundamentada, quantum inflado, peca facilmente impugnavel.
