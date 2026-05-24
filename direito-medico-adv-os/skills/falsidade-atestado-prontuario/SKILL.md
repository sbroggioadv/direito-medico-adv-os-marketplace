---
name: falsidade-atestado-prontuario
description: >
  Defesa criminal em falsidade documental praticada por profissional de saude — atestado falso (CP art. 302 — crime proprio do medico/dentista) e falsidade ideologica (CP art. 299 — quando documento nao e atestado em sentido estrito ou e laudo/declaracao). Aplica CP art. 297 (falsidade documental publica — quando profissional atende a servico publico SUS), CP art. 304 (uso de documento falso), CP art. 171§3o (estelionato qualificado — atestado para enganar INSS/seguro/empregador). Articula reflexo civel (CC 935) e PED (CEM 2.217 art. 80-81). Teses: ausencia de dolo (equivoco tecnico, boa-fe), divergencia clinica entre profissionais, erro de diagnostico, atestado retroativo legitimo (Res. CFM 1.658/2002), pedido do paciente (justa causa indireta), revogacao/correcao tempestiva. Aciona: falsidade atestado, atestado medico falso, CP 302, CP 299, CP 297, falsidade prontuario, atestado retroativo, Res. CFM 1.658, estelionato medico, INSS atestado, declaracao de obito, laudo falso, divergencia clinica boa-fe.
---

# FALSIDADE DE ATESTADO/PRONTUARIO MEDICO

> Skill **Tier 3** — defesa criminal em falsidade documental medica/odontologica. Implementa PA-02, PA-03 (sem opinar conduta), PA-08, PA-12 (cruzamento), PA-13. Acionada por `medico-master`, `triagem-medica` (esfera criminal), `timeline-multiesfera`.

---

## 0. Escopo e acionamento

Defesa em (a) **atestado medico falso (CP art. 302)** — crime proprio do medico/dentista; (b) **falsidade ideologica (CP art. 299)** — laudo, declaracao, prontuario; (c) **falsidade documental publica (CP art. 297)** — profissional em servico publico (SUS, atestado para pericia INSS, declaracao de obito); (d) **estelionato qualificado (CP art. 171§3o)** — atestado para enganar terceiro (INSS, seguradora, empregador). Pre-requisito: Selo P1 + `analise-prontuario-medico`.

## 1. Posicao na orquestra

- **Chamada por:** `medico-master`, `triagem-medica`, `timeline-multiesfera`.
- **Aciona:** `analise-prontuario-medico` (consistencia documental), `defesa-ped-crm` (cruzamento P4 — CEM 80-81), `responsabilidade-civil-medica` (reflexo civel), `revisao-final-medica`.
- **Entrega para:** resposta a acusacao, HC trancamento, alegacoes finais.

## 2. Marco normativo

| Norma | Conteudo |
|-------|----------|
| **CP art. 302** | Falsidade de atestado medico — pena 1m-1a; pena dobra se ha vantagem patrimonial |
| **CP art. 299** | Falsidade ideologica (geral) — pena 1-5a (publico) ou 1-3a (particular) |
| **CP art. 297** | Falsidade documental publica — quando medico atua a servico publico |
| CP art. 304 | Uso de documento falso — quem usa (terceiro que apresenta o atestado) |
| **CP art. 171§3o** | Estelionato qualificado — atestado contra INSS, ente publico |
| CP art. 18 I | Dolo (atestado e crime doloso) — boa-fe afasta |
| CP art. 20-21 | Erro de tipo / erro de proibicao |
| **CEM 2.217/2018 art. 80** | Vedacao etica — atestar fato inexistente |
| CEM art. 81 | Vedacao — atestar sem exame ou com base em informacao oral exclusiva |
| **Res. CFM 1.658/2002** | Atestados medicos — fundamentacao + identificacao + retroatividade limitada |
| Res. CFM 1.821/2007 | Prontuario eletronico/papel + assinatura |
| Res. CFM 2.218/2018 | Declaracao de obito (DO) |
| Codigo Etica Odontologica CFO 118/2012 | Vedacao etica analoga |
| **CPP 158-159 / 396-A / 397 / 386** | Pericia, resposta, absolvicao sumaria |
| Lei 9.099/95 76 / 89 | Transacao penal / sursis — cabiveis em CP 302 e 299 |

**Jurisprudencia:** STJ HC 421.601 (atestado de boa-fe nao configura crime — exige dolo); STJ AgRg AREsp 1.554.789 (divergencia clinica entre profissionais nao configura falsidade); STF HC 142.348 (atestado retroativo licito quando fundamentado).

## 3. Estrutura tipica do delito e linha de defesa

| Crime | Conduta tipica | Defesa nuclear |
|-------|---------------|----------------|
| **CP 302** | Atesta fato falso para ele proprio | Boa-fe; equivoco tecnico; divergencia clinica; atestado retroativo legitimo (Res. CFM 1.658) |
| CP 302 §unico | Vantagem patrimonial (pena dobra) | Ausencia de vantagem (laudo emitido sem cobranca) ou ausencia de relacao direta |
| **CP 299** | Insere/omite declaracao falsa em doc particular | Erro tecnico; divergencia clinica; ausencia de dolo |
| CP 297 | Idem em doc publico (atestado SUS, DO, pericia INSS) | Idem + pena pode ser severa — defesa cuidadosa |
| **CP 171§3o** | Atestado usado para fraudar INSS/seguradora | Ausencia de conluio com beneficiario; o medico nao sabia do uso; ausencia de dolo |

**Importante:** o **uso** do documento falso (CP 304) **e crime do terceiro** (paciente que entrega atestado a empregador) — defesa do medico recusa imputacao por uso.

## 4. Teses defensivas (cardapio)

| Tese | Fundamento | Acionar |
|------|-----------|---------|
| **Ausencia de dolo (CP 302/299 sao dolosos)** | CP 18 I | Erro tecnico; equivoco diagnostico; divergencia clinica; pressao do paciente |
| **Divergencia clinica de boa-fe** | STJ AgRg AREsp 1.554.789 + literatura | Outro medico diagnosticou diferente — divergencia nao e falsidade |
| **Erro de tipo** | CP 20 | Acreditou que o quadro existia (interpretacao do paciente convincente) |
| **Atestado retroativo legitimo** | Res. CFM 1.658/2002 art. 3o | Fundamentado em documentos (receita, prontuario, exame) + identificavel + plausivel |
| **Atestado por solicitacao do paciente sem dolo** | CP 302 caput | Sem conluio para fraude; medico examinou; eventualmente extrapolou prazo — culpa, nao dolo |
| **Falta de consciencia do uso fraudulento** | CP 171§3o exige dolo no engano | Medico emitiu legitimamente; uso fraudulento foi posterior e desconhecido |
| **Ausencia de vantagem patrimonial** | CP 302 §unico | Pena dobra so com vantagem direta — afastar majorante |
| **Inepcia da denuncia** | CPP 41 + STF HC 89.395 | Denuncia generica sem fato falso especifico |
| **Atipicidade — declaracao opinativa** | CP 299 nao alcanca juizos de valor | Atestado tipo "apresenta sintomas compativeis" — opinativo, nao afirmativo |
| **Revogacao tempestiva** | Doutrina | Medico corrigiu o documento antes do uso |
| **Prescricao** | CP 109-110 | Pena prevista x marcos |

## 5. Atestado retroativo — Res. CFM 1.658/2002 (zona cinzenta)

| Cabivel | Vedado |
|---------|--------|
| Fundamentado em documentacao previa (prontuario; receita; exame da epoca) | Sem nenhum suporte documental |
| Identificavel (CRM + data + assinatura + cabecalho) | Generico, manuscrito sem identificacao |
| Plausivel (paciente apresentou-se na epoca) | Inverossimil (paciente em viagem; impossibilidade fisica) |
| Razoavel prazo de retroatividade `[VERIFICAR limite especifico CRM-UF]` | Retroatividade extensa sem justificacao |

Defesa: o atestado retroativo **nao e per se falso** — Res. CFM 1.658 admite. Falsidade exige discrepancia com a realidade.

## 6. Esqueleto FIRAC — Resposta a acusacao

```
RESPOSTA A ACUSACAO — CPP 396-A
EXMO. SR. JUIZ DA ___ VARA CRIMINAL DE [Cidade/UF]

[ACUSADO], CRM/CRO [num/UF], por {{ADVOGADO_NOME}} OAB/{{OAB_UF}} {{OAB_NUMERO}}

I — FATOS [F] — datada (referencia CASO.md)
II — ISSUE [I] — houve falsidade ou divergencia clinica? Houve dolo?
III — DIREITO [R]
  III.1 Tipicidade — CP 302/299/297 exige (a) inveracidade objetiva; (b) dolo
        (PA-13)
  III.2 [Boa-fe / divergencia clinica / erro tecnico / atestado retroativo
        licito Res. CFM 1.658/2002]
  III.3 Cruzamento P4 — PED CEM 80-81 paralelo; eventual reflexo civel
  III.4 Ausencia de vantagem patrimonial (afastar majorante CP 302 §unico)
IV — PEDIDOS [C]
  IV.1 Absolvicao sumaria (CPP 397 III)
  IV.2 Subsidiariamente: sursis (Lei 9.099 89) — pena minima ate 1a cabe
  IV.3 Subsidiariamente: transacao (art. 76) — pena max ate 2a cabe
  IV.4 Diligencias: pericia documental + oitiva de pacientes
  IV.5 Testemunhas (max 8)

[Cidade, data] — {{ADVOGADO_NOME}} | OAB/{{OAB_UF}} {{OAB_NUMERO}}

RESSALVA (PA-05).
```

## 7. Casos tipicos

- **Atestado retroativo questionado:** Defesa: Res. CFM 1.658 + documentacao previa (receita, prontuario). Demonstrar plausibilidade.
- **Atestado para INSS e fraude descoberta:** Defesa: medico emitiu legitimamente; nao sabia do uso fraudulento; ausencia de conluio (sem mensagens; sem pagamento extra). CP 171§3o exige dolo do medico no engano.
- **Declaracao de obito (DO) com causa equivocada:** Defesa: divergencia tecnica boa-fe; informacao limitada no momento (Res. CFM 2.218); correcao via retificacao (NUS).
- **Prontuario alterado pos-evento adverso:** **Caso grave** — adulteracao retroativa para encobrir erro. Defesa: prevalecimento da versao original (analise pericial); ausencia de adulteracao com dolo de falsidade — tese dificil; foco em PED com sancao etica em vez de criminal.
- **Atestado de comparecimento simples:** geralmente atipico (CP 299 exige falsidade material/ideologica relevante); afirmacao de presenca sem juizo clinico.

## 8. Cruzamento P4 (PA-12)

| Esfera | Reflexo |
|--------|---------|
| Penal (CP 302/299/297/171§3o) | Defesa nuclear |
| PED CEM 80-81 | `defesa-ped-crm` ou `defesa-ped-cro` (CFO 118) — sancao etica |
| Civel | Dano a terceiro prejudicado pelo atestado (empregador, seguradora) — CC 186 |
| Administrativo INSS | Comunicacao para pericia federal; possivel processo de revisao |

CP 386 I/III alcanca civel/PED (PA-12). Absolvicao por V/VII nao alcanca.

## 9. Vedacoes especificas

- **PA-02** — sem promessa.
- **PA-03** — nao opinar se a conduta clinica do medico foi correta — usar protocolo e literatura.
- **PA-08** — sem critica pessoal a perito.
- **PA-13** — CP/Res. CFM/Res. CFO com identificacao precisa.
- **PA-19** — prescricao conferida.

## 10. Protocolos acionados

- **P1** — Selo.
- **P2** — `analise-prontuario-medico` (consistencia do documento questionado).
- **P3** — memoria de decisao.
- **P4** — `timeline-multiesfera`.
- **P6** — `revisao-final-medica`.

## 11. Localizacao

JE comarca do local da emissao do atestado (CPP 70). DO emitida em servico federal (Hospital federal, IML) -> JF. Estelionato contra INSS (CP 171§3o) -> JF (CF 109 IV).

## 12. Integracao

**Chamada por:** `medico-master`, `triagem-medica`, `timeline-multiesfera`.

**Entrega para:** defesa criminal coordenada com PED + civel -> `revisao-final-medica` -> operador.

**Sem esta skill:** defesa generica que confunde tipos penais (CP 302 x 299 x 297 x 171§3o), nao explora atestado retroativo licito (Res. CFM 1.658), e perde a articulacao boa-fe x dolo.
