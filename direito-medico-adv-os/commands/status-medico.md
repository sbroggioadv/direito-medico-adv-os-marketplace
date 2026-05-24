---
description: Mostra status do plugin Direito Medico Adv-OS — identidade do operador, configuracao, casos ativos, estado da Revisao Tecnica, frentes habilitadas.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [sem argumentos | --casos | --config]
---

Voce foi acionado pelo comando `/status-medico` do plugin Direito Medico Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** apresentar status operacional do plugin.

## PROTOCOLO

1. **Localizar configuracao** — procurar `direito-medico/cowork-state.json` subindo a arvore.
2. Se nao encontrar: instruir `/start-medico`.
3. Se encontrar: ler e apresentar formatado:
   ```
   [direito-medico-adv-os — status]

   Operador: {advogado_nome} | OAB/{oab_uf} {oab_numero}
   Escritorio: {firm_name}
   Sede: {cidade}/{uf}
   Area de foco: {area_foco}   (defesa-profissional / plano-saude / consultivo / todos)
   Tom de voz: {tom_voz_perfil} (intensidade {tom_voz_intensidade}/10)
   Modo de melhor saida: {modo_melhor_saida}

   Revisao Tecnica R1-R4: ATIVA | DESATIVADA

   Frentes ativas:
   - [defesa-profissional]
   - [responsabilidade-civil]
   - [criminal-medico]
   - [ped-conselho]
   - [acoes-plano-saude]
   - [consultivo-clinica]
   - [regulatorio-saude]
   - [saude-mental]
   - [reproducao-assistida]

   Casos abertos em direito-medico/casos/:
   - <slug-1> (ultima atividade YYYY-MM-DD)
   - <slug-2> (...)

   Hooks:
   - UserPromptSubmit: prompt-intercept-corte.py
   - PostToolUse: post-edit-evolve-memory.py
   - PreCompact: pre-compact-snapshot.py
   ```
4. Subcomandos:
   - `--casos` -> apenas lista detalhada de casos.
   - `--config` -> configuracao completa (persona + state).

**Skills auxiliares:** `medico-master` (carregar contexto), `memoria-de-caso-medico` (listar casos).
