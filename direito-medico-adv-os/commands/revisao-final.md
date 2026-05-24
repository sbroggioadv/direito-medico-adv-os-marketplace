---
description: Aciona diretamente a Revisao Tecnica R1-R4 (Suprema Corte do plugin) sobre uma peca/parecer ja produzido. Auditoria obrigatoria antes da entrega ao operador.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [referencia ao documento a revisar | --quick (R1+R2 apenas) | --no-revisao]
---

Voce foi acionado pelo comando `/revisao-final` do plugin Direito Medico Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** executar a Revisao Tecnica R1-R4 sobre o documento mais recente (ou referenciado).

## PROTOCOLO

1. **Acionar a skill `revisao-final-medica`** — executa as 4 rodadas sequenciais:
   - **R1 — Brief/escopo/dados:** tipo correto? CASO.md certo? fato datado (PA-09)? Selo P1?
   - **R2 — Tecnica juridica:** lei+artigo+ano (PA-13)? jurisprudencia vigente (PA-10)? subjetiva x objetiva (PA-15)? inversao fundamentada (PA-14)? prescricao (PA-19)? quantum conservador (PA-21)?
   - **R3 — Conformidade etico-regulatoria + Cruzamento P4:** 22 PAs respeitadas? Cruzamento P4 articulado quando ha 2+ esferas?
   - **R4 — Entrega/clareza/ressalva OAB:** FIRAC? memoria de quantum tabular? tokens persona resolvidos? ressalva OAB padrao? [VERIFICAR] listados?
2. **Veredito final:** APROVADO / APROVADO COM RESSALVAS / BLOQUEADO.
3. **Bypass disponivel:**
   - `--quick` -> R1+R2 apenas (rascunhos internos).
   - `--no-revisao` -> skip total (operador assume risco; log de waiver).
   - `/revisao off` -> desativa via state.json (persistente).

**Skill a acionar:** `revisao-final-medica`.
