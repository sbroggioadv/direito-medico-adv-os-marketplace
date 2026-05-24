---
description: Acionamento direto do nucleo civel — responsabilidade civil medica/odontologica, perda de chance, cirurgia estetica, prescricao. Skills Tier 2.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao opcional do caso civel]
---

Voce foi acionado pelo comando `/civil` do plugin Direito Medico Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** acionar o nucleo civel (Tier 2) — responsabilidade civil medica e correlatos.

## PROTOCOLO

1. **Verificar** Selo P1 em CASO.md (acionar `validador-legislacao-vigente` se ausente — PA-04).
2. **Selecionar skill** segundo o caso:
   - `responsabilidade-civil-medica` — nucleo
   - `tcle-especialidades` — TCLE 12 modalidades
   - `perda-de-uma-chance` — atraso diagnostico, demora cesarea
   - `cirurgia-estetica-resultado` — obrigacao de resultado
   - `responsabilidade-odontologica` — Sum. 597 STJ
   - `prescricao-erro-medico` — 3a CC x 5a CDC
3. **Aplicar:** PA-15 (subjetiva CC 951 x objetiva CDC 14), PA-14 (inversao do onus), PA-21 (conservadorismo quantum).
4. **Finalizar** com `revisao-final-medica` R1-R4 antes de entregar.

**Skills tipicas:** `responsabilidade-civil-medica`, `tcle-especialidades`, `perda-de-uma-chance`, `cirurgia-estetica-resultado`, `responsabilidade-odontologica`, `prescricao-erro-medico`.
