---
name: memoria-de-caso-medico
description: >
  Skill invariante de Memoria de Caso — CASO.md compartimentado por cliente em `<cwd>/direito-medico/casos/<slug>/`. Operacionaliza PA-22 (compartimentacao absoluta) + PA-16/PA-17 (sigilo medico + LGPD art. 11). Estrutura: CASO.md (estado vivo do caso), MEMORY.md (decisoes e historico), `arquivos/` (prontuario, exames, TCLE), `pecas/` (produzidos). Pasta gitignored por default. Alerta quando workspace e pasta sincronizada (iCloud/OneDrive/Dropbox/Google Drive). Garante que nenhum dado de paciente persista no plugin distribuido. Aciona: novo caso medico, abrir caso, CASO.md, memoria do caso, retomar caso, /caso-medico, prontuario pasta caso, sigilo LGPD compartimentacao.
---

# MEMORIA DE CASO MEDICO

> Skill **transversal** — gerencia a pasta de cada caso/cliente. Implementa PA-16/17/22 (sigilo + LGPD + compartimentacao). Acionada por `medico-master` (abertura/retomada de caso), `triagem-medica`, `onboarding-medico`, todas as skills consultoras do CASO.md.

---

## 0. Escopo e acionamento

Cria, mantem e consulta a pasta `<cwd>/direito-medico/casos/<slug>/` com a memoria operacional de cada caso/cliente. Acionada em (a) abertura de caso novo; (b) retomada de caso ja em curso; (c) leitura/atualizacao por outras skills; (d) encerramento e arquivamento. Pre-requisito: `direito-medico/cowork-state.json` configurado (via `onboarding-medico` / `/start-medico`).

## 1. Posicao na orquestra

- **Chamada por:** `medico-master`, `triagem-medica`, `onboarding-medico`, todas as skills consultivas/produtivas (Tier 1-6) que precisam do estado do caso.
- **Aciona:** `validador-legislacao-vigente` (data do Selo gravada no CASO.md), `revisao-final-medica` (leitura final).
- **Entrega para:** estado vivo + historico do caso disponivel para todas as skills.

## 2. Estrutura da pasta `<cwd>/direito-medico/`

```
<cwd>/direito-medico/                       (gitignored — LGPD)
├── persona.md                              identidade do advogado/escritorio
├── cowork-state.json                       state operacional do plugin
└── casos/                                  (uma pasta por cliente — PA-22)
    ├── <slug-cliente-1>/
    │   ├── CASO.md                         estado vivo do caso
    │   ├── MEMORY.md                       historico de decisoes
    │   ├── arquivos/                       documentos do paciente (gitignored)
    │   │   ├── prontuario/                 prontuario eletronico/papel
    │   │   ├── exames/
    │   │   ├── laudos/
    │   │   └── contratos/                  apolice, TCLE assinado
    │   └── pecas/                          produzidos pelo plugin
    │       ├── 2026-05-24-resposta-acusacao.md
    │       └── 2026-05-30-tutela.md
    ├── <slug-cliente-2>/
    └── ...
```

**Compartimentacao absoluta:** cada pasta e isolada. Skill NUNCA mistura dados entre pastas.

## 3. Estrutura do CASO.md (template)

```
# CASO.md — [Slug do cliente]

> Estado vivo do caso. Atualizar a cada acao do plugin.
> Ultima atualizacao: [YYYY-MM-DD HH:MM]

## 1. Identificacao
- **Cliente do escritorio:** [advogado vs medico/clinica/paciente/operadora — PA-01]
- **Profissional defendido (se aplicavel):** [medico/dentista — CRM/CRO + UF]
- **Paciente (se cliente):** [iniciais; sem CPF no plugin — PA-16]
- **Numero(s) processuais:** [civel / criminal / PED / MS / etc.]
- **Foro/competencia:** [JE / JF / CRM-UF / CFM Brasilia / etc. — P5]

## 2. Triagem 4D (resultado de `triagem-medica`)
- **Sujeito:** [profissional PF / clinica PJ / hospital PJ / paciente / operadora]
- **Modo:** [consultivo / contencioso]
- **Esferas ativas:** [civil / criminal / etico / regulatorio] — Cruzamento P4 se 2+
- **Subdominio:** [medicina / odonto / saude mental / reproducao / outros]

## 3. Fato gerador
- **Data do fato:** [YYYY-MM-DD]
- **Local:** [Cidade/UF]
- **Especialidade:** [obstetricia / cirurgia / odonto / etc.]
- **Tipo:** [erro diagnostico / erro cirurgico / negativa de cobertura / etc.]
- **Sintese (3-5 linhas):** [narrativa]

## 4. Selo de Validacao Legal Previa (P1)
- **Data do Selo:** [YYYY-MM-DD] (validade 60 dias)
- **Emitido por:** validador-legislacao-vigente
- **Versao normativa:** [resolucoes/leis/jurisprudencia citadas — PA-09 + PA-10]
- **[VERIFICAR]:** [items em alvo movel para conferencia]

## 5. Estrategia
- **Skills acionadas:** [lista]
- **Pecas produzidas:** [lista referenciada em `pecas/`]
- **Pendencias:** [acoes do advogado-operador]
- **Proximos passos:** [proxima fase]

## 6. Multi-esfera (P4)
| Esfera | Status | Skill | Proxima acao |
|--------|--------|-------|--------------|
| Civel | Em peticao | responsabilidade-civil-medica | Distribuir |
| Criminal | Em defesa previa | defesa-culpa-medica-criminal | Pericia |
| PED CRM | Em sindicancia | defesa-ped-crm | Aguarda denuncia formal |

## 7. Documentos do caso (gitignored — em `arquivos/`)
- Prontuario: [referencia]
- Exames: [referencia]
- Laudos: [referencia]
- TCLE: [referencia]
- Apolice / contrato: [referencia]
- Negativa formal: [referencia]

## 8. Quantum (P3 — quando aplicavel)
[Tabela]

## 9. Historico de revisoes R1-R4 (P6)
| Data | Documento | Veredito | Observacoes |
|------|-----------|----------|-------------|
| 2026-05-24 | Resposta a acusacao v1 | APROVADO COM RESSALVAS | Ajustar pedido sucessivo |

## 10. Observacoes do operador
[Anotacoes do advogado — comunicacao com cliente, decisoes estrategicas]
```

## 4. Sigilo + LGPD (PA-16/17 — vetor critico)

| Item | Aplicacao |
|------|-----------|
| **Pasta gitignored por default** | `.gitignore` raiz do plugin garante |
| **Workspace em pasta sincronizada (iCloud/OneDrive/Dropbox/Drive)** | **ALERTAR** o operador — risco LGPD + sigilo medico |
| **Mistura de clientes no mesmo prompt** | Vedada — PA-22 |
| **CPF do paciente no CASO.md** | Vedado — usar iniciais |
| **Prontuario completo no CASO.md** | Vedado — apenas referencias a `arquivos/` |
| **Fotos/imagens identificaveis** | Anonimizar (rosto coberto) — PA-16 |
| **Compartilhamento entre skills** | So o necessario a tarefa (PA-17) |
| **Backup do CASO.md** | Recomendar backup local **criptografado** — nao em cloud sem cifragem |

## 5. Detector de pasta sincronizada (alerta)

Ao abrir/criar caso, verificar se `<cwd>` esta em:
- `~/iCloud Drive/`, `~/Library/Mobile Documents/com~apple~CloudDocs/`
- `~/Dropbox/`
- `~/OneDrive/`
- `~/Google Drive/`, `~/Library/CloudStorage/GoogleDrive-*/`

Se sim, emitir alerta:
```
⚠️ ATENCAO LGPD — workspace em pasta sincronizada
Path detectado: [path]

A pasta direito-medico/ contera dados sensiveis de paciente (LGPD art. 11
+ art. 154 CP). Sincronizacao em cloud sem cifragem viola dever de sigilo.

RECOMENDACAO: mover workspace para pasta local nao-sincronizada
(ex.: ~/Documents/Trabalho/casos-medicos/) ou ativar cifragem de pasta
(BitLocker / FileVault / Veracrypt) — confirmar antes de prosseguir.

Confirma prosseguir mesmo assim? (s/n)
```

## 6. Operacoes (CRUD do caso)

| Operacao | Comando / acao |
|----------|----------------|
| **Criar caso novo** | `/caso-medico novo <slug>` -> cria pasta + CASO.md template |
| **Retomar caso** | `/caso-medico <slug>` -> le CASO.md + MEMORY.md |
| **Listar casos** | `/caso-medico list` -> lista slugs |
| **Atualizar CASO.md** | Skills produtoras gravam apos R1-R4 aprovacao |
| **Arquivar caso** | Mover para `casos/_arquivados/` quando encerrado |
| **Excluir caso** | **Confirmacao dupla** — exige justificativa + Selo de exclusao no MEMORY.md geral |

## 7. MEMORY.md do caso (historico)

```
# MEMORY.md — caso [slug]

## Eventos
- 2026-05-15 — Caso aberto; triagem 4D = profissional/contencioso/civil+criminal+PED
- 2026-05-18 — Selo P1 emitido (60d validade)
- 2026-05-20 — Resposta a acusacao v1 - R1-R4 APROVADO COM RESSALVAS
- 2026-05-24 — Tutela civel distribuida (n. ___)

## Decisoes estrategicas
- 2026-05-18 — Optar por sursis processual (Lei 9.099 89) em caso de improcedencia
  da absolvicao sumaria — paciente operacional ja em recuperacao funcional
- 2026-05-22 — Nao protocolar reconsideracao no CRM — manter MS na JF como via
  unica para preservar surpresa estrategica

## Pendencias do operador
- [ ] Conferir conviccao do laudo IML antes de R3
- [ ] Atualizacao da RN ANS antes da peticao Tier 5
```

## 8. Vedacoes especificas

- **PA-16/17** — sigilo + LGPD reforcado.
- **PA-22** — compartimentacao absoluta — sem mistura.
- **PA-19** — prescricao de cada esfera gravada no CASO.md.
- **PA-13** — referencias em CASO.md com identificacao precisa.

## 9. Protocolos acionados

- **P1** — Selo emitido fica gravado no CASO.md (validade 60d).
- **P3** — memoria de decisao + quantum.
- **P4** — quadro multi-esfera coordena defesa simultanea.
- **P5** — foro/competencia.
- **P6** — historico de revisoes R1-R4.

## 10. Localizacao

Pasta vive **em `<cwd>/direito-medico/casos/`** — local ao operador. Nao subir para cloud sem criptografia (PA-16). Backup recomendado em armazenamento criptografado local (HD externo cifrado, NAS criptografado).

## 11. Integracao

**Chamada por:** todas as skills do plugin para ler/escrever estado do caso.

**Entrega para:** estado vivo disponivel para `medico-master`, `triagem-medica`, todas as skills Tier 1-6 e `revisao-final-medica`.

**Sem esta skill:** caos operacional — skills nao tem estado persistente; impossivel coordenar defesa multi-frente (P4); risco de vazamento de dados de paciente (LGPD); mistura entre clientes (PA-22).
