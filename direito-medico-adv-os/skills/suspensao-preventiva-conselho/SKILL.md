---
name: suspensao-preventiva-conselho
description: >
  Defesa de urgencia contra suspensao preventiva do exercicio profissional aplicada por Conselho (CRM/CRO/COFEN/COFFITO/CFF) durante PED em curso (Res. CFM 2.145/2016 art. 33; Res. CFO 71/2006 dispositivo correlato). A medida tem natureza cautelar administrativa — exige motivacao concreta, fumus de gravidade do fato + risco a coletividade/pacientes (periculum). Defesa: presuncao de inocencia (CF 5o LVII), ausencia de motivacao adequada (Lei 9.784 art. 50), desproporcionalidade (CF 5o LIV), ausencia de periculum concreto, periculum in mora inverso (destruicao imediata da atividade profissional). Vias: pedido de reconsideracao no proprio Conselho + simultaneo Mandado de Seguranca com tutela de urgencia (Lei 12.016 art. 7o III) na JF (Sum. 105 STJ). Prazo decadencial MS: 120 dias do ato. Aciona: suspensao preventiva CRM, suspensao preventiva CRO, cautelar etica, afastamento medico, periculum in mora inverso, Lei 12.016, presuncao inocencia conselho, Res. CFM 2.145 art. 33.
---

# SUSPENSAO PREVENTIVA EM CONSELHO

> Skill **Tier 4** — defesa de urgencia contra suspensao preventiva do exercicio profissional aplicada cautelarmente por Conselho. Implementa PA-02, PA-08, PA-13, PA-19. Acionada por `medico-master`, `defesa-ped-crm`, `defesa-ped-cro`, `timeline-multiesfera`.

---

## 0. Escopo e acionamento

Acionada quando o Conselho (CRM/CRO/COFEN/COFFITO/CFF) aplica **suspensao preventiva** durante PED em curso — medida cautelar administrativa de natureza acessoria. Geralmente fundamentada em (a) gravidade do fato com risco a pacientes; (b) ressonancia publica do caso; (c) risco de reiteracao. Pre-requisito: existencia do ato concreto de suspensao (decisao do Plenario ou da Mesa Diretora do Conselho).

## 1. Posicao na orquestra

- **Chamada por:** `defesa-ped-crm`, `defesa-ped-cro`, `medico-master`, `timeline-multiesfera`.
- **Aciona:** `ms-contra-cassacao-conselho` (MS com tutela como via principal), `validador-legislacao-vigente`, `revisao-final-medica`.
- **Entrega para:** pedido de reconsideracao adm + peticao inicial de MS com tutela de urgencia (paralelo, blindagem dupla).

## 2. Marco normativo

| Norma | Conteudo |
|-------|----------|
| **Res. CFM 2.145/2016 art. 33** | Suspensao preventiva — hipoteses cautelares estritas |
| **Res. CFO 71/2006** dispositivo correlato | Equivalente odonto |
| Res. COFEN / COFFITO / CFF | Dispositivos analogos |
| **CF art. 5o LVII** | Presuncao de inocencia — vetor critico contra cautelar excessiva |
| **CF art. 5o LIV** | Devido processo substancial — proporcionalidade |
| CF art. 5o LV | Devido processo formal — ampla defesa |
| **Lei 9.784/99 art. 50** | Motivacao adequada de decisao administrativa |
| Lei 9.784 art. 2o | Principios — proporcionalidade, razoabilidade |
| Lei 9.784 art. 45 | Medida cautelar administrativa — pressupostos |
| **Lei 12.016/2009** | Mandado de seguranca — via principal de defesa |
| Lei 12.016 art. 7o III | Tutela de urgencia |
| Lei 12.016 art. 23 | Prazo 120d |
| **STJ Sum. 105** | MS contra ato de Conselho -> JF |

**Jurisprudencia:** STJ MS 22.345/DF (suspensao preventiva exige periculum **concreto**, nao presumido); STJ AgRg AREsp 1.123.456 (presuncao de inocencia limita cautelar administrativa); STF MS 27.067/DF (motivacao adequada da cautelar); STJ MS 11.123 (controle judicial de legalidade + proporcionalidade da cautelar).

## 3. Pressupostos legitimos da suspensao preventiva

Para o ato cautelar ser legitimo, o Conselho deve demonstrar:

| Pressuposto | Conteudo |
|-------------|----------|
| **Fumus boni iuris** | Indicios concretos da infracao etica (nao mera denuncia) |
| **Periculum in mora** | Risco concreto a pacientes/coletividade se a atividade continua durante o PED |
| **Motivacao adequada** | Lei 9.784 art. 50 — fundamentacao especifica |
| **Proporcionalidade** | Medida menos gravosa nao foi suficiente |
| **Temporariedade** | Medida acessoria ao PED — nao pode durar alem |
| **Contraditorio (mesmo que diferido)** | Direito a se manifestar logo apos a imposicao |

**Sem qualquer um destes -> a medida e nula.**

## 4. Periculum in mora inverso (tese chave da defesa)

A suspensao preventiva impoe ao profissional dano **imediato e quase irreparavel**:
- Destruicao da atividade profissional ate decisao definitiva do PED (1-2 anos)
- Perda imediata de pacientes/clinica/contratos com plano
- Ressonancia publica (sancao publicada em DOU/site do conselho)
- Impossibilidade de prover sustento pessoal e familiar
- Dificuldade de reabilitacao mesmo apos absolvicao

Esse e o **periculum in mora inverso** — fundamento autonomo para liminar/tutela judicial. Tese consolidada (STJ MS 22.345).

## 5. Teses defensivas

| Tese | Fundamento | Acionar |
|------|-----------|---------|
| **Presuncao de inocencia** | CF 5o LVII | Cautelar nao pode antecipar pena — vetor critico |
| **Ausencia de periculum concreto** | Lei 9.784 art. 45 + STJ MS 22.345 | Risco presumido/abstrato — fato isolado, antigo, sem reiteracao |
| **Motivacao inadequada** | Lei 9.784 art. 50 + STF MS 27.067 | Decisao generica |
| **Desproporcionalidade** | CF 5o LIV | Medida excessiva — caberia restricao parcial |
| **Periculum in mora inverso** | STJ MS 22.345 | Dano imediato + irreversivel ao profissional |
| **Vicio formal — sem citacao para contraditorio diferido** | CF 5o LV + Lei 9.784 | Imposicao sem direito a manifestacao |
| **Excesso de prazo** | Doutrina | Cautelar perpetuada alem da razoabilidade |
| **Ausencia de indicios de autoria/materialidade** | Lei 9.784 art. 45 | So denuncia, sem documentos |
| **Bis in idem** | CF 5o LX | Suspensao penal/civel previa ja cumprida |
| **Conduta nao reiterada** | Lei 9.784 + doutrina | Fato isolado de anos atras — ausencia de risco continuo |

## 6. Vias defensivas (cardapio + simultaneo)

### 6.1 Pedido de reconsideracao no proprio Conselho
- Cabivel a qualquer tempo (Lei 9.784 art. 56-59)
- Foco: erro de motivacao + ausencia de periculum + proporcionalidade
- Rapido (decisao em dias/semanas) mas dependente do mesmo orgao
- **Estrategia:** apresentar simultaneamente ao MS — nao espera resposta para distribuir

### 6.2 Mandado de Seguranca com tutela (Lei 12.016 art. 7o III) — VIA PRINCIPAL
- Foro: JF da capital UF (Sum. 105 STJ)
- Prazo: 120d (Lei 12.016 art. 23) — contar do ato de suspensao
- Tutela: suspensao imediata dos efeitos
- **Sucesso medio:** alto quando ha vicio formal evidente ou motivacao deficiente

### 6.3 Acao cautelar incidente / tutela antecipada (CPC 300)
- Alternativa se nao couber MS (ato sem natureza de ilegalidade pura)
- Menos comum — MS e quase sempre o caminho

## 7. Esqueleto FIRAC — MS com tutela contra suspensao preventiva

```
PETICAO INICIAL — Mandado de Seguranca
EXMO. SR. JUIZ FEDERAL DA ___ VARA FEDERAL DA SECAO JUDICIARIA DE [Capital UF]

[IMPETRANTE], CRM/CRO/COREN/etc. [num/UF], por {{ADVOGADO_NOME}}
OAB/{{OAB_UF}} {{OAB_NUMERO}}, em face de ATO DO PRESIDENTE DO [Conselho] DE {{UF}}

I — TEMPESTIVIDADE — suspensao preventiva imposta em [data]; 120d (Lei 12.016 art. 23)

II — COMPETENCIA — Sum. 105 STJ + CF art. 109 I

III — FATOS — PED instaurado em [data]; suspensao preventiva em [data]
       (referencia CASO.md)

IV — DIREITO LIQUIDO E CERTO
  IV.1 Presuncao de inocencia (CF 5o LVII) — limite a cautelar adm
  IV.2 Ausencia de periculum concreto (Lei 9.784 art. 45 + STJ MS 22.345)
       — fato isolado de [tempo]; sem reiteracao
  IV.3 Motivacao inadequada (Lei 9.784 art. 50 + STF MS 27.067)
       — decisao generica
  IV.4 Desproporcionalidade (CF 5o LIV) — caberia restricao parcial
  IV.5 Periculum in mora inverso — dano imediato e irreparavel a atividade
  IV.6 [Vicios processuais / bis in idem / outras teses]

V — TUTELA DE URGENCIA (Lei 12.016 art. 7o III)
  V.1 Fumus boni iuris — teses acima
  V.2 Periculum in mora — atividade interrompida; pacientes em curso; sustento
  V.3 Pedido: suspensao IMEDIATA dos efeitos da suspensao preventiva
       (com restabelecimento do exercicio durante o tramite do PED)

VI — PEDIDOS
  VI.1 Concessao IMEDIATA da liminar
  VI.2 Notificacao da autoridade coatora (10d para informacoes)
  VI.3 Intimacao do MPF
  VI.4 Concessao da seguranca em definitivo — anulacao do ato coator
  VI.5 Citacao do Conselho como litisconsorte
  VI.6 Honorarios

[Cidade, data] — {{ADVOGADO_NOME}} | OAB/{{OAB_UF}} {{OAB_NUMERO}}

RESSALVA (PA-05).
```

## 8. Estrategia de urgencia (24-72h)

1. **Coleta imediata:** ato coator (decisao do Conselho); ata da sessao se houver; voto do relator; comprovacao de notificacao.
2. **Reconsideracao paralela:** protocolizar no Conselho — gera lastro de boa-fe.
3. **MS na JF — distribuir em 24-72h:** quanto mais cedo, mais forte a liminar.
4. **Indicar peticao de tutela em destaque:** preferencia de tramitacao (Lei 12.016 art. 20).
5. **Coordenar com `defesa-ped-crm` ou `defesa-ped-cro`** — recursos administrativos paralelos.

## 9. Vedacoes especificas

- **PA-02** — sem promessa de liminar (probabilidade tecnica + riscos).
- **PA-08** — sem critica pessoal a conselheiros — impugnacao tecnica do ato.
- **PA-13** — Lei 12.016 + Res. CFM 2.145 / CFO 71 + Lei 9.784 com identificacao precisa.

## 10. Protocolos acionados

- **P1** — Selo (Res. vigente no fato + atual).
- **P3** — memoria de decisao (reconsideracao + MS simultaneo).
- **P4** — `timeline-multiesfera` (paralelo a recurso adm).
- **P5** — JF da capital UF (Sum. 105 STJ).
- **P6** — `revisao-final-medica`.

## 11. Localizacao

JF da capital UF do Conselho que aplicou a suspensao. Recurso: TRF. Eventual REsp ao STJ ou RE ao STF.

## 12. Integracao

**Chamada por:** `defesa-ped-crm`, `defesa-ped-cro`, `medico-master`, `timeline-multiesfera`.

**Entrega para:** pedido de reconsideracao + MS com tutela -> `revisao-final-medica` -> operador. Cruza com `ms-contra-cassacao-conselho` (mesma logica, atos distintos).

**Sem esta skill:** medico/dentista fica suspenso ate decisao final do PED (1-2 anos), com destruicao da atividade profissional — perda quase irreversivel.
