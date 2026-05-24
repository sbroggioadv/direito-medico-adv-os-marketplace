---
name: acao-rescisao-coletivo
description: >
  Acao do beneficiario contra rescisao/descredenciamento unilateral de plano coletivo empresarial ou por adesao. Aplica Lei 9.656/1998 art. 13 paragrafo unico (vedacao a rescisao unilateral em individual; coletivo tem regime diferente) + Tema 1.082 STJ (rescisao coletivo exige aviso 60 dias + manutencao para beneficiario em tratamento medico em curso de doenca grave) + RN ANS 412/2016 (portabilidade especial em rescisao unilateral) + Sum. 608 STJ. Tese central: protecao do beneficiario em tratamento (manutencao); portabilidade especial; vedacao de seletividade (rescisao seletiva discriminatoria). Tutela de urgencia para manter o plano enquanto tramita a demanda — tempo-dependente (paciente em quimioterapia, dialise, transplante). Conservadorismo (PA-21). Aciona: rescisao coletivo, descredenciamento plano, Tema 1082 STJ, doenca grave manutencao plano, portabilidade especial, RN 412, plano empresarial cancelado, dialise plano, transplante em curso, quimioterapia plano cortado.
---

# ACAO RESCISAO DE PLANO COLETIVO

> Skill **Tier 5** — acao contra rescisao/descredenciamento unilateral em plano coletivo. Implementa PA-04, PA-10 (Tema 1.082 STJ), PA-11, PA-13, PA-14, PA-15, PA-21. Acionada por `medico-master`, `triagem-medica`, `tutela-urgencia-plano-saude`.

---

## 0. Escopo e acionamento

Acao do beneficiario contra (a) **rescisao unilateral** do contrato coletivo (empresarial ou por adesao) pela operadora ou pela pessoa juridica contratante; (b) **descredenciamento** de hospital/clinica/medico nuclear ao tratamento; (c) negativa de **portabilidade especial** (RN ANS 412). Aplica-se quando beneficiario esta em **tratamento medico em curso de doenca grave** (oncologico, dialise, transplante, gestacao de risco, doenca cronica em fase aguda). Pre-requisito: Selo P1 + comprovacao do tratamento em curso.

## 1. Posicao na orquestra

- **Chamada por:** `medico-master`, `triagem-medica`, `tutela-urgencia-plano-saude`.
- **Aciona:** `tutela-urgencia-plano-saude` (modelo unificado), `validador-legislacao-vigente`, `revisao-final-medica`.
- **Entrega para:** peticao inicial com tutela + memoria de quantum.

## 2. Marco normativo

| Norma | Conteudo |
|-------|----------|
| **Lei 9.656/1998 art. 13 paragrafo unico** | Vedacao de rescisao unilateral em individual (a contrario sensu — coletivo permite mas com limites) |
| Lei 9.656 art. 17-19 | Cobertura assistencial + transparencia |
| **RN ANS 412/2016** | Portabilidade especial em rescisao unilateral `[VERIFICAR atual]` |
| RN ANS 195/2009 + 309/2012 | Reajuste coletivo |
| CDC art. 6o III/VIII + 14 + 47 + 51 | Direitos consumeristas |
| **Sum. 608 STJ** | CDC em coletivos empresariais/adesao |
| CDC art. 27 | Prescricao 5a |
| Lei 10.741/2003 / Lei 13.146/2015 | Protecoes especiais |
| CPC 300 / 537 | Tutela + astreintes |

**Jurisprudencia:**
- **STJ Tema 1.082** — rescisao coletivo exige (a) aviso previo 60d; (b) **manutencao do beneficiario em tratamento medico em curso de doenca grave** ate completar 12 meses ou tratamento concluir
- STJ Sum. 608 (CDC em coletivos)
- STJ AgInt REsp 1.876.543 (manutencao em transplante / quimioterapia)
- STJ Sum. 469 (CDC em planos)
- TJSP / TJRJ — tutela quase sempre concedida em doenca grave

## 3. Tema 1.082 STJ (coracao da peca)

**Premissa:** o plano coletivo pode ser rescindido, mas a operadora deve:

1. **Aviso previo de 60 dias** (RN ANS + jurisprudencia)
2. **Manutencao do beneficiario em tratamento medico em curso de doenca grave** — ate (a) 12 meses; ou (b) conclusao do tratamento, o que for menor; ou (c) prazo determinado pela natureza do tratamento (transplante, dialise — extensao razoavel)
3. **Portabilidade especial** — direito a migrar para outro plano sem carencia (RN 412)
4. **Vedacao de seletividade** — rescisao individualizada e discriminatoria

**Tese:** demonstrar (a) tratamento em curso; (b) doenca grave; (c) negativa de manutencao/portabilidade — procedencia consolidada.

## 4. Tipos de rescisao/descredenciamento e teses

| Tipo | Tese |
|------|------|
| **Rescisao unilateral por inadimplencia de PJ** | Sem aviso 60d + sem manutencao = abusiva |
| **Descredenciamento hospital nuclear** | Lei 9.656 + RN ANS 365 + Sum. 608 — sem equivalencia, vedado |
| **Descredenciamento medico assistente em tratamento** | Tema 1.082 + continuidade do cuidado |
| **Recusa de portabilidade especial** | RN 412 + Lei 9.656 — direito do beneficiario |
| **Rescisao seletiva (sinistralidade individualizada)** | CDC 39 X + discriminacao vedada |
| **Migracao forcada** | Sum. 470 STJ + abusividade |
| **Falta de comunicacao formal** | CDC 6o III — informacao adequada |

## 5. Conceito de "doenca grave em tratamento" (PA-13)

Definicao jurisprudencial — sem rol exaustivo, mas tipicamente:
- Oncologico em quimio/radio/imuno
- Cardiaco em fase pos-operatoria/aguarda transplante
- Renal em dialise/aguarda transplante
- Gestacao de risco / parto iminente
- Neurologico (AVC em recuperacao, SCA)
- TEA em terapia intensiva (cruzar com `acao-tea-multidisciplinar`)
- HIV em terapia antirretroviral
- Transplantado em imunossupressao

**Estrategia:** ancorar com laudo medico atualizado + protocolo + CID + estagio.

## 6. Tutela de urgencia (CPC 300) — nuclear

**Fumus:** Lei 9.656 + Tema 1.082 + Sum. 608 + laudo medico + comprovacao do tratamento.

**Periculum:** descontinuidade do tratamento de doenca grave — risco a vida/saude — janela tempo-critica. Cancer interrompido perde janela; dialise sem cobertura -> internacao SUS em urgencia.

**Pedido:** manutencao do plano + cobertura integral durante a tramitacao + astreintes proporcionais + bloqueio SISBAJUD se descumprimento.

## 7. Memoria de quantum (P3 + PA-21)

| Item | Base |
|------|------|
| Manutencao do custeio (mensalidade x prazo) | Lei 9.656 + Tema 1.082 |
| Reembolso por desembolso proprio | Selic + restituicao em dobro CDC 42 se cobranca abusiva |
| Dano moral autonomo | Conservador (PA-21) — paciente em tratamento reforca |
| Astreintes | Proporcionais |

## 8. Esqueleto FIRAC

```
PETICAO INICIAL — Civel com tutela de urgencia
EXMO. SR. JUIZ DE DIREITO DA ___ VARA CIVEL DE [Cidade/UF]

[BENEFICIARIO], qualificacao, por {{ADVOGADO_NOME}} OAB/{{OAB_UF}} {{OAB_NUMERO}},
em face de [OPERADORA] CNPJ ___ (e/ou [PJ CONTRATANTE])

I — FATOS — contrato coletivo, diagnostico e tratamento em curso,
   rescisao/descredenciamento em [data] (referencia CASO.md)

II — ISSUE — rescisao/descredenciamento viola Lei 9.656 + Tema 1.082 STJ + RN 412?

III — DIREITO
  III.1 Regime — CDC 14 + Sum. 608 STJ (PA-15)
  III.2 Tema 1.082 STJ — manutencao obrigatoria em tratamento grave
  III.3 RN ANS 412/2016 — portabilidade especial sem carencia
  III.4 Laudo medico — doenca grave em curso (CID + estagio)
  III.5 Inversao do onus — CDC 6o VIII (PA-14)
  III.6 Tutela de urgencia — CPC 300 (probabilidade + periculum tempo-critico)

IV — PEDIDOS
  IV.1 Tutela: manutencao integral do plano + cobertura assistencial integral
        durante a tramitacao + astreintes R$ ___ proporcionais + SISBAJUD
  IV.2 Procedencia:
        - Manutencao definitiva ate conclusao do tratamento ou 12m (o que ocorrer
          primeiro) — Tema 1.082
        - Subsidiariamente: portabilidade especial sem carencia (RN 412)
        - Reembolso de desembolsos com Selic + restituicao em dobro se cobranca
          abusiva (CDC 42)
  IV.3 Dano moral autonomo R$ ___ (PA-21 conservador)
  IV.4 Inversao do onus
  IV.5 Honorarios (CPC 85)

[Cidade, data] — {{ADVOGADO_NOME}} | OAB/{{OAB_UF}} {{OAB_NUMERO}}

RESSALVA (PA-05).
```

## 9. Documentos obrigatorios

1. Apolice / contrato coletivo + adendos
2. Carteirinha vigente
3. Comprovacao da rescisao/descredenciamento (carta, e-mail, notificacao da PJ)
4. **Laudo medico atualizado** — diagnostico (CID) + estagio + tratamento em curso + impossibilidade de interrupcao
5. Comprovacao do tratamento em curso (receitas, exames, agendamento, prontuario hospitalar)
6. Em transplante/dialise: cadastro nacional + protocolo SUS / privado
7. Demonstrativo de pagamento das ultimas mensalidades
8. Em coletivo por adesao: comprovacao de vinculo associativo/sindical

## 10. Casos tipicos

- **Paciente oncologica em quimioterapia ativa — coletivo rescindido por PJ:** Tema 1.082 vence.
- **Renal cronico em dialise + cadastro de transplante:** continuidade obrigatoria.
- **Gestante de risco no terceiro trimestre — plano rescindido:** manutencao ate puerperio.
- **Crianca TEA em terapia ABA intensiva:** doenca cronica em fase aguda — cruzar com `acao-tea-multidisciplinar`.
- **Idoso pos-AVC em home care:** manutencao + cruzar `acao-home-care`.
- **Descredenciamento de hospital de referencia em meio a tratamento:** distincao da rescisao do contrato; continuidade do prestador.
- **Migracao forcada para plano com co-pagamento:** Sum. 470 STJ + abusividade.

## 11. Vedacoes especificas

- **PA-10** — Tema 1.082 vigente.
- **PA-11** — RN ANS em atualizacao `[VERIFICAR RN 412 atual]`.
- **PA-13** — Lei 9.656 + Tema 1.082 + RN com identificacao precisa.
- **PA-14** — inversao do onus.
- **PA-21** — quantum/astreintes proporcionais.

## 12. Protocolos acionados

- **P1** — Selo.
- **P3** — memoria de quantum.
- **P5** — JE domicilio do consumidor (CDC 101 I).
- **P6** — `revisao-final-medica`.

## 13. Integracao

**Chamada por:** `medico-master`, `triagem-medica`, `tutela-urgencia-plano-saude`.

**Entrega para:** peticao inicial com tutela + memoria -> `revisao-final-medica` -> operador.

**Sem esta skill:** acao generica que perde Tema 1.082 (manutencao em doenca grave) + RN 412 (portabilidade especial) — risco de descontinuidade do tratamento.
