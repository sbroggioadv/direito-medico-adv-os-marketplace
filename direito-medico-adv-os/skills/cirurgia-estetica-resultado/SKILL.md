---
name: cirurgia-estetica-resultado
description: >
  Skill especializada em responsabilidade civil em cirurgia plastica estetica e procedimentos esteticos (botox, preenchedor, peeling profundo, lipo, mamoplastia, abdominoplastia, blefaroplastia, ritidoplastia). Aplica STJ REsp 1.526.466/RS, REsp 985.888/SP e REsp 1.395.254/SC — **obrigacao de resultado** (inversao da presuncao: medico/clinica prova que resultado nao-alcance decorre de causa alheia). Distincao critica meio (estetica reparadora pos-trauma/oncologica) x resultado (estetica pura). Defesa do medico estetico: TCLE realista, fotografia pre-procedimento, plano de seguimento, descumprimento do paciente (orientacoes nao-seguidas, cuidados pos-operatorios). Conservadorismo no quantum (PA-21) — STJ corta valores inflados. Aciona: cirurgia plastica estetica, REsp 1.526.466, obrigacao de resultado, mamoplastia, abdominoplastia, lipo, blefaroplastia, ritidoplastia, botox, preenchedor, peeling, defesa medico esteta, cicatriz queloide, assimetria estetica.
---

# CIRURGIA ESTETICA RESULTADO

> Skill **Tier 2** — RC em estetica com regime de **obrigacao de resultado**. Implementa PA-15 (meio x resultado), PA-13 (citacao STJ paradigmas), PA-21 (quantum conservador), PA-19 (prescricao). Acionada por `medico-master`, `triagem-medica` em casos de estetica, `responsabilidade-civil-medica` (irmao do Tier 2).

---

## 0. Escopo e acionamento

Acionada em caso de demanda por **estetica pura** — paciente nao-doente buscando melhoria de aparencia. Excluida estetica **reparadora** pos-trauma, pos-mastectomia oncologica, pos-queimadura — essas seguem regime de meio (CC art. 951 + CDC art. 14 conforme sujeito).

## 1. Posicao na orquestra

- **Chamada por:** `medico-master`, `triagem-medica` (modalidade estetica), `responsabilidade-civil-medica` (especializacao).
- **Aciona:** `analise-tcle` (validar TCLE existente) ou `tcle-especialidades` (gerar TCLE-modelo defensivo), `analise-pericia-medica` (quesitos esteticos), `analise-prontuario-medico` (lacunas), `prescricao-erro-medico`, `revisao-final-medica`.
- **Entrega para:** peca civel (autor — buscando indenizacao por resultado nao-alcancado; reu — defendendo medico/clinica) + memoria de quantum.

## 2. Marco normativo e jurisprudencial

| Norma/precedente | Conteudo |
|------------------|----------|
| CC art. 186 + 927 | Bases gerais |
| **CC art. 951** | Medico PF — base; aplicada COM **inversao da presuncao** em estetica |
| CDC art. 14 | Clinica/hospital PJ — objetiva |
| CDC art. 14 §4o | Profissional liberal subjetivo (mas em estetica = resultado) |
| **STJ REsp 1.526.466/RS (3a Turma, 2015) — paradigma** | **Cirurgia estetica = obrigacao de resultado**; inversao da presuncao; medico prova excludente |
| STJ REsp 985.888/SP | Confirma regime — estetica reparadora distinta da pura |
| STJ REsp 1.395.254/SC | Estetica nao-cirurgica (botox, preenchedor) — analogia |
| Res. CFM 2.217/2018 art. 22, 24, 31 | Dever de informar realista |
| Lei 9.656/1998 + Rol ANS | Estetica pura NAO coberta por plano (regra geral) |

## 3. Distincao critical (PA-15)

| Tipo | Regime | Justificativa |
|------|--------|---------------|
| **Estetica pura** (mamoplastia, lipo, abdominoplastia, blefaroplastia, ritidoplastia, botox, preenchedor, peeling profundo, rinoplastia funcional+estetica) | **Resultado** (STJ REsp 1.526.466) | Paciente nao-doente busca melhoria — resultado prometido obriga |
| **Estetica reparadora** (pos-trauma, pos-oncologica, pos-queimadura, fissura labiopalatina) | **Meio** | Paciente doente — diligencia obriga, nao resultado |
| **Reconstrutiva funcional+estetica** (rinoplastia para obstrucao) | Conforme dominante (se funcional preponderante = meio; se estetica preponderante = resultado) | Caso a caso |

**Erro frequente:** classificar rinoplastia para corrigir desvio de septo + estetica como obrigacao de resultado — depende da motivacao predominante.

## 4. Inversao da presuncao (REsp 1.526.466/RS)

**Regra:** em estetica pura, o resultado nao-alcance gera **presuncao** de culpa do medico/clinica. A defesa precisa provar excludente:

| Excludente | Como provar |
|------------|-------------|
| **Descumprimento do paciente** (nao-seguiu orientacoes, fumou, expôs ao sol, nao-comparece em retorno) | TCLE com orientacoes + prontuario com adesao registrada + ausencia em retorno documentada |
| **Caso fortuito/forca maior** (infeccao apesar de protocolo correto) | Protocolo de antissepsia documentado + cultura + literatura mostrando incidencia minima |
| **Fato de terceiro** (raro) | — |
| **Condicao pre-existente** (predisposicao queloide nao informada pelo paciente) | TCLE com pergunta especifica + prontuario |
| **Resultado dentro do esperado** (paciente exige perfeicao irreal) | TCLE realista + fotografia pre + literatura sobre variabilidade |

## 5. Defesa estrutural do medico esteta

Tres pilares:

1. **TCLE realista** (validar com `analise-tcle` ou gerar com `tcle-especialidades`):
   - Expectativa especifica + variabilidade
   - Fotografia pre-procedimento anexa
   - Plano de seguimento (consultas pos-operatorias)
   - Possibilidade de retoque (com custo se aplicavel)
   - Contraindicacoes informadas

2. **Prontuario documentado** (validar com `analise-prontuario-medico`):
   - Descricao cirurgica detalhada
   - Acompanhamento pos-cirurgico com fotos
   - Orientacoes registradas + adesao do paciente
   - Eventuais intercorrencias e conduta

3. **Pericia favoravel** (quesitos via `analise-pericia-medica`):
   - Conformidade com lex artis (tecnica empregada)
   - Resultado dentro da variabilidade biologica
   - Concorrencia de fatores do paciente (nao-aderencia, predisposicao)

## 6. Ataque estrutural do autor (paciente)

1. **TCLE generico ou inflado** — promessa de resultado especifico (foto retocada, "vai ficar igual a foto"). Frágil em juizo.
2. **Ausencia de fotografia pre** — impossibilidade de demonstrar resultado esperado x alcancado.
3. **Lacuna no seguimento** — falta de consultas pos-operatorias, falta de registro de orientacoes.
4. **Resultado claramente alheio** (assimetria grosseira, queloide previsivel, infeccao por falha de antissepsia).
5. **Inversao de onus (CDC art. 6o VIII + Sum. 469 STJ em clinica/hospital PJ; CPC art. 373 §1o em medico PF).**

## 7. Memoria de quantum (P3)

| Item | Base | Conservador? |
|------|------|--------------|
| Dano material — despesas de retoque/correcao | CC art. 949 | Comprovante |
| Dano moral — frustracao estetica | CC art. 186 + 927 + REsp 1.526.466 | Tema 1.094/1.095 STJ — moderado |
| Dano estetico autonomo | CC art. 949 + Sum. 387 STJ (cumulavel) | Por gravidade |
| Lucros cessantes (raros — modelo, ator) | CC art. 402 | Comprovacao |

**Conservadorismo (PA-21):** estetica e area com inflacao recorrente. STJ corta. Parametros consolidados: dano moral por frustracao estetica simples — R$ 10-30k; com sequela visivel — R$ 30-80k; com deformidade grave — R$ 80-200k. **`[VERIFICAR — atualizacao]`**.

## 8. Esqueleto FIRAC — Peca civel estetica

```
[Adaptacao do esqueleto de `responsabilidade-civil-medica`]

III — DIREITO
III.1 — Cirurgia estetica = obrigacao de RESULTADO (STJ REsp 1.526.466/RS)
III.2 — Inversao da presuncao — medico/clinica prova excludente
III.3 — Re Y (clinica/hospital) — CDC art. 14 + Sum. 469 STJ
       Re X (medico PF) — CC art. 951 + REsp 1.526.466 (regime de resultado
       transcende a regra geral subjetiva do CDC art. 14 §4o)
III.4 — Tese de defesa (se for o caso): excludente comprovada — descumprimento
       do paciente / caso fortuito / condicao pre-existente
III.5 — Quantum (P3 — conservador)
```

## 9. Vedacoes especificas

- **PA-15** — distinguir estetica pura (resultado) x reparadora (meio).
- **PA-13** — STJ REsp 1.526.466/RS sempre citado.
- **PA-21** — quantum estetico conservador — STJ corta valores inflados (Tema 1.094/1.095).
- **PA-19** — prescricao 3 anos (medico PF) vs 5 anos (clinica/hospital).
- **PA-08** — sem critica pessoal (ao medico, ao paciente, ao perito).
- **PA-02** — sem promessa de procedencia.

## 10. Protocolos acionados

- **P1** — Selo emitido.
- **P2** — `analise-tcle` + `analise-prontuario-medico` + `analise-pericia-medica`.
- **P3** — memoria de quantum.
- **P6** — revisao R1-R4.

## 11. Localizacao

JE comarca do domicilio do autor (CDC art. 101 I — quase sempre consumerista, mesmo medico PF se trabalhou via clinica) ou foro de eleicao se nao consumerista (medico PF puro autonomo — raro em estetica moderna).

## 12. Integracao

**Chamada por:** `medico-master`, `triagem-medica` (estetica), `responsabilidade-civil-medica`.

**Entrega para:** peca civel + insumo para `analise-tcle` (validar TCLE existente do reu) ou `tcle-especialidades` (gerar TCLE-modelo defensivo para a clinica-cliente).

**Sem esta skill:** caso estetico tratado como meio -> tese se desmonta. Defesa sem REsp 1.526.466 perde o regime, perde o caso.
