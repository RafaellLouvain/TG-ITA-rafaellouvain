# Protocolo da Metodologia — decisões para o capítulo 3

> Documento vivo: registra **o que foi decidido com o Rafael** para a Metodologia do TG2 e **por quê**, para virar texto
> do capítulo 3. Itens "(proposto)" ainda não foram fechados. Detalhes de dados em
> [dataset](../01_dados/dataset.md); propostas técnicas em [proposta_modelagem](proposta_modelagem.md); números
> exploratórios em [analises_exploratorias_2026-10-12](analises_exploratorias_2026-10-12.md).

## 1. Terminologia (2026-10-21)

- **Acurácia de teste**: acurácia em soldas não usadas na calibração (split oficial 78/30, splits 78/30 repetidos,
  validação cruzada, leave-one-study-out). Quando necessário: "acurácia de teste (split oficial)" e "acurácia de teste
  média (N splits)".
- **Acurácia de treino**: medida nas mesmas soldas usadas para calibrar (in-sample).

## 2. Abordagens de modelagem (2026-10-21)

Ordem de trabalho decidida: **B → A → C** (D fica como possível comparação, não confirmada).

| | Abordagem | Forma |
|---|---|---|
| B | Lei de potência em grupos Π (Buckingham), calibrada por regressão logística em ln Π | C_void = C₀ ∏ Πᵢ^βᵢ |
| A | Índice físico único + limiar | ex.: C_void = V_crit/(ω·R_s) |
| C | Híbrida: núcleo físico + correções por bloco aceitas só se melhorarem a acurácia de teste | ex.: K/[ω·R_s·(p/σ_y)^½] |
| D | (não confirmada) Semianalítica: T* de Arora et al. (2011) + limiar à la Du et al. | T* < T*_crit |

## 2a. Ferramenta de calibração: regressão logística (decidido 2026-10-21)

Viés do trabalho: **mecânica, não aprendizado de máquina.** A regressão logística entra apenas como o método
estatístico para ajustar os expoentes da lei de potência — não como "modelo de ML".

Justificativa (para o texto do cap. 3):
1. **É a própria forma da equação.** ln[P/(1−P)] = b₀ + Σ βᵢ ln Πᵢ ⇔ P/(1−P) = C₀ ∏ Πᵢ^βᵢ = C_void (chance de vazio);
   limiar C_void = 1 ⇔ P = 50 %. Mesmo raciocínio das correlações clássicas ajustadas em log (ex.: Nu = C Re^a Pr^b).
2. **Saída binária.** Mínimos quadrados (proposto no TG1) supõe resposta contínua e pode dar "probabilidades" fora de
   [0, 1]; a logística (máxima verossimilhança) é o ajuste padrão para respostas sim/não.
3. **Interpretabilidade.** Coeficientes = expoentes físicos (com IC); sinais comparáveis à Tab. de síntese (seção 2.9);
   sensibilidade sai dos expoentes.
4. **Precedente no grupo:** Bezerra (2025) usou regressão logística univariada em log₁₀ Q_eff para a probabilidade de
   túnel (figura já usada na revisão).
5. **Poucos parâmetros** → equação que cabe numa planilha.

Uso por abordagem: **B** e **C** = logística em ln Π; **A** = só busca do limiar (sem regressão).

Variações: **variar os termos, não o algoritmo.** Únicas variantes: (i) com e sem pesos de classe; (ii) regularização
L2 apenas como checagem da estabilidade dos expoentes. **Não** usar probit, árvore de decisão ou outros modelos de ML;
comparação com ML apenas citando Du et al. (métodos 1–5). Restrição: ~43 vazios → ~10 eventos por parâmetro →
conjuntos de 3–5 termos (o B1 com 7 termos é o ponto de partida e deve mostrar sobreajuste).

## 3. Tratamento dos dados (2026-10-21)

| Decisão | Justificativa | Status |
|---|---|---|
| Ler o CSV com BOM (`utf-8-sig`), descartar a linha 2 (unidades) e tratar a 1ª coluna como índice | Formato do arquivo do Kaggle | decidido |
| **Não usar a coluna `Alloy`** (nem no modelo nem para agrupar) | Inconsistente com α e σ_y em 33 linhas (21–38 e 56–70) | decidido |
| Se for preciso agrupar por liga (tabela descritiva, estratificação), identificar a liga pelo par (α, σ_y): 4,97e-5/324 → 2024; 4,89e-5/352 → 2219; 6,90e-5/276 → 6061 | Relação 1:1, sem hipótese adicional; bate com as refs. de origem | decidido |
| **Manter α e σ_y** como variáveis do modelo | Corretos (batem com a referência e com valores de handbook) | decidido |
| Registrar como limitação: α e σ_y são constantes por liga (3 níveis) | Modelo pode usá-los como "etiqueta" de liga/estudo; controlado pelo leave-one-study-out | decidido |
| **Converter tudo para o SI**: ω de rps para rad/s (ω = 2π·N), p de MPa para Pa, σ_y de MPa para Pa; comprimentos já em m, v em m/s, α em m²/s, θ em graus (adimensional) | Consistência dimensional dos grupos Π | decidido |
| Valores com `*` (p em 72/108, θ em 71/108): limpar para número e criar indicadores `p_assumido`, `theta_assumido` | Valores assumidos por Du et al., não medidos | decidido |
| Robustez 1 (**opção b**): manter as 108 linhas e **retirar p e θ do modelo** nessa versão (em vez de excluir as linhas com `*`, que deixaria ~36 linhas) | Verificar se conclusões dependem de valores assumidos por Du et al. | decidido (2026-10-21) |
| Robustez 2: repetir **sem as linhas 84–89** (ref. 7 com propriedades de 6061) | Incerteza de atribuição no dataset | proposto |
| Verificar v da ref. 15 (508–1068 mm/min) no artigo original | Possível erro de unidade | pendente |

## 4. Desbalanceamento de classes (2026-10-21)

Dataset: 43 com vazio (39,8 %) × 65 sem vazio (60,2 %) → desbalanceamento **moderado**.

| Medida | Onde entra | Status |
|---|---|---|
| Splits e folds **estratificados** pela classe (≈ 40/60 em treino e teste) | Todos os splits | decidido |
| **Pesos de classe** inversamente proporcionais à frequência na regressão logística (vazio ≈ 65/43 ≈ 1,5×) | Calibração dos expoentes (B, C); para comparação justa, rodar também sem pesos | decidido |
| **Limiar escolhido no treino por dois critérios, rodados em paralelo para todas as abordagens:** (i) máxima acurácia simples; (ii) máxima acurácia balanceada (= Youden J). Comparar as duas versões em acurácia, acurácia balanceada, sensibilidade e especificidade de teste — hipótese a demonstrar: o critério balanceado é mais eficiente (detecta mais vazios com pouca ou nenhuma perda de acurácia) | A, B, C | **decidido (2026-10-21)** |
| Reportar sempre: acurácia, **acurácia balanceada**, sensibilidade (recall de vazio), especificidade, matriz de confusão; e a **classe majoritária (60,2 %)** como piso | Resultados | decidido |
| **Não** usar reamostragem sintética (SMOTE, oversampling) | Criaria "soldas inventadas" num dataset pequeno e agrupado por estudo | decidido |

## 5. Protocolo de validação (2026-10-21; métrica principal decidida em 2026-10-22)

**Métrica principal: acurácia de teste média nos 500 splits 78/30** (com p5–p95 e % de splits ≥ 70 %). O split
oficial (semente 2026, fixada no código antes de rodar) é secundário: caiu no percentil ~99 (ver resultados).
C_void com unidade aceito para o modelo A; limiar reportado pelos dois critérios.


1. Split oficial 78/30 estratificado, semente fixa reportada (como Du et al.).
2. 500 splits 78/30 repetidos → média, p5–p95 e % de splits ≥ 70 %; IC de Wilson no split oficial.
3. Expoentes, termos e limiar escolhidos **só no treino**; seleção de termos dentro de CV aninhada.
4. Leave-one-study-out (generalização para estudo/ferramenta não vistos).
5. Comparações: classe majoritária (60,2 %); só rotação; Du et al. Método 1 (83,3 %); Du et al. com variáveis causais
   (90–96,6 %) como teto.
6. Declarar a fase exploratória (que já viu os 108 pontos) e congelar a forma da equação antes do teste final.

## 6. Análise de sensibilidade (decidido 2026-10-21)

Divisão por natureza (**decidido 2026-10-21 — 5 naturezas, fiel à Tabela 3.1 do TG1**):

| Natureza | Variáveis |
|---|---|
| Cinemática | ω, v |
| Geométrica | R_s, R_pr, R_pt, t |
| Térmica | α |
| Dinâmica | p, θ |
| Metalúrgica | σ_y |

Como os grupos Π misturam naturezas (ex.: ωR_s/v, vR_s/α, p/σ_y), a hierarquia do **modelo B** é calculada **por
variável física** (efeito de cada variável somado sobre todos os Π em que aparece) e depois **agregada por natureza**.
Retirada de bloco = retirar todas as variáveis de uma natureza (e os Π que dependem delas) e recalibrar.
Limitação a declarar: α e σ_y têm só 3 valores (um por liga) → térmica e metalúrgica são difíceis de separar.

| Modelo | Sensibilidade | Robustez dos dados (sem `*`; sem linhas 84–89) |
|---|---|---|
| **B** | **Completa:** (1) elasticidades βᵢ = ∂ln C/∂ln Πᵢ e efeito por variável física (soma dos βᵢ × expoente da variável em cada Π); (2) tornado: cada variável do p10 ao p90 com as demais na mediana, indicando se cruza o limiar; (3) retirada de bloco: queda de acurácia e acurácia balanceada de teste ao retirar cada natureza e recalibrar; (4) bootstrap por estudo (~1000): IC dos βᵢ e frequência de cada natureza em cada posição da hierarquia; (5) sinais dos βᵢ × tabela de sinais esperados (Tab. de síntese, seção 2.9) | sim |
| **A** | Hierarquia trivial (expoentes fixos 1 e 1). Só: robustez do limiar (IC do V_crit por bootstrap; acurácia com limiar ±10 %) e análise dos erros (estudos onde o índice falha) | sim |
| **C** | Ordem de entrada e ganho de acurácia de teste de cada bloco (é a própria hierarquia) + tornado da equação final como figura ilustrativa | sim |

Ressalva para o texto: mede a sensibilidade **do modelo calibrado neste dataset**, não causalidade física pura
(variáveis agrupadas por estudo podem se confundir).
