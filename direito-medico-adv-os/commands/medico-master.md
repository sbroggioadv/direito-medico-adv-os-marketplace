---
description: Ativa a cadeia completa de operacao em direito medico — 4 Camadas, 22 Proibicoes Absolutas, 6 Protocolos Tecnicos (incluindo P4 Cruzamento Multi-esfera) e Revisao Tecnica R1-R4. Comando-coracao do plugin.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [contexto opcional da demanda]
---

Voce foi acionado pelo comando `/medico-master` do plugin Direito Medico Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** ativar a cadeia completa de operacao em direito medico. A partir deste comando, toda demanda passa pela governanca integral do plugin.

## PROTOCOLO

1. **Verificar configuracao** — procurar `direito-medico/cowork-state.json` subindo a arvore. Se nao encontrar, sugerir `/start-medico`; se o operador declinar, operar em modo fallback generico.
2. **Acionar a skill `medico-master`** (Tier 0) — ela carrega a Hierarquia das 4 Camadas, as 22 PAs, os 6 Protocolos (P1-P6), o mapa de roteamento por Tier 0-6 + transversais e a regra de que nenhuma skill de producao roda sem o Selo de Validacao Legal Previa (P1).
3. **Saudar o operador** apresentando: advogado responsavel, OAB+UF, escritorio, cidade+UF, area de foco, frentes ativas, Revisao Tecnica (ativa/desativada).
4. **Conduzir** toda demanda subsequente pelo pipeline: `triagem-medica` (4D) -> `validador-legislacao-vigente` (Selo) -> Tier correto -> `revisao-final-medica` R1-R4 -> entrega + atualiza `CASO.md`.
5. Faltando dado essencial: sinalizar Ponto de Omissao `[INFORMAR]`, nunca inventar (PA-02).
6. Caso multi-esfera (P4) — articular `timeline-multiesfera` para coordenar civel + criminal + PED + regulatorio.

**Skill a acionar:** `medico-master`.
