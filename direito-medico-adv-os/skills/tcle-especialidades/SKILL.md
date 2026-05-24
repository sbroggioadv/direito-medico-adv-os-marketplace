---
name: tcle-especialidades
description: >
  Gerador de TCLE especifico por especialidade — 12 modalidades: cirurgia plastica estetica, oncologia (quimio/radio), obstetricia (parto/cesarea), anestesia, telemedicina (Res. CFM 2.314/2022), reproducao assistida (Res. CFM 2.320/2022), estetica nao-cirurgica (botox/preenchedor), ortodontia, implantodontia, transfusao sanguinea (incluindo Testemunha de Jeova — Res. CFM 1.021 + 2.232), exames invasivos (cateterismo/endoscopia/biopsia), HOF (Res. CFM 2.337/2023). Aplica STJ REsp 1.526.466/RS (estetica obrigacao de resultado), REsp 1.540.580/DF (dever de informar), Lei 15.378/2026 (linguagem acessivel). Para VALIDAR TCLE existente, ver `analise-tcle` (Tier 1). Aciona: redigir TCLE, gerar termo de consentimento, modelo TCLE, TCLE para cirurgia, TCLE estetica, TCLE oncologia, TCLE anestesia, TCLE telemedicina, TCLE reproducao, TCLE implante, TCLE ortodontia, TCLE transfusao, TCLE HOF, TCLE harmonização orofacial.
---

# TCLE ESPECIALIDADES

> Skill **Tier 2** — gerador de TCLE especifico. Implementa PA-15 (meio x resultado), PA-13 (citacao precisa), PA-04 (Selo). Acionada por `medico-master`, consultivo de clinica, ou em paralelo com `analise-tcle` quando defesa demanda TCLE-modelo a ser oferecido ao cliente.

---

## 0. Escopo e acionamento

Acionada quando o operador-advogado consultor precisa **redigir TCLE-modelo** para clinica/hospital/medico autonomo. **Esta skill GERA TCLE novo.** Para VALIDAR TCLE existente em caso litigioso, ver `analise-tcle` (Tier 1). Pre-requisito: Selo P1 emitido para o caso/contexto.

## 1. Posicao na orquestra

- **Chamada por:** `medico-master`, consultivo (Tier 6 `constituicao-sociedade-medica`, `contrato-prestacao-medica`), defesa preventiva.
- **Entrega para:** TCLE-modelo formatado por modalidade + ressalva OAB de revisao -> operador entrega ao cliente-clinica.
- **Dependencia:** Selo P1 + identificacao da modalidade.

## 2. Marco normativo comum

| Norma | Conteudo |
|-------|----------|
| Lei 8.078/1990 CDC art. 6o III | Direito a informacao adequada |
| Res. CFM 2.217/2018 (CEM) art. 22, 24, 31, 34 | Dever de informar diagnostico, prognostico, riscos, alternativas |
| Res. CFM 1.638/2002 | Consentimento informado (consolidada) |
| Res. CFM 2.232/2019 | Recusa terapeutica + DAV |
| Lei 15.378/2026 | Estatuto do Paciente — linguagem acessivel, tempo razoavel para decisao |
| CC art. 15 | Constrangimento a tratamento de risco de vida |
| STJ REsp 1.540.580/DF | Dever de informar — omissao gera nexo causal |
| STJ REsp 1.526.466/RS | Estetica obrigacao de resultado |

## 3. Estrutura canonica do TCLE (toda modalidade)

```
TERMO DE CONSENTIMENTO LIVRE E ESCLARECIDO
[MODALIDADE: ___]

PACIENTE: ____________ (RG ____, capacidade plena/responsavel legal ___)
MEDICO/DENTISTA: ____________ (CRM/CRO ___/UF)
ESTABELECIMENTO: ____________ (CNES ___)
DATA: ____________ (anterior ao procedimento)

EU, paciente acima qualificado, declaro que recebi informacoes claras e
acessiveis sobre o procedimento abaixo:

1. NATUREZA E OBJETIVO DO PROCEDIMENTO
   [Descricao especifica do que sera feito — sem jargao tecnico inacessivel]

2. ALTERNATIVAS TERAPEUTICAS / DIAGNOSTICAS
   [Lista de alternativas com pros, contras, probabilidade de eficacia]

3. RISCOS ESPECIFICOS E COMPLICACOES POSSIVEIS
   [Lista discriminada — taxas conhecidas na literatura]

4. PROGNOSTICO E EXPECTATIVA
   [Realista — meio ou resultado conforme PA-15]

5. CUIDADOS POS-PROCEDIMENTO
   [Orientacoes claras]

6. POSSIBILIDADE DE RECUSA E ALTERACAO DE DECISAO
   [Direito do paciente, CC art. 15 + Res. CFM 2.232/2019]

DECLARO ainda que: tive tempo razoavel para decidir; tive oportunidade
de esclarecer duvidas; entendi as informacoes em linguagem acessivel
(Lei 15.378/2026); a assinatura representa minha decisao livre.

_______________________     _______________________     _______________________
Paciente/Responsavel        Medico/Dentista (CRM/CRO)   Testemunha (quando exigida)
```

## 4. Modalidades especificas — TCLE blocks

### 4.1 — Cirurgia plastica estetica (OBRIGACAO DE RESULTADO — REsp 1.526.466/RS)
**Pontos criticos:**
- Expectativa **realista** — vedada promessa de resultado especifico.
- Fotografias pre-procedimento anexadas (anexo I).
- Plano de seguimento pos-cirurgico.
- Esclarecer: cicatrizacao varia por paciente; possibilidade de retoque com custo.
- **Defesa:** TCLE realista + foto pre + seguimento + descumprimento do paciente como excludentes.

### 4.2 — Oncologia (quimio/radio/imunoterapia)
**Pontos criticos:**
- Esquema (quimio especifica, ciclos, droga).
- Efeitos colaterais comuns + graves (mielossupressao, neuropatia, mucosite).
- Eficacia esperada com base em literatura (sociedade medica — SBOC).
- Alternativas (esquema diferente, paliativo, expectativa).
- Em off-label: indicacao fundada em literatura/diretriz.
- Recusa terapeutica admitida (CC art. 15 + Res. CFM 2.232/2019).

### 4.3 — Obstetricia (parto/cesarea)
**Pontos criticos:**
- Via prevista (vaginal ou cesarea) + indicacao.
- Riscos especificos materno-fetais por via.
- Possibilidade de **cesarea de urgencia** durante trabalho de parto.
- Anestesia obstetrica (peri/raqui — riscos especificos).
- Acompanhante (Lei 11.108/2005) — direito da gestante.

### 4.4 — Anestesia
**Pontos criticos:**
- Tipo: geral/raqui/peri/sedacao + escolha justificada.
- Riscos: choque anafilatico, broncoaspiracao, complicacoes neurologicas, despertar intraoperatorio.
- Jejum prescrito + monitorizacao.
- Classificacao ASA pre-anestesica.

### 4.5 — Telemedicina (Res. CFM 2.314/2022 + Lei 14.510/2022)
**Pontos criticos:**
- TCLE **digital** com assinatura ICP-Brasil ou padrao SBIS-CFM.
- Limitacoes da telemedicina (necessidade eventual de exame presencial).
- Sigilo dos dados — plataforma certificada.
- Protocolo de continuidade do cuidado.

### 4.6 — Reproducao assistida (Res. CFM 2.320/2022)
**Pontos criticos:**
- Tecnica (FIV, ICSI, IIU).
- Probabilidade de sucesso por idade e diagnostico.
- **Destino dos embrioes excedentes** (descarte / doacao para pesquisa / criopreservacao indefinida).
- Gestacao por substituicao — regras.
- Doacao de gametas — anonimato + limites.

### 4.7 — Estetica nao-cirurgica (botox, preenchedor, peeling)
**Pontos criticos (obrigacao de resultado em parte — REsp 1.526.466 analogica):**
- Principio ativo + lote + validade.
- Riscos especificos (necrose por preenchedor mal-aplicado, ptose por botox).
- Contraindicacoes (gestacao, lactacao, alergias).
- Expectativa realista + plano de manutencao (duracao do efeito).

### 4.8 — Ortodontia
**Pontos criticos:**
- Plano de tratamento + duracao estimada + custo total.
- Riscos: reabsorcao radicular, recidiva, problemas periodontais.
- Manutencao pos-tratamento (contensao).
- Compromisso do paciente com higiene + comparecimento.

### 4.9 — Implantodontia (OBRIGACAO DE RESULTADO em parte — STJ analogica)
**Pontos criticos:**
- Procedimento cirurgico (incisao, fresagem, fixacao).
- Riscos: perda de implante, perimplantite, fratura ossea.
- Cronograma (cirurgia, ossointegracao, protetização).
- Alternativas (protese sobre dentes, removivel).

### 4.10 — Transfusao sanguinea (Testemunha de Jeova — Res. CFM 1.021/1980 + Res. CFM 2.232/2019)
**Pontos criticos:**
- Necessidade fundamentada.
- Riscos infecciosos (residuais) + reacoes transfusionais.
- Alternativas: hemodiluicao, recuperador celular, eritropoetina, ferro IV.
- **Recusa por crença religiosa** (Testemunha de Jeova) — Res. CFM 1.021 + 2.232 + STF (autonomia x dever medico em risco de vida — jurisprudencia em construcao). `[VERIFICAR — STJ/STF mais recente]`.
- Termo de recusa especifica com riscos compreendidos.

### 4.11 — Exames invasivos (cateterismo/endoscopia/biopsia)
**Pontos criticos:**
- Procedimento + sedacao se houver.
- Riscos especificos (perfuracao, sangramento, infeccao).
- Alternativas diagnosticas (imagem nao-invasiva).

### 4.12 — HOF (Harmonização Orofacial — Res. CFM 2.337/2023)
**Pontos criticos — conflito interconselhos:**
- Sujeito: medico OU cirurgiao-dentista (CFO admite; CFM 2.337/2023 restringe).
- Procedimento especifico (toxina, preenchimento, fios, peeling).
- Riscos esteticos e funcionais.
- **`[VERIFICAR]` — sujeito habilitado para o procedimento concreto na sua UF** (estatuto CRM/CRO regional pode complementar).
- TCLE expressamente conformado a Res. CFO 230/2020 (se CD) ou Res. CFM 2.337/2023 (se medico).

## 5. Vedacoes especificas

- **PA-15** — distinguir meio (obstetricia, oncologia, exame, anestesia) x resultado (estetica cirurgica, estetica nao-cirurgica, implantes, parte da ortodontia).
- **PA-03** — TCLE descreve o procedimento, nao opina sobre adequacao tecnico-clinica.
- **PA-05** — TCLE-modelo gerado e **rascunho** — clinica deve revisar com seu RT medico e advogado.
- **PA-11** — alvo movel (Lei 15.378/2026 ainda em interpretacao; HOF conflito CFM x CFO ativo) -> `[VERIFICAR]`.
- **PA-22** — TCLE-modelo NAO carrega dado de paciente real — vazio para preenchimento na clinica.

## 6. Protocolos acionados

- **P1** — Selo verificado antes de gerar TCLE.
- **P3** — TCLE bem-redigido = base probatoria solida para defesa futura (P3 indireta).

## 7. Localizacao

A UF do medico/dentista importa para CRM/CRO regional (HOF tem conflito interconselhos por UF). Telemedicina interestadual -> TCLE digital com referencia a CRM da inscricao do medico.

## 8. Integracao

**Chamada por:** `medico-master`, consultivo de clinica (Tier 6), defesa preventiva.

**Entrega para:** TCLE-modelo por modalidade -> operador entrega a clinica + sugestao de revisao por RT + advogado da clinica. Em paralelo: `analise-tcle` valida TCLE ja existente; esta skill **GERA novo**.

**Sem esta skill:** clinica opera com TCLE generico, fragilidade em PED/civel; ou paga R$ 3-5k para advogado especializado redigir do zero. Esta skill entrega 12 modelos juridicamente solidos prontos para refinamento clinico.
