# Direito Médico Adv-OS

> Sistema operacional do advogado brasileiro especializado em direito médico e da saúde.
> Plugin Claude Code com **36 skills** em 7 Tiers, cobrindo defesa multi-frente do profissional de saúde, ações contra planos de saúde e consultivo empresarial.

---

## O que faz

Plugin operacional para o advogado que atende:

- **Profissionais de saúde** (médicos, dentistas, enfermeiros, fisioterapeutas) em defesa multi-frente: responsabilidade civil + criminal por culpa médica + processo ético-disciplinar (CRM/CRO).
- **Clínicas, sociedades médicas e hospitais** em consultivo empresarial: contratos médicos, sociedades, LGPD-saúde, publicidade médica, credenciamento com planos.
- **Pacientes e beneficiários** em ações contra operadoras de planos de saúde (negativa de cobertura, reajuste abusivo, rescisão coletiva, TEA, OPME, oncológicos, home care).

---

## Cobertura técnica (v0.1 — Núcleo Operacional)

### 36 skills em 7 Tiers + transversais

| Tier | Skills | Foco |
|------|--------|------|
| 0 — Núcleo & Governança | 3 | Orquestração + Selo de Validação Legal + Onboarding |
| 1 — Triagem & Análise Documental | 5 | Triagem 4D, análise de prontuário, TCLE, perícia, timeline multi-esfera |
| 2 — Responsabilidade Civil | 6 | CC + CDC + jurisprudência STJ + TCLE 12 especialidades + obrigação de resultado |
| 3 — Defesa Criminal | 4 | Culpa médica (art. 121§3º, 129§6º CP), omissão socorro, sigilo, falsidade |
| 4 — Processo Ético-Disciplinar | 4 | PED CRM/CRO, MS contra cassação, suspensão preventiva |
| 5 — Ações contra Plano de Saúde | 7 | Oncologia, home care, OPME, TEA, reajuste, rescisão, tutela de urgência |
| 6 — Consultivo Empresarial | 5 | Sociedade médica, contratos, credenciamento, LGPD-saúde, publicidade |
| Transversais | 3 | Revisão R1-R4, estilo de entrega, memória de caso (LGPD) |

### 11 commands diretos

`/start-medico` · `/medico-master` · `/caso-medico` · `/triagem` · `/civil` · `/criminal` · `/ped` · `/plano-saude` · `/consultivo` · `/revisao-final` · `/status-medico`

### 4 hooks automáticos

SessionStart (persona) · UserPromptSubmit (detecta demanda jurídico-médica e injeta protocolo) · PostToolUse (evolui memória de caso) · PreCompact (snapshot pré-compactação)

---

## Legislação coberta (atualizada 2022-2026)

- **Leis chave:** 9.656/98 (planos), 12.842/2013 (Ato Médico), 14.510/2022 (Telemedicina), 14.454/2022 (Rol ANS exemplificativo), 13.709/2018 (LGPD), 10.216/2001 (Reforma psiquiátrica), 13.146/2015 (PCD), 12.764/2012 (TEA), 13.840/2019 (internação compulsória), 15.378/2026 (Estatuto dos Direitos do Paciente).
- **Resoluções CFM:** 2.217/2018 (CEM), 2.314/2022 (Telemedicina), 2.336/2023 (Publicidade), 2.320/2022 (Reprodução), 2.337/2023 (HOF), 1.821/2007 (Prontuário), 2.145/2016 (PED), 1.805/2006 (Cuidados paliativos), 1.995/2012 (DAV).
- **Resoluções CFO:** 118/2012 (Ética), 71/2006 (PED), 196/2019 (Publicidade), 287/2022 (Teleodontologia).
- **Súmulas STJ:** 469, 597, 608, 547.
- **Temas STJ:** 952, 990, 1037, 1069, 1082.
- **STF:** ADPF 54, ADI 4275, ADI 6.586, RE 855.178.
- **ANS:** RN 465/2021, 195/2009, 387/2015, 469/2021, 539/2022.
- **ANVISA:** RDC 36/2013, 50/2002, 222/2018, 63/2011.

---

## Governança técnica (4 Camadas)

```
Camada 1 — 22 PROIBIÇÕES ABSOLUTAS (invioláveis)
Camada 2 — 6 PROTOCOLOS TÉCNICOS (Vigência, Integridade, Memória, Cruzamento Multi-esfera, Localização, Revisão R1-R4)
Camada 3 — IDENTIDADE FIRAC + estrutura padrão peça/parecer + memória de quantum + ressalva OAB
Camada 4 — 36 SKILLS OPERACIONAIS
```

**Revisão Técnica R1-R4** sobre toda entrega: escopo · técnica jurídica · conformidade ética/regulatória · clareza.

---

## Como instalar (Claude Cowork)

1. Abra **Claude Cowork** → **Settings** → **Plugins**
2. Aba **Pessoal** → clique em **+ Uploads locais**
3. Cole a URL do marketplace recebida na sua compra
4. Clique em **Sincronizar**
5. Em "Pessoal → Uploads locais", clique em **Instalar** no plugin `direito-medico-adv-os`
6. Rode `/start-medico` no Claude Cowork para configurar sua persona (advogado, OAB, cidade, área de foco, tom de voz)

---

## Privacidade (LGPD)

- Dados de paciente, prontuário e identificação **NUNCA** são gravados no plugin.
- Casos vivem em `<seu-workspace>/direito-medico/casos/<slug>/` — pasta gitignored por default.
- Compartimentação por cliente (PA-22).
- Warning automático se pasta de workspace estiver sincronizada (Dropbox/iCloud/OneDrive).

---

## Licença

MIT. Ver `LICENSE`.

---

**Versão:** 0.1.0 · **Autor:** IA Combativa
