---
name: tutela-urgencia-plano-saude
description: >
  Modelo unificado de tutela de urgencia em acoes contra operadora de plano de saude — paciente que precisa de cobertura imediata (oncologico, home care, OPME, TEA, rescisao em tratamento, exame critico, internacao, cirurgia). Aplica CPC art. 300 (tutela de urgencia — probabilidade + periculum) + CPC art. 537 (astreintes proporcionais — STJ EAREsp 650.536 + Tema 1.094/1.095) + CPC art. 854 (SISBAJUD em descumprimento) + Sum. 469/608 STJ + Lei 14.454/2022. Articula 3 pilares: probabilidade do direito (Lei 9.656 + jurisprudencia consolidada por subtipo); perigo de dano (tempo-critico, irreparabilidade); proporcionalidade (sem excesso). Mecanismos pos-deferimento: astreintes + intimacao com prazo curto + bloqueio SISBAJUD + envio direto a hospital/clinica. Conservadorismo (PA-21) em astreintes (limite e teto). Aciona: tutela urgencia plano de saude, antecipacao tutela, CPC 300, astreintes plano, SISBAJUD, EAREsp 650.536, bloqueio operadora, multa diaria plano, modelo tutela, urgencia oncologica.
---

# TUTELA DE URGENCIA — PLANO DE SAUDE (MODELO UNIFICADO)

> Skill **Tier 5** — modelo unificado de tutela de urgencia em acoes contra operadora. Implementa PA-04, PA-13, PA-14, PA-15, PA-21 (astreintes proporcionais). Acionada por todas as skills do Tier 5 (`acao-negativa-cobertura-oncologica`, `acao-home-care`, `acao-opme`, `acao-tea-multidisciplinar`, `acao-rescisao-coletivo`) + `medico-master`, `triagem-medica`.

---

## 0. Escopo e acionamento

Pacote tecnico reutilizavel de **tutela de urgencia + astreintes + execucao** para acoes contra operadora de plano de saude. Insumo das skills do Tier 5 (cada uma traz a tese material — esta traz o instrumento processual). Aplica-se a paciente que precisa de cobertura imediata (cirurgia oncologica, quimioterapia agendada, home care apos alta, OPME em cirurgia agendada, terapia TEA em janela tempo-critica, manutencao em tratamento grave).

## 1. Posicao na orquestra

- **Chamada por:** todas as skills do Tier 5; `medico-master`, `triagem-medica`.
- **Aciona:** `validador-legislacao-vigente` (STJ atual), `revisao-final-medica`.
- **Entrega para:** secao de tutela da peca + pedidos de execucao.

## 2. Marco normativo

| Norma | Conteudo |
|-------|----------|
| **CPC art. 300** | Tutela de urgencia — probabilidade + periculum |
| CPC art. 301 | Tutela cautelar |
| **CPC art. 537** | Astreintes — fixacao + modulacao |
| CPC art. 538 | Cumprimento de obrigacao de fazer |
| **CPC art. 854** | SISBAJUD — bloqueio judicial |
| CPC art. 814-823 | Cumprimento de obrigacao de pagar |
| Lei 9.656/1998 + Lei 14.454/2022 | Marco material |
| CDC art. 84 (correspondente CPC 497) | Tutela especifica em obrigacao de fazer |
| **STJ EAREsp 650.536** | **Astreintes proporcionais — sem desvio de finalidade; teto razoavel** |
| **STJ Tema 1.094/1.095** | Limite a revisao em recurso especial — sentinela de razoabilidade |
| Sum. 469 / 608 STJ | CDC em planos / coletivos |

## 3. Tres pilares da tutela

| Pilar | Conteudo |
|-------|----------|
| **1. Probabilidade do direito (fumus boni iuris)** | Lei material aplicavel + jurisprudencia consolidada do subtipo (oncologia, home care, etc.) + documentacao tecnica (prescricao, laudo) |
| **2. Perigo de dano (periculum in mora)** | Tempo-critico (perda de janela terapeutica, perda de chance — `perda-de-uma-chance`); irreparabilidade ou difícil reparacao |
| **3. Proporcionalidade** | Pedido limitado ao necessario; astreintes razoaveis com teto; sem excesso retorico |

## 4. Mapa de probabilidade por subtipo

| Subtipo | Probabilidade base |
|---------|-------------------|
| Oncologica + Lei 14.454/Tema 990 + criterios 5 | Alta |
| Home care + AgInt AREsp 1.232.473 | Media-Alta (depende dos 5 criterios) |
| OPME + REsp 1.733.013 + prescricao fundamentada | Alta |
| TEA + Lei 12.764 + LBI + RN 539 | Alta |
| Rescisao coletivo + Tema 1.082 (doenca grave) | Alta |
| Reajuste abusivo (urgencia rara) | Baixa-Media (urgencia depende de impacto na continuidade) |
| Cobertura excepcional (sem precedente claro) | Baixa-Media |

## 5. Mapa de periculum por subtipo

| Subtipo | Argumento periculum |
|---------|---------------------|
| Oncologia | Janela terapeutica; estadiamento; perda de chance (REsp 1.291.247) |
| Home care | Infeccao hospitalar; alta ja determinada; cuidador esgotado |
| OPME | Cirurgia agendada; cancelamento gera atraso clinico |
| TEA | Janela neurodesenvolvimental (literatura) |
| Rescisao | Descontinuidade de tratamento grave (Tema 1.082) |
| Dialise | Risco a vida em 48-72h |
| Transplante | Janela imunologica + alocacao no fila |

## 6. Astreintes proporcionais (PA-21 — coracao tecnico)

**STJ EAREsp 650.536 + Tema 1.094/1.095** — astreintes nao podem ter desvio de finalidade (enriquecimento sem causa). Criterios:

| Criterio | Aplicacao |
|----------|-----------|
| **Valor diario** | Proporcional ao porte da operadora + ao bem juridico tutelado |
| **Teto** | Razoavel — STJ tende a limitar |
| **Termo inicial** | Apos prazo concedido (24-48h) |
| **Termo final** | Cumprimento da obrigacao |
| **Conversao em perdas e danos** | Possivel — CPC 537 §4o |

**Exemplos comuns (`[VERIFICAR jurisprudencia recente]`):**
- Oncologia: R$ 1.000-5.000/dia
- Home care: R$ 500-3.000/dia
- OPME: R$ 1.000-5.000/dia
- TEA: R$ 500-2.000/dia

**Sempre incluir teto** (ex.: ate R$ 100.000 ou outro valor razoavel) — evita reducao por STJ em sede recursal.

## 7. Mecanismos pos-deferimento (execucao)

| Mecanismo | Quando |
|-----------|--------|
| **Intimacao da operadora com prazo curto (24-48h)** | Imediato apos deferimento |
| **Envio direto a hospital/clinica** | Para nao depender da operadora processar autorizacao |
| **SISBAJUD (CPC 854)** | Em descumprimento — bloqueio das astreintes ou do custeio |
| **Prisao por dificultar acesso (CPC 77 §1o)** | Rarissimo; ato atentatorio |
| **Conversao em obrigacao de pagar** | Quando obrigacao especifica torna-se impossivel/inadequada |

## 8. Esqueleto — Secao de tutela na peca

```
V — TUTELA DE URGENCIA (CPC art. 300)

V.1 PROBABILIDADE DO DIREITO (fumus boni iuris)
    - Lei material aplicavel: [Lei 9.656 + Lei 14.454 + RN/Sum/Tema STJ
      do subtipo] (PA-13)
    - Jurisprudencia consolidada: [precedente paradigma]
    - Documentacao: prescricao medica fundamentada (anexo X), laudo,
      exames

V.2 PERIGO DE DANO (periculum in mora)
    - Tempo-critico: [janela tecnica do subtipo]
    - Irreparabilidade: [argumento concreto — quimio interrompida,
      janela neurodesenvolvimental, transplante]
    - Literatura: [SBOC/SBP/SBN/SBC `[VERIFICAR]`]

V.3 PROPORCIONALIDADE
    - Pedido limitado ao necessario (cobertura especifica indicada)
    - Astreintes com teto (PA-21 + EAREsp 650.536)
    - Sem desvio de finalidade

V.4 PEDIDOS DE TUTELA
    a) Determinacao IMEDIATA de cobertura integral de [tratamento/OPME/
       home care/manutencao do plano] (CPC art. 300 + 497)
    b) Astreintes de R$ ___/dia em caso de descumprimento, com termo inicial
       em 24-48h apos a intimacao e termo final no cumprimento, com TETO de
       R$ ___ (STJ EAREsp 650.536 + Tema 1.094/1.095 — proporcionalidade)
    c) Em caso de descumprimento: bloqueio judicial via SISBAJUD (CPC 854)
       do valor de [custeio + astreintes]
    d) Notificacao direta dos prestadores [hospital/clinica/laboratorio]
       para que executem a cobertura independente de autorizacao prevista
       da operadora
    e) Aplicacao de multa por ato atentatorio se houver criacao deliberada
       de obstaculos (CPC art. 77 §2o)
```

## 9. Distincoes operacionais

| Modalidade processual | Quando usar |
|-----------------------|-------------|
| **Tutela antecipada** (CPC 300) | Pretensao satisfativa (custeio imediato) — regra |
| **Tutela cautelar** | Resguardar direito futuro (raro em plano de saude) |
| **Tutela de evidencia** (CPC 311) | Quando ha precedente vinculante claro |
| **Tutela antecedente** (CPC 303) | Urgencia extrema antes da inicial completa |
| **Sentenca antecipada de merito** | Apos contestacao se prova robusta |

## 10. Recursos em caso de indeferimento

| Decisao | Recurso |
|---------|---------|
| Indeferimento da tutela | **Agravo de instrumento** (CPC 1.015 I) — TJ |
| Tutela concedida + operadora recorre | **Defender em contraminuta** + execucao paralela |
| Sentenca de procedencia | Apelacao sem suspensividade em obrigacao de fazer (CPC 1.012 §1o V) |
| Sentenca de improcedencia | Apelacao com argumentacao tecnica reforcada |

## 11. Vedacoes especificas

- **PA-02** — sem promessa.
- **PA-10 / PA-11** — STJ atual + Rol ANS atualizado `[VERIFICAR]`.
- **PA-13** — CPC + Lei 9.656 + jurisprudencia com identificacao precisa.
- **PA-14** — inversao do onus fundamentada.
- **PA-21** — **astreintes proporcionais com teto** — vetor critico.

## 12. Protocolos acionados

- **P1** — Selo (Lei 14.454 + STJ atual).
- **P3** — memoria de quantum (incluindo astreintes).
- **P5** — JE domicilio do consumidor (CDC 101 I).
- **P6** — `revisao-final-medica`.

## 13. Integracao

**Chamada por:** todas as skills do Tier 5 + `medico-master`, `triagem-medica`.

**Entrega para:** secao de tutela da peca + pedidos de execucao -> `revisao-final-medica` -> operador.

**Sem esta skill:** tutelas em pecas do Tier 5 com astreintes desproporcionais (cortadas pelo STJ); sem mecanismos de execucao (operadora cumpre tarde); sem articulacao tres-pilar (probabilidade + periculum + proporcionalidade). Esta skill homogeniza a abordagem.
