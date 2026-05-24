---
name: acao-home-care
description: >
  Acao contra operadora por negativa de internacao domiciliar (home care) — paciente que substitui internacao hospitalar por atendimento em residencia com equipe multidisciplinar (medico, enfermagem 12/24h, fisioterapia, fonoaudiologia, nutricao, equipamentos). Aplica Lei 9.656/1998 + Lei 14.454/2022 (Rol exemplificativo) + STJ AgInt no AREsp 1.232.473 (criterios de cobertura: necessidade tecnica + custo equivalente ou inferior + parecer medico + estabilidade clinica) + Sum. 469 STJ + RN ANS 211/2010 (cuidados domiciliares — equivalencia funcional) `[VERIFICAR atual]`. Tutela de urgencia CPC 300 — gravidade clinica + tempo. Distingue home care **propriamente dito** (internacao domiciliar) de cuidador domiciliar e visitas domiciliares avulsas. Aciona: home care, internacao domiciliar, negativa home care, AgInt AREsp 1.232.473, cuidador, ventilacao mecanica domiciliar, alimentacao enteral PEG, paciente acamado, idoso plano de saude, equipe multidisciplinar.
---

# ACAO DE HOME CARE

> Skill **Tier 5** — acao contra operadora por negativa de home care/internacao domiciliar. Implementa PA-04, PA-10 (Lei 14.454 pos-2022 + STJ), PA-11, PA-13, PA-14, PA-15 (CDC 14 objetiva), PA-21. Acionada por `medico-master`, `triagem-medica`, `tutela-urgencia-plano-saude`.

---

## 0. Escopo e acionamento

Acao do paciente contra operadora por negativa de **home care** — internacao domiciliar com equipe multidisciplinar substituindo internacao hospitalar. Casos tipicos: paciente acamado pos-AVC, com ventilacao mecanica domiciliar, alimentacao enteral (PEG/NG), pos-cirurgico complexo, idoso com cuidados continuos, paliativo. Pre-requisito: Selo P1 + parecer do medico assistente.

## 1. Posicao na orquestra

- **Chamada por:** `medico-master`, `triagem-medica`, `tutela-urgencia-plano-saude`.
- **Aciona:** `tutela-urgencia-plano-saude` (modelo unificado), `validador-legislacao-vigente` (RN ANS atual), `revisao-final-medica`.
- **Entrega para:** peticao inicial com tutela + memoria de quantum.

## 2. Marco normativo

| Norma | Conteudo |
|-------|----------|
| **Lei 9.656/1998** | Coberturas obrigatorias (art. 10) |
| **Lei 14.454/2022** | Rol exemplificativo (art. 10§13) — aplicavel a home care fora de lista |
| **RN ANS 211/2010** | Cuidados domiciliares — equivalencia funcional `[VERIFICAR atualizacao]` |
| RN ANS 465/2021+ | Rol vigente |
| CDC art. 6o III/VIII + 14 + 47 + 51 IV | Direitos + objetiva + inversao + nulidade abusiva |
| CDC art. 27 | Prescricao 5a |
| **Lei 10.741/2003 (EI)** | Estatuto Idoso — protecao especial |
| Lei 13.146/2015 (LBI) | PCD |
| CPC art. 300 / 537 | Tutela + astreintes |

**Jurisprudencia:**
- **STJ AgInt AREsp 1.232.473/MS** — criterios para home care
- STJ AgInt REsp 1.901.234/SP — equivalencia funcional `[VERIFICAR jurisprudencia mais atual]`
- STJ Sum. 469 (CDC) / 608 (coletivos) / 597 (autogestao)
- TJSP / TJRJ recorrente — tese consolidada de cobertura quando ha equivalencia

## 3. Criterios pos-AgInt AREsp 1.232.473 (estrategia de procedencia)

A cobertura e devida quando:

1. **Indicacao medica fundamentada** — relatorio do medico assistente com detalhamento do quadro
2. **Equivalencia funcional** — home care substitui internacao hospitalar (mesmas funcoes essenciais)
3. **Custo equivalente ou inferior** — economia para operadora (chave da tese — argumento financeiro pro consumidor)
4. **Estabilidade clinica** — paciente fora de fase aguda (passou para fase de manutencao)
5. **Estrutura domiciliar adequada** — espaco fisico minimo + cuidador familiar + acesso a hospital

**Lei 14.454/2022 reforca** — mesmo fora do Rol, criterios sao acionados.

## 4. Tipos de negativa e teses

| Negativa | Tese |
|----------|------|
| **"Nao consta no Rol ANS"** | Lei 14.454/2022 + AgInt AREsp 1.232.473 + equivalencia funcional |
| **"Cuidador nao e medico"** | Equipe multidisciplinar e home care; cuidador isolado e outra coisa |
| **"Sem cobertura para enfermagem 24h"** | Equivalencia com UTI/internacao + Sum. 469 |
| **"Tratamento experimental/paliativo"** | Distinguir — paliativo nao e experimental + Res. CFM 1.805/2006 (cuidados paliativos) |
| **"Tempo limitado X dias"** | Necessidade clinica determina prazo, nao tabela arbitraria |
| **Glosa de equipamento** | Concessao integral inclui equipamentos (ventilador, aspirador, cama hospitalar) |
| **Negativa por idade** | Vedada — Lei 10.741 art. 15 + Sum. 302 STJ |
| **"Paciente cronico — fora do escopo"** | Cronico estavel cabe em home care |

## 5. Distincoes criticas (PA-13)

| Modalidade | Caracteristica | Cobertura |
|------------|----------------|-----------|
| **Home care propriamente dito** | Equipe multidisciplinar + acompanhamento continuo | Cobertura via Lei 14.454 + AgInt + Sum. 469 |
| **Atencao domiciliar (RN 211)** | Visitas eventuais (consulta, troca de curativo) | Cobertura prevista em RN |
| **Cuidador domiciliar** | Profissional unico (geralmente enfermeiro) | Geralmente nao coberta — distinguir de home care |
| **Internacao hospitalar prolongada** | Em hospital | Alternativa ao home care quando este nao cabe |

Confundir as 4 categorias enfraquece a peca.

## 6. Tutela de urgencia (CPC 300)

**Fumus:** Lei 14.454 + Sum. 469 + AgInt AREsp 1.232.473 + parecer medico + criterios 1-5 demonstrados.

**Periculum:** paciente em risco se mantido em hospital com infeccao hospitalar (Lei 13.989/2020 art. relativo `[VERIFICAR]`); ou paciente estavel em alta hospitalar sem condicao de retorno domiciliar; sofrimento familiar.

**Pedido:** custeio integral (equipe + equipamentos + insumos) + astreintes (`[VERIFICAR STJ EAREsp 650.536]` — proporcionais).

## 7. Memoria de quantum (P3 + PA-21)

| Item | Base |
|------|------|
| Custeio integral home care | Custo mensal x prazo necessario (relatorio medico) |
| Reembolso de desembolsos | Selic desde desembolso (Sum. 54) |
| Dano moral autonomo | Conservador — atraso de assistencia (PA-21) |
| Astreintes | Proporcionais — limite ao bom senso |

## 8. Esqueleto FIRAC

```
PETICAO INICIAL — Civel com tutela
EXMO. SR. JUIZ DE DIREITO DA ___ VARA CIVEL DE [Cidade/UF]

[PACIENTE/CURADOR], qualificacao, por {{ADVOGADO_NOME}} OAB/{{OAB_UF}} {{OAB_NUMERO}},
em face de [OPERADORA] CNPJ ___

I — FATOS — diagnostico, internacao, alta, prescricao de home care, negativa
   (referencia CASO.md)

II — ISSUE — negativa viola Lei 9.656 + Lei 14.454 + AgInt AREsp 1.232.473?

III — DIREITO
  III.1 Regime — CDC 14 (PA-15) + Sum. 469 STJ
  III.2 Lei 14.454/2022 — Rol exemplificativo
  III.3 Criterios AgInt AREsp 1.232.473:
        - Indicacao medica fundamentada
        - Equivalencia funcional com internacao
        - Custo equivalente ou inferior (anexar planilha comparativa)
        - Estabilidade clinica
        - Estrutura domiciliar adequada
  III.4 Inversao do onus — CDC 6o VIII (PA-14)
  III.5 [Estatuto Idoso / LBI se aplicavel — protecao reforcada]
  III.6 Tutela de urgencia — CPC 300

IV — PEDIDOS
  IV.1 Tutela: custeio integral + astreintes R$ ___ (proporcionais) + bloqueio
        SISBAJUD se descumprimento
  IV.2 Procedencia — manutencao + reembolso com Selic
  IV.3 Dano moral autonomo (PA-21)
  IV.4 Inversao do onus
  IV.5 Honorarios (CPC 85)

[Cidade, data] — {{ADVOGADO_NOME}} | OAB/{{OAB_UF}} {{OAB_NUMERO}}

RESSALVA (PA-05).
```

## 9. Documentos obrigatorios

1. Apolice + cobertura
2. Carteirinha vigente
3. Relatorio medico detalhado (CID + escala funcional Karnofsky/Barthel + prescricao + estabilidade)
4. Planilha de equivalencia funcional (compara hospital vs domicilio)
5. Plano de cuidados domiciliares (equipe + equipamentos + insumos)
6. Cotacao de empresa de home care (3 cotacoes ideal)
7. Negativa formal da operadora
8. Eventual idade do paciente (EI) ou laudo de PCD (LBI)

## 10. Casos tipicos

- **AVC com sequela motora + ventilacao mecanica:** indicacao classica — alta hospitalar com manutencao em casa.
- **Idoso em pos-AVC com PEG:** alimentacao enteral + cuidados — EI agrava protecao.
- **Paciente paliativo em fim de vida:** Res. CFM 1.805 + dignidade — tese muito forte.
- **Crianca com paralisia cerebral:** LBI + Lei 12.764 (TEA) se aplicavel + Lei 13.146 + assistencia continua.
- **Pos-cirurgia cardiaca complexa:** transicao hospital -> casa — temporario.
- **Esclerose lateral amiotrofica:** progressao — periodos crescentes — cobertura continuada.

## 11. Vedacoes especificas

- **PA-03 / PA-06** — sem opinar conduta clinica, sem orientacao ao paciente.
- **PA-10 / PA-11** — Tema STJ atual + Rol em atualizacao -> `[VERIFICAR]`.
- **PA-13** — Lei 9.656 + Lei 14.454 + RN 211 + AgInt AREsp 1.232.473.
- **PA-14** — inversao fundamentada.
- **PA-21** — astreintes proporcionais; dano moral conservador.

## 12. Protocolos acionados

- **P1** — Selo (Rol + jurisprudencia atual).
- **P3** — memoria de quantum.
- **P5** — JE domicilio do autor (CDC 101 I).
- **P6** — `revisao-final-medica`.

## 13. Integracao

**Chamada por:** `medico-master`, `triagem-medica`, `tutela-urgencia-plano-saude`.

**Entrega para:** peticao inicial com tutela + memoria -> `revisao-final-medica` -> operador.

**Sem esta skill:** acao generica que confunde home care com cuidador domiciliar; perde criterios AgInt AREsp 1.232.473; tutela frouxa.
