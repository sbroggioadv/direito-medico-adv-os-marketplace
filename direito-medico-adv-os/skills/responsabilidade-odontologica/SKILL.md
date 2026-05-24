---
name: responsabilidade-odontologica
description: >
  Skill especializada em responsabilidade civil em odontologia (CFO — Lei 5.081/1966 + Res. CFO 118/2012 CEO). Aplica STJ Sum. 597 (CDC aplica odontologia + carencia abusiva > 24h em urgencia), REsp 1.715.082 (implantodontia obrigacao de resultado), REsp 985.888 (clareamento dentário). Distincao subdominios: ortodontia (parcialmente meio, parcialmente resultado), endodontia (meio), implantodontia (resultado — osseointegracao), estetica dental — clareamento/lentes (resultado), cirurgia bucomaxilo (meio salvo estetica), periodontia (meio), HOF — Harmonizacao Orofacial (Res. CFM 2.337/2023 x Res. CFO 230/2020 — conflito interconselhos). Defesa do cirurgiao-dentista. Aciona: responsabilidade odontologica, CFO, Sum 597 STJ, implante dental, ortodontia falha, endodontia, clareamento dental, lentes de contato dental, HOF dentista, cirurgia bucomaxilo, periodontia, REsp 1.715.082.
---

# RESPONSABILIDADE ODONTOLOGICA

> Skill **Tier 2** — RC em odontologia. Implementa PA-15 (meio x resultado por subdominio), PA-13 (citacao precisa), PA-19 (prescricao). Acionada por `medico-master`, `triagem-medica` (subdominio odontologia), `responsabilidade-civil-medica` (irmao).

---

## 0. Escopo e acionamento

Acionada em demanda envolvendo cirurgiao-dentista (PF) ou clinica odontologica (PJ) — defesa do CD, ou ação do paciente, ou consultivo preventivo a clinica odonto. Cobre todas as subespecialidades: ortodontia, endodontia, implantodontia, estetica dental, cirurgia bucomaxilo, periodontia, HOF.

## 1. Posicao na orquestra

- **Chamada por:** `medico-master`, `triagem-medica` (subdominio odontologia), `responsabilidade-civil-medica`.
- **Aciona:** `analise-tcle`/`tcle-especialidades` (ortodontia, implante, HOF, clareamento), `analise-prontuario-medico`, `analise-pericia-medica`, `prescricao-erro-medico`.
- **Entrega para:** peca civel (autor/reu) + memoria de quantum.

## 2. Marco normativo

| Norma/precedente | Conteudo |
|------------------|----------|
| Lei 5.081/1966 | Regula o exercicio da odontologia |
| CC art. 951 + CDC art. 14 | Bases (igual a medicina) |
| Res. CFO 118/2012 | CEO — Codigo de Etica Odontologica |
| Res. CFO 71/2006 | PED CRO (Tier 4) |
| Res. CFO 196/2019 | Publicidade odontologica (Tier 6) |
| Res. CFO 287/2022 | Teleodontologia |
| Res. CFO 230/2020 | HOF — autorizacao do CD para procedimentos esteticos faciais |
| Res. CFM 2.337/2023 | HOF na perspectiva CFM — conflito |
| **STJ Sum. 597** | **CDC aplica odontologia + carencia abusiva > 24h em urgencia** |
| **STJ REsp 1.715.082/RJ** | **Implantodontia = obrigacao de resultado** (osseointegracao) |
| STJ REsp 985.888/SP | Clareamento dental — resultado |
| STJ REsp 1.633.453/RN | Ortodontia — caso a caso |

## 3. Regime por subespecialidade (PA-15)

| Subespecialidade | Regime | Justificativa | Defesa estrutural |
|------------------|--------|---------------|-------------------|
| **Implantodontia** | **Resultado** (osseointegracao — REsp 1.715.082) | Sucesso tecnico esperado | TCLE + planejamento (TC, modelo) + tecnica + acompanhamento + falha por fator do paciente (higiene, periimplantite, sobrecarga) |
| **Estetica dental** (clareamento, lentes de contato, facetas) | **Resultado** | Paciente nao-doente | TCLE realista + fotografia pre + plano de manutencao |
| **Ortodontia** | **Misto** — plano = meio; resultado estetico prometido = resultado (caso a caso) | Variabilidade biologica + adesao do paciente critica | TCLE com plano + duracao + manutencao + descumprimento do paciente |
| **Endodontia** | **Meio** | Variabilidade anatomica + complicacoes inerentes | TCLE + tecnica + radiografia |
| **Cirurgia bucomaxilo** | **Meio** (excluida estetica pura — resultado) | Procedimento reparador/funcional | Similar a cirurgia medica geral |
| **Periodontia** | **Meio** | Cronicidade + adesao do paciente | TCLE + plano + acompanhamento |
| **Protese dental** | **Resultado** (instalacao funcional+estetica) | Produto entregue tem que funcionar | TCLE + ajustes + retoques |
| **Odontopediatria** | **Meio** | Variabilidade do paciente pediatrico | TCLE com responsavel legal + cooperacao |
| **HOF — Harmonizacao Orofacial** | **Resultado** (estetico) — **conflito CFM x CFO** | Estetica pura | TCLE + autorizacao Res. CFO 230/2020 + competencia do CD na UF — `[VERIFICAR — conflito interconselhos]` |

## 4. CDC aplicado a odontologia (Sum. 597 STJ)

- CDC aplica-se integralmente a relacao CD-paciente (clinica/profissional).
- **Carencia abusiva > 24h em urgencia odontologica** — Sum. 597 — clausula nula.
- **Inversao do onus** — CDC art. 6o VIII + Sum. 469 STJ (planos odontologicos) / Sum. 597 (CDC odonto geral).

## 5. HOF — Harmonizacao Orofacial (conflito ativo)

**Status 2024-2026 `[VERIFICAR — afetacao]`:**
- Res. CFO 230/2020 admite HOF pelo CD habilitado (cursos especificos).
- Res. CFM 2.337/2023 restringe HOF: certos procedimentos sao **ato medico** (Lei 12.842/2013).
- Conflito interconselhos resolvido caso a caso por TRFs em ACPs — `[VERIFICAR — jurisprudencia local]`.
- **Defesa do CD (autor de HOF):** competencia da Res. CFO 230/2020 + habilitacao comprovada + TCLE adequado + procedimento dentro do nicho odonto-facial.
- **Ataque ao CD (pelo paciente):** se procedimento extrapolar HOF e for ato medico, base civel + PED CFO + eventual representacao no CFM.

## 6. Casos tipicos por subespecialidade

### 6.1 — Implantodontia (resultado)
**Falhas tipicas:** perimplantite por planejamento insuficiente; fratura ossea; sobrecarga oclusal; sensibilidade prolongada.
**Defesa:** planejamento documentado (TC, modelo de estudo); cirurgia tecnicamente correta; ossointegracao radiograficamente confirmada; descumprimento de higiene/manutencao pelo paciente.

### 6.2 — Ortodontia
**Falhas tipicas:** reabsorcao radicular, recidiva (recontensao mal-feita pelo paciente), maloclusao persistente, alergia ao bracket.
**Defesa:** TCLE com plano + duracao + manutencao + ausencia em retorno + descumprimento de uso de aparelho/contensao.

### 6.3 — Endodontia
**Falhas tipicas:** sobreobturacao, fratura de instrumento, perfuracao radicular, persistencia de infeccao.
**Defesa:** variabilidade anatomica + tecnica conforme literatura + radiografia + alternativas (extracao).

### 6.4 — Estetica (clareamento, lentes)
**Falhas tipicas:** sensibilidade prolongada, manchamento desigual, fratura de lente, mau-estetico.
**Defesa:** TCLE realista + fotografia pre + plano de manutencao + descumprimento (refrigerante, cafe).

### 6.5 — HOF
**Falhas tipicas:** assimetria, necrose por preenchedor mal-aplicado, ptose por toxina, infeccao.
**Defesa:** habilitacao Res. CFO 230/2020 + tecnica + TCLE + dentro do nicho.

## 7. Memoria de quantum (P3)

Conservadora (PA-21) — paralelo a estetica medica. Dano moral por procedimento odontologico falho: R$ 5-30k (caso simples) a R$ 50-150k (sequela grave, perda de elementos dentais, comprometimento mastigatorio). **`[VERIFICAR — atualizacao STJ]`**.

## 8. Esqueleto FIRAC — Peca civel odontologica

```
[Adaptacao do esqueleto de `responsabilidade-civil-medica`]

III — DIREITO
III.1 — Sujeito: CD-PF (CC art. 951 + CDC art. 14 §4o) / Clinica-PJ (CDC art. 14)
III.2 — Regime do procedimento (PA-15 — ver tabela 3):
        - Implante/estetica/protese = resultado (REsp 1.715.082 / REsp 985.888)
        - Endo/perio/ortodontia = meio
        - Misto: avaliacao especifica
III.3 — CDC aplicavel — Sum. 597 STJ
III.4 — Inversao do onus — CDC art. 6o VIII / Sum. 469
III.5 — Quantum conservador (P3)
```

## 9. Vedacoes especificas

- **PA-15** — regime por subespecialidade (tabela 3).
- **PA-13** — STJ Sum. 597 + REsp 1.715.082 sempre que aplicaveis.
- **PA-19** — prescricao identica: 3 anos CC (CD-PF autonomo) / 5 anos CDC (clinica PJ).
- **PA-11** — HOF, Lei 15.378/2026 e jurisprudencia em formacao -> `[VERIFICAR]`.
- **PA-08** — sem critica pessoal ao CD, ao paciente, ao perito-CD (CRO).
- **PA-21** — quantum conservador.

## 10. Protocolos acionados

- **P1** — Selo emitido.
- **P2** — analise de prontuario odonto + TCLE por subespecialidade + pericia.
- **P3** — memoria de quantum.
- **P5** — UF de inscricao do CD (PED CRO regional).
- **P6** — revisao R1-R4.

## 11. Localizacao

JE comarca do domicilio do autor (CDC art. 101 I). PED CRO sempre na UF de inscricao do CD (Res. CFO 71/2006). HOF — conflito interconselhos pode demandar acao na JF (ACP do CFM contra CFO ou vice-versa) — `[VERIFICAR — jurisprudencia local]`.

## 12. Integracao

**Chamada por:** `medico-master`, `triagem-medica` (subdominio odontologia), `responsabilidade-civil-medica`.

**Entrega para:** peca civel + insumo para `defesa-ped-cro` quando ha PED em paralelo (P4).

**Sem esta skill:** odontologia tratada como medicina geral perde particularidades — Sum. 597 ignorada, REsp 1.715.082 ignorado em implante, regime por subespecialidade confundido, HOF mal-articulado.
