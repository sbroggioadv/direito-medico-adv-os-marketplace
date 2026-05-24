---
description: Acionamento direto da triagem 4D do plugin — classificacao sujeito x modo x esfera x subdominio. Porta de entrada de toda demanda de direito medico.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao opcional do caso]
---

Voce foi acionado pelo comando `/triagem` do plugin Direito Medico Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** executar a triagem 4D — sujeito x modo x esfera x subdominio — e gravar no `CASO.md`.

## PROTOCOLO

1. **Acionar `medico-master`** brevemente para verificar configuracao + governanca.
2. **Acionar a skill `triagem-medica`** — classifica:
   - **Sujeito:** profissional PF / clinica PJ / hospital PJ / paciente / operadora
   - **Modo:** consultivo / contencioso
   - **Esfera:** civel / criminal / etico-disciplinar / regulatorio (pode ter 2+ paralelas — P4)
   - **Subdominio:** medicina / odonto / saude mental / reproducao / outros
3. **Gravar resultado** no CASO.md (acionar `memoria-de-caso-medico` se necessario abrir caso novo).
4. **Acionar `validador-legislacao-vigente`** para emitir o Selo P1 antes de qualquer producao.
5. **Sugerir proximas skills** com base no resultado da triagem (Tier 2-6).

**Skill a acionar:** `triagem-medica`.
