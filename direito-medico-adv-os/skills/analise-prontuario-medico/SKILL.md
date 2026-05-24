---
name: analise-prontuario-medico
description: >
  Leitura juridica probatoria do prontuario medico (Res. CFM 1.821/2007 + LGPD art. 11 + art. 154 CP) — NUNCA emite juizo clinico (PA-03), apenas mapa de risco probatorio. Identifica lacunas (folha em branco em dia critico, evolucao faltante, ausencia de TCLE em procedimento invasivo), rasuras sem ressalva, contradicoes intra-documentais, atestados/laudos fora de ordem, identificacao incompleta do profissional. Aplica o Protocolo 2 (integridade documental) sobre o prontuario. Aciona: prontuario medico, analise de prontuario, lacuna em prontuario, rasura, ausencia de TCLE, evolucao medica, sumario de alta, perda probatoria, falha de documentacao, Res. CFM 1.821, sigilo medico em prontuario.
---

# ANALISE DE PRONTUARIO MEDICO

> Skill **Tier 1** — leitura juridica probatoria do prontuario. Implementa PA-03 (sem juizo clinico), PA-16 (sigilo + LGPD), PA-17 (informacao na medida da defesa), Protocolo 2 (integridade documental). Acionada por `medico-master`, `triagem-medica` ou diretamente quando ha prontuario no caso.

---

## 0. Escopo e acionamento

Acionada quando o caso envolve prontuario medico/odontologico como prova — defesa em PED CRM/CRO, ação de erro medico (autor ou reu), defesa criminal, perícia. **Nao opina sobre conduta clinica (PA-03)** — apenas mapeia o que o prontuario prova juridicamente, que lacunas existem (peso probatorio), que contradicoes podem ser exploradas pela contraparte ou pela defesa.

## 1. Posicao na orquestra

- **Chamada por:** `medico-master`, `triagem-medica`, `responsabilidade-civil-medica`, `defesa-culpa-medica-criminal`, `defesa-ped-crm`, `defesa-ped-cro`, `analise-pericia-medica`.
- **Entrega para:** mapa de risco probatorio adicionado ao `CASO.md`; insumo para `analise-pericia-medica`, `defesa-ped-crm`, `responsabilidade-civil-medica`.
- **Dependencia:** Selo P1 emitido (PA-04).

## 2. Marco normativo do prontuario

| Norma | Disciplina |
|-------|------------|
| Res. CFM 1.821/2007 | Manual operacional do prontuario — guarda 20 anos da ultima entrada, registros legiveis, lancamento por profissional identificado |
| Res. CFO 118/2012 (CEO) | Prontuario odontologico — analogo ao medico |
| Lei 13.787/2018 | Digitalizacao de prontuarios e dispensa de impressao |
| Lei 13.709/2018 (LGPD) art. 11 | Dado de saude e dado sensivel — tratamento condicionado a base legal especifica |
| DL 2.848/1940 art. 154 CP | Violacao de sigilo profissional |
| CC art. 388 (revogado) / CPC art. 388 | Sigilo profissional oponivel em juizo |
| Lei 15.378/2026 | Estatuto dos Direitos do Paciente — direito ao prontuario, copia, informacao |

## 3. Checklist de integridade (P2)

### 3.1 — Completude e cronologia
- **Anamnese inicial** — historia clinica, queixa, antecedentes. Ausencia ou superficialidade = fragilidade probatoria.
- **Exame fisico inicial** — sinais vitais, exame segmentar. Lacuna em paciente grave (UTI/PA) e ponto de explorabilidade.
- **Hipotese diagnostica e plano** — registrados? Mudancas justificadas?
- **Evolucao diaria** (internado) ou **por atendimento** (ambulatorial) — sequencia cronologica completa? Dia critico (cirurgia, intercorrencia) registrado?
- **Conduta** — prescricao, procedimentos, alteracoes terapeuticas registrados na evolucao?
- **Sumario de alta** — diagnostico final, conduta no internamento, conduta apos alta. Ausencia = perda probatoria grave.

### 3.2 — Identificacao
- **Paciente** — nome, prontuario, dados completos.
- **Profissional assistente em cada lancamento** — nome + CRM/UF (ou CRO/UF) + assinatura ou carimbo. **Lançamento anonimo = fragilidade.**
- **Data e horario de cada lancamento** — registrados? Sequencia logica?

### 3.3 — Rasuras, contradicoes, lancamentos posteriores
- **Rasura sem ressalva** — Res. CFM 1.821/2007 exige ressalva e contra-assinatura. Rasura nao ressalvada e ponto exploravel.
- **Lancamento extemporaneo** (escrito apos o evento, em ordem fora de sequencia) — indicado como "registro retrospectivo"?
- **Contradicao intra-prontuario** — divergencia entre evolucao de dias distintos, ou entre evolucao e sumario.
- **Divergencia prontuario x laudo de exame x prescricao** — mapear todas.

### 3.4 — TCLE anexado
- TCLE presente para procedimento que exige (cirurgia, anestesia, oncologia, reproducao assistida, telemedicina, estetica, transfusao, procedimento invasivo)?
- Data anterior ao procedimento?
- Especificidade do procedimento (nao TCLE generico)?
- Assinatura paciente + medico + testemunha quando aplicavel?

Detalhamento de TCLE -> skill `analise-tcle` (acionar em paralelo).

### 3.5 — Assinatura digital e prontuario eletronico (PEP)
- PEP certificado SBIS-CFM? (Res. CFM 1.821/2007 Anexo II)
- Assinatura digital ICP-Brasil?
- Log de acesso disponivel? (sinaliza modificacao posterior)

## 4. Mapa de risco probatorio (output da skill)

```
MAPA DE RISCO PROBATORIO — Caso <slug>
Data da analise: <DD/MM/AAAA>

## Documentos analisados
- prontuario.pdf (paginas: <N>)
- exames anexos: <lista>
- TCLE: <presente | ausente | parcial>

## Pontos fortes do prontuario (PRO defesa do medico/clinica)
- [Lista de itens corretamente documentados]

## Pontos fragmentes / lacunas (PRO autor — explorabilidade pela contraparte)
1. <Lacuna>: <descricao> — <onde no prontuario> — <perspectiva juridica probatoria>
2. ...

## Rasuras e contradicoes
| Local (pagina/data) | Tipo (rasura/contradicao/extemporaneo) | Explorabilidade |

## Ausencias criticas
- TCLE ausente em procedimento invasivo: <sim/nao>
- Sumario de alta ausente: <sim/nao>
- Evolucao faltante em dia critico (<data>): <sim/nao>

## Recomendacoes ao operador (defesa)
- [VERIFICAR] obter PEP completo / log de acesso / 2a via
- Quesitos a formular para o perito (ver analise-pericia-medica)
- Pontos a antecipar na contestacao / razoes

## Recomendacoes ao operador (autor)
- Quesitos a formular para o perito
- Provas adicionais a requerer (ex.: depoimento de testemunhas, perícia tecnica em laudo)

## Lembrete PA-03
Esta analise NAO opina sobre adequacao tecnico-clinica da conduta — esse juizo cabe ao perito medico ou ao assistente tecnico (CPC arts. 466-480 / CPP art. 159). A skill aponta peso probatorio juridico do documento.
```

## 5. Padroes recorrentes (top 10 — referencia para o operador)

1. **Prontuario de PA/emergencia ralo** — comum; aponta dificuldade da defesa em demonstrar evolucao.
2. **Ausencia de TCLE em estetica** — fragilidade absoluta (obrigacao de resultado — STJ REsp 1.526.466).
3. **Sumario de alta superficial** — sem orientacoes pos-alta, dificulta defesa em demanda por nao-seguimento.
4. **Prescricao manuscrita ilegivel** — Res. CFM 1.821/2007 exige legibilidade.
5. **Lancamento "passei plantao sem intercorrencias"** sem registro de exame fisico — fragilidade em caso com intercorrencia.
6. **Atestado/laudo sem CRM** ou CRM rasurado — questionavel em sede de PED.
7. **Prontuario eletronico sem certificacao SBIS-CFM** — peso probatorio reduzido.
8. **Cirurgia sem descricao cirurgica detalhada** — Res. CFM 1.821 art. 5o exige.
9. **Telemedicina sem TCLE digital** (pos-Lei 14.510/2022 + Res. CFM 2.314/2022) — fragilidade.
10. **Prontuario com lancamento extemporaneo nao identificado** — Res. CFM 1.821 art. 3o exige indicacao de registro retrospectivo.

## 6. Vedacoes especificas

- **PA-03** — JAMAIS opinar se a conduta clinica foi adequada ou inadequada. Apenas mapeia o documento.
- **PA-16** — prontuario fica em `<cwd>/direito-medico/casos/<slug>/arquivos/` (gitignored). Conteudo clinico NUNCA persistido em CASO.md (apenas refencia).
- **PA-17** — compartilha informacao clinica entre skills so na medida da defesa. Em peca publica (peticao, defesa em PED), redacao preserva o sigilo no possivel.
- **PA-22** — vedado misturar prontuarios de pacientes diferentes na mesma rodada.
- **PA-08** — sem critica pessoal ao medico-cliente nem ao colega que documentou. Articulacao tecnica.

## 7. Protocolos acionados

- **P2 — Conferencia de Integridade Documental** (esta skill executa).
- **P5 — Localizacao** — UF de inscricao do medico assistente, eixo do CRM regional.

## 8. Localizacao

A UF de inscricao do medico que lancou o prontuario importa para: (a) competencia do PED — CRM da UF de inscricao; (b) eventuais peculiaridades de estatuto regional sobre prontuario (raras, mas existem). Sinalizar quando relevante.

## 9. Integracao

**Chamada por:** `medico-master`, `triagem-medica`, todas as skills de Tier 2-4 que se apoiam em prontuario.

**Entrega para:** mapa de risco probatorio anexado ao `CASO.md`; insumo direto para `analise-pericia-medica`, `defesa-ped-crm`, `defesa-ped-cro`, `responsabilidade-civil-medica`, `defesa-culpa-medica-criminal`.

**Sem esta skill:** defesa/ataque sobre prontuario opera no escuro — perde-se forca probatoria e expoe-se a impugnacao da contraparte.
