---
name: credenciamento-plano-saude
description: >
  Contratos e contencioso de credenciamento de clinica/hospital/medico com operadoras de planos de saude. Aplica Lei 9.656/1998 art. 17 (dever de cobertura assistencial em rede credenciada + dever de informacao do descredenciamento ao beneficiario) + RN ANS 365/2014 (regras de credenciamento + descredenciamento substitutivo) + Lei 9.961/2000 art. 32 (ressarcimento ao SUS — operadora deve reembolsar SUS quando beneficiario usa rede publica) + ADI 1.931. Aborda glosa de procedimento (Lei 9.656 + RN 305/2012), descredenciamento unilateral (substitutivo x sem substituicao — beneficiario protegido), revisao de tabela praticada, contrato de credenciamento por hospital x medico individual. Sinaliza ressarcimento ao SUS como obrigacao tributaria-administrativa da operadora. Aciona: credenciamento ANS, descredenciamento hospital, glosa procedimento, RN 365, Lei 9.961 ressarcimento SUS, tabela TUSS, contrato credenciamento, revisao tabela operadora, ADI 1.931.
---

# CREDENCIAMENTO COM PLANO DE SAUDE

> Skill **Tier 6** — consultivo e contencioso para credenciamento e descredenciamento. Implementa PA-04, PA-13, PA-15 (CDC 14 reflexo), PA-20. Acionada por `medico-master`, `triagem-medica` (modo consultivo), `constituicao-sociedade-medica`, `acao-rescisao-coletivo` (descredenciamento ja realizado).

---

## 0. Escopo e acionamento

Consultivo e contencioso para (a) **credenciamento** de clinica/hospital/medico com operadora; (b) **descredenciamento unilateral** pela operadora; (c) **glosa de procedimentos** (recusa de pagamento pos-atendimento); (d) **revisao de tabela TUSS** praticada (defasada vs custo real); (e) **ressarcimento ao SUS** (Lei 9.961/2000 art. 32 — obrigacao da operadora). Pre-requisito: Selo P1 + contrato de credenciamento + historico de glosas/tabelas.

## 1. Posicao na orquestra

- **Chamada por:** `medico-master`, `triagem-medica`, `constituicao-sociedade-medica`, `acao-rescisao-coletivo`.
- **Aciona:** `validador-legislacao-vigente`, `revisao-final-medica`, `contrato-prestacao-medica` (clausulas internas).
- **Entrega para:** minuta de contrato + parecer + eventual peticao contenciosa.

## 2. Marco normativo

| Norma | Conteudo |
|-------|----------|
| **Lei 9.656/1998 art. 17** | Cobertura assistencial via rede credenciada + dever de informar descredenciamento |
| Lei 9.961/2000 | Cria ANS |
| **Lei 9.961/2000 art. 32 + ADI 1.931** | **Ressarcimento ao SUS** — operadora reembolsa SUS quando beneficiario usa rede publica |
| **RN ANS 365/2014** | Credenciamento + descredenciamento (substitutivo) `[VERIFICAR atual]` |
| RN ANS 305/2012 | Glosa — regulamento `[VERIFICAR]` |
| RN ANS 412/2016 | Portabilidade especial |
| RN ANS 195/2009 + 309/2012 | Reajuste coletivo |
| RN ANS 471/2021 | TUSS — tabela unificada |
| CC art. 421 + 422 | Funcao social + boa-fe |
| CDC art. 14 + 39 + 51 IV/X | Objetiva + abusivas |
| Sum. 469 / 608 STJ | CDC |
| CPC 300 / 537 | Tutela |
| Lei 8.078/90 art. 7o paragrafo unico (relacao acessoria) | Aplicacao reflexa |

**Jurisprudencia:**
- **STJ REsp 1.826.505/SP** — credenciado pode contestar descredenciamento abusivo
- STJ AgInt REsp 1.876.543 (descredenciamento substitutivo + comunicacao previa)
- STF ADI 1.931 — constitucionalidade do ressarcimento SUS (Lei 9.961 art. 32)
- TJSP/TJRJ — glosa abusiva quando ausente justificativa tecnica documentada

## 3. Cenarios (matriz)

| Cenario | Frente | Tese |
|---------|--------|------|
| **Negativa de credenciamento** | Consultivo + contencioso | Geralmente nao ha direito subjetivo a credenciar; operadora tem autonomia (limitada por abusividade e discriminacao) |
| **Descredenciamento substitutivo** | Lei 9.656 + RN 365 | Operadora deve oferecer substituto na mesma regiao com cobertura equivalente |
| **Descredenciamento sem substituicao** | Lei 9.656 + Sum. 608 | Vedado — beneficiario afetado pode acionar (vide `acao-rescisao-coletivo`) |
| **Glosa de procedimento** | RN 305 + Lei 9.656 | Glosa exige fundamentacao tecnica; sem ela, cobranca devida |
| **Tabela TUSS defasada** | Lei 9.656 + RN 471 | Renegociacao com base em custo + razoabilidade |
| **Ressarcimento ao SUS** | Lei 9.961 art. 32 + ADI 1.931 | Operadora reembolsa SUS — defesa em execucao fiscal eventual |
| **Cobranca direta do beneficiario apos atendimento** | CDC 39 V | Vedada se procedimento coberto — restituicao em dobro |

## 4. Descredenciamento — analise (Lei 9.656 + RN 365)

**Substitutivo** (admitido):
- Operadora descredencia + **comunica beneficiarios em 30 dias** (RN 365)
- Apresenta **rede alternativa equivalente** na mesma regiao
- Beneficiarios tem direito a continuidade de tratamento em curso (Tema 1.082 STJ)

**Sem substituicao** (vedado):
- Falta substituto equivalente na regiao
- Beneficiarios tem direito a manutencao da rede ou portabilidade especial (RN 412)
- Acoes do Tier 5 — `acao-rescisao-coletivo`

## 5. Glosa — analise (RN 305 + Lei 9.656)

**Requisitos para glosa legitima:**
1. **Justificativa tecnica documentada** — porque a operadora considera o procedimento nao coberto/excessivo
2. **Comunicacao formal ao prestador** com prazo para recurso
3. **Cobertura conforme apolice + Lei 9.656** — coerencia com Rol e exclusoes
4. **Auditoria pos-pagamento limitada** — sem desvio de finalidade

**Defesa do prestador (clinica/hospital/medico) em glosa:**
- Comprovacao tecnica do procedimento (laudo + prontuario)
- Indicacao medica fundamentada
- Codigos TUSS corretos
- Cobertura no Rol ou criterios Lei 14.454

## 6. Ressarcimento ao SUS (Lei 9.961 art. 32)

**Quando ha:** beneficiario de plano usa rede SUS (urgencia em hospital publico, transplante SUS, etc.).

**Mecanismo:** ANS apura + cobra da operadora (via TRU — Tabela de Ressarcimento por Unidade).

**Defesa da operadora em execucao fiscal:**
- Comprovacao de que ja prestou cobertura
- Identificacao incorreta do beneficiario
- Inadimplencia da operadora ja sanada (atualizacao TRU)
- Prescricao 5a `[VERIFICAR jurisprudencia]`

## 7. Clausulas criticas — contrato de credenciamento

| Clausula | Conteudo |
|----------|----------|
| **Objeto + procedimentos cobertos** | Lista TUSS + exclusoes expressas |
| **Tabela praticada + reajuste** | Periodicidade + indice (custo medico medico — IPCA-Saude) |
| **Pagamento** | Prazo (15-45d), forma, juros de mora |
| **Glosa** | Procedimento + prazo para recurso + restituicao se improcedente |
| **Auditoria pos-pagamento** | Limites + boa-fe |
| **Exclusividade — vedada** | (sob pena de pejotizacao + abusividade) |
| **Padrao tecnico** | Sem ingerencia tecnica da operadora — autonomia clinica preservada |
| **Sigilo + LGPD** | Compartilhamento limitado a operacao do plano |
| **Rescisao** | Aviso 60d + substituicao (RN 365) |
| **Foro / Arbitragem** | JE comarca + arbitragem |

## 8. Esqueleto — Parecer de descredenciamento

```
PARECER — Descredenciamento por Operadora

I — CONSULTA — descricao do ato + impacto financeiro/operacional

II — ANALISE
  II.1 Modalidade: substitutivo ou sem substituicao
  II.2 Conformidade RN 365 — prazo + comunicacao + substituto
  II.3 Continuidade obrigatoria — Tema 1.082 STJ (beneficiarios em tratamento)
  II.4 Direito a indenizacao da clinica/hospital — rarissimo; geralmente
       contratual (multa por rescisao injustificada)
  II.5 Direito dos beneficiarios — manutencao ou portabilidade RN 412

III — ESTRATEGIA
  III.1 Caminho administrativo — ANS (Notificacao ou Termo de Compromisso)
  III.2 Caminho judicial — acao da clinica + acoes individuais beneficiarios
        (Tier 5 — `acao-rescisao-coletivo`)

IV — RESSALVA (PA-05).

[Cidade, data] — {{ADVOGADO_NOME}} | OAB/{{OAB_UF}} {{OAB_NUMERO}}
```

## 9. Casos tipicos

- **Hospital regional descredenciado:** Tema 1.082 + RN 365 — acao da clinica + acoes individuais.
- **Glosa massiva de cirurgia bariatrica:** auditoria pos-pagamento abusiva — recurso interno + judicial.
- **Tabela TUSS de honorario medico defasada 50% em 10a:** renegociacao + eventual revisional.
- **Recusa de credenciamento:** geralmente sem direito subjetivo, salvo discriminacao caracterizada.
- **Cobranca direta do paciente apos atendimento coberto:** CDC 39 V — restituicao em dobro.
- **Ressarcimento SUS em curso:** defesa em execucao + verificacao da TRU.

## 10. Vedacoes especificas

- **PA-03** — sem opinar conduta clinica (a tese e juridico-contratual).
- **PA-10 / PA-11** — RN ANS atualizadas `[VERIFICAR]`.
- **PA-13** — Lei 9.656 + Lei 9.961 + RN com identificacao precisa.
- **PA-20** — sem cross-sell tributario-fiscal (slot generico em execucao fiscal).

## 11. Protocolos acionados

- **P1** — Selo (RN ANS atual).
- **P3** — memoria de decisao (administrativo x judicial).
- **P5** — JE comarca + JF se ressarcimento SUS (CF 109 I).
- **P6** — `revisao-final-medica`.

## 12. Localizacao

JE comarca da clinica/hospital. Execucao fiscal de ressarcimento SUS na JF. ANS em Brasilia (administrativo).

## 13. Integracao

**Chamada por:** `medico-master`, `triagem-medica`, `constituicao-sociedade-medica`, `acao-rescisao-coletivo`.

**Entrega para:** parecer + minuta + eventual peticao -> `revisao-final-medica` -> operador.

**Sem esta skill:** contratos de credenciamento sem clausulas anti-glosa + ausencia de articulacao Lei 9.656/RN 365 + ressarcimento SUS ignorado — riscos financeiros para clinica/hospital.
