---
description: Acionamento direto do nucleo etico-disciplinar — defesa em PED CRM, PED CRO, MS contra cassacao, suspensao preventiva. Skills Tier 4.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao opcional do caso etico-disciplinar]
---

Voce foi acionado pelo comando `/ped` do plugin Direito Medico Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** acionar a defesa em Processo Etico-Disciplinar (Tier 4).

## PROTOCOLO

1. **Verificar** Selo P1 em CASO.md.
2. **Selecionar skill:**
   - `defesa-ped-crm` — Res. CFM 2.145/2016 + CEM 2.217/2018 (fluxo + recurso CFM)
   - `defesa-ped-cro` — Res. CFO 71/2006 + CEO 118/2012 + Res. CFO 196 (particularidades odonto, PJ inscrita, HOF)
   - `ms-contra-cassacao-conselho` — Lei 12.016/2009 + Sum. 105 STJ + CF 109 I (JF)
   - `suspensao-preventiva-conselho` — Res. CFM 2.145 art. 33 + Lei 9.784 + MS com tutela
3. **Conferir prescricao etica** — 5 anos (Res. CFM 2.145 art. 32 / Res. CFO 71 art. 35) — PA-19.
4. **Cruzamento P4 (PA-12):** penal absolveu por CPP 386 I/III? Alcanca PED via CC 935.
5. **Finalizar** com `revisao-final-medica` R1-R4.

**Skills tipicas:** `defesa-ped-crm`, `defesa-ped-cro`, `ms-contra-cassacao-conselho`, `suspensao-preventiva-conselho`.
