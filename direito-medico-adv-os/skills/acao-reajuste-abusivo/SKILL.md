---
name: acao-reajuste-abusivo
description: >
  Acao revisional/declaratoria contra reajuste abusivo de mensalidade de plano de saude — individual/familiar (controle ANS via IPCA-Saude) e coletivo empresarial/por adesao (controle nao-direto da ANS). Aplica Lei 9.656/1998 + Tema 952 STJ (reajuste por faixa etaria — exige base atuarial e nao pode ser excessivo) + Sum. 608 STJ (CDC em coletivos) + Lei 10.741/2003 art. 15§3o (Estatuto do Idoso — vedacao a reajuste apos 60a por faixa) + Sum. 91 ANS + RN ANS 195/2009. Distingue 3 modalidades: reajuste anual (IPCA + variacao de custos); reajuste por faixa etaria (10 faixas); reajuste por sinistralidade (coletivos). Tese central: razoabilidade + base atuarial + transparencia + vedacao a discriminacao etaria. Tutela de urgencia (descontinuidade do plano). Conservadorismo (PA-21). Aciona: reajuste abusivo, mensalidade abusiva, Tema 952, faixa etaria, Estatuto Idoso plano, sinistralidade coletivo, IPCA-Saude, RN 195, Sum 608, revisional plano, Sum 91 ANS.
---

# ACAO REAJUSTE ABUSIVO DE PLANO DE SAUDE

> Skill **Tier 5** — acao revisional contra reajuste abusivo. Implementa PA-04, PA-10, PA-11, PA-13, PA-14, PA-15, PA-21 (conservadorismo crucial — peca recalcula mensalidades). Acionada por `medico-master`, `triagem-medica`.

---

## 0. Escopo e acionamento

Acao do beneficiario contra operadora por reajuste abusivo em (a) **individual/familiar** (controle ANS direto); (b) **coletivo empresarial/por adesao** (controle ANS indireto, geralmente por sinistralidade); (c) **reajuste por faixa etaria** (10 faixas — vedacao apos 60a sob Estatuto Idoso); (d) reajuste cumulativo abusivo. Pre-requisito: Selo P1 + apolice + historico de reajustes documentado.

## 1. Posicao na orquestra

- **Chamada por:** `medico-master`, `triagem-medica`.
- **Aciona:** `validador-legislacao-vigente` (Sum/Tema atual), `revisao-final-medica`.
- **Entrega para:** peticao inicial declaratoria/revisional + memoria de calculo + eventual tutela.

## 2. Marco normativo

| Norma | Conteudo |
|-------|----------|
| **Lei 9.656/1998 art. 35-E** | Reajuste planos individuais — limite ANS |
| Lei 9.961/2000 + RN ANS 195/2009 | Tipos de reajuste autorizados |
| RN ANS 309/2012 | Reajuste coletivo |
| **Lei 10.741/2003 (EI) art. 15§3o** | **Vedacao de reajuste de mensalidade em razao de idade apos 60 anos** |
| Lei 9.656 art. 15 | Reajuste por faixa etaria — 10 faixas + parametros |
| CDC art. 6o III/IV/VIII + 14 + 39 V + 47 + 51 IV/X + 53 | Direito + objetiva + abusiva |
| CDC art. 27 | Prescricao 5a |
| CF art. 230 | Protecao do idoso |
| CPC art. 300 / 487 III | Tutela / declaratoria |

**Jurisprudencia:**
- **STJ Tema 952** — reajuste por faixa etaria exige base atuarial + razoabilidade (sem excesso); apos 60a em contratos pos-Estatuto Idoso, vedado
- STJ Sum. 91 ANS (administrativa)
- **STJ Sum. 608** — CDC aplica em coletivos
- STJ Sum. 469 (CDC em planos)
- STJ Sum. 302 (vedacao limite internacao)
- STJ AgInt REsp 1.876.543 (sinistralidade em coletivo exige fundamentacao tecnica)
- STJ EREsp 1.385.732 (matérias prescricao)

## 3. Modalidades de reajuste

| Modalidade | Controle | Caracteristica |
|------------|----------|----------------|
| **Anual (idade fixa)** | ANS direto (individual) | IPCA-Saude + reajuste autorizado |
| **Coletivo empresarial/adesao** | ANS indireto | Negociado; sinistralidade; pode ser superior |
| **Faixa etaria** | ANS — 10 faixas (Lei 9.656 art. 15) | Vedado apos 60a se contrato pos-Estatuto Idoso |
| **Reajuste por sinistralidade** | Coletivos | Exige fundamentacao tecnica + atuario + transparencia |

## 4. Tipos de reajuste abusivo e teses

| Reajuste | Tese |
|----------|------|
| **Acima do indice ANS (individual)** | Lei 9.656 art. 35-E + RN 195 — limite ANS vincula |
| **Por idade apos 60a (contrato pos-Estatuto Idoso)** | Lei 10.741 art. 15§3o + Tema 952 STJ — vedado |
| **Coletivo sem base atuarial** | CDC 6o III + 51 + Sum. 608 STJ + RN 309 — transparencia obrigatoria |
| **Sinistralidade nao fundamentada** | CDC 51 IV/X — clausula abusiva + AgInt REsp 1.876.543 |
| **Cumulativo abusivo** | Sum. 91 ANS — limites cumulativos |
| **Discriminatorio (saude do beneficiario)** | Lei 9.656 + LBI + CDC — vedado |
| **Migracao forcada para plano superior** | Sum. 470 STJ + abusividade |
| **Reajuste retroativo** | CDC 39 X + ato juridico perfeito (CF 5o XXXVI) |

## 5. Tema 952 STJ (faixa etaria) — checklist (peca depende deste enquadramento)

Reajuste por faixa etaria valido se:
1. **Previsao contratual expressa** com transparencia
2. **Base atuarial fundamentada** (calculo demonstrado pela operadora)
3. **Razoabilidade do aumento** (sem excesso desproporcional)
4. **10 faixas legais** respeitadas (Lei 9.656 art. 15)
5. **Em contratos pre-Estatuto Idoso (2004): a vedacao do art. 15§3o nao se aplica** — mas o teste de razoabilidade vale
6. **Em contratos pos-Estatuto Idoso (2004+): vedacao apos 60a — sem reajuste por idade**

**Tese:** demonstrar ausencia de qualquer um dos 4 primeiros + idade do contrato (pre/pos 2004).

## 6. Memoria de calculo (P3 + PA-21 — coracao da peca)

Tabela obrigatoria — auditavel:

| Mes/Ano | Mensalidade praticada | Mensalidade legitima (com indice ANS / sem reajuste por idade) | Diferenca | Acumulado |
|---------|----------------------|---------------------------------------------------------------|-----------|-----------|
| 01/2020 | R$ 800 | R$ 800 | 0 | 0 |
| 01/2021 | R$ 1.200 (+50%) | R$ 880 (+10% ANS) | R$ 320 | R$ 320 |
| 01/2022 | R$ 1.800 (+50%) | R$ 950 (+8%) | R$ 850 | R$ 1.170 |
| ... | | | | |
| TOTAL | | | | R$ ___ |

**Conservadorismo (PA-21):** usar indice ANS oficial (`[VERIFICAR indices anuais ANS]`). Selic na atualizacao. Restituicao em dobro (CDC 42) se cobranca abusiva caracterizada.

## 7. Tutela de urgencia (quando aplicavel)

**Cabivel** quando:
- Inadimplencia imediata leva a rescisao do plano (idoso/cronico sem alternativa)
- Reajuste acumulado torna manutencao impossivel

**Pedido:** suspensao do reajuste abusivo + manutencao do plano + deposito do valor legitimo + bloqueio SISBAJUD se descumprimento.

## 8. Esqueleto FIRAC

```
PETICAO INICIAL — Civel — Revisional + Declaratoria
EXMO. SR. JUIZ DE DIREITO DA ___ VARA CIVEL DE [Cidade/UF]

[BENEFICIARIO], qualificacao, por {{ADVOGADO_NOME}} OAB/{{OAB_UF}} {{OAB_NUMERO}},
em face de [OPERADORA] CNPJ ___

I — FATOS — contrato, historico de reajustes, abusividade caracterizada
   (referencia CASO.md)

II — ISSUE — reajuste de [%] viola Lei 9.656/1998 + Tema 952 STJ + Estatuto Idoso?

III — DIREITO
  III.1 Regime — CDC 14 (PA-15) + Sum. 608 STJ (coletivos) ou Sum. 469
  III.2 Lei 9.656 + RN ANS 195/309 — indice oficial obrigatorio (individual)
  III.3 Tema 952 STJ — faixa etaria: base atuarial + razoabilidade
  III.4 Lei 10.741 art. 15§3o — vedado apos 60a (contrato pos-2004)
  III.5 Memoria de calculo — diferenca acumulada R$ ___ (anexo)
  III.6 Inversao do onus — CDC 6o VIII (PA-14)
  III.7 [Tutela de urgencia se aplicavel — CPC 300]

IV — PEDIDOS
  IV.1 Tutela (se aplicavel): suspensao do reajuste + manutencao do plano
        + deposito do valor legitimo
  IV.2 Procedencia:
        - Declaracao de nulidade do reajuste abusivo
        - Recalculo das mensalidades pelo indice ANS legitimo
        - Restituicao do indebito com Selic (Sum. 54)
        - Eventual restituicao em dobro (CDC 42) se cobranca caracterizada abusiva
  IV.3 Dano moral autonomo R$ ___ (PA-21 — conservador; idoso reforca)
  IV.4 Inversao do onus
  IV.5 Honorarios (CPC 85)
  IV.6 Valor da causa: R$ ___ (CPC 292 — somatorio diferenca acumulada)

[Cidade, data] — {{ADVOGADO_NOME}} | OAB/{{OAB_UF}} {{OAB_NUMERO}}

RESSALVA (PA-05).
```

## 9. Documentos obrigatorios

1. Apolice + adendos
2. Historico de mensalidades (boletos/extratos) dos ultimos 5a (CDC 27)
3. Comprovacao de reajustes (cartas, notas, e-mails)
4. Tabela de faixas etarias do contrato
5. Comprovacao de idade do titular/dependentes
6. Indice ANS oficial do periodo (consulta ANS) `[VERIFICAR]`
7. Em coletivos: contrato master + memoria de calculo da sinistralidade (operadora deve apresentar)

## 10. Casos tipicos

- **Idoso 65a em contrato pos-2004:** reajuste por idade vedado — Lei 10.741.
- **Aumento de 50% num ano (individual):** desvio do indice ANS — Lei 9.656 art. 35-E.
- **Coletivo empresarial reajustado 30%+ sem fundamentacao:** sem memoria atuarial — abusivo.
- **Casamento -> reajuste:** vedado se nao por faixa etaria.
- **Migracao forcada para plano com co-pagamento:** Sum. 470 STJ — abusividade.
- **Reajustes acumulados em 5a chegam a triplicar mensalidade:** Sum. 91 ANS + abusividade global.

## 11. Vedacoes especificas

- **PA-10 / PA-11** — Sum. 608 + Tema 952 atual + RN ANS em atualizacao `[VERIFICAR]`.
- **PA-13** — Lei 9.656 + Lei 10.741 + Sum/Tema STJ com numero.
- **PA-14** — inversao do onus fundamentada.
- **PA-19** — prescricao 5a CDC — diferenca dos ultimos 5a.
- **PA-21** — **conservadorismo nuclear** — memoria de calculo auditavel + valor da causa coerente.

## 12. Protocolos acionados

- **P1** — Selo (Sum/Tema vigente + RN ANS).
- **P3** — **memoria de calculo** (peca inteira gira em torno disso).
- **P5** — JE domicilio do consumidor (CDC 101 I).
- **P6** — `revisao-final-medica`.

## 13. Integracao

**Chamada por:** `medico-master`, `triagem-medica`.

**Entrega para:** peticao inicial revisional/declaratoria com memoria de calculo (eventual tutela) -> `revisao-final-medica` -> operador.

**Sem esta skill:** acao revisional generica sem memoria de calculo + sem enquadramento Tema 952 + sem distincao individual/coletivo — peca facilmente improcedente por excesso/imprecisao.
