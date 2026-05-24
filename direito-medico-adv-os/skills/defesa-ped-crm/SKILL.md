---
name: defesa-ped-crm
description: >
  Defesa em Processo Etico-Profissional/Disciplinar (PED) no Conselho Regional de Medicina (CRM) — Res. CFM 2.145/2016 (Codigo de Processo Etico) + CEM 2.217/2018 (Codigo Etica Medica). Cobre fluxo completo: sindicancia -> defesa previa (15 dias) -> instrucao -> alegacoes finais -> julgamento 1a instancia CRM -> recurso voluntario ao CFM (30 dias) -> pedido de revisao. Penas: advertencia confidencial -> censura confidencial -> censura publica -> suspensao 30d -> cassacao do exercicio. Prescricao 5 anos (Res. CFM 2.145 art. 32) — interruptivos especificos. Articula independencia relativa civel/penal/etico (CC 935 + PA-12). Teses: vicio processual (nulidade), cerceamento de defesa, ausencia de tipicidade etica especifica, ausencia de provas, prescricao, desproporcionalidade da sancao. Aciona: PED CRM, defesa etica medica, processo etico-disciplinar, Res. CFM 2.145, CEM, codigo etica medica, sindicancia CRM, recurso CFM, cassacao CRM, suspensao etica, censura medica, Camara Sindicancia.
---

# DEFESA EM PED CRM

> Skill **Tier 4** — defesa do medico em Processo Etico-Profissional no CRM. Implementa PA-02 (sem promessa), PA-03 (sem opinar conduta), PA-07 (sem julgar etica), PA-08 (sem critica pessoal), PA-12 (cruzamento esferas), PA-13. Acionada por `medico-master`, `triagem-medica` (esfera etica), `timeline-multiesfera`.

---

## 0. Escopo e acionamento

Defesa em PED instaurado por CRM contra medico inscrito por suposta infracao a (a) CEM Res. CFM 2.217/2018 (124 artigos); (b) resolucoes especificas (publicidade 2.336/2023, sigilo 1.605/2000, prontuario 1.821/2007, telemedicina 2.314/2022, HOF 2.337/2023, reproducao assistida 2.320/2022, etc.). Pre-requisito: Selo P1.

## 1. Posicao na orquestra

- **Chamada por:** `medico-master`, `triagem-medica` (esfera etica), `timeline-multiesfera`.
- **Aciona:** `analise-prontuario-medico`, `validador-legislacao-vigente` (CEM vigente no fato — PA-09), `ms-contra-cassacao-conselho` (se sancao = cassacao/suspensao), `suspensao-preventiva-conselho` (se aplicada), `defesa-culpa-medica-criminal` (cruzamento P4), `revisao-final-medica`.
- **Entrega para:** defesa previa, instrucao, alegacoes finais, recurso ao CFM, pedido de revisao.

## 2. Marco normativo

| Norma | Conteudo |
|-------|----------|
| **Lei 3.268/57 + 4.961/66** | Cria CRM/CFM — competencia ético-disciplinar |
| **Res. CFM 2.145/2016** | Codigo de Processo Etico-Profissional (CPEP) — fluxo do PED |
| **Res. CFM 2.217/2018** | Codigo de Etica Medica (CEM) — 124 artigos |
| Res. CFM 1.605/2000 | Sigilo de prontuario |
| Res. CFM 1.821/2007 | Prontuario eletronico/papel |
| Res. CFM 2.336/2023 | Publicidade medica |
| Res. CFM 2.314/2022 | Telemedicina |
| Res. CFM 2.337/2023 | HOF — conflito interconselhos `[VERIFICAR estado da norma]` |
| Res. CFM 2.320/2022 | Reproducao assistida |
| CF art. 5o LV | Devido processo + ampla defesa |
| **CC art. 935** | Independencia relativa — penal alcanca etico/civel se 386 I/III |
| **Lei 9.784/99** | Processo administrativo federal — aplica subsidiariamente |
| Sum. 105 STJ | MS contra cassacao -> JF |
| Lei 12.016/2009 | Mandado de seguranca |

**Jurisprudencia:** STJ AgRg AREsp 1.456.987 (devido processo no PED + dever de motivar sancao); STF MS 27.067 (cassacao exige fundamentacao + proporcionalidade); STJ MS 11.123/DF (revisao judicial limitada — controle de legalidade, nao de merito).

## 3. Fluxo do PED (Res. CFM 2.145/2016)

| Fase | Prazo | Acao do advogado |
|------|-------|------------------|
| 1. Denuncia/Representacao | — | Aguarda |
| 2. Sindicancia (Comissao) | 90d prorrog. | Acompanha; pode peticionar |
| 3. Plenario instaura ou arquiva | — | Prepara defesa se instaura |
| 4. Citacao do denunciado | — | Confere validade (PA-13) |
| **5. Defesa Previa** | **15d (art. 12)** | **Nucleo** — testemunhas (max 5), prova documental, pericia |
| 6. Instrucao (oitivas+pericia) | Variavel | Presenca; assistente tecnico opcional |
| 7. Alegacoes finais | 15d | Resumo + tese + pedido |
| 8. Julgamento 1a inst. CRM | — | Sustentacao oral |
| 9. Decisao | — | Notificacao |
| **10. Recurso voluntario CFM** | **30d (art. 84)** | Recurso + sustentacao em Brasilia |
| 11. Julgamento CFM (2a inst.) | — | — |
| 12. Pedido de revisao | A qualquer tempo (art. 95) | Prova nova / contradicao penal / vicio insanavel |
| 13. MS contra cassacao | 120d (Lei 12.016 23) | `ms-contra-cassacao-conselho` (JF — Sum. 105) |

**Suspensao preventiva (art. 33):** durante o PED, CRM pode suspender preventivamente em casos extremos — `suspensao-preventiva-conselho`.

## 4. Penas (Res. CFM 2.145 art. 22 + Lei 3.268 art. 22)

| # | Pena | Caracteristica |
|---|------|----------------|
| I | **Advertencia confidencial** em aviso reservado | Sigilosa |
| II | **Censura confidencial** em aviso reservado | Sigilosa |
| III | **Censura publica** em publicacao oficial | Publica |
| IV | **Suspensao do exercicio profissional ate 30 dias** | Publica |
| V | **Cassacao do exercicio profissional** | Publica + ad referendum do CFM (necessario) |

Pena ad referendum do CFM (cassacao) so se confirma em sessao do CFM. **Recurso suspende efeitos** em geral.

## 5. Prescricao (Res. CFM 2.145 art. 32)

| Elemento | Regra |
|----------|-------|
| **Prazo** | **5 anos** a contar do fato |
| Interruptivos | Citacao valida; sentenca de pronuncia analoga; sentenca recorrivel |
| Permanente/continuada | Termo inicial: ultima conduta |
| Crime + PED | Se crime tem prescricao maior, **suspende** a etica `[VERIFICAR doutrina especifica]` |

Sempre articular preliminar de prescricao na defesa previa quando aplicavel.

## 6. Teses defensivas (cardapio)

| Tese | Fundamento | Acionar |
|------|-----------|---------|
| **Prescricao** | Res. CFM 2.145 art. 32 | Fato > 5a; interruptivos verificados |
| **Inepcia da denuncia** | Lei 9.784 art. 22 + CF 5o LV | Generica; sem indicar artigo CEM violado; sem fato concreto |
| **Cerceamento de defesa** | CF 5o LV | Negativa de prova; oitiva sem intimacao; perita parcial |
| **Vicio de citacao/intimacao** | Lei 9.784 + Res. CFM 2.145 | AR ausente; endereco errado; prazo nao concedido |
| **Atipicidade etica** | CEM art. especifico | Conduta nao se enquadra no tipo etico — interpretacao restritiva |
| **Ausencia de prova** | CF 5o LV + onus do CRM | CRM nao demonstrou autoria/culpa etica |
| **Boa-fe / divergencia clinica** | CEM 33+ | Conduta dentro de protocolo; divergencia entre profissionais |
| **Conduta em emergencia / estado de necessidade** | CEM 32-35 + CP 24 | Risco iminente + recurso limitado |
| **Cruzamento P4 — absolvicao penal por 386 I/III** | CC art. 935 | Penal absolveu por inexistencia ou sem autoria -> alcanca PED |
| **Desproporcionalidade da pena** | CF 5o LIV + Sum. 14 CFM (proporcionalidade) | Sancao excede gravidade do fato |
| **Reincidencia inexistente** | Res. CFM 2.145 art. 24 | Conduta isolada — afasta agravamento |
| **Vicio de motivacao do voto** | Lei 9.784 art. 50 | Decisao generica; sem analise da defesa |

## 7. Esqueleto — Defesa Previa em PED CRM

```
DEFESA PREVIA — Processo Etico-Profissional n. ___
AO PLENARIO DO CONSELHO REGIONAL DE MEDICINA DE {{OAB_UF}}

[DENUNCIADO], CRM/{{OAB_UF}} n. ___, por {{ADVOGADO_NOME}} OAB/{{OAB_UF}}
{{OAB_NUMERO}}, oferece DEFESA PREVIA (Res. CFM 2.145/2016 art. 12 — 15 dias)

I — PRELIMINARES
  1. Prescricao (Res. CFM 2.145 art. 32) — fato em [data] > 5 anos
  2. Inepcia da denuncia (CF 5o LV + Lei 9.784 22) — generica
  3. Vicio de citacao (Lei 9.784) — endereco/AR

II — FATOS [F] — narrativa defensiva datada (CASO.md)

III — DIREITO [R]
  III.1 Tipicidade etica — CEM art. ___ exige (PA-13)
  III.2 Conduta conforme literatura/protocolo vigente em [ano fato — PA-09]
  III.3 [Boa-fe / divergencia clinica / emergencia / cruzamento P4]
  III.4 Cruzamento P4 — penal absolveu por 386 ___ -> CC 935 alcanca etico

IV — PEDIDOS
  IV.1 Reconhecimento das preliminares
  IV.2 Subsidiariamente: producao de prova — pericia tecnica + oitiva de
       [N testemunhas, max 5] + juntada de documentos anexos
  IV.3 Subsidiariamente: arquivamento por atipicidade ou ausencia de prova
  IV.4 Se procedente, dosimetria proporcional (CF 5o LIV)

[Cidade, data] — {{ADVOGADO_NOME}} | OAB/{{OAB_UF}} {{OAB_NUMERO}}

RESSALVA (PA-05).
```

## 8. Estrategia processual

1. **Defesa previa (15d) e a chance principal** — toda prova e arrolada aqui. Perder = restricao na instrucao.
2. **Sustentacao oral no julgamento** — pratica nuclear; preparar resumo de 10-15 min.
3. **Recurso ao CFM (30d)** — efeito suspensivo amplo em geral; sustentacao oral em Brasilia.
4. **Pedido de revisao** — so com prova nova ou contradicao com penal absolutoria.
5. **MS contra cassacao** — JF; via simultanea ao recurso administrativo (nao se exige esgotamento — Sum. 105 STJ).
6. **Suspensao preventiva** — se aplicada, agir imediatamente — `suspensao-preventiva-conselho`.

## 9. Cruzamento P4 (PA-12) — coracao da defesa multi-frente

| Esfera | Reflexo no PED |
|--------|----------------|
| Penal — absolvicao 386 I (inexistencia) | **Alcanca** — vincula CRM |
| Penal — 386 III (sem autoria) | **Alcanca** — vincula |
| Penal — 386 V/VII (insuficiencia) | NAO alcanca — CRM pode prosseguir |
| Penal — atipicidade 386 II | NAO alcanca (ato etico nao se confunde com tipo penal) |
| Civel | Influencia probatoria, sem vinculacao automatica |

Articular com `timeline-multiesfera` para coordenar prazos e estrategia simultanea.

## 10. Vedacoes especificas

- **PA-02 / PA-03 / PA-07 / PA-08** — sem promessa, sem opinar conduta tecnica, sem julgar etica, sem critica pessoal.
- **PA-13** — citar CEM (Res. CFM 2.217) por artigo + Res. CFM 2.145 com artigo.
- **PA-19** — prescricao etica (5a) conferida sempre.

## 11. Protocolos acionados

- **P1** — Selo (CEM e Res. vigentes no fato).
- **P2** — `analise-prontuario-medico`.
- **P3** — memoria de decisao (defesa x recurso x MS).
- **P4** — `timeline-multiesfera`.
- **P5** — CRM da UF de inscricao; CFM em Brasilia; MS na JF da capital UF (Sum. 105 STJ).
- **P6** — `revisao-final-medica`.

## 12. Localizacao

CRM da UF de inscricao do medico. Recurso administrativo: CFM (Brasilia). MS contra cassacao/suspensao: JF da capital da UF (Sum. 105 STJ). Estatuto interno do CRM-UF pode complementar Res. CFM 2.145 — `[VERIFICAR estatuto CRM-UF]`.

## 13. Integracao

**Chamada por:** `medico-master`, `triagem-medica` (esfera etica), `timeline-multiesfera`.

**Entrega para:** defesa previa / alegacoes finais / recurso ao CFM / pedido de revisao -> `revisao-final-medica` -> operador. Aciona `ms-contra-cassacao-conselho` se sancao = suspensao/cassacao, e `suspensao-preventiva-conselho` se aplicada.

**Sem esta skill:** defesa generica de PED, perdendo prescricao, preliminares processuais e cruzamento P4 — exposicao a sancao severa que poderia ser afastada.
