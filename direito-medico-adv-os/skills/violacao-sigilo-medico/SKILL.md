---
name: violacao-sigilo-medico
description: >
  Defesa criminal em violacao de segredo profissional (CP art. 154) e desdobramentos civis/eticos/ANPD. Articula sigilo medico tripartite — penal (CP 154), etico (CEM 2.217/2018 art. 73 + Res. CFM 1.605/2000 + 1.821/2007) e LGPD art. 11 (dado sensivel). Mapeia excecoes legitimas: notificacao compulsoria (Portaria GM/MS 264/2020 + Lei 6.259/75), denuncia obrigatoria (ECA art. 13; EI art. 19; Lei 10.778/2003), estado de necessidade (CP 24), justa causa, consentimento. Teses: justa causa, estado de necessidade, ausencia de dolo, consentimento, sigilo cessado, comunicacao interna licita. Casos: prontuario vazado, foto em rede social, depoimento em juizo extrapolado, perito que excede. Aciona: violacao sigilo medico, CP 154, segredo profissional, LGPD saude, vazamento prontuario, foto paciente rede social, notificacao compulsoria, ECA 13, ANPD, dado sensivel.
---

# VIOLACAO DE SIGILO MEDICO

> Skill **Tier 3** — defesa criminal/etica/civel em violacao de segredo profissional medico/odontologico. Implementa PA-03 (sem opinar conduta), PA-06 (sem orientacao clinica), PA-08 (sem critica pessoal), PA-13 (citacao precisa), PA-16 (sigilo do plugin), PA-17 (so o necessario). Acionada por `medico-master`, `triagem-medica` (esfera criminal/civel), `timeline-multiesfera`.

---

## 0. Escopo e acionamento

Defesa de profissional acusado de quebra de sigilo medico/odontologico em (a) acao penal (CP 154 — pena 3m-1a + multa); (b) PED CRM/CRO (CEM 2.217 art. 73 e correlatos); (c) acao civel por dano moral (CC 186 + LGPD 42); (d) sancao ANPD (LGPD 52). Inclui: vazamento de prontuario, publicacao de foto/imagem em rede social, depoimento extrapolando o necessario, divulgacao por funcionario, perdas de USB/HD com dados, conversa indiscreta em local publico.

## 1. Posicao na orquestra

- **Chamada por:** `medico-master`, `triagem-medica`, `timeline-multiesfera`, `compliance-publicidade-medica` (caso de imagem/foto), `lgpd-saude` (vazamento massa).
- **Aciona:** `defesa-ped-crm` ou `defesa-ped-cro`, `responsabilidade-civil-medica` (reflexo civel), `revisao-final-medica`.
- **Entrega para:** defesa criminal e/ou administrativa e/ou civel coordenada.

## 2. Marco normativo (tripartite)

| Esfera | Norma | Conteudo |
|--------|-------|----------|
| **Penal** | **CP art. 154** | Crime de violacao de segredo profissional — pena 3m-1a + multa |
| Penal | CP art. 153 | Divulgacao de segredo (correlato, doc privado) |
| Etica | **Res. CFM 2.217/2018 art. 73** | CEM — vedacao de quebra; excecoes |
| Etica | Res. CFM 1.605/2000 + 1.821/2007 | Sigilo de prontuario + guarda 20 anos |
| Etica odonto | Res. CFO 118/2012 + CFO 196/2019 | CEO — sigilo + publicidade |
| LGPD | **Art. 11** | Dado de saude — sensivel — bases legais restritas |
| LGPD | Art. 11§2o | Bases: consentimento; tutela da saude; obrigacao legal; pesquisa; protecao da vida; exercicio regular |
| LGPD | Art. 7o III + 11§2o "a" | Cumprimento de obrigacao legal — notificacao compulsoria |
| LGPD | Art. 42-45 / 52 | Responsabilidade civil + sancao ANPD |
| Civel | CC art. 186 + 927 | Dano moral por quebra |
| Excecoes legitimas | Portaria GM/MS 264/2020 + Lei 6.259/75 | Notificacao compulsoria (LRDC/Sinan) — agravos transmissiveis + nao-transmissiveis listados |
| Excecoes | ECA art. 13 / EI Lei 10.741 art. 19 / Lei 10.778 | Denuncia obrigatoria — crianca, idoso, mulher violencia |
| Processual | CPC art. 388 / CPP 207 | Sigilo oponivel em juizo (recusa fundamentada) |

**Jurisprudencia:** STJ AgRg AREsp 1.122.345 (vazamento prontuario por funcionario — responsabilidade objetiva do estabelecimento — CDC 14); STF RE 1.236.834 (dado de saude e dado sensivel — sigilo reforcado); TJSP n. precedentes recorrentes em foto de paciente em rede social `[VERIFICAR jurisprudencia atual]`.

## 3. Quebra autorizada — mapa de excecoes legitimas

| Excecao | Base legal | Quem aciona | Limite |
|---------|-----------|-------------|--------|
| **Notificacao compulsoria** | Portaria GM/MS 264/2020 + Lei 6.259/75 | Medico/dentista assistente | Lista LRDC/Sinan; preenchimento Sinan |
| **Denuncia obrigatoria — crianca** | ECA art. 13 + art. 245 | Profissional | Conselho Tutelar + autoridade |
| **Denuncia obrigatoria — idoso** | EI art. 19 (Lei 10.741) | Profissional | Conselho do Idoso / MP |
| **Notificacao violencia mulher** | Lei 10.778/2003 | Profissional | Notificacao compulsoria + atendimento Lei Maria da Penha |
| **Notificacao violencia sexual** | Lei 12.845/2013 | Profissional | Atendimento obrigatorio |
| **Estado de necessidade medico** | CP 24 + Res. CFM 2.217 73 | Medico/dentista | Risco a terceiros (homicida confessor; dirige embriagado) `[VERIFICAR doutrina]` |
| **Justa causa (CP 154 caput)** | CP 154 | Profissional | Defesa propria; exigencia legitima; concurso |
| **Autorizacao expressa do paciente** | CC art. 421 + LGPD 7o I + 11§2o "a" | Paciente | Por escrito; especifica e limitada |
| **Sigilo cessado** | Doutrina | — | Paciente revelou publicamente o fato medico |
| **Comunicacao a colega substituto** | CEM 2.217 art. 72§2o | Medico assistente | So o necessario a continuidade |
| **Ordem judicial fundamentada** | CPC 369 + 396 | Juizo | Pode-se recusar (CPC 388 + CPP 207); ponderar com fundamentacao |

**Importante:** essas excecoes **autorizam** a quebra, nao **obrigam** — exceto notificacao compulsoria e denuncias correlatas, que sao deveres legais.

## 4. Teses defensivas (cardapio)

| Tese | Fundamento | Acionar |
|------|-----------|---------|
| **Atipicidade — justa causa** | CP 154 caput in fine | Defesa propria; estado de necessidade; cumprimento de dever |
| **Estado de necessidade** | CP 24 + Res. CFM 2.217 73 | Risco concreto a terceiro |
| **Ausencia de dolo (CP 154 e doloso)** | CP 18 I | Vazamento culposo (perda de dispositivo); sem intencao de divulgar |
| **Consentimento expresso** | LGPD 7o I + 11§2o "a" + CC 421 | Autorizacao escrita do paciente |
| **Sigilo cessado** | Doutrina | Paciente publicou o fato; fato notorio |
| **Comunicacao interna licita** | CEM 2.217 art. 72§2o | Continuidade do cuidado; equipe multidisciplinar |
| **Cumprimento de dever legal** | CP 23 III + Portaria 264/2020 | Notificacao compulsoria; ECA 13; Lei 10.778 |
| **Erro de proibicao** | CP 21 | Conviccao equivocada de legitimidade |
| **Inepcia da denuncia** | CPP 41 | Acusacao generica; sem individualizar conteudo divulgado |
| **Prescricao** | CP 109-110 | Pena prevista x marcos |

## 5. Casos tipicos

- **Foto/imagem em rede social:** antes/depois identificavel; foto prontuario; relato clinico. Defesa: ausencia de consentimento valido (Res. CFM 2.336/2023); reducao por dosimetria. Reflexo civel + PED certos.
- **Prontuario vazado por funcionario:** objetiva da clinica (CDC 14 + LGPD 42). Defesa do medico PF: ausencia de conduta + dever de fiscalizacao razoavel.
- **Depoimento em juizo:** CPC 388 + CPP 207 — direito-dever de silenciar. Defesa: depos so o necessario; convalidacao do magistrado.
- **WhatsApp/grupo profissional vazado por terceiro:** CEM 72§2o — comunicacao interna com expectativa razoavel; ausencia de previsibilidade.
- **Notificacao compulsoria + denuncia ECA 13:** excecao licita.
- **Perito que extrapola:** ausencia de dever pericial sobre dado nao-objeto; impugnacao (CPC 480).

## 6. Quesitos para a pericia (P2 — em casos de vazamento documental)

1. O conteudo divulgado configura dado de saude (LGPD art. 11)?
2. O canal de divulgacao foi controlado (interno) ou aberto (rede social, publico)?
3. Houve consentimento? Especifico ou generico?
4. Foi feita anonimizacao tecnica (LGPD art. 5o III) suficiente para descaracterizar a identificabilidade?

## 7. Esqueleto FIRAC — Resposta a acusacao (CP 154)

```
RESPOSTA A ACUSACAO — CPP 396-A
EXMO. SR. JUIZ DA ___ VARA CRIMINAL DE [Cidade/UF]

[ACUSADO], CRM/CRO [num/UF], por {{ADVOGADO_NOME}} OAB/{{OAB_UF}} {{OAB_NUMERO}}

I — FATOS [F] — narrativa datada (referencia CASO.md)
II — ISSUE [I] — houve divulgacao a quem o sigilo era oponivel? Houve dolo?
III — DIREITO [R]
  III.1 Tipicidade — CP 154 exige (a) segredo a que se obrigou; (b) divulgacao
        sem justa causa; (c) potencial dano (PA-13)
  III.2 [Justa causa / consentimento / sigilo cessado / dever legal / atipicidade]
  III.3 LGPD art. 11§2o — base legal aplicavel
  III.4 Cruzamento P4 — PED CRM/CRO + civel + ANPD em paralelo
IV — PEDIDOS [C]
  IV.1 Absolvicao sumaria (CPP 397 III — atipicidade)
  IV.2 Subsidiariamente: sursis processual (Lei 9.099/95 89)
  IV.3 Subsidiariamente: transacao penal (art. 76 — pena max 1a cabe)
  IV.4 Arrolamento de testemunhas (max 8)

[Cidade, data] — {{ADVOGADO_NOME}} | OAB/{{OAB_UF}} {{OAB_NUMERO}}

RESSALVA (PA-05).
```

## 8. Cruzamento P4 — efeito propagado (PA-12)

| Esfera | Risco |
|--------|-------|
| Penal (CP 154) | Sursis ou transacao em geral disponiveis |
| PED CRM/CRO (CEM 73) | Sancao etica — censura confidencial -> cassacao |
| Civel (CC 186 + 927 + LGPD 42) | Dano moral; quantum conservador (PA-21) |
| ANPD (LGPD 52) | Multa ate 2% do faturamento (limite R$ 50M) |

Articulacao paralela: defesa criminal nao basta; PED + civel + ANPD correm em paralelo. `timeline-multiesfera` coordena.

## 9. Vedacoes especificas

- **PA-03 / PA-06 / PA-08** — sem opinar conduta, sem orientacao ao paciente, sem critica pessoal.
- **PA-13** — CP/LGPD/Res. CFM/CFO com identificacao precisa.
- **PA-16 / PA-17** — esta skill **opera sobre sigilo** — atenção redobrada com dados do CASO.md (compartimentacao + so o necessario).
- **PA-21** — em quantum civel reflexo, conservadorismo.

## 10. Protocolos acionados

- **P1** — Selo.
- **P2** — `analise-prontuario-medico` (conteudo divulgado + autorizacao) + pericia se aplicavel.
- **P4** — `timeline-multiesfera` (penal + PED + civel + ANPD).
- **P5** — JE comum (CP 154 e infracao de menor potencial — Lei 9.099); JF se estabelecimento federal.
- **P6** — `revisao-final-medica`.

## 11. Localizacao

JE da comarca do local da divulgacao (CPP 70). ANPD competente em todo territorio nacional.

## 12. Integracao

**Chamada por:** `medico-master`, `triagem-medica`, `timeline-multiesfera`, `compliance-publicidade-medica`, `lgpd-saude`.

**Entrega para:** defesa criminal + PED + civel coordenada -> `revisao-final-medica` -> operador.

**Sem esta skill:** defesa fragmentada — perda da articulacao tripartite (penal x etico x civel x ANPD); risco de sancao acumulada.
