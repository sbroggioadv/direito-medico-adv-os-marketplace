# direito-medico-adv-os-marketplace

Marketplace oficial do plugin **Direito Medico Adv-OS** — sistema operacional do advogado especialista em direito medico e da saude.

## O que o plugin entrega

- **37 skills** organizadas em 7 Tiers (Tier 0 governanca; Tier 1 triagem 4D + analise documental; Tier 2 responsabilidade civil; Tier 3 defesa criminal; Tier 4 processo etico-disciplinar CRM/CRO; Tier 5 acoes contra plano de saude; Tier 6 consultivo empresarial em saude) + 3 transversais (revisao final R1-R4, estilo, memoria de caso)
- **11 commands** (`/start-medico`, `/medico-master`, `/caso-medico`, `/triagem`, `/civil`, `/criminal`, `/ped`, `/plano-saude`, `/consultivo`, `/revisao-final`, `/status-medico`)
- **4 hooks** (`UserPromptSubmit` com deteccao automatica de demanda juridico-medica + injecao da governanca; `PostToolUse` para evolucao de memoria; `PreCompact` para snapshot)
- **22 Proibicoes Absolutas (PA-01 a PA-22)** + **6 Protocolos Tecnicos (P1 Vigencia, P2 Integridade, P3 Memoria de Decisao, P4 Cruzamento Multi-esfera, P5 Localizacao, P6 R1-R4)** + camada FIRAC + ressalva OAB ativa em toda entrega

## Cobertura

- Defesa multi-frente do profissional — civil (CC art. 951 + CDC art. 14), criminal (CP arts. 121§3o, 129§6o, 135, 154, 299), etico-disciplinar (Res. CFM 2.145/2016 + Res. CFO 71/2006)
- Acoes contra operadora — Lei 9.656/1998 + **Lei 14.454/2022 (Rol exemplificativo)** + Tema 990 STJ pos-lei + Sum. 469/597/608 STJ
- Consultivo de clinica/sociedade medica — Lei 12.842/2013 (Ato Medico) + Lei 13.874/2019 + Res. CFM 1.493/1998 + LGPD aplicada a saude
- Cruzamento multi-esfera (P4) — coordena civil x criminal x PED CRM/CRO simultaneos, aproveitando CPP art. 386 I/III + CC art. 935

## Como instalar

### Via UI do aplicativo Claude (Cowork)

1. Abrir Claude (Cowork).
2. Settings → Plugins → aba **Pessoal** → botao **"+"** (Uploads locais).
3. Colar a URL deste repositorio.
4. Confirmar a instalacao.

### Via CLI

```bash
claude plugin marketplace add https://github.com/sbroggioadv/direito-medico-adv-os-marketplace
claude plugin install direito-medico-adv-os@direito-medico-adv-os-marketplace
```

## Primeiros passos

1. No diretorio de trabalho do advogado, rode `/start-medico` para o wizard de configuracao (cria `direito-medico/` com persona, OAB, escritorio, cidade/UF, area de foco).
2. Use `/medico-master` para ativar a cadeia completa.
3. Para um caso novo, `/caso-medico novo <slug-do-cliente>`.
4. `/triagem` faz a classificacao 4D (sujeito x modo x esfera x subdominio).
5. Toda entrega passa por `/revisao-final` (R1-R4) antes do operador.

## Estrutura

```
direito-medico-adv-os-marketplace/
├── .claude-plugin/marketplace.json
├── README.md (este arquivo)
├── LICENSE
└── direito-medico-adv-os/
    ├── .claude-plugin/plugin.json
    ├── CLAUDE.md
    ├── README.md
    ├── skills/ (37 SKILL.md)
    ├── commands/ (11 commands)
    ├── hooks/
    ├── scripts/
    ├── context/
    └── templates/
```

## Atencao LGPD + Sigilo Medico (CP art. 154)

Dados de paciente (prontuario, exames, identificacao) sao **dados sensiveis** (LGPD art. 11) e estao protegidos por sigilo profissional. O plugin **NUNCA** persiste dados de paciente no produto distribuido — eles ficam em `<cwd>/direito-medico/casos/<slug>/` (pasta gitignored). O wizard `/start-medico` alerta se o workspace estiver em pasta sincronizada (iCloud/OneDrive/Dropbox/Google Drive) sem cifragem.

## Licenca

MIT — veja `LICENSE`.

## Suporte

Plugin comercial distribuido via Kirvano. Suporte e atualizacoes conforme licenca de aquisicao.
