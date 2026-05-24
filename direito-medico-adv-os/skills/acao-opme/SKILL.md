---
name: acao-opme
description: >
  Acao contra operadora por glosa ou imposicao de marca/fornecedor em Orteses, Proteses e Materiais Especiais (OPME) prescritos pelo medico assistente — protese ortopedica, marca-passo, stent, valvulas cardiacas, neuroestimulador, lente intraocular, implantes de coluna, cirurgia bariatrica. Aplica Lei 9.656/1998 art. 10§4o (cobertura obrigatoria de OPME) + Lei 14.454/2022 (Rol exemplificativo) + STJ REsp 1.733.013/PR (operadora nao impoe marca; prevalece prescricao medica fundamentada) + Tema 990 + Sum. 469 STJ. Distingue OPME coberta (vinculada a procedimento do Rol) de OPME nao coberta. Tese central: autonomia tecnica (Lei 12.842/2013 art. 4o) + prescricao fundamentada vs poder regulatorio. Tutela de urgencia. Aciona: OPME negada, glosa material cirurgico, REsp 1.733.013, marca implante, stent, marca-passo, valvula cardiaca, lente intraocular, autonomia medica.
---

# ACAO DE OPME (Orteses, Proteses, Materiais Especiais)

> Skill **Tier 5** — acao contra operadora por glosa/imposicao de marca/fornecedor em OPME. Implementa PA-04, PA-10, PA-11, PA-13, PA-14, PA-15 (CDC 14 objetiva), PA-21. Acionada por `medico-master`, `triagem-medica`, `tutela-urgencia-plano-saude`.

---

## 0. Escopo e acionamento

Acao do paciente contra operadora em (a) negativa de OPME prescrito pelo medico assistente em procedimento cirurgico coberto; (b) imposicao de marca/fornecedor diversa da prescricao fundamentada (substituicao por equivalencia controversa); (c) glosa de material apresentado em internacao; (d) recusa de revisao de OPME (troca de protese desgastada, marca-passo). Pre-requisito: Selo P1 + parecer cirurgiao + 3 cotacoes (norma ANS).

## 1. Posicao na orquestra

- **Chamada por:** `medico-master`, `triagem-medica`, `tutela-urgencia-plano-saude`.
- **Aciona:** `tutela-urgencia-plano-saude`, `validador-legislacao-vigente`, `revisao-final-medica`.
- **Entrega para:** peticao inicial com tutela + memoria de quantum.

## 2. Marco normativo

| Norma | Conteudo |
|-------|----------|
| **Lei 9.656/1998 art. 10§4o** | Cobertura de OPME — ligada a procedimento cirurgico do Rol |
| **Lei 14.454/2022** | Rol exemplificativo (art. 10§13) — aplicavel a OPME |
| Lei 12.842/2013 art. 4o V/VII | **Autonomia tecnica do medico** — prescricao e ato medico |
| RN ANS 424/2017 | Comissao tecnica de OPME (procedimento institucional) `[VERIFICAR atual]` |
| RN ANS 465/2021+ | Rol vigente |
| CDC art. 6o III/VIII + 14 + 47 + 51 IV | Direitos + objetiva + inversao + nulidade abusiva |
| CDC art. 27 | Prescricao 5a |
| Lei 10.741/2003 / Lei 13.146/2015 | Protecoes especiais |
| CPC 300 / 537 | Tutela + astreintes |

**Jurisprudencia:**
- **STJ REsp 1.733.013/PR** — operadora **nao pode impor marca** se prescricao medica e fundamentada
- STJ REsp 1.815.071/PR — paciente nao paga por marca diversa imposta
- STJ AgInt REsp 1.892.453 — distincao OPME funcional x marca-especifica
- STJ Sum. 469 / 597 / 608

## 3. Estrutura da tese (3 eixos)

| Eixo | Conteudo |
|------|----------|
| **1. Cobertura do procedimento principal** | Cirurgia esta no Rol -> OPME vinculada e devida (Lei 9.656 §4o) |
| **2. Autonomia tecnica da prescricao** | Lei 12.842/2013 art. 4o V/VII — medico assistente escolhe marca **fundamentadamente** (caracteristicas tecnicas especificas: tipo, tamanho, material, performance) |
| **3. Vedacao a imposicao da operadora** | REsp 1.733.013 — operadora pode oferecer alternativa equivalente, **nao pode impor**; ausencia de equivalencia funcional invalida a recusa |

## 4. Tipos de negativa e teses

| Negativa | Tese |
|----------|------|
| **"OPME nao consta do Rol"** | Vinculacao ao procedimento principal coberto + Lei 14.454 |
| **"Marca substituida por equivalente"** | REsp 1.733.013 — operadora nao impoe; prescricao fundamentada prevalece |
| **"OPME importada nao coberta"** | RN 424 prescreve criterios — ausencia nacional + fundamentacao + ANVISA regular |
| **"OPME experimental"** | Distinguir — registrada ANVISA = nao experimental |
| **"Co-participacao excessiva"** | Lei 9.656 + Sum. 469 — co-participacao abusiva e nula |
| **"Limite de internacao"** | Sum. 302 STJ — vedacao |
| **Glosa pos-cirurgia (cobranca do paciente)** | CDC 39 V — cobranca abusiva — restituicao em dobro |

## 5. Prescricao medica fundamentada (PA-13 — ponto critico)

A operadora **pode** propor alternativa equivalente quando a prescricao for **generica** ("colocar protese"). Quando a prescricao for **fundamentada tecnicamente** ("protese X com caracteristicas Y, Z, W por motivos A, B, C"), a substituicao e vedada.

**Estrategia:** **toda peca traz a prescricao fundamentada como anexo nuclear** — sem ela, a operadora vence pelo argumento de equivalencia.

## 6. Tutela de urgencia

**Fumus:** Lei 9.656 §4o + Lei 14.454 + REsp 1.733.013 + prescricao fundamentada + Sum. 469.

**Periculum:** procedimento cirurgico agendado; cancelamento gera atraso clinico (cardiologico — instabilidade hemodinamica; ortopedico — sequela funcional); paciente em pos-op aguarda revisao.

**Pedido:** custeio + bloqueio SISBAJUD + astreintes proporcionais.

## 7. Memoria de quantum (P3 + PA-21)

| Item | Base |
|------|------|
| Custeio integral do OPME prescrito | Cotacao oficial + 3 propostas RN 424 |
| Reembolso de desembolso (se paciente pagou) | Selic + restituicao em dobro se cobranca abusiva (CDC 42) |
| Dano moral autonomo | Conservador (PA-21) — atraso de procedimento |
| Astreintes | Proporcionais |

## 8. Esqueleto FIRAC

```
PETICAO INICIAL — Civel com tutela
EXMO. SR. JUIZ DE DIREITO DA ___ VARA CIVEL DE [Cidade/UF]

[PACIENTE], qualificacao, por {{ADVOGADO_NOME}} OAB/{{OAB_UF}} {{OAB_NUMERO}},
em face de [OPERADORA] CNPJ ___

I — FATOS — diagnostico, indicacao cirurgica, prescricao fundamentada de OPME,
   negativa/imposicao de marca (referencia CASO.md)

II — ISSUE — negativa/imposicao viola Lei 9.656 art. 10§4o + REsp 1.733.013?

III — DIREITO
  III.1 Regime — CDC 14 (PA-15) + Sum. 469 STJ
  III.2 Lei 9.656 art. 10§4o — OPME ligada a procedimento do Rol
  III.3 Lei 12.842/2013 art. 4o V/VII — autonomia tecnica do medico
  III.4 STJ REsp 1.733.013 — vedada imposicao de marca pela operadora
  III.5 Prescricao fundamentada (anexo X) — caracteristicas tecnicas especificas
  III.6 Lei 14.454/2022 se aplicavel
  III.7 Inversao do onus — CDC 6o VIII (PA-14)

IV — PEDIDOS
  IV.1 Tutela: custeio integral do OPME prescrito + astreintes R$ ___ + SISBAJUD
  IV.2 Procedencia + reembolso com Selic + restituicao em dobro (CDC 42)
        se houver cobranca abusiva
  IV.3 Dano moral autonomo (PA-21)
  IV.4 Inversao do onus
  IV.5 Honorarios

[Cidade, data] — {{ADVOGADO_NOME}} | OAB/{{OAB_UF}} {{OAB_NUMERO}}

RESSALVA (PA-05).
```

## 9. Documentos obrigatorios

1. Apolice + cobertura
2. Carteirinha vigente
3. **Prescricao medica fundamentada** — relatorio do cirurgiao detalhando: tipo de OPME, marca, modelo, caracteristicas tecnicas (material, dimensao, performance), justificativa clinica de cada item
4. 3 cotacoes oficiais (norma ANS RN 424)
5. Negativa formal da operadora (ou imposicao formal de marca diversa)
6. Bula/registro ANVISA do OPME prescrito
7. Parecer da sociedade de especialidade (SBC, SBOT, SBN, SBC-Ophtalmologia) se aplicavel

## 10. Casos tipicos

- **Marca-passo bicameral com sensor de adaptacao:** prescricao fundamentada (Lei 12.842 + parecer SBC); operadora propoe basico — REsp 1.733.013.
- **Stent farmacologico vs metalico:** indicacao por risco de re-estenose; operadora propoe convencional — fundamentacao clinica + diretriz SBC.
- **Implante de coluna (cage + placas + parafusos):** complexo + multimaterial; operadora glosa itens isolados.
- **Lente intraocular toricia/multifocal:** parte cobertura + parte estetica — distinguir; cobre componente funcional.
- **Protese de quadril/joelho importada:** ausencia nacional + ANVISA regular.
- **Cirurgia bariatrica (clipes, grampos, instrumentais):** integralidade do procedimento.

## 11. Vedacoes especificas

- **PA-03** — sem opinar conduta clinica; a tese e juridica (Lei 12.842 + REsp).
- **PA-10 / PA-11** — STJ atual + Rol em atualizacao `[VERIFICAR]`.
- **PA-13** — Lei 9.656 + 12.842 + REsp 1.733.013 com identificacao precisa.
- **PA-14** — inversao do onus fundamentada.
- **PA-21** — quantum e astreintes proporcionais.

## 12. Protocolos acionados

- **P1** — Selo.
- **P3** — memoria de quantum.
- **P5** — JE domicilio do autor (CDC 101 I).
- **P6** — `revisao-final-medica`.

## 13. Integracao

**Chamada por:** `medico-master`, `triagem-medica`, `tutela-urgencia-plano-saude`.

**Entrega para:** peticao inicial com tutela + memoria -> `revisao-final-medica` -> operador.

**Sem esta skill:** acao OPME generica que ignora REsp 1.733.013 + autonomia tecnica + prescricao fundamentada — operadora ganha argumento de equivalencia.
