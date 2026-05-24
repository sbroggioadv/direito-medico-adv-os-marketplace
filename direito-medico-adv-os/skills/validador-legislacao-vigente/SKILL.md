---
name: validador-legislacao-vigente
description: >
  Protocolo 1 do plugin. Valida vigencia normativa nos 4 niveis (federal + conselho profissional CFM/CFO + regulador ANS/ANVISA + estadual/municipal) e a jurisprudencia STJ/STF/TRFs (Sumulas e Temas repetitivos) no ANO DO FATO GERADOR. Emite o Selo de Validacao Legal Previa — pre-requisito absoluto de toda peca, parecer, contrato, defesa e calculo de quantum. Cobre a reforma 2022-2026: Lei 14.510/2022 (telemedicina), Lei 14.454/2022 (Rol ANS exemplificativo), Lei 15.378/2026 (Estatuto do Paciente), Res. CFM 2.336/2023 (publicidade), Res. CFM 2.337/2023 (HOF), Res. CFM 2.320/2022 (reproducao). Marca [VERIFICAR] em alvo movel (Rol ANS, RN, prazos locais, sumula em revisao). Aciona: validar legislacao, lei vigente, a norma ainda vale, datar fato gerador, qual regime se aplica, reforma medica, Lei 14.454, Tema 990 STJ, Sum. 469/597/608 STJ, Res. CFM, Res. CFO, RDC ANVISA, RN ANS, emitir o Selo.
---

# VALIDADOR DE LEGISLACAO VIGENTE

> Skill **Tier 0** — o Protocolo 1 em operacao. Pre-requisito absoluto de toda skill de producao (Tier 2-6). Emite o **Selo de Validacao Legal Previa**. Implementa PA-04, PA-09, PA-10, PA-11, PA-13.

---

## 0. Escopo e acionamento

Acionada por `medico-master` antes de toda producao, ou diretamente pelo operador: "validar legislacao", "qual regra se aplica", "datar fato gerador", "a reforma impacta este caso?". Recebe: norma(s) citada(s), tipo de caso (4D), data do fato gerador, UF de atuacao e UF de inscricao no conselho. Entrega: laudo de vigencia nos dois eixos + **Selo** registrado no `CASO.md`.

## 1. Posicao na orquestra

- **Chamada por:** `medico-master` (obrigatorio antes de Tier 2-6), `triagem-medica`, qualquer skill que precise confirmar norma/jurisprudencia.
- **Entrega para:** a skill de producao solicitante + campo `Selo de Validacao Legal Previa` no `CASO.md`.
- **Dependencia (PA-04):** **nenhuma producao opera sem o Selo.**

## 2. Os dois eixos do alvo movel

O direito medico muda em duas dimensoes simultaneas:

- **Eixo temporal** — reforma legislativa 2022-2026: Lei 14.510/2022 (telemedicina), Lei 14.454/2022 (Rol ANS exemplificativo — afeta Tema 990 STJ), Res. CFM 2.314/2022 (telemedicina), Res. CFM 2.320/2022 (reproducao), Res. CFM 2.336/2023 (publicidade), Res. CFM 2.337/2023 (HOF — conflito CFM x CFO), Lei 15.378/2026 (Estatuto do Paciente). A norma aplicavel e a vigente **no ano do fato gerador** (PA-09).
- **Eixo geografico** — foro federal (MS contra conselho — Sum. 105 STJ + CF art. 109 I), estadual (civel/criminal — CDC art. 101 I; CPP art. 70), municipal (vigilancia sanitaria local), administrativo (CRM/CRO da UF de inscricao — Res. CFM 2.145/2016 + Res. CFO 71/2006). Estatutos regionais complementam.

## 3. Os 8 passos do Protocolo 1

### Passo 1 — Datar o fato gerador
Identificar a data exata do ato medico controvertido (cirurgia, parto, atendimento, alta, publicidade) ou do evento contratual (negativa de cobertura, reajuste, rescisao). Esta data e marco para a redacao aplicavel (PA-09). Se nao informado, perguntar: "Qual a data do fato gerador? Ex.: 12/03/2024."

### Passo 2 — Inventariar as normas nos 4 niveis
- **Federal:** Lei 9.656/1998 (planos), Lei 12.842/2013 (ato medico), Lei 14.510/2022 (telemedicina), Lei 14.454/2022 (Rol exemplificativo), Lei 15.378/2026 (Estatuto do Paciente), Lei 13.709/2018 (LGPD), Lei 8.078/1990 (CDC), Lei 10.406/2002 (CC arts. 186, 187, 927, 932, 948-950, 951), DL 2.848/1940 (CP arts. 121§3o, 129§6o, 135, 154, 282, 299), Lei 10.216/2001 + Lei 13.840/2019 (saude mental).
- **Conselhos (forca regulamentar):** Res. CFM 2.217/2018 (CEM), 2.314/2022 (telemedicina), 2.336/2023 (publicidade), 2.337/2023 (HOF), 1.821/2007 (prontuario), 2.145/2016 (PED CRM), 2.320/2022 (reproducao), 1.805/2006 (paliativos), 1.995/2012 (DAV); Res. CFO 118/2012, 71/2006 (PED CRO), 196/2019 (publicidade), 287/2022.
- **Reguladores:** RDC ANVISA 36/2013, 50/2002, 222/2018, 63/2011; RN ANS (Rol — `[VERIFICAR]` — sucessoras RN 465/2021), RN 539/2022 (TEA).
- **Estadual/Municipal:** estatuto CRM/CRO regional, vigilancia sanitaria municipal/estadual, internacao compulsoria local.

### Passo 3 — Validar vigencia no ano do fato gerador
Para cada norma: publicacao (DOU), vacatio legis, vigencia efetiva, revogacao expressa/tacita. Classificar: **VIGENTE / ALTERADA / REVOGADA / VACATIO / INDETERMINADO**. Norma INDETERMINADO -> sinalizar e pedir orientacao. Distinguir leis com redacao alterada por MP/lei posterior — usar a redacao do ano do fato gerador, nao a atual (PA-09).

### Passo 4 — Validar jurisprudencia STJ/STF/TRFs/Conselho
**Sumulas vivas em 2026** (verificar status `[VERIFICAR — revisao]`):
- Sum. 469 STJ — CDC aplica a planos.
- Sum. 597 STJ — CDC odontologia (subjetiva CD); CDC nao aplica autogestao; carencia abusiva > 24h em urgencia.
- Sum. 608 STJ — CDC aplica a coletivos (nao autogestao).
- Sum. 105 STJ — MS contra ato de conselho profissional (autarquia federal) -> JF.
- Sum. 387 STJ — cumulacao dano moral + estetico.
- Sum. 326 STJ — quantum/sucumbencia reciproca.
- Sum. 278 STJ — actio nata (termo inicial prescricao).

**Temas STJ vivos:** 952 (reajuste faixa etaria), 1.037 (clausulas limitativas abusivas), 1.069 (reembolso integral excepcional), 1.082 (rescisao coletivo + tratamento grave), 1.094/1.095 (limites de revisao do quantum).

**Tema 990 STJ** (rol ANS taxativo mitigado) — **alterado pela Lei 14.454/2022**: pre-lei usa redacao anterior; pos-lei aplica rol exemplificativo. Status `[VERIFICAR — afetacao 2026]`.

**STF:** RE 855.178 (responsabilidade solidaria dos entes na saude publica), Tema 793 (alto custo SUS), RE 958.252 (terceirizacao/pejotizacao — repercussao geral).

### Passo 5 — Travar o regime aplicavel
Distinguir o regime do ano:

| Tema | Pre-marco | Pos-marco |
|------|-----------|-----------|
| Telemedicina | Res. CFM 1.643/2002 (transitoria) | Lei 14.510/2022 + Res. CFM 2.314/2022 |
| Rol ANS | Tema 990 STJ taxativo mitigado | Lei 14.454/2022 — exemplificativo + criterios |
| DAV | Res. CFM 1.995/2012 (administrativa) | Lei 15.378/2026 — status legal |
| Publicidade medica | Res. CFM 1.974/2011 | Res. CFM 2.336/2023 |
| HOF | Res. CFO autonoma | Res. CFM 2.337/2023 — conflito interconselhos |
| Reproducao assistida | Res. CFM 2.168/2017 | Res. CFM 2.320/2022 |

### Passo 6 — Verificar regras locais e regulatorias finais
Estatuto do CRM/CRO regional pode complementar Res. CFM/CFO em prazos administrativos do PED. Regulamento local de vigilancia sanitaria (RDC complementada por norma estadual/municipal). Sem confirmacao da regra local -> `[VERIFICAR — estatuto CRM-UF / vigilancia municipal / norma estadual]` (PA-11).

### Passo 7 — Rastrear PL/MP/ADIN pendente
Verificar PL em tramitacao, ADIN/ADC ajuizada que pode alterar o cenario (ex.: contestacao da Lei 14.454/2022 por operadoras, debates sobre Lei 15.378/2026 e DAV, RN ANS em consulta publica). Sinalizar.

### Passo 8 — Emitir o Selo
Ao final, emitir o Selo formal.

## 4. Formato do Selo de Validacao Legal Previa

```
SELO DE VALIDACAO LEGAL PREVIA
Data-base: [DD/MM/AAAA]
Data do fato gerador: [DD/MM/AAAA]
Esfera(s): [civel | criminal | etico-disciplinar | regulatorio]
Subdominio: [medicina | odontologia | saude mental | reproducao | outros]
Localizacao: [Cidade/UF] — CRM/CRO regional: [UF]
Normas validadas (4 niveis):
  Federal:    [Lei + ano + art.] — VIGENTE — redacao de [data]
  Conselho:   [Res. CFM/CFO + numero/ano] — [VIGENTE | VERIFICAR]
  Regulador:  [RDC ANVISA / RN ANS + numero/ano] — [VIGENTE | VERIFICAR atualizacao]
  Estadual/Municipal: [estatuto CRM-UF / lei estadual / norma municipal] — [VIGENTE | VERIFICAR]
Jurisprudencia aplicavel: [Sumula | Tema STJ | REsp + ano + turma — status: viva / superada / em revisao]
Foro/competencia: [JF Sum. 105 STJ | JE comarca [Cidade] | administrativo CRM-UF/CRO-UF]
Alertas: [PL/MP pendente | sumula em revisao | Rol ANS atualizacao | conflito interconselhos HOF]
[VERIFICAR]: [pontos que demandam checagem manual pelo operador]
Validade: reflete legislacao na data-base. Reverificar se caso fechar apos [data-base + 60 dias].
```

Selo registrado no `CASO.md` (skill `memoria-de-caso-medico`). Qualquer skill de producao que receba demanda sem Selo aciona esta skill primeiro.

## 5. Flag de norma desatualizada

```
[ALERTA NORMATIVO]
A norma citada ([Lei X art. Y]) nao se aplica ao fato gerador de [data].
Motivo: [revogada por / alterada por / substituida por]
Norma aplicavel ao periodo: [Z]
Acao: [substituir referencia / verificar texto vigente / aguardar regulamentacao]
```

Nunca prosseguir com norma REVOGADA sem confirmacao expressa do operador.

## 6. Casos transitorios criticos (alvo movel)

- **Pre vs pos Lei 14.454/2022** — Tema 990 STJ: pre-lei usa rol como referencia obrigatoria com excecoes restritas; pos-lei aplica rol exemplificativo + criterios (eficacia comprovada, recomendacao oficial, evidencia cientifica).
- **Telemedicina** — pre-Lei 14.510/2022: Res. CFM 1.643/2002 (transitoria); pos-Lei + Res. CFM 2.314/2022: moldura estavel.
- **DAV** — pre-Lei 15.378/2026: Res. CFM 1.995/2012 (administrativa); pos-lei: status legal expresso.
- **HOF — Res. CFM 2.337/2023** — conflito CFM x CFO ativo: pre-Res. regime CFO autonomo; pos-Res. demanda triagem do sujeito (medico x CD) e do procedimento.
- **Rol ANS** — `[VERIFICAR — atualizacao ANS]` sempre. RN 465/2021 e sucessoras.

## 7. Vedacoes especificas

- **PA-09** — a redacao atual nao substitui a redacao do ano do fato gerador.
- **PA-04** — Selo nao emitido = producao bloqueada.
- **PA-10** — vedado citar Sumula/Tema revogado, superado ou em revisao sem ressalva.
- **PA-11** — alvo movel ou regra local nao confirmada -> `[VERIFICAR]`. Nunca inventar item de Rol, numero de RN ou prazo de estatuto regional.
- **PA-13** — toda norma com lei+artigo+ano, jurisprudencia com tribunal+turma+numero+ano.
- Nunca emitir Selo sem completar os 8 passos. Nunca afirmar vigencia sem checar fonte oficial.

## 8. Protocolos acionados

- **P1** — esta skill **e** o Protocolo 1.
- **P5 — Localizacao** — o Passo 6 aplica o eixo geografico.

## 9. Localizacao

A localizacao e estrutural da validacao. Le cidade + UF + UF de inscricao no conselho (da persona e do `CASO.md`). O Selo so e emitido com a localizacao identificada — o eixo geografico determina qual estatuto CRM/CRO regional, qual vigilancia sanitaria, qual foro estadual valem. Regra local nao confirmada -> `[VERIFICAR — norma local]` no Selo (PA-11).

## 10. Integracao

**Chamada por:** `medico-master` (obrigatorio antes de Tier 2-6), `triagem-medica`, qualquer skill que receba citacao de norma.

**Entrega para:** a skill de producao que aguarda o Selo + campo `Selo` no `CASO.md`. Entrega final passa por `revisao-final-medica` (R1-R4).

**Sem esta skill:** nenhuma producao opera (PA-04). Invariante (nao-removivel).
