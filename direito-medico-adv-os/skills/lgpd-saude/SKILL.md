---
name: lgpd-saude
description: >
  Consultivo LGPD aplicado a clinica/hospital/medico — dados de saude sao SENSIVEIS (LGPD art. 5o II + art. 11). Articula bases legais admissiveis (art. 11§2o — consentimento; tutela da saude; cumprimento de obrigacao legal; protecao da vida; exercicio regular do direito; pesquisa) com regulamentacao especifica (Res. CFM 1.821/2007 — prontuario; certificacao SBIS-CFM nivel 2 para PEP). Estrutura programa de privacidade: RIPD, encarregado (DPO), politica de privacidade, contratos com operadores, controle de acesso, retencao (20 anos prontuario CFM 1.821) vs minimizacao (LGPD art. 6o III), incidentes (ANPD), direitos do titular (art. 18). Cruzamento com sigilo medico tripartite (`violacao-sigilo-medico`). Aciona: LGPD saude, dados sensiveis, art 11 LGPD, prontuario eletronico, SBIS-CFM, encarregado DPO clinica, RIPD, politica privacidade clinica, incidente ANPD, base legal tutela da saude, vazamento prontuario.
---

# LGPD APLICADA A CLINICA / HOSPITAL / MEDICO

> Skill **Tier 6** — consultivo LGPD em saude — clinica/hospital como controlador, medico como operador. Implementa PA-04, PA-13, PA-16 (sigilo do plugin), PA-17 (so o necessario), PA-20 (sem cross-sell tecnologia). Acionada por `medico-master`, `triagem-medica` (modo consultivo), `constituicao-sociedade-medica`, `violacao-sigilo-medico` (reflexo civel/administrativo).

---

## 0. Escopo e acionamento

Implantacao + manutencao de programa de adequacao LGPD em estabelecimento de saude. Cobre: bases legais para tratar dados sensiveis (art. 11), prontuario eletronico (PEP + SBIS-CFM), retencao 20 anos vs minimizacao, encarregado (DPO), RIPD obrigatorio em alguns casos, politica de privacidade, contratos com operadores (laboratorios, sistemas, sw), gestao de incidente e comunicacao a ANPD + titular. Pre-requisito: Selo P1 + brief do estabelecimento (porte, atividades, fluxo de dados).

## 1. Posicao na orquestra

- **Chamada por:** `medico-master`, `triagem-medica`, `constituicao-sociedade-medica` (clinica e controladora), `violacao-sigilo-medico` (reflexo).
- **Aciona:** `validador-legislacao-vigente`, `revisao-final-medica`, `compliance-publicidade-medica` (uso de imagem em redes).
- **Entrega para:** programa de privacidade + RIPD + minutas (politica, contratos, termo de consentimento) + cronograma de adequacao.

## 2. Marco normativo

| Norma | Conteudo |
|-------|----------|
| **LGPD Lei 13.709/2018** | Lei Geral de Protecao de Dados |
| **LGPD art. 5o II** | **Dados sensiveis** — saude e raca, religiao, opiniao politica, biometria, etc. |
| **LGPD art. 11** | Tratamento de dados sensiveis — bases legais restritas |
| LGPD art. 11§2o "a" | Consentimento especifico e destacado |
| LGPD art. 11§2o "b" | Cumprimento de obrigacao legal |
| LGPD art. 11§2o "c" | Politicas publicas |
| **LGPD art. 11§2o "d/e/f"** | **Tutela da saude exclusivamente por profissionais/servicos/autoridades de saude** |
| LGPD art. 11§2o "g" | Garantia da prevencao a fraude |
| LGPD art. 6o I-X | Principios — finalidade, adequacao, necessidade, minimizacao, transparencia, seguranca |
| LGPD art. 18 | Direitos do titular (9) — confirmacao, acesso, correcao, anonimizacao, eliminacao, portabilidade, info, oposicao |
| LGPD art. 41 | Encarregado (DPO) — obrigatorio em controlador (existem nuances) |
| LGPD art. 42-45 | Responsabilidade civil + reparacao |
| LGPD art. 48 | Comunicacao de incidente a ANPD + titular |
| LGPD art. 52 | **Sancoes administrativas** ANPD — multa ate 2% faturamento ou R$ 50M por infracao |
| **Res. CFM 1.821/2007** | Prontuario eletronico/papel — guarda 20 anos minimo |
| Res. CFM 2.218/2018 | Declaracao de obito |
| **SBIS-CFM (CMD nivel 2)** | Certificacao do PEP |
| CP art. 154 + 153 | Violacao de segredo profissional |
| ANPD Resolucoes / Guias | Atualizacao ANPD `[VERIFICAR]` |

**Jurisprudencia:**
- STJ AgRg AREsp 1.122.345 (vazamento prontuario — objetiva CDC 14 + LGPD 42)
- STF RE 1.236.834 (dado de saude e sensivel — protecao reforcada)
- TJSP/TJRJ recorrente — danos morais em vazamento

## 3. Estrutura do programa LGPD-saude

| Pilar | Conteudo |
|-------|----------|
| **1. Mapeamento de dados** | Inventario — quais dados, onde, quem trata, finalidade, base legal |
| **2. Bases legais** | Para cada tratamento — `tutela da saude` (art. 11§2o d) e base nuclear; consentimento como complementar |
| **3. Politica de privacidade publica** | Comunicacao ao titular |
| **4. Termos de consentimento + TCLE** | Quando necessario alem de "tutela da saude" |
| **5. Contratos com operadores** | Laboratorios, sw, terceiros — clausulas LGPD |
| **6. Controle de acesso (need-to-know)** | Logs de acesso PEP — SBIS-CFM nivel 2 |
| **7. Retencao + minimizacao** | 20a CFM 1.821 vs minimizacao LGPD — manter prontuario integral, descartar coleta excessiva |
| **8. Encarregado (DPO)** | Designado + publicado |
| **9. RIPD (Relatorio de Impacto)** | Obrigatorio em tratamento de alto risco (PEP de grande porte; integracoes com IA) |
| **10. Plano de resposta a incidente** | Procedimento + comunicacao ANPD + titular em 24-72h `[VERIFICAR]` |

## 4. Bases legais — escolha (art. 11§2o)

| Base | Quando |
|------|--------|
| **Tutela da saude** (d/e/f) | **Regra para tratamento clinico** — exercicio profissional + servico de saude |
| Consentimento especifico (a) | Casos excedentes (publicidade, pesquisa, marketing) |
| Obrigacao legal (b) | Notificacao compulsoria + comunicacoes obrigatorias |
| Politica publica (c) | SUS, programas governamentais |
| Protecao da vida (h) | Emergencia |
| Pesquisa (g) | Anonimizacao + comites de etica |

**Estrategia:** **base "tutela da saude" cobre o nucleo** — atendimento, prontuario, comunicacao entre profissionais. Consentimento e para usos **alem** disso (marketing, pesquisa, redes sociais).

## 5. Prontuario eletronico (PEP) + SBIS-CFM

| Item | Conteudo |
|------|----------|
| **Certificacao SBIS-CFM nivel 2** | Padrao recomendado — controle de acesso, log, integridade |
| **Retencao minima 20a (CFM 1.821)** | Mantida — LGPD art. 11§2o "d" permite |
| **Acesso multinivel** | Medico assistente (full); enfermagem (parcial); administrativo (so nao-clinico) |
| **Log de acesso** | Quem acessou, quando, o que viu — auditavel |
| **Backup + criptografia** | LGPD art. 46 — seguranca |
| **Compartilhamento entre profissionais** | Permitido — CEM 72§2o (medico) e analogos |
| **Compartilhamento com operadora** | Limitado ao operacionalizado (autorizacao prevista) |

## 6. Direitos do titular (art. 18) + procedimento

| Direito | Procedimento clinica |
|---------|---------------------|
| Confirmacao da existencia | Resposta em 15 dias |
| Acesso ao prontuario | Copia em ate 15d (Res. CFM 1.821) |
| Correcao | Anotacao adendo (sem apagar) |
| Anonimizacao | Em pesquisa |
| Eliminacao | **Limitado** — 20a obrigatoria — exceto dados nao-clinicos |
| Portabilidade | Compartilhamento estruturado com novo medico/clinica |
| Informacao | Sobre operadores |
| Oposicao | Cessar tratamento |
| Revogacao do consentimento | Para tratamentos baseados em consentimento |

## 7. Gestao de incidente (vazamento)

| Etapa | Prazo |
|-------|-------|
| Contencao tecnica | Imediata |
| Avaliacao de risco | 24-48h |
| **Comunicacao a ANPD** | Razoavel (Lei + Resolucao ANPD `[VERIFICAR prazo atual]`) |
| **Comunicacao ao titular afetado** | Se risco relevante |
| Documentacao | Registro do incidente |
| Plano de mitigacao | Apos contencao |

**Multa ANPD (art. 52):** ate 2% do faturamento ou R$ 50M por infracao. Atenuante: programa LGPD documentado.

## 8. Esqueleto — Programa LGPD para clinica

```
PROGRAMA LGPD — CLINICA [Nome]

I — DIAGNOSTICO
  - Mapeamento de dados (inventario)
  - Avaliacao de bases legais por tratamento
  - Avaliacao de riscos

II — DOCUMENTOS-CHAVE
  1. Politica de Privacidade publica (site + recepcao)
  2. Termo de consentimento especifico (alem da "tutela da saude")
  3. TCLE integrado a base LGPD
  4. Contratos com operadores (laboratorios, sw, lab. terceiros)
  5. Politica interna de controle de acesso ao PEP
  6. Plano de resposta a incidente
  7. RIPD (se aplicavel)

III — DPO (Encarregado)
  - Designacao + publicacao

IV — TREINAMENTO
  - Funcionarios + medicos + enfermagem + administrativo
  - Periodicidade anual

V — AUDITORIA + REVISAO
  - Anual + apos incidentes

RESSALVA (PA-05).
```

## 9. Casos tipicos

- **Clinica pequena (2 medicos + 1 secretaria):** programa minimo — politica + termo + treinamento + controle de acesso ao PEP + plano de incidente.
- **Hospital de grande porte:** programa robusto — DPO dedicado + RIPD + comites + auditorias.
- **Vazamento por funcionario:** investigacao interna + comunicacao ANPD + titular + dano moral civel (`violacao-sigilo-medico` reflexo).
- **Pesquisa cientifica em clinica:** consentimento + anonimizacao + Comite de Etica (Res. CNS 466/2012).
- **Marketing com fotos de pacientes:** consentimento especifico — alem da "tutela da saude" (`compliance-publicidade-medica`).
- **Integracao com IA medica:** RIPD obrigatorio + transparencia + Res. CFM 2.347/2023 (IA medica `[VERIFICAR]`).

## 10. Vedacoes especificas

- **PA-13** — LGPD + Res. CFM + CP com identificacao precisa.
- **PA-16 / PA-17** — sigilo do plugin reforcado; sem dados de paciente neste contexto.
- **PA-20** — sem cross-sell para tecnologia/sw especifico (slot generico).

## 11. Protocolos acionados

- **P1** — Selo (LGPD + ANPD + Res. CFM atual).
- **P3** — memoria de decisao (bases legais por tratamento).
- **P5** — ANPD em Brasilia (administrativo); JF + JE conforme demanda; CRM/CFO em PED reflexo.
- **P6** — `revisao-final-medica`.

## 12. Localizacao

ANPD em Brasilia (administrativo). JF Federal (acoes contra ANPD). JE comarca da clinica (responsabilidade civil por vazamento).

## 13. Integracao

**Chamada por:** `medico-master`, `triagem-medica`, `constituicao-sociedade-medica`, `violacao-sigilo-medico`.

**Entrega para:** programa LGPD + minutas + cronograma -> `revisao-final-medica` -> operador. Cruza com `compliance-publicidade-medica` (uso de imagem) e `violacao-sigilo-medico` (incidente reflexo).

**Sem esta skill:** clinica/hospital sem programa LGPD estruturado — expostos a multa ANPD ate 2% faturamento ou R$ 50M + responsabilidade civil em vazamento (LGPD 42) + reflexos eticos (CEM 73).
