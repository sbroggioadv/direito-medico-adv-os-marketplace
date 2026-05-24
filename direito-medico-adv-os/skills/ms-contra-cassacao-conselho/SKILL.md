---
name: ms-contra-cassacao-conselho
description: >
  Mandado de seguranca contra ato de Conselho Profissional (CRM/CRO/COFEN/COFFITO/CFF) que aplique cassacao, suspensao do exercicio profissional ou ato analogo lesivo a direito liquido e certo. Foro: Justica Federal (CF art. 109 I + STJ Sum. 105 — autarquia federal). Aplica Lei 12.016/2009 (MS). Teses: violacao do devido processo (CF 5o LV), cerceamento de defesa, ausencia de motivacao adequada (Lei 9.784 art. 50), desproporcionalidade da sancao (CF 5o LIV), prescricao etica (5a — Res. CFM 2.145 art. 32 / Res. CFO 71 art. 35), nulidade por composicao indevida do colegiado, contradicao com decisao penal absolutoria (CC art. 935). Tutela de urgencia para suspender efeitos da cassacao/suspensao (Lei 12.016 art. 7o III). Prazo decadencial 120 dias (Lei 12.016 art. 23). Aciona: MS contra CRM, MS contra CRO, mandado seguranca conselho, cassacao medica, suspensao etica, suspensao preventiva, Sum 105 STJ, Lei 12.016, devido processo PED.
---

# MS CONTRA CASSACAO/SUSPENSAO EM CONSELHO PROFISSIONAL

> Skill **Tier 4** — mandado de seguranca contra ato de Conselho profissional (CRM/CRO/COFEN/COFFITO/CFF) lesivo a direito liquido e certo (cassacao, suspensao, outras sancoes severas). Implementa PA-02, PA-08 (sem critica pessoal a conselheiro), PA-13, PA-19. Acionada por `medico-master`, `defesa-ped-crm`, `defesa-ped-cro`, `suspensao-preventiva-conselho`, `timeline-multiesfera`.

---

## 0. Escopo e acionamento

Impetra MS contra:
- **Cassacao do exercicio profissional** (pena V da Res. CFM 2.145 / Res. CFO 71)
- **Suspensao do exercicio (ate 30 dias)** quando lesiva imediata
- **Suspensao preventiva** durante PED (`suspensao-preventiva-conselho`)
- Outros atos do Conselho com lesao a direito liquido e certo (negativa de registro, cancelamento, censura publica em violacao a sigilo).

Pre-requisito: ato administrativo concreto (decisao do Conselho); prazo decadencial 120d (Lei 12.016 art. 23).

## 1. Posicao na orquestra

- **Chamada por:** `defesa-ped-crm`, `defesa-ped-cro`, `suspensao-preventiva-conselho`, `medico-master`, `timeline-multiesfera`.
- **Aciona:** `validador-legislacao-vigente` (norma do conselho vigente no fato), `revisao-final-medica`.
- **Entrega para:** peticao inicial de MS + pedido liminar -> JF; eventual sustentacao oral no TRF; RE/REsp.

## 2. Marco normativo

| Norma | Conteudo |
|-------|----------|
| **CF art. 5o LXIX** | Mandado de seguranca — direito liquido e certo |
| **CF art. 109 I** | JF competente — autarquias federais |
| **Lei 12.016/2009** | Lei do Mandado de Seguranca |
| Lei 12.016 art. 1o | Cabimento |
| **Lei 12.016 art. 7o III** | Liminar — relevancia + risco de ineficacia |
| Lei 12.016 art. 19 | Recurso de oficio em concessao |
| **Lei 12.016 art. 23** | Prazo decadencial 120d |
| **STJ Sum. 105** | MS contra ato de Conselho profissional (autarquia federal) -> JF |
| CF 5o LIV (devido processo substancial) e LV (formal) | Fundamentos materiais |
| Lei 9.784/99 | Processo administrativo federal — aplicacao subsidiaria |
| Lei 9.784 art. 50 | Motivacao adequada da decisao |
| Lei 9.784 art. 2o | Principios (legalidade, proporcionalidade, motivacao, razoabilidade) |
| Res. CFM 2.145/2016 / Res. CFO 71/2006 | Regulamento do PED + prescricao 5a |
| **CC art. 935** | Independencia relativa — penal alcanca etico se 386 I/III |
| Lei 3.268/57 + 4.324/64 | Cria CRM/CFM e CRO/CFO (autarquias federais) |
| Sum. 14 CFM (proporcionalidade) | Principio aplicavel |

**Jurisprudencia:** STF MS 27.067/DF (cassacao exige fundamentacao + proporcionalidade); STJ MS 11.123/DF (controle judicial e de legalidade, nao de merito etico — `[mas controle de proporcionalidade e admitido]`); STJ AgRg AREsp 1.456.987 (motivacao adequada); STJ Sum. 105.

## 3. Pressupostos do MS

| Elemento | Conteudo |
|----------|----------|
| **Direito liquido e certo** | Comprovavel documentalmente — sem dilacao probatoria |
| **Ato coator** | Decisao do Conselho (cassacao, suspensao, etc.) — concreta |
| **Autoridade coatora** | Presidente do CRM/CRO/COFEN/COFFITO/CFF |
| **Prazo** | 120d do ato (Lei 12.016 art. 23) — decadencial |
| **Foro** | JF da capital UF do Conselho (Sum. 105 STJ) |

## 4. Teses tipicas (cardapio)

| Tese | Fundamento | Acionar |
|------|-----------|---------|
| **Violacao do devido processo formal** | CF 5o LV + Lei 9.784 | Citacao defeituosa; prazo nao concedido; prova negada |
| **Cerceamento de defesa** | CF 5o LV | Recusa de oitiva de testemunhas; impugnacao de perito ignorada |
| **Ausencia de motivacao adequada** | Lei 9.784 art. 50 + STF MS 27.067 | Decisao generica; sem analise da defesa |
| **Desproporcionalidade da sancao** | CF 5o LIV + Sum. 14 CFM + Lei 9.784 art. 2o | Cassacao por fato isolado de baixa gravidade |
| **Prescricao** | Res. CFM 2.145 art. 32 / Res. CFO 71 art. 35 | Fato > 5a; interruptivos verificados |
| **Composicao defeituosa do colegiado** | Lei 9.784 art. 18-21 | Conselheiro impedido/suspeito participou |
| **Contradicao com decisao penal absolutoria 386 I/III** | CC art. 935 | Penal absolveu por inexistencia/autoria -> vincula etico |
| **Atipicidade etica** | CEM/CEO art. especifico | Conduta nao se enquadra |
| **Erro grosseiro na valoracao da prova** | Sum. 7 STJ excepcionada — controle de legalidade | Prova mal apreciada de forma grosseira |
| **Bis in idem** | CF 5o XLVI + LX | Mesma conduta punida 2x em PED diferentes |

Controle judicial e **de legalidade** — nao reexame de merito etico. Mas controle de proporcionalidade, motivacao e devido processo e admitido.

## 5. Liminar (Lei 12.016 art. 7o III)

Cabivel quando:
- **Relevancia da fundamentacao** — tese juridica plausivel (fumus boni iuris)
- **Risco de ineficacia da medida** — perda imediata do meio de vida; sancao publica que destroi reputacao; pacientes em curso sem atendimento

Pedido: suspensao dos efeitos do ato coator ate decisao de merito.

**Importante:** Lei 12.016 art. 7o §2o — vedacao de liminar contra "atos administrativos da autoridade fazendaria" e analogos NAO se aplica a Conselhos (sao autarquias profissionais).

## 6. Esqueleto FIRAC — Peticao inicial MS

```
PETICAO INICIAL — Mandado de Seguranca
EXMO. SR. JUIZ FEDERAL DA ___ VARA FEDERAL DA SECAO JUDICIARIA DE [Capital UF]

[IMPETRANTE], CRM/CRO/COREN/CREFITO/CRF [num/UF], qualificacao,
por {{ADVOGADO_NOME}} OAB/{{OAB_UF}} {{OAB_NUMERO}},
em face de ATO DO PRESIDENTE DO [CRM/CRO/etc.] DE {{UF}}

I — DA TEMPESTIVIDADE — ato coator de [data] — dentro de 120d (Lei 12.016 art. 23)

II — DO CABIMENTO E COMPETENCIA — Sum. 105 STJ + CF art. 109 I

III — DOS FATOS — narrativa do PED + ato coator (referencia CASO.md)

IV — DO DIREITO LIQUIDO E CERTO
  IV.1 Violacao do devido processo (CF 5o LV + Lei 9.784) — [especifica]
  IV.2 Cerceamento de defesa — [especifica]
  IV.3 Ausencia de motivacao adequada (Lei 9.784 art. 50)
  IV.4 Desproporcionalidade da sancao (CF 5o LIV)
  IV.5 Prescricao (Res. CFM 2.145 art. 32 / Res. CFO 71 art. 35)
  IV.6 [Contradicao com decisao penal absolutoria — CC 935 — se aplicavel]

V — DA LIMINAR (Lei 12.016 art. 7o III)
  V.1 Fumus boni iuris — teses acima
  V.2 Periculum in mora — sancao publica que destroi atividade
  V.3 Pedido: suspensao imediata dos efeitos do ato

VI — DOS PEDIDOS
  VI.1 Liminar suspensiva dos efeitos
  VI.2 Notificacao da autoridade coatora (10d para informacoes)
  VI.3 Intimacao do MPF (parecer)
  VI.4 Concessao da seguranca em definitivo — anulacao do ato coator
  VI.5 Citacao do Conselho como litisconsorte (Lei 12.016 art. 7o II)
  VI.6 Honorarios na forma da lei

[Cidade, data] — {{ADVOGADO_NOME}} | OAB/{{OAB_UF}} {{OAB_NUMERO}}

RESSALVA (PA-05).

Anexos: comprovacao OAB ativa; copia do PED; ato coator; ressalva de OAB.
```

## 7. Estrategia processual

1. **Coletar TUDO do PED** — copia integral; ata; voto do relator; ata da sessao; notificacao do ato coator.
2. **Distribuir MS em 120d** — preferencialmente nos primeiros 30d para manter forca de liminar.
3. **Liminar e nuclear** — perder a liminar = sancao em curso ate sentenca (1-2 anos). Investir tudo na liminar.
4. **Coordenar com recurso administrativo CFM/CFO** — vias podem ser simultaneas (nao se exige esgotamento — Sum. 105). Recurso adm com efeito suspensivo + MS na JF = blindagem dupla.
5. **MPF e parecer obrigatorio** — Lei 12.016 art. 12.
6. **Recursos:** Agravo de Instrumento (se nega liminar — TRF) + Apelacao + REsp/RE.

## 8. Casos tipicos

- **Cassacao por fato isolado:** desproporcionalidade — Sum. 14 CFM. Tese forte.
- **Suspensao preventiva sem motivacao concreta:** violacao Lei 9.784 art. 50 + presuncao de inocencia. Tese muito forte.
- **PED prescrito julgado mesmo assim:** Res. CFM 2.145 art. 32 (5a). Tese vencedora se prescricao consumada.
- **Penal absolveu por 386 I (inexistencia) e CRM/CRO insistiu em PED:** CC art. 935 vincula. Tese forte.
- **Conselheiro relator que ja se manifestou publicamente:** suspeicao (Lei 9.784 art. 18). Vicio insanavel.

## 9. Vedacoes especificas

- **PA-02** — sem promessa de procedencia do MS.
- **PA-08** — sem critica pessoal a conselheiro, ao relator, a autoridade coatora. Impugnacao tecnica do ato — nao da pessoa.
- **PA-13** — Lei 12.016 + Lei 9.784 + Res. CFM/CFO com identificacao precisa.
- **PA-19** — prazo decadencial 120d conferido.

## 10. Protocolos acionados

- **P1** — Selo (norma vigente no fato + no ato coator).
- **P3** — memoria de decisao (MS x recurso adm + estrategia liminar).
- **P4** — `timeline-multiesfera` (penal/civel/etico).
- **P5** — JF da capital UF — Sum. 105 STJ.
- **P6** — `revisao-final-medica`.

## 11. Localizacao

JF da capital UF (CF 109 I + Sum. 105 STJ). Recurso: TRF da regiao. RE: STF. REsp: STJ. **Atencao:** o ato coator e do Conselho REGIONAL — foro vai pela sede do Conselho que praticou o ato.

## 12. Integracao

**Chamada por:** `defesa-ped-crm`, `defesa-ped-cro`, `suspensao-preventiva-conselho`, `medico-master`, `timeline-multiesfera`.

**Entrega para:** MS + pedido de liminar -> `revisao-final-medica` -> operador. Cruza com recurso administrativo ao CFM/CFO (paralelo).

**Sem esta skill:** advogado preso so a via administrativa, perdendo a JF como instancia revisora — risco grande de sancao se consolidando enquanto recurso administrativo tramita.
