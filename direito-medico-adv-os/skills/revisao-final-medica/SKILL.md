---
name: revisao-final-medica
description: >
  Skill invariante de Revisao Tecnica R1-R4 (Suprema Corte do plugin) — auditoria obrigatoria de 4 rodadas (R1 brief/escopo + dados; R2 tecnica juridica; R3 conformidade etico-regulatoria + cruzamento P4; R4 entrega/clareza/ressalva OAB) sobre toda peca, parecer, contrato ou estrategia antes da entrega. Reprovacao em qualquer rodada bloqueia entrega e devolve ao produtor. Operacionaliza Protocolo P6. Bypass disponivel `--no-revisao`, `--quick` (R1+R2 apenas), `/revisao off`. Aciona: revisar peca, auditoria final, conferir antes entregar, revisao final, R1-R4, Suprema Corte medica, /revisao-final.
---

# REVISAO FINAL MEDICA (R1-R4)

> Skill **transversal** — auditora invariante do plugin. Nenhuma peca/parecer/contrato sai sem passar pelas 4 rodadas. Implementa Protocolo P6. Acionada por `medico-master` (sempre antes de entrega) e operador direto via `/revisao-final`.

---

## 0. Escopo e acionamento

Acionada por `medico-master` **antes de toda entrega**, ou pelo operador via comando `/revisao-final` ou expressao "revisar peca", "auditoria final", "conferir antes de entregar", "R1-R4".

**Sem esta auditoria, nenhuma peca e considerada entregue** — mesmo conteudo correto.

## 1. Posicao na orquestra

- **Chamada por:** `medico-master` (obrigatoriamente antes de toda entrega) + operador direto.
- **Recebe de:** qualquer skill produtora (Tier 1-6) — peca, parecer, minuta, calculo, estrategia, defesa.
- **Entrega para:** operador — documento APROVADO ou BLOQUEADO para retrabalho.
- **Bypass:** `--no-revisao` (registra waiver explicito); `--quick` (R1+R2 apenas — rascunhos internos); `/revisao off` (desativa via state.json — operador assume risco).

## 2. Sequencia obrigatoria — R1 -> R2 -> R3 -> R4

```
R1 — Brief / Escopo / Dados
   |
   v (APROVADO)
R2 — Tecnica juridica
   |
   v (APROVADO)
R3 — Conformidade etico-regulatoria + Cruzamento Multi-esfera (P4)
   |
   v (APROVADO)
R4 — Entrega / Clareza / Ressalva OAB
   |
   v (APROVADO)
ENTREGA AUTORIZADA
```

Rodadas sequenciais. Reprovacao em qualquer **bloqueia as seguintes** e devolve ao produtor.

## 3. R1 — Brief, escopo e dados

**Pergunta:** a entrega responde ao que foi pedido?

Checklist R1:
```
[ ] Documento e do tipo solicitado (peca civel/criminal/PED/MS, parecer, contrato)
[ ] Escopo cobre os pontos da triagem 4D (sujeito x modo x esfera x subdominio)
[ ] CASO.md referenciado — caso correto (sem mistura — PA-22)
[ ] Dados pessoais (cliente, CRM/CRO da parte, OAB do operador) corretos
[ ] Fato gerador datado (PA-09 — ano do fato)
[ ] Selo de Validacao Legal Previa emitido (PA-04)
[ ] Sem conteudo fora do escopo (excesso que confunde operador)
[ ] Foro/competencia identificados (P5 — Localizacao)
```

**Veredito:** APROVADO / APROVADO COM RESSALVAS (listadas) / REPROVADO (devolver).

## 4. R2 — Tecnica juridica

**Pergunta:** fundamentacao juridica e correta, vigente e bem classificada?

Checklist R2:
```
[ ] Lei + artigo + ano (PA-13)
[ ] Jurisprudencia STJ/STF/TST com tribunal + turma + numero + ano
[ ] Sumula/Tema vigente e nao-superado (PA-10)
[ ] Lei 14.454/2022 considerada quando ha discussao de Rol
[ ] Tema 990 STJ pos-Lei 14.454 corretamente citado
[ ] Subjetiva (CC 951) x objetiva (CDC 14) (PA-15)
[ ] Inversao do onus fundamentada com norma certa (PA-14)
[ ] Prescricao conferida (PA-19 — 3a CC x 5a CDC)
[ ] Quantum conservador (PA-21) — ancorado em parametros STJ
[ ] Citacoes de literatura medica/diretriz: SBOC/FEBRASGO/SBC/SBP/SBN/etc. quando aplicavel
[ ] [VERIFICAR] marcado em alvo movel (PA-11)
[ ] Memoria de quantum em tabela auditavel (P3)
[ ] FIRAC estruturado (F-I-R-A-C — Camada 3)
```

**Veredito:** APROVADO / APROVADO COM RESSALVAS / REPROVADO.

## 5. R3 — Conformidade etico-regulatoria + Cruzamento P4

**Pergunta:** respeita as 22 PAs + protocolos? Aproveita cruzamento multi-esfera?

Checklist R3:
```
[ ] PA-01 — cliente-final e o advogado, nao paciente/medico
[ ] PA-02 — sem promessa de resultado
[ ] PA-03 — sem opinar conduta clinica (vedacao Lei 12.842)
[ ] PA-04 — Selo emitido pelo `validador-legislacao-vigente`
[ ] PA-05 — ressalva OAB no fechamento
[ ] PA-06 — sem orientacao clinica direta ao paciente
[ ] PA-07 — sem julgar etica do colega (CFM/CFO julga)
[ ] PA-08 — sem critica pessoal a perito/conselheiro/magistrado
[ ] PA-09/10/11/12/13 — eixos temporal/normativo/jurisprudencial conferidos
[ ] PA-14/15 — onus + regime separados com precisao
[ ] PA-16/17 — sigilo medico + LGPD respeitados (sem prontuario no plugin)
[ ] PA-18 — internacao involuntaria? comunicar MP 72h
[ ] PA-19/20/21/22 — prescricao + sem cross-sell + quantum + compartimentacao
[ ] P4 — Cruzamento Multi-esfera: caso tem 2+ esferas? articulou aproveitamento
       defensivo cruzado (CPP 386 I/III via CC 935)?
[ ] Res. CFM 2.336/CFO 196 se ha publicidade
[ ] Res. CFM 2.145/CFO 71 se ha PED
[ ] Sum. 105 STJ se MS contra Conselho
```

**Veredito:** APROVADO / APROVADO COM RESSALVAS / REPROVADO.

## 6. R4 — Entrega, clareza, ressalva OAB

**Pergunta:** o documento esta pronto, claro e com ressalva tecnica?

Checklist R4:
```
[ ] Formato adequado (peticao com partes + fundamentos + pedidos)
[ ] FIRAC ou estrutura analoga (Camada 3)
[ ] Memoria de quantum (P3) em tabela quando ha valor
[ ] Anexos listados explicitamente (prontuario, laudo, TCLE, exames, apolice)
[ ] Linguagem tecnica + clara (sem floreio)
[ ] Tokens persona resolvidos (sem `{{...}}` literais no produto final)
[ ] Ressalva OAB padrao no fechamento (PA-05) — "minuta tecnico-operacional
     sujeita a revisao + responsabilidade tecnica do advogado OAB ativo"
[ ] [VERIFICAR] listados ao final para o operador acionar
[ ] Foro + data + assinatura advogada (formato OAB/UF n. ___)
[ ] Cidade/UF coerente com triagem (P5)
[ ] Numero de paginas razoavel (sem inchaco)
```

**Veredito:** APROVADO / APROVADO COM RESSALVAS / REPROVADO.

## 7. Saida da revisao (formato canonico)

```
[REVISAO FINAL R1-R4 — direito-medico-adv-os]
Documento: [tipo + caso + data]

R1 — Brief/escopo/dados: APROVADO | APROVADO COM RESSALVAS | REPROVADO
   Ressalvas: [lista]

R2 — Tecnica juridica: APROVADO | APROVADO COM RESSALVAS | REPROVADO
   Ressalvas: [lista]

R3 — Conformidade + P4: APROVADO | APROVADO COM RESSALVAS | REPROVADO
   Ressalvas: [lista]

R4 — Entrega + clareza + ressalva OAB: APROVADO | APROVADO COM RESSALVAS | REPROVADO
   Ressalvas: [lista]

VEREDITO FINAL:
   [APROVADO — pode entregar ao operador]
   [APROVADO COM RESSALVAS — operador aplica correcoes listadas antes da
    entrega ao cliente final]
   [BLOQUEADO — devolver ao produtor com instrucoes de retrabalho:
    {especificacao concreta}]

[VERIFICAR] ao operador (PA-11):
   - [item 1 — atualizacao normativa]
   - [item 2 — jurisprudencia em revisao]
   ...

Selo:
   Data do Selo de Validacao Legal Previa: [data]
   Fonte: validador-legislacao-vigente
```

## 8. Bypass e modulacao

| Bypass | Efeito |
|--------|--------|
| `--no-revisao` | Skip total — operador assume risco; log de waiver |
| `--quick` | So R1+R2 — rascunhos internos / pre-conversa com cliente |
| `/revisao off` | Desativa via state.json — operador toggle persistente |

**Em qualquer bypass:** registrar no log que a entrega saiu sem R3/R4 — operador ciente.

## 9. Casos tipicos de reprovacao

| Rodada | Reprovacao tipica |
|--------|-------------------|
| R1 | Documento e parecer mas pedido era peca; CASO.md errado |
| R2 | Tema 990 citado como "rol taxativo" (pre-Lei 14.454 — PA-10) |
| R2 | Inversao do onus sem fundamentacao (PA-14) |
| R2 | Quantum inflado sem ancoragem STJ (PA-21) |
| R3 | Plugin opinou sobre conduta clinica (PA-03) |
| R3 | Ressalva OAB ausente (PA-05) |
| R3 | Cruzamento multi-esfera ignorado (P4) |
| R4 | Tokens `{{ADVOGADO_NOME}}` literais no produto final |
| R4 | Ressalva OAB ausente |
| R4 | [VERIFICAR] nao listados |

## 10. Vedacoes especificas

- **PA-04** — sem Selo, R3 reprova automatico.
- **PA-05** — sem ressalva OAB, R4 reprova automatico.
- **PA-08** — esta skill aponta vicios — sem critica pessoal ao produtor.

## 11. Protocolos acionados

Esta skill **e** o Protocolo P6 operacionalizado. Verifica P1-P5 em todas as rodadas.

## 12. Localizacao

Verifica em R1 que foro/competencia (P5) estao corretos para o caso (JE/JF/CRM/CFO).

## 13. Integracao

**Chamada por:** `medico-master` (obrigatorio antes de toda entrega) + operador direto.

**Entrega para:** operador — documento aprovado ou bloqueado.

**Sem esta skill:** pecas com defeitos sutis (Tema 990 pre/pos-lei, subjetiva x objetiva, ressalva OAB ausente, cruzamento P4 perdido) chegam ao operador sem auditoria — risco de improcedencia/PED/responsabilidade tecnica.
