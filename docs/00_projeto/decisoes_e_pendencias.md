# Decisões tomadas e pendências

Atualizar este arquivo sempre que algo for decidido com o Rafael. Datas em AAAA-MM-DD.

## Decisões já tomadas (pelo Rafael, durante o TG1)

| Data aprox. | Decisão | Origem |
|---|---|---|
| 2026 (1º sem.) | Sem experimentos; usar dados secundários | chat Gemini p. 6 |
| 2026 (1º sem.) | Base de dados = Kaggle / Du et al. (2019), 108 ensaios | chat p. 19–43 |
| 2026 (1º sem.) | Abordagem = **equação analítico-fenomenológica (C_void)** calibrada, **não** benchmark de ML | chat p. 43; feedback "reduzir protagonismo de ML" p. 48 |
| 2026 (1º sem.) | Split **78 treino / 30 teste**, como Du et al.; limiar T | relatório TG1 §3 |
| 2026 (1º sem.) | **Meta: ≥ 70 % de acurácia** em teste cego ("Du alcançou 83,33 %; façamos 70 %") | chat p. 73 |
| 2026 (1º sem.) | Objetivo adicional: hierarquia de sensibilidade por natureza (geom./cin./térm./din.) | relatório + slide 10 |
| 2026 (1º sem.) | Título = o da ficha aprovada | relatório TG1 |
| 2026-10-12 | Documentação do projeto em `docs/` (markdown), organizada por tema | pedido do Rafael |
| 2026-10-12 | Dados e PDFs do workspace conferidos com Downloads do Windows (MD5 idênticos, nada corrompido) | pedido do Rafael |
| 2026-10-12 | Análises exploratórias feitas (não oficiais) — ver `05_modelagem/analises_exploratorias_2026-10-12.md` | pedido do Rafael |

## Pendências / decisões a tomar (sugeridas pelo assistente)

- [ ] **Discutir os resultados exploratórios**: candidato principal ω·R_s (velocidade na borda do ombro, limiar
      ≈ 0,86 m/s, ~73 % fora da amostra) e ω·R_s·(p/σ_y)^0,5 (~75 %); bloco térmico (α, v, t) sem ganho robusto.
      Decidir se o C_void pode ter unidade (m/s) + limiar, ou se precisa normalizar por uma velocidade de referência.
- [ ] **Forma final do C_void** — sugestão: lei de potência em Π's adimensionais calibrada por regressão logística
      (une as versões aditiva e multiplicativa do TG1). Ver [proposta_modelagem](../05_modelagem/proposta_modelagem.md).
- [ ] **Quais Π's** (e se inclui índice térmico tipo T/T_m de Arbegast–Hartley ou Roy–Nandan–DebRoy).
- [ ] Usar a **correção da coluna Alloy** por α/σ_y (recomendado) e declarar no texto.
- [ ] Tratar `*` (p e θ assumidos): manter, remover ou testar ambos.
- [ ] Reportar **baselines** (60,2 % majoritária; melhor variável única) e validação **leave-one-study-out**.
- [ ] Rever a meta (70 % formal; mirar ~80 %?) — decisão do Rafael/orientador.
- [ ] Corrigir no texto final todos os itens de [erros_e_correcoes_tg1](../03_tg1/erros_e_correcoes_tg1.md).
- [ ] Obter PDFs prioritários: Threadgill 2009; Arbegast 2008; Arora/DebRoy/Bhadeshia 2011; Roy/Nandan/DebRoy 2006;
      Qian 2013; Kim 2006; Schmidt/Hattel/Wert 2004 (ver [indice_referencias](../02_referencias/indice_referencias.md)).
- [ ] Obter a **classe LaTeX oficial do ITA** (Ângelo/orientador) e migrar o texto; criar `referencias.bib`.
- [ ] Confirmar nome completo do orientador e se há coorientador; datas oficiais de entrega/defesa do TG2.
- [ ] Recuperar imagens do Overleaf (`Imagens/ita-logo.png`, figura de Du et al.) para o repositório, se quiser
      versionar o LaTeX aqui.
- [ ] Remover PDF duplicado `referencias/s11665-023-08671-1 (1).pdf` (= Laska) e os `*:Zone.Identifier` (lixo do
      Windows) — só com autorização do Rafael.
- [ ] Verificar ref. 15 do dataset (Balasubramanian 2008): v de 508–1068 mm/min parece erro de unidade.
