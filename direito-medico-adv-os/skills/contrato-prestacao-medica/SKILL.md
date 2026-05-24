---
name: contrato-prestacao-medica
description: >
  Contratos de prestacao de servicos medicos/odontologicos em 3 modalidades — PJ-PJ (clinica contrata empresa de plantonistas), PJ-PF (clinica contrata medico autonomo), PF-PF (paciente x medico privado). Atencao especial a pejotizacao (Lei 13.467/2017 — reforma trabalhista admite + STF RE 958.252 + Sum. 331 TST — distinguir vinculo CLT de PJ legitima), plantao (medico-plantonista CLT x PJ), responsabilidade civil compartilhada (Sum. 469 STJ + CDC art. 14 + CC art. 951), nao-concorrencia, sigilo, exclusividade, multa, rescisao. Aplica Lei 12.842/2013 (ato medico privativo) + CC arts. 593-609 (prestacao de servico) + CDC 14 + CLT 3o (vinculo). Aciona: contrato prestacao medica, pejotizacao medica, plantao medico, contrato plantonista, vinculo CLT medico, RE 958.252, Sum 331 TST, nao concorrencia medica, contrato PJ clinica, contrato medico autonomo.
---

# CONTRATO DE PRESTACAO MEDICA

> Skill **Tier 6** — elaboracao e analise de contratos de prestacao medica/odontologica. Implementa PA-04, PA-13, PA-15 (subjetiva x objetiva), PA-20 (sem cross-sell com trabalhista). Acionada por `medico-master`, `triagem-medica` (modo consultivo), `constituicao-sociedade-medica`.

---

## 0. Escopo e acionamento

Elaboracao/analise de contratos: (a) **clinica/hospital PJ contrata medico PF** (autonomo); (b) **clinica/hospital PJ contrata clinica/PJ de medicos** (pejotizacao); (c) **socios da clinica entre si** (acordo de socios paralelo ao contrato social); (d) **paciente x medico privado** (PF-PF — pre-tratamento estetico, particular). Pre-requisito: Selo P1 + brief da relacao.

## 1. Posicao na orquestra

- **Chamada por:** `medico-master`, `triagem-medica`, `constituicao-sociedade-medica`.
- **Aciona:** `lgpd-saude` (clausulas LGPD), `credenciamento-plano-saude` (quando ha cobertura de operadora), `validador-legislacao-vigente`, `revisao-final-medica`.
- **Entrega para:** minuta de contrato + parecer de risco trabalhista.

## 2. Marco normativo

| Norma | Conteudo |
|-------|----------|
| **CC arts. 593-609** | Prestacao de servicos — regras gerais |
| **Lei 12.842/2013** | Ato medico privativo |
| Lei 5.081/66 | Odontologico |
| **CLT art. 3o** | Vinculo de emprego — subordinacao + pessoalidade + habitualidade + onerosidade |
| Lei 13.467/2017 (Reforma Trabalhista) | Autonomia legitima + terceirizacao |
| **STF RE 958.252** | Terceirizacao de atividade-fim e licita |
| **Sum. 331 TST** | Vinculo se fraude — pejotizacao com elementos de CLT e vinculada |
| CDC art. 14 + 14§4o | Objetiva da PJ + subjetiva do profissional liberal |
| CC art. 951 | Subjetiva do medico PF |
| Sum. 469 STJ | CDC em plano de saude — reflexo |
| CF art. 5o XX | Livre exercicio de associacao/profissao |
| Codigo Civil arts. 1.011-1.027 | Acordo de socios |

**Jurisprudencia:**
- **STF RE 958.252** — terceirizacao licita
- **Sum. 331 TST** — fraude na pejotizacao
- TST AIRR 1.234.567 (medico PJ com vinculo reconhecido) `[VERIFICAR jurisprudencia atual TST]`
- STJ REsp 1.832.105 (sociedade medica simples)

## 3. As 3 modalidades

| Modalidade | Sujeitos | Risco principal |
|------------|----------|-----------------|
| **PJ-PF (medico autonomo)** | Clinica PJ + medico PF | Pejotizacao por elementos CLT |
| **PJ-PJ (empresa de plantonistas)** | Clinica PJ + clinica PJ | Pejotizacao via PJ — STF RE 958.252 mitiga |
| **PF-PF** | Paciente + medico | CDC 14 §4o subjetiva — relacao de consumo |
| **Socios** | Socios da clinica | Acordo de socios complementar |

## 4. Pejotizacao — elementos de risco (PA-13, sem cross-sell PA-20)

CLT art. 3o vinculo se cumulativos:

| Elemento | Conteudo |
|----------|----------|
| **Subordinacao** | Ordens; horarios fixos; chefe imediato |
| **Pessoalidade** | So aquele medico pode prestar |
| **Habitualidade** | Frequencia regular |
| **Onerosidade** | Pagamento |

**STF RE 958.252:** terceirizacao **licita** mesmo em atividade-fim — desde que **autonomia real**.

**Defesa contra fraude (Sum. 331 TST):** documentos comprovando autonomia: PJ propria; equipamentos proprios; multiplos contratos; sem horario fixo; ausencia de subordinacao direta; capacidade negocial de ajustes.

**No contrato:** clausulas que evidenciam **autonomia** — sem horario fixo rigido; possibilidade de substituicao; ausencia de exclusividade absoluta; ausencia de obrigacao de "comparecer com uniforme da clinica".

## 5. Clausulas criticas (matriz)

| Clausula | Conteudo + alerta |
|----------|-------------------|
| **Objeto** | Especifico — sem confundir ato medico (vedado terceirizar — Lei 12.842) com terceirizacao de PJ (licita) |
| **Forma de execucao** | Autonomia tecnica (medico decide conduta) — vs subordinacao tecnica |
| **Remuneracao** | Por procedimento / hora / repartido — sem mascara de salario |
| **Plantao** | Distincao crucial — CLT (24h fixo, escala da clinica, uniforme) x PJ (escolha do plantao, multipla atividade) |
| **Exclusividade** | Vedada exclusividade absoluta — sinal de vinculo CLT |
| **Nao-concorrencia pos-contratual** | 2-5a + raio geografico + compensacao financeira — STJ admite com razoabilidade |
| **Sigilo (LGPD + Res. CFM 1.821)** | Clinica e controladora; medico operador; cadeia de responsabilidade |
| **Responsabilidade civil compartilhada** | Sum. 469 + CDC 14 — clinica objetiva; medico subjetiva — clausula de regresso |
| **Seguro de responsabilidade civil** | Quem paga + cobertura — recomendar a clinica |
| **Multa rescisoria** | Razoavel — sem desnaturar autonomia |
| **Foro / Arbitragem** | JE comarca + arbitragem em hospital grande |

## 6. Riscos da PJ-PF (pejotizacao) — checklist do contrato

| Risco | Mitigacao no contrato |
|-------|------------------------|
| Horario fixo + escala da clinica | Permitir escolha + substituicao |
| Equipamentos so da clinica | Documentar equipamentos do medico |
| Salario disfarcado | Por procedimento ou por hora variavel |
| Ausencia de outras atividades | Sem clausula de exclusividade total |
| Uniforme / cartao de ponto | Vedados |
| Reuniao obrigatoria semanal | Voluntaria |
| Capacitacao obrigatoria | Voluntaria |
| Subordinacao a "chefe de equipe" | Autonomia tecnica preservada |

## 7. Plantao medico (caso recorrente)

| Modelo | Caracteristica | Risco trabalhista |
|--------|----------------|-------------------|
| **CLT plantonista (escalas fixas)** | Vinculo + 13o + ferias + FGTS + INSS empregador | Sem risco — esta dentro |
| **PJ por plantao com multiplos hospitais** | Autonomia real + multiplos contratos | Baixo se documentado |
| **PJ exclusiva 1 hospital com escalas fixas** | Mascara de CLT | Alto — Sum. 331 TST |
| **Cooperativa** | Cooperado se ha capital social + assembleia + rateio | Medio — TST tem oscilacao |

## 8. Esqueleto — Minuta contrato PJ-PF

```
CONTRATO DE PRESTACAO DE SERVICOS MEDICOS

CONTRATANTE: [CLINICA PJ] CNPJ ___, doravante CLINICA
CONTRATADO: Dr. ___, CRM ___, doravante MEDICO

OBJETO — Cl. 1a — prestacao de servicos medicos de [especialidade] com
   autonomia tecnica do MEDICO (Lei 12.842/2013 art. 4o)

EXECUCAO — Cl. 2a — sem subordinacao; o MEDICO conserva conduta clinica;
   horario flexivel; substituicao admitida; possibilidade de outras
   atividades; ausencia de uniforme exigido

REMUNERACAO — Cl. 3a — R$ ___ por consulta + R$ ___ por procedimento
   (sem salario mensal fixo)

PLANTAO — Cl. 4a (se aplicavel) — escolha pelo MEDICO entre escalas
   ofertadas; possibilidade de recusa

SIGILO + LGPD — Cl. 5a — CLINICA e CONTROLADORA (Res. CFM 1.821 + LGPD);
   MEDICO opera dados com finalidade de cuidado; obrigacoes art. 6o LGPD

RESPONSABILIDADE — Cl. 6a — CLINICA assume RC objetiva (CDC 14 +
   Sum. 469 STJ); MEDICO assume RC subjetiva (CC 951); clausula de regresso

NAO-CONCORRENCIA — Cl. 7a — apos a rescisao, MEDICO se obriga por 24 meses
   a nao prestar servicos em raio de 5 km mediante compensacao mensal
   de R$ ___ (STJ admite com razoabilidade)

PRAZO + RESCISAO — Cl. 8a — indeterminado; rescisao com 60 dias de aviso
   previo; multa de 1 mensalidade media em rescisao injustificada

FORO — Cl. 9a — comarca de [Cidade/UF] OU Arbitragem [Camara X]

[Cidade, data]
__________________  __________________
CLINICA              MEDICO  CRM ___

RESSALVA (PA-05) — minuta tecnico-operacional sujeita a revisao do
operador OAB ativo.
```

## 9. Casos tipicos

- **Clinica + 5 medicos PJ:** modelo PJ-PJ — STF RE 958.252 admite; checklist autonomia.
- **Hospital + plantonista PJ exclusivo 36h/semana:** ALTO RISCO — TST converte em CLT.
- **Clinica estetica + 2 medicos socios + 3 medicos terceiros PJ:** sociedade simples LTDA + 3 contratos PJ-PJ + acordo de socios.
- **Medico PF prestador para 3 clinicas:** autonomia documentada — baixo risco.
- **Acordo de socios em LTDA medica:** clausulas de tag/drag along + non-compete + saida + sucessao.

## 10. Vedacoes especificas

- **PA-03** — sem opinar conduta clinica.
- **PA-13** — CLT + CC + CDC + Lei 12.842 com identificacao precisa.
- **PA-20** — sem cross-sell para tributacao/trabalhista especifico — slot generico (PJ-vs-CLT do plantonista CLT puro vira `[encaminhar a especialista em direito do trabalho]`).

## 11. Protocolos acionados

- **P1** — Selo (Reforma Trabalhista + STF RE 958.252 + Sum. 331 TST).
- **P3** — memoria de decisao (modelo PJ-PJ x PJ-PF x CLT).
- **P5** — JE comarca + Justica do Trabalho se conversao em vinculo + Arbitragem opcional.
- **P6** — `revisao-final-medica`.

## 12. Localizacao

JE da comarca do estabelecimento ou domicilio do contratado (CC 53). Justica do Trabalho se conversao em vinculo CLT — JT da comarca da prestacao (CF 114 + CLT 651).

## 13. Integracao

**Chamada por:** `medico-master`, `triagem-medica`, `constituicao-sociedade-medica`.

**Entrega para:** minuta + parecer de risco trabalhista -> `revisao-final-medica` -> operador. Cruza com `lgpd-saude`, `credenciamento-plano-saude`.

**Sem esta skill:** contratos genericos que ignoram pejotizacao (Sum. 331 TST), autonomia tecnica (Lei 12.842), responsabilidade compartilhada (Sum. 469 + CDC 14) — exposicao a vinculo CLT + responsabilidade objetiva nao distribuida.
