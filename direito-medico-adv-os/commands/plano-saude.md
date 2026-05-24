---
description: Acionamento direto do nucleo de acoes contra plano de saude — oncologia, home care, OPME, TEA, reajuste, rescisao, tutela de urgencia. Skills Tier 5.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao opcional do caso contra plano]
---

Voce foi acionado pelo comando `/plano-saude` do plugin Direito Medico Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** acionar acoes contra operadora de plano de saude (Tier 5).

## PROTOCOLO

1. **Verificar** Selo P1 em CASO.md (Lei 14.454/2022 + RN ANS atualizada vigentes).
2. **Selecionar skill conforme tipo de negativa:**
   - `acao-negativa-cobertura-oncologica` — quimio, imunoterapia, off-label
   - `acao-home-care` — internacao domiciliar (AgInt AREsp 1.232.473)
   - `acao-opme` — Orteses/Proteses (REsp 1.733.013 — autonomia tecnica)
   - `acao-tea-multidisciplinar` — autismo (RN 539 sessoes ilimitadas)
   - `acao-reajuste-abusivo` — Tema 952 + Estatuto Idoso
   - `acao-rescisao-coletivo` — Tema 1.082 + RN 412 (portabilidade especial)
3. **Aplicar `tutela-urgencia-plano-saude`** — modelo unificado CPC 300 + 537 + 854 + astreintes proporcionais (EAREsp 650.536).
4. **Aplicar:** PA-10 (Tema 990 pos-Lei 14.454), PA-11 (Rol ANS em atualizacao), PA-14 (inversao do onus — CDC 6o VIII), PA-21 (conservadorismo).
5. **Finalizar** com `revisao-final-medica` R1-R4.

**Skills tipicas:** todas do Tier 5.
