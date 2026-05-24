---
name: analise-pericia-medica
description: >
  Leitura critica de laudo pericial medico/odontologico (judicial, IML criminal, conselho), formulacao de quesitos defensivos por especialidade, impugnacao de laudo (CPC arts. 466-480 + CPP art. 159), papel e operacao do assistente tecnico (CPC art. 466). Identifica falhas tecnicas do laudo (omissao de exame relevante, ausencia de bibliografia, divergencia com prontuario, falta de qualificacao especifica do perito) — vedada critica pessoal (PA-08). Aplica jurisprudencia STJ sobre pericia medica em erro medico, defesa criminal e PED. Aciona: pericia medica, laudo pericial, IML, assistente tecnico, quesitos, impugnacao de laudo, pericia em PED, divergencia laudo prontuario, CPC 466, CPP 159, qualificacao do perito.
---

# ANALISE DE PERICIA MEDICA

> Skill **Tier 1** — leitura critica de laudo + formulacao de quesitos + impugnacao. Implementa PA-03 (sem juizo clinico — analise tecnico-juridica), PA-08 (sem critica pessoal — articulacao tecnica), Protocolo 2 (integridade documental). Acionada por `medico-master`, `triagem-medica`, todas as skills de Tier 2-4.

---

## 0. Escopo e acionamento

Acionada quando o caso ja tem ou tera **pericia** — judicial em acao civel ou criminal, IML em criminal, pericia em PED CRM/CRO, sindicancia de operadora. Funcoes: (a) leitura critica do laudo existente; (b) formulacao de quesitos defensivos antes da pericia; (c) impugnacao tecnica do laudo apos a pericia; (d) orientacao operacional sobre o assistente tecnico.

## 1. Posicao na orquestra

- **Chamada por:** `medico-master`, `triagem-medica`, `responsabilidade-civil-medica`, `defesa-culpa-medica-criminal`, `defesa-ped-crm`, `defesa-ped-cro`, `cirurgia-estetica-resultado`, `responsabilidade-odontologica`, `perda-de-uma-chance`.
- **Entrega para:** lista de quesitos + parecer critico ao laudo + minuta de impugnacao -> `CASO.md` + insumo para peticao/contestacao/defesa em PED.
- **Pre-requisito:** Selo P1 emitido; `analise-prontuario-medico` (cruzamento prontuario x laudo).

## 2. Marco normativo

| Norma | Conteudo |
|-------|----------|
| CPC arts. 156, 464-480 | Pericia judicial — nomeacao, quesitos, prazo, laudo, assistente tecnico |
| CPC art. 466 | Assistente tecnico — indicacao pela parte; parecer paralelo |
| CPP art. 159 | Pericia criminal — perito oficial; assistente tecnico admitido (Lei 11.690/2008) |
| Res. CFM 2.057/2013 | Pericias medicas — orientacao do CFM |
| Lei 14.689/2023 | Vigencia/ajustes processuais; conferir prazos |
| Res. CFM 2.145/2016 art. 35-40 | Pericia em PED CRM |
| Res. CFO 71/2006 art. ~ | Pericia em PED CRO |
| STJ REsp 1.291.247/RS | Perda de uma chance — papel da pericia na fixacao do percentual |
| STJ REsp 1.526.466/RS | Estetica — inversao de presuncao (medico prova que resultado nao-alcance deriva de causa alheia) |
| STJ AgInt no AREsp 1.245.831/MG | Pericia em civel x penal x etico — CC art. 935 |

## 3. Anatomia do laudo pericial

| Elemento | O que checar |
|----------|--------------|
| **Qualificacao do perito** | CRM/CRO ativo; especializacao COMPATIVEL com o caso (ex.: perito ortopedista em caso de obstetricia = fragilidade); habilitacao em pericias (titulo de Pericia Medica AMB) |
| **Identificacao do caso** | Numero do processo, partes, juizo, data |
| **Metodologia** | Descricao dos exames realizados, materiais consultados, literatura citada |
| **Quesitos respondidos** | Todos os quesitos (do juiz, do autor, do reu, do MP, dos assistentes) respondidos? Resposta fundamentada ou vaga? |
| **Bibliografia** | Literatura medica citada e atualizada? Diretrizes de sociedade medica (SBOC oncologia, FEBRASGO obstetricia, AMB) referenciadas? |
| **Cronologia** | Linha do tempo do evento clinico reconstruida? |
| **Nexo causal** | Pronunciamento sobre nexo causal medico (existencia, contribuicao, exclusao)? |
| **Conduta x lex artis** | Comparacao com padrao tecnico vigente no ano do fato gerador (PA-09)? |
| **Sequelas/dano** | Avaliacao do dano material, estetico, funcional, perda de chance? |
| **Assinatura e identificacao** | CRM/UF + assinatura digital ICP-Brasil quando peticionamento eletronico |

## 4. Formulacao de quesitos defensivos (pre-pericia)

### 4.1 — Quesitos universais (todo caso medico)
1. Qual era o quadro clinico do paciente ao chegar ao atendimento? (estado, gravidade, comorbidades — CID-10)
2. Qual conduta indicada pela **lex artis** vigente no ano do fato (PA-09)?
3. A conduta documentada no prontuario divergiu da lex artis? Em que ponto?
4. Houve documentacao do TCLE? Foi adequado a especialidade?
5. Ha **nexo causal** entre a conduta e o dano alegado?
6. O dano alegado tem outras causas concorrentes (doenca de base, condicao pre-existente, falibilidade)?
7. O tratamento praticado tem **taxa de complicacao conhecida** na literatura? Qual?
8. A conduta poderia ter sido prestada por **profissional medio**? (criterio do "razoavel medico do mesmo nivel" — STJ REsp paradigma)

### 4.2 — Quesitos por especialidade (sintese)

**Obstetricia:** indicacao de cesarea? CTG monitorizada? Apgar? pH cordao? tempo de sofrimento fetal?
**Anestesia:** classificacao ASA pre-anestesica? jejum confirmado? monitorizacao? medicacao de emergencia disponivel?
**Cirurgia plastica estetica:** TCLE com expectativa realista? Fotos pre? Plano de seguimento? Causa do resultado divergente (paciente, infeccao, retoque)?
**Oncologia (atraso diagnostico):** sintomas iniciais documentados? Exames pedidos? Diagnostico em qual janela? Sobrevida na fase diagnosticada x na fase em que deveria ter sido diagnosticada?
**Implantodontia:** planejamento (TC, modelo)? Tecnica cirurgica? Acompanhamento pos-cirurgico? Causa de falha (paciente, periimplantite, sobrecarga)?

### 4.3 — Quesitos para impugnar perito mal-qualificado
- Tem o perito titulo de especialista AMB/CFM na area? Numero do registro?
- Realizou pericias previas em casos similares (curriculum)?
- Pertenceu a sociedade medica da especialidade?

## 5. Pontos de impugnacao do laudo (pos-pericia) — PA-08 sempre respeitada

**Impugnacao tecnica, NUNCA pessoal:**
1. **Omissao de exame relevante** — laudo nao analisou ECG do dia X, ou CTG do parto, ou exame anatomopatologico.
2. **Ausencia de bibliografia** — laudo afirma sem citar diretriz, sociedade medica ou literatura.
3. **Divergencia com prontuario** — laudo afirma X; prontuario diz Y; cruzamento com `analise-prontuario-medico`.
4. **Qualificacao incompativel** — perito de especialidade alheia ao caso.
5. **Resposta vaga ou evasiva a quesito tecnico** — quesito X recebeu "depende", "possivelmente" sem fundamentacao.
6. **Conclusao sem nexo causal explicitado** — laudo afirma "houve erro" sem demonstrar nexo entre conduta e dano.
7. **Aplicacao de lex artis nao-vigente no ano do fato** (PA-09) — perito aplica diretriz nova a fato antigo.
8. **Inobservancia de jurisprudencia paradigma** (perda de chance — REsp 1.291.247; estetica — REsp 1.526.466).
9. **Falta de visita ao paciente** quando aplicavel (avaliacao de sequela).

## 6. Operacao do assistente tecnico (CPC art. 466)

- **Quando indicar:** caso complexo, alto valor, especialidade nichada. Custo do escritorio.
- **Quem indicar:** medico especialista com experiencia pericial; conferir conflito de interesses (PA-22 — vedada relacao com partes).
- **Funcao:** acompanhar pericia oficial, formular quesitos suplementares na audiencia de pericia, apresentar **parecer tecnico paralelo** (CPC art. 477 §1o — 15 dias apos laudo).
- **Operacao em PED:** Res. CFM 2.145/2016 admite assistente tecnico do denunciado (verificar regulamento regional `[VERIFICAR — estatuto CRM-UF]`).
- **Operacao criminal:** CPP art. 159 §3o-5o (Lei 11.690/2008) — assistente tecnico admitido apos exame pericial oficial.

## 7. Parecer critico do laudo (output da skill)

```
PARECER CRITICO DO LAUDO PERICIAL — Caso <slug>
Pericia: <oficial judicial | IML | PED CRM | sindicancia operadora>
Data do laudo: <DD/MM/AAAA>
Perito: <CRM ___ /UF — especialidade ___>

## Aspectos formais
- Qualificacao compativel: <sim/nao>
- Assinatura/identificacao: <ok/falha>
- Quesitos respondidos integralmente: <sim/parcial/nao>

## Aspectos materiais
- Metodologia descrita: <adequada/superficial>
- Bibliografia atualizada citada: <sim/nao>
- Cronologia reconstruida: <sim/nao>
- Nexo causal explicitado: <sim/nao>
- Lex artis aplicada do ano do fato (PA-09): <sim/nao>
- Cruzamento com prontuario: <coerente/divergente — apontar pontos>

## Pontos de fragilidade tecnica do laudo (PRO defesa)
1. <Ponto> — fundamentacao: <norma + jurisprudencia + bibliografia>
2. ...

## Pontos de forca do laudo (PRO autor)
1. <Ponto> — fundamentacao
2. ...

## Quesitos suplementares a formular
1. <Quesito> — finalidade
2. ...

## Recomendacao operacional
- Indicar assistente tecnico: <sim/nao> — perfil sugerido: <especialidade + perfil>
- Impugnacao do laudo: <sim/parcial/nao>
- Pedido de nova pericia: <sim/nao> — fundamento: CPC art. ___

## [VERIFICAR]
- Atualizacao de diretriz da especialidade
- Regulamento regional de pericia em PED [PA-11]
```

## 8. Vedacoes especificas

- **PA-03** — nao opinar sobre adequacao tecnico-clinica fora dos limites do laudo — apenas analise tecnico-juridica.
- **PA-08** — vedada critica pessoal a perito, magistrado, conselheiro. Articulacao tecnica do laudo, nao do peritor.
- **PA-09** — laudo deve aplicar lex artis vigente no ano do fato gerador, nao a atual.
- **PA-11** — regulamento regional `[VERIFICAR]`.
- **PA-16** — laudo original em `<cwd>/direito-medico/casos/<slug>/arquivos/`.

## 9. Protocolos acionados

- **P2** — integridade documental do laudo (esta skill executa).
- **P5** — UF de inscricao do perito (relevante em impugnacao por incompatibilidade ou suspeicao).

## 10. Localizacao

A UF do perito importa para CRM regional (sindicancia disciplinar contra perito ele mesmo, raro mas possivel). Em telemedicina pericial (avancando) — Res. CFM 2.314/2022 admite teleperícia em hipoteses restritas; `[VERIFICAR]` quando relevante.

## 11. Integracao

**Chamada por:** `medico-master`, `triagem-medica`, todas as skills de Tier 2-4 envolvendo pericia.

**Entrega para:** parecer critico + lista de quesitos + minuta de impugnacao -> insumo direto para `responsabilidade-civil-medica`, `defesa-culpa-medica-criminal`, `defesa-ped-crm`, `defesa-ped-cro`, `perda-de-uma-chance`, `cirurgia-estetica-resultado`.

**Sem esta skill:** pericia opera como "caixa preta" — defesa sem quesitos, sem impugnacao tecnica, sem assistente tecnico = derrota probatoria quase certa.
