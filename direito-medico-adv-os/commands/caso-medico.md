---
description: Abre, retoma ou lista caso/cliente em `direito-medico/casos/`. Cada caso e compartimentado (PA-22 + LGPD). Suporta `novo <slug>`, `<slug>` (retomar), `list`, `arquivar <slug>`.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [novo <slug> | <slug> | list | arquivar <slug>]
---

Voce foi acionado pelo comando `/caso-medico` do plugin Direito Medico Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** gerenciar a pasta de caso/cliente — compartimentacao absoluta por LGPD + sigilo medico (PA-16/22).

## PROTOCOLO

1. **Acionar a skill `memoria-de-caso-medico`** — ela orquestra CRUD do caso.
2. Subcomandos suportados:
   - `novo <slug>` -> cria `<cwd>/direito-medico/casos/<slug>/` com CASO.md + MEMORY.md (templates) + `arquivos/` e `pecas/`. Verifica se workspace esta em pasta sincronizada (iCloud/OneDrive/Dropbox/Drive) e alerta antes de criar.
   - `<slug>` (sem subcomando) -> retoma caso existente — le CASO.md + MEMORY.md + listagem de pecas.
   - `list` -> lista todos os slugs em `casos/`.
   - `arquivar <slug>` -> move para `casos/_arquivados/` apos confirmacao.
3. **Sigilo:** dados de paciente nunca sao gravados no plugin distribuido — apenas em `casos/<slug>/` (gitignored).
4. **Sem CPF do paciente** em CASO.md — usar iniciais.

**Skill a acionar:** `memoria-de-caso-medico`.
