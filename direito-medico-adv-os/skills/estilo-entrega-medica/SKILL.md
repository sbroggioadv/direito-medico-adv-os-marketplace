---
name: estilo-entrega-medica
description: >
  Skill invariante de Camada 3 — define a estrutura canonica das entregas do plugin (peca civel, criminal, PED, MS, contrato, parecer). Aplica FIRAC (Fato-Issue-Regra-Analise-Conclusao) + 6 secoes obrigatorias da peca/parecer (Escopo, Dados, Base legal, Memoria de quantum, Resultado, Ressalva OAB). Estabelece abertura com Selo P1 + data do fato gerador (PA-09) + fechamento com ressalva OAB ativa (PA-05). Operacionaliza memoria de decisao (P3 — tabela auditavel). Aciona: formato peca, estrutura parecer, FIRAC medica, ressalva OAB, memoria de quantum, abertura com Selo, fechamento padrao.
---

# ESTILO E ENTREGA MEDICA (CAMADA 3)

> Skill **transversal** — define a estrutura canonica de toda entrega do plugin. Acionada por todas as skills produtoras (Tier 1-6) antes de finalizar o documento. Operacionaliza a Camada 3 da hierarquia.

---

## 0. Escopo e acionamento

Skill referencial — toda skill produtora consulta esta para formato. Acionada implicitamente em qualquer peca/parecer/contrato. Pode ser invocada diretamente com "formato da peca", "estrutura do parecer", "FIRAC".

## 1. Posicao na orquestra

- **Chamada por:** todas as skills do Tier 2-6 + `revisao-final-medica` (R4 verifica esta estrutura).
- **Aciona:** —
- **Entrega para:** padroniza formato — entrega vai para `revisao-final-medica`.

## 2. Estrutura canonica — peca processual (FIRAC)

```
[ABERTURA]
- Destinatario (Exmo. Sr. Juiz de Direito / TRF / STJ / Camara CRM, etc.)
- Identificacao da parte + qualificacao
- Representacao: por {{ADVOGADO_NOME}}, OAB/{{OAB_UF}} {{OAB_NUMERO}}
- Tipo de peca + base legal (CPC art. ___ / CPP art. ___)
- Data do Selo de Validacao Legal Previa: [data] — CASO.md

I — FATOS [F]
  Narrativa cronologica datada (PA-09 — ano do fato gerador).
  Referencia ao CASO.md (sem expor dados sensiveis no plugin — PA-16).

II — ISSUE [I]
  Questao juridica controvertida em 1-2 frases tecnicas.

III — DIREITO [R + A]
  III.1 Regime juridico — base legal (lei + artigo + ano — PA-13)
  III.2 Jurisprudencia paradigma (Sum/Tema/REsp — PA-10 + PA-11)
  III.3 Subsuncao fato -> norma
  III.4 Onus probatorio fundamentado (PA-14)
  III.5 Quantum/Memoria de decisao (P3 — tabela)
  III.6 Cruzamento P4 quando aplicavel (CC art. 935)

IV — PEDIDOS [C]
  IV.1 Tutela/Antecipacao (se aplicavel — CPC 300 + 537)
  IV.2 Pedidos principais
  IV.3 Subsidiariamente
  IV.4 Inversao do onus se aplicavel
  IV.5 Valor da causa (CPC 292)

[FECHAMENTO]
[Cidade], [data] — {{ADVOGADO_NOME}} | OAB/{{OAB_UF}} {{OAB_NUMERO}}

RESSALVA (PA-05):
"Minuta tecnico-operacional sujeita a revisao + responsabilidade
tecnica do advogado-operador com OAB ativa. Selo de Validacao
Legal Previa emitido em [data] (CASO.md). [VERIFICAR] listados:
[item 1], [item 2]..."
```

## 3. Estrutura canonica — Parecer / Consultivo (6 secoes)

```
PARECER — [Tema] — Emitente: {{ADVOGADO_NOME}} | OAB/{{OAB_UF}} {{OAB_NUMERO}}
Data: [DD/MM/AAAA] — Selo P1 emitido em [data]

1. ESCOPO
   - Consulta apresentada pelo cliente em [data]
   - Pontos especificos a responder
   - Limites do parecer

2. DADOS
   - Documentos e informacoes apresentados (lista referenciada ao CASO.md)
   - Fato gerador datado (PA-09)

3. BASE LEGAL E JURISPRUDENCIAL
   - Lei + artigo + ano (PA-13)
   - Sumula / Tema STJ / STF (PA-10)
   - Resolucoes CFM/CFO/ANS/ANVISA aplicaveis

4. MEMORIA DE QUANTUM / DECISAO (P3)
   - Tabela auditavel quando ha valor
   - Conservadorismo (PA-21)

5. RESULTADO / TESE
   - Subsuncao
   - Risco e probabilidade tecnica (sem promessa — PA-02)
   - Recomendacao operacional

6. RESSALVA OAB (PA-05)
   "Parecer tecnico-operacional sujeito a revisao do advogado-operador.
   Selo P1 emitido em [data]. [VERIFICAR]: [items]."

[Cidade, data] — {{ADVOGADO_NOME}} | OAB/{{OAB_UF}} {{OAB_NUMERO}}
```

## 4. Memoria de decisao / quantum (P3 — coracao tecnico)

Tabela canonica para qualquer entrega com valor:

| Item | Base legal | Fundamentacao | Valor | Atualizacao |
|------|-----------|---------------|-------|-------------|
| Dano material | CC 949 | Comprovantes NF | R$ X | Selic (Sum. 54 STJ) |
| Lucros cessantes | CC 402+950 | Renda x tempo | R$ X | Selic |
| Pensao por morte/incap. | CC 948-950 | Sum. 491 STF | R$ X x prazo Y | Selic |
| Dano moral | CC 186+927 + parametro STJ | Conservador (PA-21) | R$ X | Sum. 362 STJ |
| Dano estetico | CC 949 + Sum. 387 | Cumulavel com moral | R$ Y | Selic |
| Perda de chance | REsp 1.291.247 | % x prejuizo total | R$ Z | Selic |
| Honorarios | CPC 85 §§2o-3o | 10-20% sobre condenacao | — | — |
| **TOTAL** | — | — | **R$ T** | — |

## 5. Abertura padrao (formula)

```
[Destinatario: Exmo. Sr. Juiz / TRF / Camara]

[Parte], qualificacao completa, [estado civil, profissao, RG, CPF, endereco],
representada por {{ADVOGADO_NOME}}, advogado(a) inscrito(a) na OAB/{{OAB_UF}}
sob o n. {{OAB_NUMERO}}, do escritorio {{FIRM_NAME}}, vem, respeitosamente,
a presenca de V. Exa., com fundamento [CPC art. ___ / CPP art. ___ /
Lei 12.016/2009 / etc.], propor a presente [tipo de peca], em face de
[Re], pelos motivos de fato e de direito a seguir expostos.
```

## 6. Ressalva OAB padrao (PA-05 — formula canonica)

```
RESSALVA: minuta tecnico-operacional sujeita a revisao e responsabilidade
tecnica do advogado-operador, inscrito na OAB com situacao ativa.

Selo de Validacao Legal Previa emitido em [data] (CASO.md), fonte:
`validador-legislacao-vigente`.

[VERIFICAR] (PA-11) — itens em alvo movel para conferencia pelo operador:
- [Rol ANS / RN ANS especifica em atualizacao]
- [Estatuto CRM-UF / CRO-UF / norma local]
- [Tema STJ em revisao]
- [Literatura medica em evolucao — SBOC/FEBRASGO/SBP/etc.]

A versao final entregue ao cliente exige conferencia, atualizacao para
o ano do fato gerador (PA-09) e validacao pelo advogado responsavel.
```

## 7. Tokens persona — resolucao em runtime

Tokens permanecem **LITERAIS** no disco:
- `{{ADVOGADO_NOME}}` — nome completo
- `{{OAB_NUMERO}}`, `{{OAB_UF}}` — inscricao
- `{{FIRM_NAME}}` — escritorio
- `{{CIDADE}}`, `{{UF}}` — sede
- `{{AREA_FOCO}}` — defesa-profissional / plano-saude / consultivo / todos
- `{{TOM_VOZ_PERFIL}}`, `{{TOM_VOZ_INTENSIDADE}}` — comunicacao
- `{{MODO_MELHOR_SAIDA}}` — preferencia de output

LLM resolve em runtime via persona em `<cwd>/direito-medico/persona.md`. **No produto final entregue ao cliente, tokens DEVEM estar resolvidos** — R4 da revisao verifica.

## 8. Citacao normativa (PA-13)

| Forma | Exemplo |
|-------|---------|
| Lei | Lei 9.656/1998 art. 10§4o |
| CC/CP/CPP/CPC | CC art. 951 / CP art. 121§3o / CPP art. 386 III / CPC art. 300 |
| Constitucional | CF art. 5o LV |
| Sumula STJ | STJ Sum. 469 / Sum. 608 / Sum. 105 |
| Tema STJ | STJ Tema 990 (pos-Lei 14.454/2022) |
| REsp paradigma | STJ REsp 1.733.013/PR (2a Turma, Min. ___, 2019) |
| Resolucao | Res. CFM 2.336/2023 art. 13 |
| Portaria | Portaria GM/MS 264/2020 |

## 9. Tom (`TOM_VOZ_PERFIL`)

| Perfil | Caracteristica |
|--------|----------------|
| **Tecnico-direto** | Frase curta, vocabulario tecnico, ausencia de adjetivacao |
| **Acolhedor-firme** | Frase com cuidado, mas conclusivo |
| **Combatente** | Tom afirmativo, sem hesitacao (PA-08 — sem critica pessoal) |
| **Conciliador** | Tom de proposta, com aberturas |

Intensidade 1-10 modula o uso de adjetivacao e o peso retorico.

## 10. Vedacoes especificas

- **PA-05** — ressalva OAB obrigatoria em toda entrega.
- **PA-09** — datar pelo ano do fato gerador.
- **PA-13** — citacao precisa de norma + jurisprudencia.
- **PA-22** — peca de um caso nao mistura dados de outro.

## 11. Protocolos acionados

- **P3** — memoria de decisao/quantum (tabela auditavel).
- **P6** — `revisao-final-medica` verifica esta estrutura em R4.

## 12. Localizacao

Foro/competencia (P5) sempre na abertura. Cidade/UF da OAB do advogado vs cidade do foro — distinguir.

## 13. Integracao

**Chamada por:** todas as skills do Tier 2-6 quando produzem entrega + `revisao-final-medica` R4.

**Entrega para:** padroniza formato — produto vai para `revisao-final-medica`.

**Sem esta skill:** pecas/pareceres sem FIRAC + sem 6 secoes + sem memoria de quantum tabular + sem ressalva OAB padrao — risco de inconsistencia entre skills produtoras e fragilidade tecnica.
