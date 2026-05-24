---
name: timeline-multiesfera
description: >
  Skill ancora do Protocolo 4 — articulacao integrada das esferas civel + criminal + etico-disciplinar (CRM/CRO) + regulatorio (ANS/ANVISA) quando o mesmo caso aciona 2 ou mais simultaneamente. Mapeia linha do tempo de cada esfera, prazos prescricionais distintos (CC art. 206 §3o V vs CDC art. 27 vs CP arts. 109-110 vs Res. CFM 2.145/2016), prejudicialidades (CC art. 935 — coisa julgada penal alcanca civel/etico em hipoteses especificas), aproveitamento defensivo cruzado de provas/teses (perícia, prontuario, depoimento). Aplica STJ AgInt no AREsp 1.245.831/MG e independencia relativa (PA-12). Aciona: caso multi-frente, multi-esfera, civel e criminal e PED, parto distocico, erro medico grave, cruzamento de esferas, CC art. 935, independencia das instancias, prejudicialidade, aproveitamento de prova.
---

# TIMELINE MULTI-ESFERA

> Skill **Tier 1 transversal** — ancora do Protocolo 4. Implementa PA-12 (independencia relativa das instancias), PA-13 (norma+jurisprudencia precisas). Acionada por `medico-master`, `triagem-medica` quando ha 2+ esferas, e por skills de Tier 2-4 que operam em paralelo.

---

## 0. Escopo e acionamento

Acionada quando a triagem 4D identifica **2 ou mais esferas** simultaneas (civel + criminal + etico + regulatorio). Funcoes: (a) mapear linha do tempo de cada esfera; (b) calcular prazos prescricionais distintos; (c) identificar prejudicialidades (CC art. 935); (d) priorizar estrategia entre as esferas; (e) operacionalizar aproveitamento defensivo cruzado de provas/teses. **Premissa nuclear (P4):** o advogado da saude nao escolhe entre esferas — recebe as 3 simultaneas quando ha erro grave; gestao integrada e tecnica nuclear.

## 1. Posicao na orquestra

- **Chamada por:** `medico-master`, `triagem-medica` (sinalizando 2+ esferas), `responsabilidade-civil-medica`, `defesa-culpa-medica-criminal`, `defesa-ped-crm`, `defesa-ped-cro`.
- **Entrega para:** secao `Timeline multi-esfera` no `CASO.md`; estrategia priorizada anexada; insumo direto para todas as skills das esferas envolvidas.
- **Pre-requisito:** triagem 4D feita; Selo P1 emitido.

## 2. Marco normativo da independencia relativa

| Norma | Conteudo |
|-------|----------|
| CC art. 935 | Independencia: responsabilidade civil e independente da criminal, MAS nao se pode questionar mais sobre existencia do fato ou autoria quando decididas no juizo criminal |
| CC art. 200 | Prescricao da pretensao civil decorrente de ato apurado em criminal nao corre antes do transito em julgado da sentenca criminal |
| CPP art. 64 | Acao civil ex delicto pode prosseguir independentemente da criminal |
| CPP art. 66 | Suspensao facultativa do civel pelo penal — pode ser pedida |
| CPP art. 386 | Hipoteses de absolvicao penal — algumas alcancam civel, outras nao (ver secao 3) |
| CP art. 91 I | Efeitos da condenacao penal — vincula civel |
| STJ AgInt no AREsp 1.245.831/MG | Independencia relativa — aproveitamento cruzado |
| STJ Sum. 17 | Sentenca penal absolutoria por falta de provas nao impede acao civil |

## 3. Hipoteses do art. 386 CPP (mapa de alcance penal -> civel/etico)

| Hipotese CPP art. 386 | Inciso | Alcanca civel/etico? |
|-----------------------|--------|----------------------|
| Inexistencia do fato | I | **SIM** — civel/etico inviabilizados (CC art. 935) |
| Fato nao constitui infracao penal | III | Parcialmente — depende: se a conduta nao e tipica penal mas pode ser ilicita civil, civel prossegue |
| Nao ser autor o reu | IV | **SIM** — civel/etico contra esse reu inviabilizados |
| Insuficiencia de prova de autoria | V | **NAO** — civel/etico podem prosseguir (Sum. 17 STJ) |
| Existir excludente de ilicitude/culpabilidade | VI | Parcialmente: legitima defesa absoluta protege civel; insuficiencia de prova de dolo nao |
| Insuficiencia de prova para condenar | VII | **NAO** — civel/etico podem prosseguir |

**Implicacao estrategica:** quando ha risco penal, prioriza-se obter **absolvicao por inexistencia ou negativa de autoria** (incisos I e IV) — porque protege civel e PED. Absolvicao por insuficiencia de prova (V e VII) e fragil para o civel.

## 4. Esfera Penal x Etico-disciplinar

- **Independencia relativa tambem** — absolvicao penal por inexistencia/negativa de autoria impede sancao etica pela mesma materia.
- Absolvicao penal por insuficiencia de prova **NAO** inviabiliza PED.
- O PED pode prosseguir antes do transito em julgado da acao penal — mas o conselho costuma aguardar quando ha prejudicialidade evidente (Res. CFM 2.145/2016 art. 33 — suspensao a criterio do conselho).
- Condenacao penal transitada -> efeito vinculante em PED quanto a existencia do fato e autoria (CC art. 935 + analogia).

## 5. Esfera Civel x Etico-disciplinar

- O CRM/CRO **nao esta vinculado** a decisao civel — pode aplicar sancao etica mesmo com civel improcedente. E vice-versa.
- O acervo probatorio de uma esfera (laudo pericial, prontuario, depoimentos) e **compartilhado entre as 3** — gestao integrada (CC art. 372 — direito comum das provas).
- Acordo civel **nao extingue** PED automaticamente; conselho pode prosseguir (interesse publico — defesa da etica profissional).

## 6. Esfera Regulatoria (ANS/ANVISA) x outras

- Autuacao **ANS** contra operadora pode embasar acao civel do beneficiario (negativa abusiva documentada).
- Autuacao **ANVISA** contra estabelecimento de saude pode embasar acao civel por evento adverso (RDC 36/2013 — protocolo de seguranca do paciente).
- Autuacao **vigilancia sanitaria municipal** contra clinica pode embasar PED do(s) responsavel(eis) tecnico(s).

## 7. Tabela de prazos prescricionais por esfera

| Esfera | Acao | Prazo | Fundamento | Termo inicial |
|--------|------|-------|-----------|---------------|
| Civel | Erro medico vs medico-PF (sem vinculo consumerista) | 3 anos | CC art. 206 §3o V | Actio nata (Sum. 278 STJ) — ciencia inequivoca do dano |
| Civel | Erro medico vs hospital/clinica/operadora (consumerista) | 5 anos | CDC art. 27 | Mesmo |
| Civel | Negativa de cobertura plano | 5 anos | CDC art. 27 | Negativa documentada |
| Civel | Pretensao decorrente de ato criminal | Suspensa pelo penal | CC art. 200 | Transito em julgado criminal |
| Criminal | Lesao corporal culposa (art. 129§6o CP) | 4 anos | CP art. 109 V | Cessacao do dano permanente (continuada) ou crime instantaneo |
| Criminal | Homicidio culposo (art. 121§3o CP) | 12 anos | CP art. 109 III | Data do obito |
| Criminal | Omissao de socorro (art. 135 CP) | 4 anos | CP art. 109 V | Data da omissao |
| Criminal | Violacao de sigilo (art. 154 CP) | 4 anos | CP art. 109 V + |
| Criminal | Falsidade ideologica (art. 299 CP) | 12 anos | CP art. 109 III | Data da falsificacao |
| PED CRM | Apuracao etica | 5 anos | Res. CFM 2.145/2016 art. 19 | Data do fato |
| PED CRO | Apuracao etica | 5 anos | Res. CFO 71/2006 | Data do fato |
| Administrativo ANS | Apuracao | 5 anos | Lei 9.873/1999 | Data do fato |

> **PA-19** — prazo prescricional sempre conferido e fundamentado.

## 8. Aproveitamento defensivo cruzado

| Origem | Aproveitamento |
|--------|----------------|
| Laudo pericial do **civel** | Util na criminal (assistente tecnico apresenta como ja produzido) e em PED (anexar a defesa em CRM/CRO) |
| Pericia IML do **criminal** | Util no civel (peca anexa); util em PED como prova publica |
| Documentos juntados em **PED** (defesa, prontuario, certidoes) | Anexos em civel e criminal |
| Depoimento de testemunha em **uma esfera** | Pode ser convertido em prova emprestada (CPC art. 372) com contraditorio |
| Diretriz/sumula de **sociedade medica** ou da AMB | Insumo em todas as 3 esferas |
| Sentenca civel transitada | Sem efeito vinculante automatico na criminal/PED, mas e elemento contextual |

## 9. Estrategia priorizada (quando 2+ esferas)

Roteiro de decisao:

1. **Se ha risco penal grave (obito, lesao grave)** — prioridade: defesa criminal com foco em absolvicao por inexistencia/autoria (art. 386 I/IV CPP).
2. **Se PED esta em prazo apertado de defesa previa (15 dias — Res. CFM 2.145/2016)** — prioridade temporal: defesa-ped-crm/cro tem que sair primeiro.
3. **Se civel ja foi proposto e instrucao avanca** — assegurar pericia robusta (assistente tecnico) — produz laudo aproveitavel nas outras esferas.
4. **Se ha tutela de urgencia pendente (PED com suspensao preventiva ou MS contra cassacao)** — prioridade absoluta: skill `suspensao-preventiva-conselho` ou `ms-contra-cassacao-conselho`.
5. **Coordenar:** todas as pecas das 3 esferas devem coerencia narrativa — divergencia entre versoes ataca o cliente.

## 10. Estrutura do bloco timeline no CASO.md

```
## Timeline multi-esfera (P4)
| Esfera | Fase atual | Data marco | Prazo proximo | Prejudicialidade | Aproveitamento |
|--------|-----------|-----------|---------------|------------------|----------------|
| Civel  | Contestacao em curso | <data> | <prazo> | Aguarda pericia | Pericia oficial sera util em criminal/PED |
| Criminal | IP em curso | <data> | <prazo> | Aguarda IML | Defende-se nos atos investigativos |
| PED CRM | Defesa previa pendente | <data> | 15d <data> | — | Prazo MAIS curto, sair primeiro |
| Regulatorio | — | — | — | — | — |

## Estrategia priorizada
- Prioridade 1: <esfera> — <razao>
- Prioridade 2: <esfera>
- Coordenacao: <pontos de coerencia narrativa>

## Aproveitamento cruzado planejado
- Pericia civel -> assistente tecnico defendendo no IP penal e juntada em PED
- Laudo IML -> juntada em civel apos producao
- Sentenca penal de absolvicao (I ou IV CPP art. 386) -> bloqueia civel/PED por CC art. 935
```

## 11. Vedacoes especificas

- **PA-12** — independencia relativa: nem cadeia automatica nem compartimentos estanques.
- **PA-13** — toda afirmacao com norma+artigo+ano (CC art. 935, CPP art. 386 I/IV, CP arts. 109-110, Res. CFM 2.145/2016).
- **PA-19** — prazo prescricional especifico por esfera, sempre fundamentado.
- **PA-22** — vedada mistura de casos no mesmo timeline.

## 12. Protocolos acionados

- **P4 — Cruzamento Multi-esfera** (esta skill **e** a ancora).
- **P5 — Localizacao** — cada esfera tem foro proprio (JF para MS conselho; JE para civel/criminal; administrativo CRM-UF para PED).

## 13. Localizacao

Cada esfera roteia para foro proprio:
- Civel/criminal -> JE comarca (do dano civel-consumerista; do lugar da infracao penal).
- PED CRM/CRO -> Conselho Regional da UF de inscricao.
- MS conselho -> JF.
- Regulatorio ANS -> federal.

## 14. Integracao

**Chamada por:** `medico-master`, `triagem-medica` (sinaliza 2+ esferas), todas as skills de Tier 2-4 em caso multi-frente.

**Entrega para:** bloco timeline + estrategia priorizada + aproveitamento cruzado -> `CASO.md` + insumo para todas as skills das esferas envolvidas.

**Sem esta skill:** caso multi-frente perde coerencia, prazos se perdem entre esferas, prova produzida em uma esfera nao aproveita as outras — perda estrategica massiva.
