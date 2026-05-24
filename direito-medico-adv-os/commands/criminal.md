---
description: Acionamento direto do nucleo criminal — culpa medica, omissao de socorro, violacao de sigilo, falsidade atestado/prontuario. Skills Tier 3.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao opcional do caso criminal]
---

Voce foi acionado pelo comando `/criminal` do plugin Direito Medico Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** acionar a defesa criminal do profissional de saude (Tier 3).

## PROTOCOLO

1. **Verificar** Selo P1 em CASO.md.
2. **Selecionar skill** conforme caso:
   - `defesa-culpa-medica-criminal` — CP 121§3o / 129§6o (homicidio/lesao culposa)
   - `omissao-de-socorro-medico` — CP 135 + omissao impropria CP 13§2o
   - `violacao-sigilo-medico` — CP 154 (tripartite: penal + etico + civel + ANPD)
   - `falsidade-atestado-prontuario` — CP 302/299/297/171§3o
3. **Articular vias defensivas:** HC trancamento, absolvicao sumaria (CPP 397), sursis processual (Lei 9.099 89), transacao penal (art. 76), desclassificacao dolo eventual -> culposo.
4. **Cruzamento P4 (PA-12):** absolvicao por CPP 386 I/III alcanca civel e PED (CC 935) — coordenar com `timeline-multiesfera`.
5. **Finalizar** com `revisao-final-medica` R1-R4.

**Skills tipicas:** `defesa-culpa-medica-criminal`, `omissao-de-socorro-medico`, `violacao-sigilo-medico`, `falsidade-atestado-prontuario`.
