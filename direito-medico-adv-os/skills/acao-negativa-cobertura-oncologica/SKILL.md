---
name: acao-negativa-cobertura-oncologica
description: >
  Acao contra operadora por negativa de cobertura de tratamento oncologico — quimioterapia/imunoterapia/terapia-alvo (incluindo off-label e nao-Rol), cirurgia oncologica, radioterapia, PET-CT, transplante, medicamentos de alto custo. Aplica Lei 9.656/1998 + Lei 14.454/2022 (que tornou o Rol ANS exemplificativo) + Tema 990 STJ pos-Lei 14.454 + Sum. 469 STJ (CDC) + Sum. 597 (CDC + autogestao). Criterios pos-Lei 14.454 art. 10§13: comprovacao de eficacia + recomendacao de orgao tecnico (CONITEC, SBOC, NICE, etc.) ou aprovacao FDA/EMA/PMDA + bula nacional/internacional + ausencia de substituto pelo Rol. Tutela de urgencia CPC 300 — gravidade clinica + tempo (chance de cura tempo-dependente — perda de chance). Conservadorismo (PA-21) no quantum. Aciona: negativa oncologia, quimioterapia negada, imunoterapia, off-label, Lei 14.454, Tema 990 STJ, Rol exemplificativo, alto custo plano, transplante negado, PET-CT negado, SBOC, NICE, CONITEC, terapia alvo.
---

# ACAO NEGATIVA DE COBERTURA ONCOLOGICA

> Skill **Tier 5** — acao contra operadora de plano de saude por negativa de cobertura oncologica. Implementa PA-04 (Selo), PA-09 (ano do fato — Rol vigente), PA-10 (jurisprudencia atual pos-Lei 14.454), PA-11 (Rol em atualizacao), PA-13, PA-14 (inversao do onus), PA-15 (objetiva — CDC 14), PA-21 (conservadorismo). Acionada por `medico-master`, `triagem-medica`.

---

## 0. Escopo e acionamento

Acao do paciente/beneficiario contra operadora por negativa de tratamento oncologico. Inclui: quimioterapia oral/EV, imunoterapia, terapia-alvo (TKI, anti-PD1, etc.), CAR-T, transplante de medula, cirurgia oncologica, radioterapia (3D, IMRT, IGRT, protons), PET-CT, medicamentos de alto custo (Trastuzumabe, Pembrolizumabe, etc.), procedimento off-label. Pre-requisito: Selo P1 + analise da apolice + parecer do oncologista assistente.

## 1. Posicao na orquestra

- **Chamada por:** `medico-master`, `triagem-medica` (esfera civel — paciente vs operadora), `tutela-urgencia-plano-saude`.
- **Aciona:** `tutela-urgencia-plano-saude` (modelo de tutela unificado), `validador-legislacao-vigente` (Rol ANS vigente + jurisprudencia atual), `revisao-final-medica`.
- **Entrega para:** peticao inicial com tutela de urgencia + memoria de quantum.

## 2. Marco normativo

| Norma | Conteudo |
|-------|----------|
| **Lei 9.656/1998** | Lei dos planos de saude — art. 10 (coberturas obrigatorias), art. 12 (segmentacoes) |
| **Lei 14.454/2022** | Alterou Lei 9.656 — Rol ANS **exemplificativo** (art. 10§13) + criterios para cobertura fora do Rol |
| Lei 9.961/2000 | Cria ANS |
| **RN ANS 465/2021 + sucessoras** | Rol de Procedimentos `[VERIFICAR atualizacao]` |
| CDC art. 6o III/VIII + 47 + 51 IV | Direito a informacao + inversao do onus + nulidade abusiva |
| **CDC art. 14** | Responsabilidade objetiva do prestador |
| CDC art. 27 | Prescricao 5a |
| Lei 10.741/2003 (EI) | Estatuto Idoso — protecao especial |
| Lei 13.146/2015 (LBI) | Estatuto da Pessoa com Deficiencia |
| CPC art. 300 | Tutela de urgencia |
| CPC art. 537 | Astreintes |

**Sumulas STJ:** **469** (CDC em plano de saude); **597** (CDC nao em autogestao; carencia > 24h em emergencia); **608** (CDC em coletivos empresariais).

**Temas STJ (atualizar pos-Lei 14.454):**
- **Tema 990** — pos-Lei 14.454/2022 — Rol exemplificativo, com criterios objetivos para cobertura fora do Rol
- Tema 1.069 — limites a recusa de medicamento de alto custo
- Tema 952 — reajuste por faixa etaria
- **REsp 1.733.013/PR** (OPME), **REsp 1.846.502/SP** (off-label oncologico) `[VERIFICAR jurisprudencia mais recente]`

## 3. Criterios pos-Lei 14.454/2022 art. 10§13 (corecao da peca)

Cobertura **fora do Rol** deve ser concedida quando comprovada:

1. **Eficacia comprovada cientificamente** — estudos clinicos publicados em revistas indexadas, parecer da SBOC/sociedade de especialidade, diretrizes (NICE, NCCN, ESMO)
2. **Recomendacao por orgao tecnico** — CONITEC, comissoes oncologicas estaduais, ou
3. **Aprovacao por orgao regulador internacional** — FDA, EMA, PMDA, Health Canada
4. **Bula** — uso registrado em pais de origem (off-label aceito se literatura sustenta)
5. **Ausencia de substituto eficaz no Rol** — esgotamento das alternativas previstas

**Estrategia:** sempre demonstrar TODOS os 5 — quanto mais demonstrados, mais robusta a tese.

## 4. Tipos de negativa e teses correspondentes

| Negativa | Tese juridica |
|----------|---------------|
| **"Fora do Rol ANS"** | Lei 14.454/2022 — Rol exemplificativo + criterios 1-5 demonstrados |
| **"Off-label"** | Eficacia cientifica (NCCN/ESMO) + indicacao oncologica analoga + ausencia substituto |
| **"Alto custo"** | Tema 1.069 STJ + Lei 9.656 art. 10 — operadora nao pode recusar por valor |
| **"Carencia"** | Lei 9.656 art. 12 V "c" — emergencia oncologica 24h; URGENCIA |
| **"Pre-existencia"** | Lei 9.656 art. 11 — CPT 24 meses limitado; oncologia em curso = continuidade |
| **"Procedimento experimental"** | Distinguir experimental (nao registrado) de off-label (registrado, uso analogo) |
| **Glosa de medicamento de uso domiciliar** | Sum. 469 + tratamento conexo a quimio (antiemetico, hematopoietico) |
| **Negativa de PET-CT/exame diagnostico** | Necessidade tecnica + diretriz SBOC |
| **Negativa de transplante** | Lei 9.434/1997 + protocolo SUS de prioridade `[VERIFICAR]` |
| **Negativa de CAR-T / terapia avancada** | Lei 14.454 + parecer SBOC + aprovacao internacional |

## 5. Tutela de urgencia (CPC 300) — coracao da peca

**Probabilidade do direito (fumus):** Lei 14.454 + Sum. 469/608 + Tema 990 pos-lei + parecer medico assistente + comprovacao dos 5 criterios.

**Perigo de dano (periculum):** oncologia e tempo-dependente — atraso reduz chance de cura/sobrevida (`perda-de-uma-chance` aplicavel). Documentar: estadio do tumor; janela terapeutica; literatura sobre impacto do atraso.

**Pedido:** custeio integral do tratamento + astreintes diarias (CPC 537) + bloqueio SISBAJUD (CPC 854) se descumprimento.

## 6. Memoria de quantum (P3 + PA-21 conservadorismo)

| Item | Base | Valor |
|------|------|-------|
| **Custeio do tratamento** | Lei 9.656 + Lei 14.454 | Custo efetivo (faturas hospitalares + recibos) |
| **Reembolso por desembolso proprio** | CDC 14 + CC 944 | Comprovantes (NF) — Selic desde desembolso (Sum. 54) |
| **Dano moral autonomo** | CC 186 + 927 + ancorado em Tema 1.094/1.095 | Parametro conservador (PA-21) |
| **Astreintes** | CPC 537 | Diaria proporcional (`[VERIFICAR EAREsp 650.536 STJ]`) com teto |
| **Honorarios sucumbenciais** | CPC 85 | 10-20% |

## 7. Esqueleto FIRAC — Peticao inicial

```
PETICAO INICIAL — Civel com tutela de urgencia
EXMO. SR. JUIZ DE DIREITO DA ___ VARA CIVEL DE [Cidade/UF]

[PACIENTE], qualificacao, por {{ADVOGADO_NOME}} OAB/{{OAB_UF}} {{OAB_NUMERO}},
propoe ACAO DE OBRIGACAO DE FAZER com tutela em face de
[OPERADORA] CNPJ ___

I — FATOS — diagnostico em [data]; prescricao em [data]; negativa em [data]
   (referencia CASO.md)

II — ISSUE — negativa de [tratamento X] viola Lei 9.656 + Lei 14.454/2022?

III — DIREITO
  III.1 Regime — CDC art. 14 (objetiva — PA-15) + Sum. 469 STJ (PA-13)
  III.2 Lei 14.454/2022 art. 10§13 — Rol exemplificativo
  III.3 Criterios atendidos (PA-13):
        - Eficacia cientifica: [estudos + NCCN/ESMO + parecer SBOC]
        - Recomendacao tecnica: [CONITEC/sociedade]
        - Aprovacao internacional: [FDA/EMA]
        - Bula: [registro/indicacao analoga]
        - Ausencia de substituto eficaz no Rol
  III.4 Inversao do onus — CDC 6o VIII + Sum. 469 STJ (PA-14 fundamentado)
  III.5 Tutela de urgencia — CPC 300 (probabilidade + perigo tempo-dependente)
  III.6 [Estatuto Idoso / LBI se aplicavel]

IV — PEDIDOS
  IV.1 Tutela de urgencia: custeio imediato + astreintes diarias R$ ___ (CPC 537)
        + bloqueio SISBAJUD se descumprimento (CPC 854) — astreintes proporcionais
        (`[VERIFICAR EAREsp 650.536 STJ]`)
  IV.2 Procedencia — manutencao do custeio + reembolso de desembolsos com Selic
  IV.3 Dano moral autonomo R$ ___ (PA-21 conservador)
  IV.4 Inversao do onus
  IV.5 Honorarios (CPC 85)
  IV.6 Valor da causa: R$ ___ (CPC 292)

[Cidade, data] — {{ADVOGADO_NOME}} | OAB/{{OAB_UF}} {{OAB_NUMERO}}

RESSALVA (PA-05).
```

## 8. Documentos obrigatorios (anexar)

1. Apolice / contrato + cobertura discriminada
2. Carteirinha vigente
3. Solicitacao medica detalhada (CID + estadio + protocolo + justificativa)
4. Parecer/relatorio do oncologista assistente
5. Negativa formal da operadora (carta, e-mail, registro telefonico, transcricao)
6. Bula nacional + bula do pais de origem se off-label
7. Estudos cientificos relevantes
8. Diretriz da sociedade de especialidade (SBOC, NCCN, ESMO)
9. Comprovantes de desembolsos proprios (se houver)

## 9. Casos tipicos

- **Imunoterapia (Pembrolizumabe/Nivolumabe) em tumor sem indicacao especifica:** off-label com PD-L1 alto — eficacia cientifica robusta — Tema 990 pos-lei.
- **Terapia alvo (Trastuzumabe) em tumor HER2 ressuscitado:** indicacao adjuvante x metastatica — distinguir Rol.
- **CAR-T em LLA refrataria:** alto custo + tecnologia avancada — Tema 1.069 + Lei 14.454.
- **Transplante de medula em LMA:** Rol cobre — recusa indica vicio de glosa.
- **PET-CT para estadiamento:** Rol cobre em hipoteses; fora delas, Lei 14.454.
- **Radioterapia protontoterapia:** raramente coberta — Lei 14.454 + estudos NICE.

## 10. Vedacoes especificas

- **PA-02** — sem promessa.
- **PA-03 / PA-06** — sem opinar sobre conduta clinica nem orientacao ao paciente.
- **PA-10** — Tema 990 **pos-Lei 14.454** — citar como Rol **exemplificativo** (nao taxativo).
- **PA-11** — Rol ANS em atualizacao -> `[VERIFICAR RN vigente]`.
- **PA-13** — Lei 9.656 + Lei 14.454 + CDC com identificacao precisa.
- **PA-14** — inversao do onus fundamentada (CDC 6o VIII + Sum. 469).
- **PA-21** — quantum conservador.

## 11. Protocolos acionados

- **P1** — Selo (Rol vigente + jurisprudencia pos-Lei 14.454).
- **P3** — memoria de quantum.
- **P5** — JE comarca do domicilio do autor (CDC 101 I).
- **P6** — `revisao-final-medica`.

## 12. Localizacao

JE comarca do domicilio do consumidor (CDC art. 101 I). Foro de eleicao desconsiderado em relacao consumerista.

## 13. Integracao

**Chamada por:** `medico-master`, `triagem-medica`, `tutela-urgencia-plano-saude`.

**Entrega para:** peticao inicial com tutela + memoria de quantum -> `revisao-final-medica` -> operador.

**Sem esta skill:** acao oncologica generica que ignora Lei 14.454 pos-2022 e os 5 criterios objetivos do art. 10§13 — tese vulneravel a contestacao tecnica.
