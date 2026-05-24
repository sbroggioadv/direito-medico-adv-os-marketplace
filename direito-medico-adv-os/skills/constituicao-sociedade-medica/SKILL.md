---
name: constituicao-sociedade-medica
description: >
  Consultivo para constituicao de sociedade medica/odontologica — tipo societario (LTDA pluripessoal, sociedade simples, LTDA unipessoal), contrato social, clausulas criticas (administracao, exclusao, sucessao, nao-concorrencia), registro no CRM/CRO (Res. CFM 1.493/1998 + Res. CFO 63/2005), CNPJ + alvara + vigilancia sanitaria. Aplica Lei 12.842/2013 (Ato Medico — vedacao de terceirizacao) + Lei 13.874/2019 (LTDA pluripessoal) + CC arts. 982-1.087 + Lei 5.764/71 (cooperativa). Distingue sociedade simples x empresaria (CC 982-983). Slot generico para tributacao (PA-20). Sucessao e clausulas anti-conflito sao nucleos. Aciona: constituicao clinica medica, sociedade medica, contrato social clinica, LTDA medica, Res. CFM 1.493, Lei 12.842, sociedade uniprofissional, registro CRM clinica, alvara sanitario, CNAE medico.
---

# CONSTITUICAO DE SOCIEDADE MEDICA/ODONTOLOGICA

> Skill **Tier 6** — consultivo empresarial para constituicao de clinica/sociedade na area saude. Implementa PA-04, PA-13, PA-20 (sem cross-sell com tributario-societario/auditoria-contabil), PA-21. Acionada por `medico-master`, `triagem-medica` (modo consultivo).

---

## 0. Escopo e acionamento

Consultivo de constituicao para clinica medica, odontologica, multidisciplinar (CFM+CFO+COFEN+COFFITO), hospital privado e centros especializados. Inclui: escolha do tipo societario, contrato social, registro no Conselho profissional, CNPJ + alvara, vigilancia sanitaria municipal, contratos com plantonistas/socios/empresas terceiras. Pre-requisito: Selo P1 + brief do cliente (numero de socios, atividades, local, projecao de faturamento, sucessao).

## 1. Posicao na orquestra

- **Chamada por:** `medico-master`, `triagem-medica` (modo consultivo).
- **Aciona:** `contrato-prestacao-medica` (contratos de socios/plantonistas), `lgpd-saude` (clinica como controladora), `compliance-publicidade-medica`, `validador-legislacao-vigente`, `revisao-final-medica`.
- **Entrega para:** parecer + contrato social minuta + checklist de regularizacao + checklist de obrigacoes.

## 2. Marco normativo

| Norma | Conteudo |
|-------|----------|
| **Lei 12.842/2013 (Ato Medico)** | Define ato medico privativo — vedacao a terceirizacao do diagnostico/conduta |
| Lei 5.081/66 | Exercicio odontologico (CFO) |
| **Lei 13.874/2019 (Liberdade Economica)** | LTDA pluripessoal possivel; sociedade unipessoal LTDA |
| **CC arts. 982-1.087** | Sociedades — simples x empresaria; LTDA; clausulas |
| CC art. 1.052 (LTDA) | Limitada — limite da responsabilidade |
| CC art. 966 | Empresario individual |
| **Res. CFM 1.493/1998** | Registro de sociedade medica no CRM — vedacoes |
| **Res. CFO 63/2005** | Registro de clinica odontologica no CRO — vedacoes |
| Res. CFM 1.821/2007 + 1.605/2000 | Prontuario + sigilo (clinica e controladora) |
| Lei 5.764/71 | Cooperativa medica (Unimed e correlatas) |
| LC 123/2006 + Lei 14.789/2023 | Simples Nacional (anexos III e V `[VERIFICAR]`) |
| Lei 6.404/76 | S.A. (em hospitais de grande porte) |
| Lei 13.097/2015 art. 36+ | Cisao/incorporacao de hospitais — capital estrangeiro |
| CDC art. 14 + 39 + 51 | Clinica e prestadora — objetiva |

**Jurisprudencia:**
- STJ REsp 1.832.105 (LTDA medica e sociedade simples — natureza)
- STF RE 595.838 (cobertura SUS e cooperativas) `[VERIFICAR]`
- STJ AgInt REsp 1.768.456 (registro no CRM como condicao de exercicio)

## 3. Escolha de tipo societario (matriz)

| Tipo | Quando recomendar | Vantagens | Riscos |
|------|-------------------|-----------|--------|
| **LTDA pluripessoal** | 2+ socios; medio porte | Limite de responsabilidade; flexibilidade contratual | Exige contrato detalhado |
| **LTDA unipessoal (CC 1.052§§)** | Profissional unico | Limite + simplicidade | Sem partilha; CC 50 (desconsideracao) |
| **Sociedade simples (CC 997-1.038)** | Profissionais socios + atividade nao-empresaria | Tributacao IRPF profissional | Responsabilidade ilimitada subsidiaria |
| **Cooperativa (Lei 5.764)** | Coletivo de profissionais (Unimed, Uniodonto) | Modelo de coop; isencoes especificas | Complexidade de gestao |
| **S.A.** | Hospital de grande porte; investimentos externos | Captacao; profissionalizacao | Custo + governanca |
| **EIRELI** | **Extinta (Lei 14.382/22)** | N/A | Migracao para LTDA unipessoal |

**Lei 12.842/2013** veda **terceirizacao do ato medico** — clinica nao pode "terceirizar" o diagnostico/conduta a fornecedor; medico assistente e PF.

## 4. Sociedade simples x empresaria (PA-13)

**CC art. 982-983:**
- **Simples** — atividade intelectual, cientifica, literaria, artistica (regra para medico/dentista quando atua **pessoalmente**)
- **Empresaria** — atividade economica organizada para producao/circulacao de bens/servicos (clinica com estrutura significativa de funcionarios + equipamentos + sistema; hospital)

**STJ REsp 1.832.105** — clinica medica/odontologica tradicional e tendencialmente **simples**, mesmo registrada como LTDA. Hospital e empresaria.

**Importancia tributaria:** afeta enquadramento Simples (anexo III x V) — PA-20 (sem opinar tributacao especifica — slot generico "consultar especialista em tributacao da clinica").

## 5. Clausulas criticas do contrato social

| Clausula | Conteudo |
|----------|----------|
| **Objeto social** | Especificidade — atividades CNAE compativeis (8610, 8630, 8650 etc. — `[VERIFICAR codigos vigentes]`) — sem extrapolar Lei 12.842 |
| **Quotas + integralizacao** | Distribuicao por socio; integralizacao em dinheiro x bens (laudo) |
| **Administracao** | Socio-administrador (registrado no CRM/CRO + responsavel tecnico — Res. CFM 1.493) |
| **Exclusao de socio** | CC 1.085 — falta grave + assembleia + ampla defesa |
| **Direito de retirada** | CC 1.029 — prazo + apuracao de haveres |
| **Apuracao de haveres** | Metodologia — patrimonio liquido x valuation (medio termo: balanco + valor real) |
| **Sucessao em caso de morte/invalidez** | Herdeiros nao-medicos — Res. CFM 1.493 veda — apuracao em dinheiro |
| **Nao-concorrencia** | Limite tempo (2-5a) + geografico (raio) + atividade — STJ admite com razoabilidade |
| **Sigilo + LGPD** | Clinica e controladora — todos socios respondem |
| **Distribuicao de lucros** | Pro-labore + dividendos (PA-20 — slot generico) |
| **Resolucao de conflitos** | Arbitragem ou foro |

## 6. Registro e regularizacao (checklist)

| Etapa | Onde | Conteudo |
|-------|------|----------|
| 1 | Junta Comercial / Cartorio RPJ | Registro do contrato social |
| 2 | CNPJ Receita Federal | Inscricao |
| 3 | **CRM/CRO da UF** | **Registro da sociedade** (Res. CFM 1.493 / Res. CFO 63) — responsavel tecnico inscrito |
| 4 | Inscricao estadual (se aplicavel) | Estadual |
| 5 | Inscricao municipal + alvara | Municipal |
| 6 | **Vigilancia Sanitaria municipal/estadual** | Lei 6.437/77 + RDC ANVISA aplicaveis — laudo + protocolo |
| 7 | Bombeiros (AVCB) | Estadual |
| 8 | CNES Ministerio da Saude | Cadastro nacional de estabelecimentos |
| 9 | RPP-Saude (se atender SUS) | Convenio |
| 10 | LGPD (RIPD se grande) | ANPD `[VERIFICAR]` |

## 7. Esqueleto — Parecer de constituicao

```
PARECER — Constituicao de Sociedade Medica
EMITENTE: {{ADVOGADO_NOME}} | OAB/{{OAB_UF}} {{OAB_NUMERO}}

I — CONSULTA — descricao da intencao (socios, atividades, local)

II — ANALISE
  II.1 Tipo societario recomendado: [LTDA pluripessoal/simples/etc.]
  II.2 Enquadramento (CC 982-983) — simples ou empresaria
  II.3 Registro CRM/CRO — Res. CFM 1.493 / Res. CFO 63 + responsavel tecnico
  II.4 Clausulas criticas — [administracao, exclusao, sucessao, nao-concorrencia]
  II.5 Restricoes Lei 12.842 — vedacao a terceirizacao do ato medico
  II.6 Tributacao — [SLOT GENERICO — PA-20]
        "A escolha tributaria (Simples anexo III/V, Lucro Presumido, Lucro Real)
        deve ser feita com especialista contabil-tributario."

III — CHECKLIST DE REGULARIZACAO
  [Lista 10 etapas — Junta -> CNPJ -> CRM -> ... -> CNES]

IV — CRONOGRAMA — [estimativa de prazos]

V — RISCOS — [responsabilidade objetiva CDC 14; sigilo LGPD; sucessao;
   responsabilidade pessoal do socio-administrador medico]

VI — RESSALVA (PA-05) — minuta sujeita a revisao do operador OAB ativo.

[Cidade, data]
```

## 8. Casos tipicos

- **2 medicos + clinica de medio porte:** LTDA pluripessoal simples; clausula sucessao essencial.
- **Hospital com 50+ medicos + estrutura significativa:** S.A. ou LTDA empresaria.
- **Dentista solo + 2 secretarias:** LTDA unipessoal simples; vedacao Res. CFO 63 ao "agenciador" de pacientes.
- **3 medicos + cooperativa para credenciamento ANS:** Lei 5.764 + Res. CFM 1.493.
- **Clinica multidisciplinar (medicos + dentistas + fisio):** registros multiplos (CRM + CRO + CREFITO).
- **Sucessao planejada (medico aposentando — herdeiros nao-medicos):** Res. CFM 1.493 + apuracao de haveres.

## 9. Vedacoes especificas

- **PA-03** — sem opinar conduta clinica/medica.
- **PA-13** — Lei 12.842 + Res. CFM 1.493 + CC com identificacao precisa.
- **PA-20** — **sem cross-sell** tributario/contabil/sucessorio especifico — usar slot generico.

## 10. Protocolos acionados

- **P1** — Selo (Lei 12.842 + Res. CFM/CFO vigentes).
- **P3** — memoria de decisao (escolha societaria).
- **P5** — registro estadual (Junta) + municipal (alvara) + federal (CNPJ + CRM/CFO).
- **P6** — `revisao-final-medica`.

## 11. Localizacao

Junta Comercial / Cartorio RPJ na UF de sede. CRM/CRO na UF de inscricao do responsavel tecnico. Alvara + vigilancia sanitaria municipal. Capital estrangeiro em hospitais Lei 13.097/2015 — `[VERIFICAR exigencias atualizadas]`.

## 12. Integracao

**Chamada por:** `medico-master`, `triagem-medica` (modo consultivo).

**Entrega para:** parecer + contrato social minuta + checklist -> `revisao-final-medica` -> operador. Cruza com `contrato-prestacao-medica` (socios + plantonistas), `lgpd-saude` (clinica e controladora), `compliance-publicidade-medica`.

**Sem esta skill:** constituicao generica que ignora Res. CFM 1.493/Res. CFO 63 (registro no Conselho), Lei 12.842 (vedacao terceirizacao do ato medico) e clausulas criticas de sucessao — risco de irregularidade + conflito societario.
