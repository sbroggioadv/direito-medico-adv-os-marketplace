---
description: Acionamento direto do nucleo consultivo empresarial — constituicao de sociedade medica, contratos, credenciamento, LGPD-saude, publicidade. Skills Tier 6.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao opcional do caso consultivo]
---

Voce foi acionado pelo comando `/consultivo` do plugin Direito Medico Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** acionar o consultivo empresarial em saude (Tier 6).

## PROTOCOLO

1. **Verificar** Selo P1 em CASO.md.
2. **Selecionar skill:**
   - `constituicao-sociedade-medica` — Lei 12.842 + Lei 13.874 + Res. CFM 1.493 / CFO 63
   - `contrato-prestacao-medica` — 3 modalidades (PJ-PJ, PJ-PF, PF-PF); pejotizacao Sum. 331 TST + RE 958.252
   - `credenciamento-plano-saude` — Lei 9.656 art. 17 + RN 365 + glosa RN 305 + ressarcimento SUS Lei 9.961 art. 32
   - `lgpd-saude` — LGPD art. 11 (dado sensivel) + Res. CFM 1.821/2007 + SBIS-CFM + ANPD
   - `compliance-publicidade-medica` — Res. CFM 2.336/2023 + Res. CFO 196/2019 + PROAD
3. **Aplicar PA-20** — sem cross-sell com plugins irmaos; quando demanda extrapola direito medico (litigio trabalhista puro, holding, fiscal especifico, beneficio INSS), usar slot generico "encaminhar a especialista em [area]".
4. **Finalizar** com `revisao-final-medica` R1-R4.

**Skills tipicas:** todas do Tier 6.
