---
name: perda-de-uma-chance
description: >
  Teoria da perda de uma chance aplicada ao erro medico/odontologico. Aplica STJ REsp 1.291.247/RS (paradigma — 2a Secao), REsp 1.677.083/SP, REsp 1.254.141/PR (oncologia/atraso diagnostico), REsp 1.622.538/MS (obstetricia). Casos tipicos: atraso de diagnostico oncologico, demora na cesarea de urgencia (paralisia cerebral neonatal), atraso no diagnostico de infarto/AVC, demora em diagnostico de sepsis. Calcula percentual de chance perdida sobre prejuizo total (formula: chance% x prejuizo_integral). Diferencia perda de chance de dano consumado e de dano hipotetico. Conservadorismo (PA-21) na arbitragem. Aciona: perda de uma chance, perda de chance, REsp 1.291.247, atraso diagnostico oncologia, paralisia cerebral neonatal, demora cesarea, atraso AVC, atraso infarto, chance de sobrevida, chance de cura.
---

# PERDA DE UMA CHANCE

> Skill **Tier 2** — teoria da perda de uma chance no direito medico. Implementa PA-13 (citacao precisa), PA-15 (regime), PA-21 (conservadorismo no quantum). Acionada por `responsabilidade-civil-medica`, `cirurgia-estetica-resultado`, `responsabilidade-odontologica`, em casos com nexo causal **probabilistico** (nao determinístico).

---

## 0. Escopo e acionamento

Acionada quando o caso envolve **chance perdida de cura ou sobrevida** — nao o dano consumado direto. Casos tipicos: atraso diagnostico oncologico (paciente teria X% de sobrevida em 5 anos com diagnostico precoce), demora em cesarea de urgencia (chance de neonato sem sequela), atraso em diagnostico de AVC/infarto, demora em tratamento de sepsis. **A perda de chance e** **dano autonomo** **— nao identificavel com o dano final**.

## 1. Posicao na orquestra

- **Chamada por:** `medico-master`, `responsabilidade-civil-medica`, `analise-pericia-medica` (quesitos), `triagem-medica`.
- **Aciona:** `analise-pericia-medica` para formular quesitos especificos (qual era a chance? em que faixa de tempo? a literatura confirma?), `prescricao-erro-medico`, `revisao-final-medica`.
- **Entrega para:** tese e calculo de quantum por perda de chance, anexada a peca de `responsabilidade-civil-medica`.

## 2. Marco normativo e teorico

| Norma/precedente | Conteudo |
|------------------|----------|
| CC art. 186, 187, 927 | Bases gerais — ato ilicito, abuso, indenizacao |
| CC art. 944 | Indenizacao mede-se pela extensao do dano |
| **STJ REsp 1.291.247/RS (2a Secao, 2014)** | **Paradigma**: teoria da perda de uma chance reconhecida em direito medico |
| STJ REsp 1.677.083/SP | Aplicacao — calculo do percentual |
| STJ REsp 1.254.141/PR | Oncologia — atraso diagnostico que reduziu chance de sobrevida |
| STJ REsp 1.622.538/MS | Obstetricia — chance de neonato sem sequela |
| STJ Tema 1.094/1.095 | Limites de revisao do quantum em STJ |
| Doutrina (Sergio Cavalieri Filho; Rafael Pacheco Lanes Ribeiro) | Teoria da perda da chance — origem francesa |

## 3. Pressupostos da teoria

1. **Chance real e seria** — nao mera possibilidade. Probabilidade quantificavel pela literatura medica/estatistica.
2. **Conduta ilicita** — erro/omissao/atraso medico documentado.
3. **Nexo causal entre conduta e perda da chance** — nao com o dano final, mas com a **perda da oportunidade**.
4. **Quantificacao** — percentual de chance perdida x prejuizo total que adviria se a chance se concretizasse.

## 4. Diferenciacao critica

| Conceito | Definicao | Aplicacao |
|----------|-----------|-----------|
| **Dano consumado** | Dano direto da conduta — nexo causal determinístico | Indenizacao integral (CC art. 944) |
| **Perda de uma chance** | Chance de evitar dano/obter beneficio perdida pela conduta — nexo probabilistico | Percentual de chance x dano hipotetico |
| **Dano hipotetico** | Dano que nao aconteceu nem teve chance perdida | **Indenizavel? NAO** — pressuposto: chance real e seria |

**Erro frequente:** confundir perda de chance com dano consumado e pedir indenizacao integral em vez do percentual. STJ corta.

## 5. Casos tipicos e percentuais de referencia

| Caso tipico | Conduta | Chance perdida tipica |
|-------------|---------|-----------------------|
| Atraso diagnostico cancer mama (4 meses) | Mamografia mal-lida ou pedida tardiamente | Reducao de 30-50% na sobrevida em 5 anos (depende do tipo e estadio) — `[VERIFICAR — literatura SBOC]` |
| Demora em cesarea de urgencia (sofrimento fetal prolongado) | Decisao tardia diante de CTG alterada | 40-70% chance de neonato sem paralisia cerebral — `[VERIFICAR — literatura FEBRASGO]` |
| Atraso em diagnostico de infarto/AVC | Triagem inadequada, ECG nao realizado | 30-60% chance de sobrevida ou recuperacao funcional |
| Demora em diagnostico de sepsis | Sintomas mal-interpretados | 40-70% chance de sobrevida (cada hora conta) |
| Erro odontologico em endodontia que leva a perda dental | Tecnica inadequada | 50-80% chance de manter o dente |

**Percentuais sao referencias** — caso concreto exige laudo pericial com fundamentacao em literatura especifica.

## 6. Quantificacao (formula)

```
INDENIZACAO POR PERDA DE CHANCE = % chance perdida x R$ dano integral hipotetico
```

**Exemplo (atraso diagnostico cancer):**
- Chance perdida (laudo pericial): 35%
- Dano integral hipotetico (se diagnostico precoce, sobrevida): R$ 200.000 (pensao 5 anos + dano moral)
- Indenizacao por perda de chance: 35% x R$ 200.000 = R$ 70.000

**Exemplo (obstetricia, paralisia cerebral):**
- Chance perdida (laudo): 50%
- Dano integral hipotetico (sequela vitalícia, cuidador, pensao, dano moral): R$ 600.000
- Indenizacao por perda de chance: 50% x R$ 600.000 = R$ 300.000

> **PA-21 conservadorismo:** percentual ancorado em laudo pericial + literatura. Sem percentual = quantum nao calculavel.

## 7. Esqueleto FIRAC — Peca civel por perda de chance

```
[Estrutura de peca de `responsabilidade-civil-medica`, com adaptacao]

III — DIREITO
III.3 — Teoria da perda de uma chance (CC arts. 186, 927 + STJ REsp 1.291.247/RS)
       - A demora de [N] dias/meses no diagnostico/conduta reduziu a chance
         de [cura/sobrevida/recuperacao funcional] em [%] (laudo pericial)
       - Nexo causal entre a conduta e a perda da chance (nao com o dano final)
III.5 — Quantum
       - Dano integral hipotetico: R$ X (CC arts. 948-950 + dano moral)
       - Chance perdida (laudo pericial): % Y
       - Indenizacao por perda de chance: % Y x R$ X = R$ Z
       - Cumulada com dano material direto (despesas) e dano moral autonomo
```

## 8. Quesitos para a pericia (P2 + insumo `analise-pericia-medica`)

1. Qual era a probabilidade estatistica de [cura/sobrevida/recuperacao] caso o diagnostico/conduta correta tivesse sido prestada no momento adequado?
2. A literatura medica vigente no ano do fato (PA-09) confirma esse percentual? Em qual diretriz/sociedade medica?
3. A demora/conduta erronea reduziu essa chance? Em quanto?
4. O resultado adverso final (dano consumado) e atribuivel exclusivamente a perda da chance ou ha outras causas concorrentes (doenca de base, falibilidade)?
5. Qual a faixa temporal critica em que a conduta correta ainda teria preservado a chance?

## 9. Vedacoes especificas

- **PA-02** — vedada promessa de procedencia (chance e probabilidade, nao certeza).
- **PA-03** — nao opinar sobre chance — quem opina e o perito ancorado em literatura.
- **PA-13** — STJ REsp 1.291.247/RS sempre citado como paradigma.
- **PA-21** — quantum conservador, sem inflar percentual nem dano integral.
- **PA-11** — literatura medica em atualizacao -> `[VERIFICAR]`.

## 10. Protocolos acionados

- **P1** — Selo emitido.
- **P2** — pericia medica como prova nuclear (a chance e quantificada pelo perito).
- **P3** — memoria de quantum com formula explicita (% x R$ hipotetico).
- **P6** — revisao R1-R4.

## 11. Localizacao

Foro: JE comarca conforme `responsabilidade-civil-medica`. Sem peculiaridade local na teoria.

## 12. Integracao

**Chamada por:** `responsabilidade-civil-medica`, `cirurgia-estetica-resultado`, `responsabilidade-odontologica`, `triagem-medica` em casos de atraso/omissao/demora.

**Entrega para:** secao III.3 do FIRAC da peca de `responsabilidade-civil-medica` + quesitos para `analise-pericia-medica` + calculo de quantum.

**Sem esta skill:** caso de atraso diagnostico/demora e pleiteado como dano consumado (indenizacao integral) -> STJ converte em improcedente ou reduz drasticamente. A teoria da perda de chance e tese estruturante quando o nexo e probabilistico.
