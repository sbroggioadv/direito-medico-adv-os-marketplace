---
name: prescricao-erro-medico
description: >
  Skill especializada em prescricao em erro medico/odontologico. Distingue 3 anos CC art. 206 §3o V (medico PF autonomo, relacao nao-consumerista) vs 5 anos CDC art. 27 (hospital/clinica/operadora/relacao consumerista). Aplica STJ Sum. 278 (actio nata — termo inicial = ciencia inequivoca do dano), EREsp 1.385.732 (matérias divergentes), REsp 1.708.628/RS (3 anos hospital privado quando consumerista vs CC), STJ Tema 1.061 (prescricao em erro medico vs Lei 8.078). Trata efeito lesivo continuado (sequela), morte do paciente (sucessao + termo inicial), interrupcao por acao penal (CC art. 200), suspensao por requerimento administrativo. Aciona: prescricao erro medico, prazo prescricional medico, 3 anos CC, 5 anos CDC, actio nata, Sum 278, ciencia inequivoca do dano, EREsp 1.385.732, Tema 1.061, prescricao odonto, prescricao hospital, prescricao operadora.
---

# PRESCRICAO ERRO MEDICO

> Skill **Tier 2** — analise dedicada de prazo prescricional. Implementa PA-19 (prescricao sempre conferida + fundamentada), PA-09 (datacao por fato gerador), PA-13 (norma+jurisprudencia precisas). Acionada por `responsabilidade-civil-medica`, `responsabilidade-odontologica`, `cirurgia-estetica-resultado`, `perda-de-uma-chance`, todas as ações do Tier 5, defesa em contestacao com arguicao de prescricao.

---

## 0. Escopo e acionamento

Acionada em toda peca civel envolvendo prazo (petic. inicial, contestacao, parecer). Funcoes: (a) classificar a relacao (consumerista x nao-consumerista); (b) identificar prazo aplicavel; (c) calcular termo inicial (actio nata — Sum. 278 STJ); (d) verificar causas de suspensao/interrupcao; (e) emitir parecer de prescricao com fundamentacao. Pre-requisito: Selo P1 + identificacao do sujeito (PF/PJ) na triagem 4D.

## 1. Posicao na orquestra

- **Chamada por:** `responsabilidade-civil-medica`, `cirurgia-estetica-resultado`, `responsabilidade-odontologica`, `perda-de-uma-chance`, todas as skills do Tier 5 (acoes contra plano), defesa em contestacao.
- **Entrega para:** parecer de prescricao com prazo, termo inicial, causas de suspensao/interrupcao -> insumo direto para peca (autor) ou defesa (contestacao). Anexa ao `CASO.md`.

## 2. Marco normativo

| Norma | Conteudo | Prazo |
|-------|----------|-------|
| **CC art. 206 §3o V** | Pretensao de reparacao civil contra **medico PF autonomo** | **3 anos** |
| **CDC art. 27** | Pretensao de reparacao em relacao **consumerista** — vs hospital, clinica, operadora | **5 anos** |
| CC art. 197 | Suspensao entre conjuges, ascendentes/descendentes (raro em medico, mas pode incidir em caso de cliente medico-paciente proximo) | — |
| CC art. 199 | Suspensao por condicao suspensiva ou prazo | — |
| **CC art. 200** | **Pretensao decorrente de ato apurado em criminal NAO corre antes do transito em julgado da sentenca criminal** | Suspensao |
| CC art. 202 | Interrupcao da prescricao | — |
| CPC art. 487 II | Sentenca de merito acolhendo prescricao | — |

**Sumulas STJ:**
- **Sum. 278** — termo inicial da prescricao = ciencia inequivoca do dano (actio nata).
- **Sum. 326** — quantum inferior ao pleiteado nao gera sucumbencia reciproca.

**STJ paradigma:**
- **EREsp 1.385.732** — embargos de divergencia: prescricao em erro medico (materias divergentes nas Turmas STJ; 2a Secao pacificou).
- **REsp 1.708.628/RS** — hospital privado em relacao consumerista: **5 anos CDC art. 27** (nao 3 do CC). Confirma posicao STJ.
- **REsp 731.078/SP** — actio nata em caso de sequela tardia.
- **Tema 1.061 STJ** (afetado) — prescricao em erro medico — **`[VERIFICAR — afetacao 2026]`** — pode alterar quadro.

## 3. Tabela operacional de prazos

| Demandado (sujeito) | Relacao | Prazo | Base legal | Termo inicial |
|---------------------|---------|-------|-----------|---------------|
| Medico PF autonomo | NAO consumerista | **3 anos** | CC art. 206 §3o V | Ciencia inequivoca do dano (Sum. 278) |
| Medico PF autonomo | CONSUMERISTA (atendimento via clinica/hospital como prestador) | **5 anos** | CDC art. 27 + Sum. 469 + REsp 1.708.628 (analogia) | Mesmo |
| Hospital privado (relacao consumerista) | CONSUMERISTA | **5 anos** | CDC art. 27 + REsp 1.708.628/RS | Mesmo |
| Clinica/consultorio PJ | CONSUMERISTA | **5 anos** | CDC art. 27 + Sum. 469 | Mesmo |
| Operadora de plano | CONSUMERISTA | **5 anos** | CDC art. 27 + Sum. 469 | Mesmo |
| Autogestao (Geap, Cassi) | NAO consumerista (Sum. 608) | **3 anos** | CC art. 206 §3o V | Mesmo |
| SUS / hospital publico | Adm. publica (CF art. 37 §6o) | **5 anos** | DL 20.910/1932 art. 1o | Mesmo |
| Acao regressiva (medico responde a hospital condenado) | Civil | 3 anos | CC art. 206 §3o V | Pagamento da condenacao |

## 4. Termo inicial — actio nata (Sum. 278 STJ)

**Regra:** o prazo nao corre da data do ato medico — corre da **ciencia inequivoca do dano**. Importante porque dano em erro medico pode aparecer dias, meses ou anos depois.

**Hipoteses tipicas:**

| Hipotese | Termo inicial |
|----------|---------------|
| Dano imediato (obito perioperatorio, perfuracao cirurgica diagnosticada na mesma alta) | Data do ato medico ou da alta |
| Dano apurado em pericia (corpo estranho deixado, instrumental retido) | Data do diagnostico em exame de imagem |
| Sequela tardia (paralisia neonatal por sofrimento fetal — REsp 731.078/SP) | Data do diagnostico definitivo da sequela |
| Sequela em crianca (paciente menor) | Idade adulta (CC art. 198 I — nao corre contra absolutamente incapaz) OU desde ciencia dos pais (jurisprudência oscila — `[VERIFICAR]`) |
| Falha estetica progressiva | Data em que o resultado se mostra inalcancavel/agravado (laudo pericial ou diagnostico) |
| Erro diagnostico em oncologia (atraso) | Data do diagnostico correto posterior |
| Lesao oculta descoberta tardiamente | Data do diagnostico ou da pericia que apurou |

**Carga argumentativa:** autor que descobre o dano em data X tem 3 ou 5 anos a partir de X — nao da data do ato medico.

## 5. Suspensao e interrupcao

### 5.1 — Suspensao (CC arts. 197-201)
- **CC art. 197** — entre conjuges, ascendente/descendente — raro em erro medico.
- **CC art. 198 I** — contra absolutamente incapaz (menor de 16 — CC art. 3o). **Critico em pediatria/neonatologia:** prazo nao corre ate o paciente completar 16 anos.
- **CC art. 199** — condicao suspensiva, prazo pendente.
- **CC art. 200** — **pretensao decorrente de ato apurado no juizo criminal nao corre antes do transito em julgado da sentenca criminal**. **Critico em caso multi-frente (P4)**: enquanto a acao penal por homicidio culposo/lesao culposa esta em curso, a prescricao civil nao corre.

### 5.2 — Interrupcao (CC art. 202)
- Despacho positivo de citacao (CPC art. 240 §1o — interrupcao retroativa a propositura).
- Protesto judicial (CPC).
- Apresentacao de credito em concurso (raro).
- Ato judicial que constitua o devedor em mora (raro).
- Ato inequivoco do devedor que reconheca o direito (acordo extrajudicial; conciliacao pre-processual sem ajustes).
- **Interrompida, recomeca a contar do zero** (CC art. 202 paragrafo unico).

### 5.3 — Requerimento administrativo (CDC) — efeito pratico
- Reclamacao na ANS contra operadora -> conta como interpelacao mas **nao interrompe** prescricao civel (STJ tem oscilacoes; `[VERIFICAR]`).
- Reclamacao no PROCON -> idem.
- Notificacao extrajudicial -> nao interrompe (CC art. 202 nao prevê), mas pode ser elemento de pre-constituicao de mora.

## 6. Parecer de prescricao (output da skill)

```
PARECER DE PRESCRICAO — Caso <slug>
Data do fato gerador: <DD/MM/AAAA>
Data da ciencia inequivoca do dano: <DD/MM/AAAA> [Sum. 278 STJ]
Demandados: <lista por sujeito>

## Classificacao
- Sujeito 1 (<nome>): <medico PF / clinica PJ / hospital PJ / operadora>
  Relacao: <consumerista / nao consumerista>
  Prazo: <3 anos CC art. 206 §3o V / 5 anos CDC art. 27>
  Fundamento: <Sum. 469 STJ / REsp 1.708.628/RS / Sum. 608 STJ>
- Sujeito 2: [...]

## Calculo
- Termo inicial: <data da ciencia inequivoca>
- Prazo: <3 anos | 5 anos>
- Prazo limite: <data limite>
- Hoje (<data>): <prescrito | em curso | em risco — N dias restantes>

## Suspensoes/interrupcoes aplicaveis
- CC art. 198 I (menor): <sim/nao — paciente menor de 16>
- CC art. 200 (acao penal): <sim/nao — penal em curso>
- CC art. 202 (interrupcao): <citacao realizada em DD/MM/AAAA — reinicia>

## Recomendacao
- [Para o autor:] ajuizamento ate <data> sob pena de prescricao
- [Para o reu:] arguir prescricao em contestacao (CPC art. 487 II)
- [VERIFICAR] — Tema 1.061 STJ afetado (afetacao 2026)
```

## 7. Vedacoes especificas

- **PA-09** — datacao pelo ano do fato gerador (e da ciencia, nao do ajuizamento).
- **PA-13** — citacao precisa (CC art. 206 §3o V / CDC art. 27 / Sum. 278 STJ / REsp 1.708.628).
- **PA-19** — sempre conferir e fundamentar prazo — autor que erra prazo perde caso; reu que nao argui em contestacao precluiu (CPC art. 337 — preliminar).
- **PA-11** — Tema 1.061 STJ afetado -> `[VERIFICAR]`.
- **PA-02** — sem promessa: "provavelmente prescrito" e nao "estara prescrito".

## 8. Protocolos acionados

- **P1** — Selo emitido pelo `validador-legislacao-vigente`.
- **P5** — UF do foro nao afeta prazo (federal), mas afeta tempo de tramitacao real.

## 9. Localizacao

Prazo prescricional e norma federal (CC e CDC) — uniforme em todo o pais. Localizacao afeta apenas o tempo real de tramitacao do feito.

## 10. Integracao

**Chamada por:** todas as skills do Tier 2 e Tier 5, contestacao com arguicao de prescricao, `responsabilidade-civil-medica`, `responsabilidade-odontologica`, `cirurgia-estetica-resultado`, `perda-de-uma-chance`.

**Entrega para:** parecer de prescricao anexado ao `CASO.md` + insumo direto para peca/defesa. Em contestacao: preliminar de merito (CPC art. 487 II).

**Sem esta skill:** erro de prazo e a principal causa de extincao do feito em erro medico. Autor perde caso; reu perde a defesa mais simples.
