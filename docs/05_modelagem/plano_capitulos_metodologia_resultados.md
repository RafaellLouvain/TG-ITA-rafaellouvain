# Plano dos capítulos 3 (Metodologia) e 4 (Resultados e Discussões) do TG2

> Alinhado com o Rafael em 2026-10-21. Decisões detalhadas (dados, desbalanceamento, validação, sensibilidade) em
> [protocolo_metodologia](protocolo_metodologia.md). A Conclusão (cap. 5) fica para depois.

## Diretrizes gerais

- Ordem de trabalho e de apresentação: **B → A → C**.
- Narrativa: buscou-se **primeiro a abordagem sugerida no TG1** (C_void como combinação de grupos adimensionais por
  natureza, via Buckingham) e, a partir dos resultados dela, **variações** (índice único A; híbrida C).
- **Modelo B com 2–3 conjuntos de termos (Π), todos com embasamento teórico** nas referências da revisão; cada
  conjunto é validado pelo mesmo protocolo e escolhe-se o melhor. Relacionar cada termo ao máximo com as referências
  (equações e figuras do cap. 2).
- Em cada modelo: acurácia **e** acurácia balanceada (limiar pelos dois critérios) e a sensibilidade correspondente
  ficam **dentro da subseção do próprio modelo** (sem subseções separadas para isso).
- Sem seção de aplicação prática.

## Capítulo 3 — Metodologia

| Seção | Conteúdo | Figuras / tabelas |
|---|---|---|
| 3.1 Visão geral | Etapas do trabalho (dados → tratamento → grupos Π → modelos B, A, C → validação → sensibilidade) | Fluxograma |
| 3.2 Base de dados | Origem (Du et al. 2019 / Kaggle); 108 soldas, 14 estudos, 3 ligas; 43 com vazio e 65 sem | Tabela de variáveis (símbolo, unidade, faixa, natureza) |
| 3.3 Tratamento dos dados | Formato do arquivo; coluna Alloy descartada (liga identificada por α e σ_y quando preciso); conversão para o SI; valores com `*` (marcadores); casos duvidosos (v da ref. 15; linhas 84–89) | Tabela de correções |
| 3.4 Análise dimensional e naturezas | Buckingham: 10 variáveis, 3 dimensões → 7 grupos; 5 naturezas (cinemática, geométrica, térmica, dinâmica, metalúrgica) | Tabela dos Π (expressão, natureza, interpretação, sinal esperado, referência) |
| 3.5 Abordagens de modelagem | 3.5.1 B — lei de potência em grupos Π, com os 2–3 conjuntos de termos e a justificativa teórica de cada um · 3.5.2 A — índice único + limiar · 3.5.3 C — híbrida (núcleo físico + blocos aceitos só se melhorarem a acurácia de teste) | Equações; tabela dos conjuntos de termos |
| 3.6 Calibração e desbalanceamento | Regressão logística em ln Π (B, C) e busca de limiar (A); pesos de classe (com e sem); limiar por acurácia e por acurácia balanceada | – |
| 3.7 Protocolo de validação | Split oficial 78/30 estratificado (semente fixa); 500 splits; CV aninhada; leave-one-study-out; métricas; comparações (classe majoritária, só rotação, Du et al.); declaração da fase exploratória | Esquema dos splits |
| 3.8 Sensibilidade e robustez | B completa; A só limiar + erros; C ordem de entrada dos blocos + tornado final; robustez 1 (sem p e θ) e 2 (sem linhas 84–89) para todos | – |
| 3.9 Ferramentas computacionais | Python (pandas, numpy, scikit-learn, statsmodels, matplotlib); repositório | – |

## Capítulo 4 — Resultados e Discussões

| Seção | Conteúdo |
|---|---|
| 4.1 Caracterização do dataset | Estatísticas descritivas; vazio por estudo e por liga; dentro de cada estudo a rotação decide (figura rotação × estudo) |
| 4.2 Modelo B — grupos adimensionais | Para cada conjunto de termos: expoentes (IC), sinais × tabela de síntese (seção 2.9), acurácia e acurácia balanceada (treino e teste, dois critérios de limiar); escolha do melhor conjunto; **sensibilidade completa** do conjunto escolhido (elasticidades, tornado, retirada de bloco, bootstrap, ranking das 5 naturezas); discussão com as referências |
| 4.3 Modelo A — índice único | Limiar V_crit; acurácia e acurácia balanceada; robustez do limiar; análise dos erros (motiva o C) |
| 4.4 Modelo C — híbrido | Ordem de entrada e ganho de cada bloco (hierarquia); equação final; acurácia e acurácia balanceada; tornado ilustrativo |
| 4.5 Comparação entre modelos e com a literatura | Tabela central: classe majoritária, só rotação, A, B, C × Du et al. (métodos 1–5); split oficial, média de 500 splits, leave-one-study-out; síntese acurácia × acurácia balanceada |
| 4.6 Robustez dos dados | Sem p e θ; sem linhas 84–89 (todos os modelos) |
| 4.7 Análise dos erros e limitações | Onde os modelos erram (refs. 6 × 8; 2219 em rotação baixa); teto de acurácia do dataset |

## Conjuntos de termos do modelo B (revisado 2026-10-21, antes de rodar)

Todos os termos são grupos adimensionais formados só com variáveis do dataset (sem ρ, k, c_p externos). Expoentes livres
(logística em ln Π). Sinais esperados no risco (Tab. de síntese, seção 2.9): ω −, v +, R_s −, t +, p −, θ −, α +,
pino e σ_y incertos.

| Conjunto | Ideia | Termos (Π) | Base teórica |
|---|---|---|---|
| **B1 — Buckingham completo (TG1)** | Os 7 grupos independentes da análise dimensional, um por natureza | ωR_s/v; vR_s/α; p/σ_y; t/R_s; R_pr/R_s; R_pt/R_pr; θ | Fox (Teorema Π); analogia de Reynolds (Du et al.); avanço por rotação (Mishra e Ma). Esperado: sobreajuste (7 termos para 43 vazios) |
| **B2 — térmico (geração e condução de calor)** | Vazio = solda fria: temperatura governada pela taxa de geração de calor do ombro e pela condução | ωR_s²/α (Péclet rotacional); vR_s/α (Péclet de avanço); p/σ_y; t/R_s | Schmidt (Q ∝ τωR_s³) com condução (ΔT ∝ Q/(kR_s) ⇒ ΔT·ρc_p/τ ∝ ωR_s²/α); ωR_s²/α é fator do Q* de Arora et al. (2011); Pe mede o peso do avanço (Pe ≪ 1 no FSW ⇒ regime dominado por condução); p/σ_y = parcela de atrito × adesão (δ de Schmidt); t/R_s = raiz fria |
| **B3 — escoamento / extrusão** | Vazio = material insuficiente transportado/forjado ao redor do pino | ωR_s/v (avanço por rotação); R_pr/R_s; R_pt/R_pr; t/R_pr; p/σ_y | Arbegast (2008, zonas de escoamento, massa crítica ∝ φ = ω/v); Ahmed et al. (2021, razão pino/ombro); Ahmed et al. (2019, pino cônico × paralelo); Threadgill/Bezerra (forjamento) |

θ fica só no B1 (vale só 2 ou 2,5° e é assumido em 71/108 linhas).
