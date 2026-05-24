---
name: analise-tcle
description: >
  Validacao juridica do Termo de Consentimento Livre e Esclarecido (TCLE) por especialidade basica (cirurgia, anestesia, oncologia, estetica, telemedicina, reproducao assistida, ortodontia, implantodontia, transfusao, exame invasivo). Checa especificidade, datacao anterior ao procedimento, assinaturas (paciente/responsavel + medico + testemunha), linguagem acessivel (Lei 15.378/2026 — Estatuto do Paciente), conformidade com STJ REsp 1.540.580 (dever de informar). Diferencia obrigacao de meio x resultado (PA-15). Para gerador especifico de 12 modalidades, ver skill `tcle-especialidades` (Tier 2). Aciona: TCLE, termo de consentimento, consentimento informado, dever de informar, REsp 1.540.580, estética cirurgica, anestesia, oncologia consentimento, reproducao assistida termo, telemedicina TCLE, transfusao consentimento, implante consentimento, ortodontia consentimento.
---

# ANALISE DE TCLE

> Skill **Tier 1** — validacao do TCLE como documento juridico-probatorio. Implementa Protocolo 2 (integridade documental) e PA-15 (meio x resultado). Acionada por `medico-master`, `triagem-medica` ou diretamente quando o caso envolve consentimento informado.

---

## 0. Escopo e acionamento

Acionada quando o caso depende de consentimento informado — defesa em PED por procedimento sem TCLE, ação de erro medico por violação do dever de informar, validacao consultiva de TCLE-modelo do cliente-clinica. **Esta skill VALIDA o TCLE existente.** Para **GERACAO** de TCLE especifico por especialidade (12 modalidades), acionar `tcle-especialidades` (Tier 2).

## 1. Posicao na orquestra

- **Chamada por:** `medico-master`, `triagem-medica`, `responsabilidade-civil-medica`, `cirurgia-estetica-resultado`, `responsabilidade-odontologica`, `defesa-ped-crm`, `defesa-ped-cro`, `analise-prontuario-medico` (verifica TCLE anexo).
- **Entrega para:** parecer de validade do TCLE + insumo para defesa/ataque em peca; gerador especifico -> `tcle-especialidades`.
- **Dependencia:** Selo P1 emitido.

## 2. Marco normativo do dever de informar

| Norma | Conteudo |
|-------|----------|
| Lei 8.078/1990 (CDC) art. 6o III | Direito a informacao adequada |
| Res. CFM 1.638/2002 (consolidada) + 2.217/2018 (CEM) | Dever do medico de informar diagnostico, prognostico, riscos e alternativas |
| Res. CFM 2.232/2019 | Recusa terapeutica e diretivas — relacao com TCLE |
| Res. CFM 2.314/2022 + Lei 14.510/2022 | TCLE digital em telemedicina |
| Res. CFM 2.320/2022 | TCLE em reproducao assistida — destino dos embrioes, gestacao por substituicao |
| Res. CFO 118/2012 (CEO) | TCLE em odontologia |
| Lei 15.378/2026 | Estatuto dos Direitos do Paciente — direito a informacao adequada, linguagem acessivel, tempo razoavel para decisao |
| CC art. 15 | Ninguem pode ser constrangido a tratamento medico de risco de vida |
| STJ REsp 1.540.580/DF (3a Turma, 2018) | Dever de informar; nexo causal com o dano se omitido |
| STJ REsp 1.526.466/RS | Cirurgia estetica — obrigacao de resultado; TCLE realista |
| STJ REsp 1.708.628/RS | Hospital privado — relacao consumerista |

## 3. Checklist de validade do TCLE (P2)

### 3.1 — Especificidade
- TCLE generico ("autorizo o procedimento") e FRAGIL.
- TCLE deve descrever: **procedimento especifico**, **alternativas terapeuticas** (com pros/contras), **riscos especificos** com taxas conhecidas, **prognostico**, **possiveis complicacoes**.
- Em **estetica** (obrigacao de resultado — STJ REsp 1.526.466): expectativa **realista**, fotografias pre/pos quando aplicavel, plano de tratamento.

### 3.2 — Datacao e prazo de reflexao
- **Data anterior ao procedimento** — TCLE assinado na sala cirurgica ou momentos antes e fragil. Idealmente: 24-72h antes para procedimentos eletivos.
- **Urgencia/emergencia** (CC art. 15 + Res. CFM 2.217/2018) — admite consentimento verbal/presumido; documentar a posteriori.

### 3.3 — Assinaturas
- **Paciente** (capaz, maior de 18 anos) ou **responsavel legal** (incapaz, menor — pais/tutor; idoso interdito — curador).
- **Medico responsavel** com CRM/UF.
- **Testemunha** quando legalmente exigida (procedimentos eletivos invasivos, transfusao, oncologia, esterilizacao).
- **Assinatura digital** em telemedicina/PEP — ICP-Brasil ou padrao SBIS-CFM.

### 3.4 — Linguagem acessivel
- Lei 15.378/2026 — direito a informacao em linguagem **adequada ao paciente** (escolaridade, idioma, capacidade cognitiva).
- Paciente estrangeiro -> traducao ou interprete identificado.
- Paciente analfabeto -> leitura por terceiro identificado + assinatura por digital + 2 testemunhas (CC art. 595).
- Paciente menor maduro (12-17) — assentimento do menor + consentimento do responsavel (Resolucao CONEP analogica + jurisprudencia familia).

### 3.5 — Conteudo minimo por especialidade (sintese)

| Especialidade | Pontos obrigatorios no TCLE |
|---------------|------------------------------|
| Cirurgia (geral) | Procedimento, anestesia, riscos especificos, transfusao se possivel, tempo de internacao, recuperacao, complicacoes |
| Cirurgia plastica estetica | **Obrigacao de resultado** — STJ REsp 1.526.466; expectativa realista; fotografias pre; possibilidade de retoque; plano de seguimento |
| Anestesia | Tipo de anestesia, riscos anestesicos especificos (choque anafilatico, broncoaspiracao, complicacao neurologica), monitorizacao, jejum |
| Oncologia | Esquema quimio/radio, efeitos colaterais, alternativas, prognostico — Res. CFM 1.638/2002 art. 5o; jurisprudencia oncologica especifica |
| Obstetricia | Parto via vaginal x cesarea, riscos materno-fetais, indicacao da via; possibilidade de cesarea de urgencia |
| Telemedicina | TCLE digital ICP-Brasil ou SBIS — Res. CFM 2.314/2022; ciencia das limitacoes da telessaude |
| Reproducao assistida | **Res. CFM 2.320/2022** — destino dos embrioes excedentes; gestacao por substituicao; doacao de gametas; restricoes legais |
| Estetica nao-cirurgica (botox, preenchedor, peeling) | Procedimento, principio ativo, riscos especificos, contraindicacoes, expectativa realista, plano de manutencao |
| Ortodontia | Plano de tratamento, duracao estimada, custo total, riscos (reabsorcao radicular, recidiva), manutencao pos |
| Implantodontia | Procedimento cirurgico, ossointegracao, riscos (perimplantite, falha), tempo total, custo, alternativas |
| Transfusao sanguinea | Necessidade, riscos infecciosos, alternativas, recusa por Testemunha de Jeova — Res. CFM 1.021/1980 + Res. CFM 2.232/2019 + jurisprudencia |
| Procedimento invasivo (cateterismo, endoscopia, biopsia) | Procedimento, riscos especificos, sedacao se houver, alternativas diagnosticas |

## 4. Parecer de validade (output da skill)

```
PARECER DE VALIDADE DO TCLE — Caso <slug>
Procedimento: <descricao>
Data do TCLE: <DD/MM/AAAA>
Data do procedimento: <DD/MM/AAAA>

## Aspectos formais
- Datacao anterior ao procedimento: <sim/nao>
- Assinatura do paciente/responsavel: <sim/nao> — capacidade verificada: <sim/nao>
- Assinatura do medico (com CRM/UF): <sim/nao>
- Testemunha (quando exigida): <sim/nao>
- Linguagem acessivel (Lei 15.378/2026): <adequada/inadequada/[VERIFICAR]>

## Aspectos materiais
- Especificidade do procedimento: <adequada/generica>
- Alternativas terapeuticas descritas: <sim/nao>
- Riscos especificos discriminados: <sim/nao/parciais>
- Prognostico/expectativa realista: <adequado/inflado/omisso>
- Conteudo minimo da especialidade: <atende/nao atende> [ver tabela 3.5]

## Risco juridico
- Para defesa do medico/clinica: <forte/medio/fraco>
- Para ataque (autor): <forte/medio/fraco>
- Jurisprudencia paradigma aplicavel: <STJ REsp ___>

## Recomendacoes
- [Para o operador, defesa: pontos a destacar]
- [Para o operador, ataque: lacunas explorá­veis]
- [VERIFICAR — atualizacao Lei 15.378/2026 / Res. CFM nova / RN ANS]
```

## 5. Diferenciacao critica meio x resultado (PA-15)

- **Obrigacao de meio** (regra geral medica) — diligencia, conformidade com lex artis; o nao-alcance do resultado clinico nao gera responsabilidade automatica. TCLE com expectativa **realista** e adequado.
- **Obrigacao de resultado** (cirurgia estetica — STJ REsp 1.526.466; certas hipoteses odontologicas — clareamento, lentes, implantes; ortodontia em parte) — o resultado prometido vincula. TCLE com expectativa **inflada** torna a defesa impossivel.

Em estetica: TCLE realista e **defesa estrutural**; TCLE com fotos retocadas, promessa de resultado especifico ou linguagem vendedora desmonta a defesa.

## 6. Vedacoes especificas

- **PA-03** — nao opinar sobre adequacao tecnica do procedimento descrito — apenas validade juridica do TCLE.
- **PA-15** — distinguir meio x resultado na especialidade.
- **PA-16** — TCLE original em `<cwd>/direito-medico/casos/<slug>/arquivos/` (gitignored).
- **PA-11** — RN ANS / Res. CFM/CFO em atualizacao -> `[VERIFICAR]` no parecer.

## 7. Protocolos acionados

- **P2** — esta skill aplica integridade documental ao TCLE.
- **P5** — UF de inscricao do medico (relevante em PED por TCLE inadequado).

## 8. Localizacao

A UF do medico que assinou o TCLE importa para PED CRM/CRO. Telemedicina interestadual -> Res. CFM 2.314/2022 + jurisdição CRM da inscricao do medico (PED) + foro do paciente (civel, CDC art. 101 I).

## 9. Integracao

**Chamada por:** `medico-master`, `triagem-medica`, `analise-prontuario-medico` (TCLE anexo ao prontuario), todas as skills de Tier 2 envolvendo consentimento, Tier 4 PED.

**Entrega para:** parecer de validade ao `CASO.md`; insumo para `cirurgia-estetica-resultado`, `responsabilidade-civil-medica`, `responsabilidade-odontologica`, `defesa-ped-crm`, `defesa-ped-cro`. Quando o caso demanda **redacao de TCLE novo** -> acionar `tcle-especialidades` (Tier 2).

**Sem esta skill:** defesa/ataque sobre dever de informar opera no escuro — perda de jurisprudência STJ paradigma (REsp 1.540.580/DF, REsp 1.526.466/RS) e linha defensiva.
