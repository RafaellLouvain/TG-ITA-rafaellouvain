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
| 2026-10-17 | **Fluxo de trabalho do TG final:** redigir o relatório na pasta `TG2/` primeiro; abordagens/análises de resultados serão deliberadas pelo Rafael quando chegar a esse capítulo | Rafael |
| 2026-10-17 | `TG2/TG1_revisado_anotado.tex`: TG1 com texto intacto + marcação colorida dos erros (vermelho = sem fonte, laranja = fonte trocada, azul = impreciso, roxo = falta referência, verde = metodológico) | Rafael |
| 2026-10-19 | Revisão de literatura com 9 subseções (2.1 processo; 2.2 calor/temperatura; 2.3 escoamento; 2.4 microestrutura; 2.5 defeitos/vazio; 2.6 influência dos parâmetros; 2.7 modelagem/predição; 2.8 análise dimensional; 2.9 síntese com tabela de sinais esperados). Sem limite rígido de páginas (> 25 ok). Avaliação de classificadores vai para a Metodologia | Rafael |
| 2026-10-20 | Revisão de literatura 2.1–2.9 redigida no `TG2_relatorio.tex` (cap. 2 = p. 7–34), com caixas vermelhas "INSERIR IMAGEM" indicando figura/página exata (artigos ou slides do TG1; imagens dos slides precisam de fonte original identificada) | Rafael pediu |
| 2026-10-20 | Caixas "INSERIR IMAGEM" viraram `\figura{arquivo}{largura}{legenda}{rótulo}{instrução}`: a figura entra sozinha quando `TG2/Imagens/<arquivo>.png/.jpg/.pdf` existe; senão aparece caixa vermelha. Lista de nomes em `TG2/Imagens/LEIA-ME.md` | Rafael pediu |
| 2026-10-21 | Terminologia: "acurácia fora da amostra" (CV / splits 78/30 repetidos) passa a se chamar **acurácia de teste**; "in-sample" = acurácia de treino | Rafael |
| 2026-10-21 | Metodologia: abordagens na ordem B → A → C; **não usar a coluna Alloy** (α e σ_y mantidos); converter tudo para o SI. Protocolo completo em `05_modelagem/protocolo_metodologia.md` | Rafael |
| 2026-10-21 | Estrutura dos caps. 3 e 4 fechada (resultados por modelo B → A → C; acurácia × balanceada e sensibilidade dentro de cada modelo; sem aplicação prática; B com 2–3 conjuntos de termos com base teórica). Ver `05_modelagem/plano_capitulos_metodologia_resultados.md` | Rafael |
| 2026-10-21 | Códigos e resultados oficiais de A, B, C rodados (`TG2/codigos`, `TG2/resultados`); resumo em `05_modelagem/resultados_2026-10-21.md`. Aguardando alinhamento com o Rafael antes da escrita | Rafael pediu |
| 2026-10-22 | Resultados: métrica principal = média dos 500 splits (split oficial secundário); narrativa B → A → C aprovada (A como C_void recomendado pela simplicidade); C_void com unidade aceito; limiar pelos dois critérios. Ver `05_modelagem/resultados_2026-10-21.md` §4–6 | Rafael |
| 2026-10-22 | TG2 adequado ao modelo de TG do ITA (zip em `referencias/diretrizes/`): Times 12, títulos 18/14/12, legendas com travessão, páginas romanas no pré-textual e arábicas no canto superior direito, referências em espaço simples à esquerda, Abstract incluído. Pendentes do modelo: folha de rosto, folha de aprovação, citações em caixa baixa (NBR 10520:2023), Resumo/Abstract com resultados | Rafael |
| 2026-11-02 | Após comparar com 5 trabalhos do ITA (`referencias/OUTROS TRABALHOS ACADEMICOS DO ITA/`): fonte Computer Modern (Latin Modern) mantendo tamanhos 18/14/12 do modelo; folha de rosto, verso (ficha CIP), folha de aprovação, dedicatória, agradecimentos, epígrafe (textos a escrever) e Lista de Símbolos; legendas "FIGURA/TABELA x.y – Título (AUTOR, ano)." sem "Fonte:"; marcadores do PDF para todos os elementos; *apud* removido (redação natural citando a fonte consultada); "Filho (2018)" passa a ser Cintra (2018), citado diretamente | Rafael |
| 2026-11-02 | Revisão de literatura enxugada de 39 para 26 páginas (redundâncias, citações periféricas e 12 figuras removidas; Tabela 2.1 e Adiga 2024 retirados); backup em scratchpad | Rafael |
| 2026-11-02 | Metodologia/Resultados simplificados (de ~18 para ~8 conceitos): um critério de limiar (acurácia) + limiar conservador de 1,05 m/s só como recomendação industrial; cortados pesos de classe (1 frase), Wilson, seleção aninhada 1a–1c, bootstrap, contribuição/retirada por natureza, L2; hierarquia (2º objetivo) agora por evidências convergentes (Seção 4.6); "split oficial" → "divisão de referência"; validação por estudo < 70% declarada | Rafael |
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

- **2026-11-02 — Ajustes de clareza em Metodologia/Resultados (TG2):** IC do expoente $c$ explicado na Seção 3.8 (bootstrap de 1.000 reamostragens de estudos); coluna "efeito esperado" removida da Tab. 3.2 (remete à Tab. 2.3); $\sigma_8$ e $U$ remetidos à Eq. de Arora; "razão de chances"/"escore" trocados por linguagem simples; "sorteio" = cada uma das 500 divisões aleatórias, "divisão de referência" = a de semente fixa; exemplo numérico de aplicação na Seção 4.3 ($R_s$ = 10 mm); nova Fig. 4.3 (curva logística vs $\omega R_s$, `codigos/r11_figura_logistica.py`). PDF com 66 páginas.
