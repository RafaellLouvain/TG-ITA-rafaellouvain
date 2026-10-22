# Resultados dos modelos A, B e C — 2026-10-21 (para alinhamento antes da escrita)

> Código: `TG2/codigos/` (README lá). Tabelas: `TG2/resultados/tabelas/`; figuras: `TG2/resultados/figuras/`.
> Protocolo: [protocolo_metodologia](protocolo_metodologia.md). Plano: [plano_capitulos_metodologia_resultados](plano_capitulos_metodologia_resultados.md).
> "Acurácia de teste média" = média em 500 splits 78/30 estratificados; LOSO = deixa um estudo de fora (14 grupos);
> split oficial = semente 2026 (fixada no código antes de rodar qualquer modelo).

## 1. Tabela principal (limiar escolhido pela acurácia)

| Modelo | Acur. teste média | p5–p95 | % splits ≥ 70 % | Acur. bal. | Sens. | Espec. | Acur. treino | LOSO | Split oficial |
|---|---|---|---|---|---|---|---|---|---|
| Classe majoritária | 60,0 | – | 0 % | 50,0 | 0 | 100 | 60,3 | 60,2 | 60,0 |
| Só rotação ω | 66,7 | 53–77 | 44 % | 68,1 | 75,4 | 60,9 | 70,8 | 63,0 | 60,0 |
| **A: ωR_s** | **72,9** | 60–83 | **74 %** | 71,2 | 63,0 | 79,4 | 76,8 | **66,7** | 90,0 |
| A′: ωR_s/v (adim.) | 60,9 | 53–67 | 4 % | 54,6 | 23,1 | 86,1 | 66,3 | 59,3 | 60,0 |
| A″: ωR_s²/α (adim.) | 63,7 | 53–73 | 20 % | 59,1 | 36,5 | 81,8 | 69,2 | 59,3 | 66,7 |
| B1 (Buckingham, 7 termos) | 63,2 | 50–73 | 25 % | 61,7 | 54,6 | 68,8 | 74,4 | 54,6 | 83,3 |
| B2 (térmico, 4 termos) | 64,0 | 53–77 | 28 % | 59,8 | 38,8 | 80,8 | 72,1 | 59,3 | 80,0 |
| B3 (escoamento, 5 termos) | 60,7 | 50–70 | 13 % | 56,7 | 37,1 | 76,4 | 70,6 | 58,3 | 70,0 |
| B* (seleção entre B1–B3) | 62,7 | 50–73 | 23 % | 58,9 | 40,1 | 77,7 | 73,0 | 54,6 | 80,0 |
| **C: ωR_s + termos** | **74,0** | 60–87 | **79 %** | 72,5 | 65,1 | 79,9 | 81,2 | **66,7** | 90,0 |
| Du et al. (NN, brutos) | – | – | – | – | – | – | 98,4 | – | 83,3 (1 split) |

Com limiar pela **acurácia balanceada**: A 70,3 % (bal. 71,0; sens. 74,9; espec. 67,2; 63 % dos splits ≥ 70 %);
C 71,6 % (bal. 72,0; sens. 73,6; espec. 70,3; 67 %); B* 60,3 %; B2 60,3 %.

## 2. Achados

1. **Meta de 70 %:** atingida em média por **A (72,9 %)** e **C (74,0 %)**; **não** atingida por nenhum B (61–64 %).
2. **B (Buckingham) fica abaixo de "só rotação" e, no LOSO, abaixo da classe majoritária.** Diagnóstico:
   - não é sobreajuste puro: a regularização L2 não ajuda (B2: 64,0 → 63,5 → 62,1 %) e a própria acurácia de
     treino é baixa (72–74 %);
   - é a **exigência de adimensionalidade**: num grupo adimensional, ω só pode aparecer dividido por uma velocidade
     de referência (v ou α/R_s). Neste dataset nem v nem α carregam essa informação: A′ = ωR_s/v (60,9 %) e
     A″ = ωR_s²/α (63,7 %) destroem o sinal de ωR_s (72,9 %). A mesma logística com variáveis dimensionais livres
     chega a 75,0 % (10 variáveis), mas com LOSO de 53,7 %, e a 71,8 % com só ln ω + ln R_s (LOSO 61,1 %);
   - leitura física: **Pe = vR_s/α < 1 em 93 % das soldas** → regime dominado por condução, em que a temperatura
     de pico depende da taxa de geração de calor (ω, R_s), não do calor por comprimento (que divide por v);
     coerente com Mishra e Ma ("rotação governa a temperatura máxima; avanço governa a taxa de aquecimento");
   - α funciona como "rótulo de liga" e prejudica a generalização: o B erra quase todo o estudo 14 (AA6061,
     LOSO 15 %), que o A acerta 100 %.
3. **A: velocidade periférica crítica do ombro.** Limiar no treino oficial: **V_crit = 0,84 m/s** (N·R_s ≈ 8 050
   rpm·mm) pelo critério de acurácia; 1,05 m/s pelo balanceado. IC bootstrap: 0,69–1,05 m/s (por solda); 0,31–1,09
   (por estudo, largo). Um único parâmetro, sem expoente ajustado.
4. **C ≈ A.** Ganho médio de +1,1 p.p. (74,0 × 72,9 %) e LOSO igual (66,7 %). A seleção de termos é **instável**:
   em média +1,3 termo; o mais escolhido é a conicidade R_pt/R_pr (~55 % dos splits), depois p/σ_y (~30 %),
   θ (~18 %), t/R_s (~15 %); v e α quase nunca (≤ 4 %). Só o núcleo: 15–24 % dos splits.
5. **Acurácia × acurácia balanceada (critério do limiar):** o critério balanceado **não aumenta a acurácia
   balanceada de teste** (A: 71,2 → 71,0; C: 72,5 → 72,0); ele **troca especificidade por sensibilidade**:
   +12 p.p. de vazios detectados (63 → 75 %) por −2,6 p.p. de acurácia (A). A hipótese "o balanceado é mais
   eficiente" não se confirma como ganho líquido; confirma-se como **escolha mais segura** (menos vazios aprovados),
   mantendo a meta de 70 % (A 70,3 %; C 71,6 %).
6. **Hierarquia (B2, conjunto escolhido no treino):** contribuição ao ln C_void: cinemática 0,62 ≈ geométrica 0,57
   > dinâmica 0,49 ≫ térmica 0,13 ≈ metalúrgica 0,13. Bootstrap por estudo: cinemática em 1º lugar em 60 % das
   reamostragens, geométrica em 37 %; térmica e metalúrgica sempre em 4º–5º. Retirar a geometria custa mais
   (−5,2 p.p.); retirar a térmica, quase nada (−0,4 p.p.). **Coerente com A e C: o mecanismo dominante é
   cinemático-geométrico (ωR_s).**
7. **Sinais dos expoentes (B2) × Tab. de síntese:** ω − ✔, v + ✔, R_s − ✔, α + ✔, p − ✔ (bootstrap: 100, 88, 95,
   100, 80 % no sinal esperado). **t sai com sinal contrário** (chapa mais grossa → menos vazio) em B2, B3, C e no
   bootstrap (só 12 % no sinal esperado) → provável confusão entre estudos (a discutir).
8. **Robustez:** sem p e θ, A não muda (não usa p, θ), C 73,7 %, B cai 1–2 p.p. → conclusões não dependem dos
   valores assumidos. Sem as linhas 84–89: A 74,1 %, C 76,8 % (LOSO 71,6 e 72,6 %) → essas 6 soldas são
   "difíceis"; conclusões mantidas.
9. **Erros:** concentrados nos estudos 8 (erra 67 % — mesma liga e ferramenta quase igual à do estudo 6, mas
   rotação crítica muito diferente), 10, 12, 13 (AA2219 em rotação baixa) e 6/7. Teto de acurácia do dataset.

## 3. Pontos estranhos / atenção

- **O split oficial (semente 2026) é excepcionalmente "fácil":** fica no percentil ~99 dos 500 splits para A, B e C
  (A = 90 %, C = 90 %, B* = 80 %). O teste oficial não contém soldas dos estudos difíceis 8, 10, 12 e 17; a taxa de
  erro média dessas 30 soldas é 14 % contra 26 % do dataset. Sugestão: **acurácia de teste média (500 splits) como
  número principal**; o split oficial como resultado secundário, com essa ressalva (e o mesmo vale para os 83,3 % de
  Du et al., também de um único split).
- Expoente de t com sinal contrário ao esperado (item 7).
- Bootstrap do B1 com intervalos enormes (separação perfeita em reamostragens com poucos estudos) → B1 instável.
- Pressão p tem o maior efeito no tornado do B2, mas 72/108 valores são assumidos → interpretar com cautela
  (a robustez 1 mostra que o desempenho quase não depende deles).

## 4. Decisões do Rafael sobre os resultados (2026-10-22)

1. **Número principal = acurácia de teste média (500 splits)**; split oficial (semente 2026) como secundário, com a
   ressalva de que caiu no percentil ~99 (teste sem os estudos difíceis).
2. **Narrativa aprovada** (B → A → C). Na escrita, **aprofundar a explicação do fracasso do B** (Péclet < 1, regime
   de condução, taxa de geração de calor × calor por comprimento) **relacionando com as referências**, e dizer que,
   idealmente, o C_void recomendado seria o A, pela simplicidade.
3. **C_void com unidade aceito** (C_void = V_crit/(ωR_s)), discutindo por que a versão adimensional falha.
   Limiar: **reportar os dois critérios** (acurácia e acurácia balanceada).
4. Commit/push de `TG2/codigos`, `TG2/resultados` e docs.

## 5. Achado extra (2026-10-22): o que varia dentro de cada estudo

Só **ω (14/14 estudos) e v (12/14)** variam dentro dos estudos; **R_s, R_pr, R_pt, t, α, p, θ e σ_y são constantes
em todos os 14 estudos**. Consequências para a escrita:
- o efeito dessas 8 variáveis só pode ser estimado **entre estudos** (14 "pontos"), confundido com máquina, critério
  de inspeção, perfil do pino etc. → explica o sinal trocado de t, a instabilidade do C e o LOSO mais baixo;
- a hierarquia "geométrica/dinâmica/metalúrgica" deve ser lida como **associação entre estudos**, não efeito causal;
- em contrapartida, **v varia dentro de 12 estudos e mesmo assim não separa vazios** (AUC intra-estudo 0,55 na
  análise exploratória) → evidência limpa, sem confusão entre estudos, de que o avanço pesa pouco no regime do
  dataset — reforça o argumento do Péclet.

V_crit calibrado nas 108 soldas (equação final recomendada): **0,843 m/s (≈ 8 050 rpm·mm)** pelo critério de
acurácia; **1,052 m/s (≈ 10 040 rpm·mm)** pelo balanceado — iguais aos do treino oficial.

## 6. Notas para a escrita da explicação do B (relacionar com as referências)

- Schmidt: Q ∝ τ ω R_s³ (taxa de geração de calor; não depende de v) — eq. de Schmidt na seção 2.2.
- Mishra e Ma (2005): a temperatura máxima é governada pela rotação; o avanço governa a taxa de aquecimento/
  resfriamento; Tang et al. (ganhos decrescentes de T com ω).
- Arbegast–Hartley: T/T_m = K(ω²/v·10⁴)^α → ω pesa o dobro de v, e o expoente α é pequeno.
- Arora et al. (2011): Q* = σ₈Aωc_p/(kU²) contém o fator ωR_s²/α (Péclet rotacional) — mas também 1/U²; a
  correlação T* = 0,151 log Q* + 0,097 tem inclinação pequena (dependência logarítmica).
- Péclet vR_s/α < 1 em 93 % das soldas (mediana 0,30): o calor se difunde à frente da ferramenta mais rápido do que
  a ferramenta avança → campo térmico quase estacionário em torno do ombro (regime de condução) → a temperatura de
  pico depende da potência gerada, não da energia por comprimento.
- Meyghani e Awang (2022): velocidade do material ≈ ωR_s (eq. 15) → ωR_s = velocidade de deslizamento máxima na
  interface (calor de atrito por área q = τ ω r máximo na borda do ombro).
- Bezerra (2025): regressão logística na energia efetiva **por comprimento** (Q_eff/v) teve acurácia igual à da classe
  majoritária → coerente com o nosso achado de que dividir por v destrói o sinal.
- Du et al. (2019): o vazio se forma por temperatura baixa / tensão alta perto do pino no lado de avanço; T* é a
  variável causal mais importante.
