---
description: Inicia o wizard de configuracao do plugin Direito Medico Adv-OS — cria a pasta direito-medico/ com identidade do advogado, OAB, cidade/UF, area de foco (defesa-profissional / plano-saude / consultivo / todos), frentes ativas, tom e modo de melhor saida.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [--update para reconfigurar]
---

Voce foi acionado pelo comando `/start-medico` do plugin Direito Medico Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** configurar o plugin direito-medico no ambiente do operador (advogado especialista em direito medico e da saude).

## PROTOCOLO

1. **Acionar a skill `onboarding-medico`** imediatamente — ela conduz o wizard completo.
2. O wizard cria `<cwd>/direito-medico/` com `persona.md`, `config.md`, `casos/` e o `cowork-state.json`, alem de `.claude/settings.local.json`. Captura: identidade do advogado, OAB + UF, escritorio, **cidade + UF** (eixo de Localizacao — Protocolo 5), `area_foco` (defesa-profissional / plano-saude / consultivo / todos), frentes ativas, tom de voz e `MODO_MELHOR_SAIDA`.
3. Se ja existir `direito-medico/cowork-state.json`, a skill oferece continuar / atualizar / recriar (idempotencia).
4. Se o argumento for `--update`, ir direto para o fluxo de atualizacao.

**Atencao LGPD (PA-16/22):** a skill avisa se o diretorio estiver em pasta sincronizada (iCloud/OneDrive/Dropbox/Drive) — dados sensiveis de paciente (LGPD art. 11 + sigilo medico CP 154) nao devem ser sincronizados sem controle.

**Skill a acionar:** `onboarding-medico`.
