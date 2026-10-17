# Proposta de modelagem do C_void (rascunho técnico para o TG2)

> Status: **proposta + testes exploratórios de viabilidade** (12/10/2026). Nada aqui foi decidido com o Rafael ainda.
> Decisões confirmadas ficam em [decisoes_e_pendencias](../00_projeto/decisoes_e_pendencias.md).

## 1. Requisitos (do TG1 e das conversas)

- Equação **explícita, simples, calculável no chão de fábrica** (calculadora/planilha), sem CFD nem NN.
- Fundamentada em física/análise dimensional; blocos de naturezas **geométrica, cinemática, térmica, dinâmica**.
- Calibrada nos 108 ensaios de Du et al.; **split 78/30** (como o artigo); limiar T; **≥ 70 % de acurácia** em teste
  cego; **hierarquia de sensibilidade** entre as naturezas.
- Preferência do Rafael: **pouco protagonismo de ML**; o "motor" é a equação física.

## 2. Análise dimensional (Buckingham Π)

Variáveis dimensionais do dataset: v [L T⁻¹], ω [T⁻¹], t, R_s, R_pr, R_pt [L], α [L² T⁻¹], p, σ_y [M L⁻¹ T⁻²];
θ já é adimensional. São 10 variáveis dimensionais e 3 dimensões (M, L, T) → **7 grupos independentes** + θ.
(A liga entra só via α e σ_y — e esses dois são constantes por liga.)

Um conjunto natural (todos realmente adimensionais):

| Grupo | Expressão | Natureza | Interpretação física | Sinal esperado no risco de vazio |
|---|---|---|---|---|
| Π_cin | ω R_s / v | cinemática | velocidade periférica do ombro / avanço = 2π·R_s / (avanço por rotação); ↔ "weld pitch" inverso (Reynolds, Mishra & Ma §3.1) e v_material = ωR_s (Meyghani) | ↑ Π_cin → mais calor/mistura → **menos** vazio |
| Pe | v R_s / α | térmica | número de Péclet: advecção (avanço) × difusão de calor; Pe alto = pouco pré-aquecimento à frente | ↑ Pe → **mais** vazio (frio) |
| Π_conf | p / σ_y | dinâmica | pressão de forja relativa à resistência do material (Frigaard: p ≤ σ_y(T)) | ↑ → menos vazio |
| Π_esp | t / R_s | geométrica | espessura relativa ao ombro (calor do ombro tem de atravessar t) | ↑ → mais vazio (raiz fria) |
| Π_pino | R_pr / R_s | geométrica | razão pino/ombro (ótimo citado 1/2,5–1/3; Ahmed 2021) | ? |
| Π_cone | R_pt / R_pr | geométrica | conicidade do pino (fluxo na raiz) | ? |
| θ | θ | dinâmica | tilt (forja traseira) | quase sem informação no dataset |

Combinações físicas úteis (todas produtos de potências dos grupos acima):
- **Energia por comprimento adimensional** (Schmidt / Ahmed 2021 / Ângelo): Q/v ∝ μ p ω R_s³ / v →
  Q/(v·σ_y·R_s·t) ∝ (p/σ_y)·(ωR_s/v)·(R_s/t). ➡ o bloco "térmico" de energia **já é** um produto dos Π básicos.
- **Péclet rotacional** ωR_s²/α = Π_cin·Pe.
- **T/T_m (Arbegast–Hartley):** T/T_m ≈ K(ω²/v)^α_A com α_A ≈ 0,05 → expoente pequeno ⇒ trabalhar em log.
  Exige T_m por liga (solidus aprox.: 2024 ≈ 502 °C, 2219 ≈ 543 °C, 6061 ≈ 582 °C — **confirmar com ASM Handbook**).
- Correlação adimensional de T_pico de **Roy, Nandan & DebRoy (2006)** e "back-of-the-envelope" de **Arora, DebRoy &
  Bhadeshia (2011)** (refs. 40–41 de Du et al.) — **buscar**: são exatamente "variáveis causais" (T*, torque) em forma
  fechada, sem CFD. Podem ser o elo entre o C_void e os 90–93 % de Du et al. com modelo analítico.

⚠️ O Π_Term das versões do TG1, ωR_s³/(v·t·α), **tem dimensão s/m** (não é adimensional). Corrigir.

## 3. Forma do C_void: unificando a versão aditiva e a multiplicativa

Lei de potência (forma "Reynolds", slide 33 do TG1):

$$C_{void} = C_0 \prod_i \Pi_i^{\,\beta_i} \qquad \text{vazio previsto se } C_{void} > 1$$

Tomando log: ln C_void = ln C₀ + Σ βᵢ ln Πᵢ → **é exatamente a forma aditiva da eq. 3.1 do TG1, mas em log**.
Calibração natural: **regressão logística** com entradas ln Πᵢ:

P(vazio) = 1 / (1 + C_void⁻¹)  (C_void = "odds" de vazio)

Vantagens: (i) une as duas formas do TG1; (ii) β = **expoentes** físicos interpretáveis; (iii) dá **probabilidade**,
não só 0/1; (iv) **sensibilidade sai de graça**: ∂ln C/∂ln Πᵢ = βᵢ (elasticidade); para hierarquia de naturezas usar
βᵢ·desvio-padrão(ln Πᵢ) e/ou contribuição na deviance (drop-one); (v) no chão de fábrica: calcular C_void com
calculadora e comparar com 1 — ou um **ábaco/nomograma** ω × v para cada ferramenta/liga.
Opção "expoentes simples": arredondar βᵢ para frações simples (½, 1, 2…) e reportar a perda de acurácia.

Alternativas a comparar (todas ainda "equação explícita"): limiar único sobre um índice físico (estilo Du et al. com
T* > 0,93); árvore de decisão rasa (profundidade 2–3) sobre Π's — regras do tipo "se Π_cin < a e Pe > b → vazio".

## 4. Testes exploratórios de viabilidade (12/10/2026)

Regressão logística (padronizada), CV estratificado 5-fold × 20 repetições | **leave-one-study-out** (13 grupos):

| Entradas | CV estratificado | Deixa 1 estudo de fora |
|---|---|---|
| ln(ωR_s/v) | 0,615 | 0,577 |
| + ln Pe | 0,624 | 0,622 |
| + ln(p/σ_y) | 0,632 | 0,616 |
| + ln(t/R_s) | **0,665** | 0,630 |
| 6 Π's (acima + R_pt/R_pr, R_pr/R_s) | 0,625 | 0,603 |
| ln ω sozinho | 0,644 | 0,569 |
| ln ω, ln v, ln R_s, ln t | 0,710 | 0,616 |
| 10 variáveis brutas (log) | **0,731** | 0,605 |
| árvore de decisão prof. 3 (brutas) | 0,728 | – |

(Baselines: classe majoritária 60,2 %; Du et al. NN com brutas: 83,3 % em **um** split de 30.)

**Leituras:**
1. **A meta de 70 % não é trivial fora da amostra.** O "ω < 1100 rpm → vazio" (70,4 %) é in-sample.
2. Os Π "óbvios" sozinhos ficam em 62–67 %: dentro de cada estudo o sinal é forte e monotônico (ω baixo / v alto →
   vazio), mas **o nível crítico muda de estudo para estudo** (outra ferramenta, espessura, liga). O desafio é achar a
   normalização que alinha os estudos: um ω_crítico(geometria, liga) ou um índice térmico tipo T/T_solidus.
3. Nas variáveis brutas o peso maior é de ω, depois σ_y, α, t, tilt; **v quase não pesa entre estudos** — porque v
   varia muito entre estudos (ex.: ref. 15 com v ~ 900 mm/min) e não se alinha com o risco. Ponto a investigar
   (inclusive possível erro de unidade na ref. 15).
4. Leave-one-study-out ~60 %: generalizar para uma ferramenta/estudo nunca visto é difícil — **limitação honesta a
   discutir**; e o 83,3 % de Du et al. vem de split aleatório (estudos aparecem no treino e no teste).
5. Próximos testes sugeridos: índice térmico T/T_m (Arbegast–Hartley, com T_solidus por liga) e a correlação de
   Roy–Nandan–DebRoy; Π de energia por volume; interações ω×geometria; checar estabilidade dos expoentes por
   bootstrap.

Scripts dos testes: estavam no scratchpad da sessão (não versionados). Recriar em `src/` quando começarmos o código.

## 5. Protocolo de avaliação proposto (para o TG2)

1. **Dados:** corrigir `alloy` via α; flags `p_assumed`, `tilt_assumed`; converter ω para rad/s (2π·rps) quando
   necessário; manter SI. Documentar no texto (apêndice com tabela corrigida).
2. **Split principal** idêntico em espírito a Du et al.: estratificado, 78 treino / 30 teste, **semente fixa**
   reportada. Como 30 amostras → cada erro vale 3,3 pp, reportar também **CV repetido** (média ± dp) e
   **intervalo de confiança** (Wilson) da acurácia de teste.
3. **Robustez:** leave-one-study-out (13 grupos) como análise de generalização.
4. **Métricas:** acurácia, acurácia balanceada, sensibilidade (recall de vazio — o erro caro na indústria é aprovar
   solda com vazio), especificidade, F1, AUC-ROC, matriz de confusão.
5. **Comparações obrigatórias:** classe majoritária (60,2 %); melhor variável única; regressão logística nas brutas;
   árvore rasa; Du et al. 83,3 % (NN brutas) e 90–96,6 % (variáveis causais).
6. **Limiar:** escolher no treino (máx. acurácia ou Youden) — nunca no teste.
7. **Sensibilidade/hierarquia:** elasticidades βᵢ, tornado (OAAT em torno da mediana), e importância por natureza
   (agrupando Π's de cada natureza).
8. **Ferramentas:** Python (pandas, numpy, scikit-learn, statsmodels, matplotlib). Sugestão de estrutura:
   `src/` (código), `notebooks/` (exploração), `resultados/` (figuras/tabelas para o LaTeX).
