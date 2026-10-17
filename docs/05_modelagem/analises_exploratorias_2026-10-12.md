# Análises exploratórias — 2026-10-12 (noite)

> **Status: exploratório, não oficial.** Objetivo: achar relações promissoras entre variáveis (expoentes, combinações
> por bloco) com embasamento físico, e testá-las contra o CSV. Código e saídas em `analises_exploratorias/`
> (README lá explica como rodar). Nada aqui foi decidido com o Rafael.

## 0. Verificação dos dados (pedido do Rafael)

- `Downloads/TG/Welding_process_parameters.csv` (03/10/2026) **é idêntico byte a byte** ao `dados/` do workspace
  (MD5 `6220d9db…`). O `.txt` da mesma pasta é um resumo de artigo sobre FMEA em laboratórios de química — **sem
  relação com o TG, pode ser descartado**.
- Todos os PDFs de `referencias/` e `TG1/` têm **MD5 idêntico** às cópias em `Downloads/` e `Downloads/TG1/`
  (baixados em 30–31/05/2026) e todos foram lidos sem erro → **nenhum arquivo corrompido**. Os "erros" do dataset
  (coluna `Alloy`, `*`) vêm da fonte (Kaggle/Du et al.), não de corrupção; o tratamento está em
  `analises_exploratorias/dados_fsw.py`.
- No Downloads há ainda, fora do workspace: os `.pptx` da apresentação do TG1 (`Downloads/TG1/`),
  `fsw_research1.pdf` (Matitopanum et al. 2023, *Intelligent Systems with Applications* 19:200259 — ML para UTS/dureza/
  heat input em AA7075; **não cita Mendeley** → o link do Mendeley dado pelo Gemini era inventado) e
  `computation-11-00100.pdf` (Kraiklang et al. 2023, *Computation* 11:100 — ML para AA5083/AA6061 dissimilar). Ambos
  sem relação direta com vazios.

## 1. Achado central: dentro de cada estudo, a ROTAÇÃO decide; entre estudos, o nível crítico muda

AUC **intra-estudo** (só compara soldas do mesmo estudo, mesma ferramenta e liga) — A01:

| Índice | AUC intra-estudo |
|---|---|
| N (rotação) | **0,962** |
| ω²/v (pseudo heat index de Arbegast) | 0,892 |
| ω/v, ωR_s/v, Q/v (qualquer coisa ÷ v) | 0,794 |
| v | 0,545 (≈ aleatório) |

➡ Dividir por v **piora**. No dataset, a velocidade de avanço quase não explica vazio (nem dentro nem entre
estudos); a rotação explica quase tudo dentro do estudo. **Fisicamente coerente** com Mishra & Ma §3.2 / Arbegast &
Hartley: "a temperatura máxima é função forte da rotação; a velocidade de avanço governa a taxa de aquecimento",
T/T_m ∝ (ω²/v)^0,05 (ω pesa o dobro de v), e o aumento de T com ω (Tang et al.). Figura:
`analises_exploratorias/resultados/fig_a06_rotacao_por_estudo.png`.

**Rotação crítica por estudo (A02)** — de ~280 rpm (ref 12, AA2219, 17,5 mm) a ~1500 rpm (ref 18, AA6061, 3 mm).
Correlação de ln N_crit com características do estudo: **R_s −0,55**, σ_y −0,66, **α +0,55**, t −0,50, R_pr −0,52,
**v −0,06**, p −0,12. Leitura: ombro maior → precisa de menos rotação (Q ∝ ω R_s³); liga de maior difusividade (6061)
→ precisa de mais rotação (perde calor mais rápido). σ_y e t estão confundidos com o tamanho da ferramenta.

## 2. Índices de 1 número + 1 limiar (formato "chão de fábrica")

Selecionados (A01, A04, A05). "Vazio previsto se I < I_crit". CV = 5-fold × 20 com limiar escolhido no treino;
LOSO = deixa um estudo inteiro de fora; "78/30" = média de 500 splits estratificados 78/30 (como Du et al.).

| Índice | Origem | in-sample | CV | LOSO | 78/30 média (p5–p95) | % splits ≥ 70 % | sens. / espec. |
|---|---|---|---|---|---|---|---|
| F0 N | baseline | 0,704 | 0,679 | 0,630 | 0,678 (0,57–0,80) | 47 % | 0,86 / 0,60 |
| **F1 ω·R_s** | **física, sem busca** | 0,759 | 0,733 | 0,694 | 0,735 (0,63–0,83) | 77 % | 0,72 / 0,79 |
| F2 ω·(p/σ_y)^0,5 | grade | 0,759 | 0,745 | 0,759 | 0,741 (0,63–0,83) | 82 % | 0,70 / 0,80 |
| **F3 ω·R_s·(p/σ_y)^0,5** | grade (2 termos) | 0,778 | 0,757 | 0,750 | 0,755 (0,63–0,87) | 86 % | 0,77 / 0,79 |
| F4 ω·R_s^0,5·t·(p/σ_y)·α^−0,5 | grade (4 termos) | 0,787 | 0,787 | 0,787 | 0,780 (0,67–0,90) | 92 % | 0,74 / 0,82 |

Referências: classe majoritária 60,2 %; Du et al. NN com parâmetros brutos 83,3 % (um split).
**CV aninhada** (escolhendo expoentes + limiar só no treino, a cada fold): **0,696 ± 0,099** → é a estimativa honesta
de "procurar expoentes na grade"; F2–F4 têm otimismo de seleção.

### F1 — velocidade tangencial na borda do ombro (o mais "limpo")

**Vazio previsto se ω·R_s < ≈ 0,86 m/s** (ω em rad/s, R_s em m) — equivalente a N[rpm]·R_s[mm] < ≈ 8 250.
- Não teve expoente ajustado: vem direto da física — calor de atrito por área q = τ·ω·r é máximo na borda do ombro;
  v_material ≈ ω·R_s (Meyghani & Awang 2022, eq. 15); ombro domina o calor (Mishra & Ma; Ahmed 2021).
- Em leis de potência com expoentes livres (A03), o melhor expoente de R_s com N foi **+1,11** — praticamente 1.
- Figura: `fig_a06_velocidade_periferica_ombro.png`.

### F3 — F1 × confinamento relativo (p/σ_y)^0,5

- Coerente com Frigaard (p ≤ tensão de escoamento) e com "pressão de forja insuficiente → vazio" (Threadgill 2009).
- **Cuidado:** 72/108 pressões são *assumidas* por Du et al. Teste: trocando todo p assumido por 13 MPa, o LOSO de F3
  continua 0,75 (o de F2 cai para 0,69) → o sinal de p em F3 parece vir das pressões **reais** (refs 7, 7b, 11, 16),
  mas são só 4 estudos. Tratar como hipótese.
- Figura: `fig_a06_indice_F3.png`.

### F4 — melhor da grade, mas suspeito

Expoente **+1 para t** (chapa mais grossa → menos vazio) contraria a física esperada → provavelmente artefato de
confusão (estudos de chapa grossa usam ferramentas grandes/baixa rotação). Não recomendo sem justificativa física.

## 3. Leis de potência com expoentes livres (A03 — logística em ln)

| Modelo (variáveis) | CV | LOSO | expoentes relativos a N |
|---|---|---|---|
| N | 0,641 | 0,593 | – |
| N, v | 0,626 | 0,574 | v: +0,11 (≈ 0) |
| **N, R_s** | **0,722** | **0,722** | R_s: +1,11 |
| N, R_s, t | 0,728 | 0,676 | R_s +0,57, t +0,43 |
| N, R_s, α, σ_y | 0,742 | 0,722 | α +6,2, σ_y +11,8 (⚠ só "aprende a liga": 3 níveis) |
| N, R_s, α, p | 0,680 | 0,685 | p +0,38 |
| 10 variáveis brutas | 0,737 | **0,537** | ⚠ sobreajuste entre estudos |
| Péclet rotacional ωR_s²/α (+ outros grupos) | 0,60–0,63 | 0,52–0,62 | – |

Leituras: (i) **acrescentar variáveis melhora in-sample mas piora o LOSO** — com 14 estudos, o modelo decora os
estudos; (ii) os grupos adimensionais "de livro" (Péclet, ωR_s²/α, Q/v, E*, Q* de Roy–DebRoy, T/T_sol de
Arbegast–Hartley) ficaram **piores que ω·R_s** (CV 0,59–0,65) — principalmente porque dividem por v ou usam R_s²/R_s³
e α com expoentes que não batem com os dados.

## 4. Limiar por liga (A07)

Tabela de 3 limiares de ω·R_s (2024: 1,05; 2219: 0,67; 6061: 0,95 m/s): in-sample 81 %, mas **LOSO 68 %** (pior que o
universal, 69 %). Para F3: in-sample 81 % → LOSO 66 % (universal 75 %). ➡ **Um limiar universal generaliza melhor.**

## 5. Onde os índices erram (limite do dataset)

Erros concentrados em: **refs 10, 12, 13 (AA2219, rotações baixas, 150–800 rpm)** e **ref 8**. Caso emblemático:
**ref 6 e ref 8 — mesma liga (AA2024), ferramentas quase idênticas (R_s 10 mm, pino 3,1/0,9 mm), chapa 4 vs 3 mm —
rotação crítica ~1300 vs ~400 rpm.** Nenhuma variável do dataset explica isso; provavelmente máquina, critério de
inspeção, perfil do pino (não registrado) etc. ⇒ há um **teto de acurácia** para qualquer equação que use só essas
colunas, especialmente no LOSO. Bom ponto de discussão no TG (honestidade + limitação de dados agregados de literatura).

## 6. Conclusões provisórias e sugestões para conversar

1. **Candidato principal ao "coração" do C_void: a velocidade periférica do ombro ω·R_s** — simples, fisicamente
   justificável, sem busca de expoentes, ~73 % fora da amostra (CV e 78/30), limiar ≈ 0,86 m/s.
   Forma sugerida: **C_void = V_crit/(ω·R_s)** (vazio se > 1) ou, com confinamento,
   **C_void = K/(ω·R_s·√(p/σ_y))**.
2. Isso **reinterpreta os blocos do TG1**: Π_Cin·Π_Geom ≈ ω·R_s (cinemático × geométrico), Π_Din ≈ (p/σ_y)^0,5;
   Π_Term (α, v, t) **não mostrou ganho robusto** no dataset — resultado a discutir, não esconder.
3. A meta de **70 % é atingível fora da amostra** com F1/F3 (77–86 % dos splits 78/30 passam de 70 %), mas a variação
   entre splits é grande (p5 ≈ 63 %): reportar **intervalo**, não só um número.
4. Grupos adimensionais formais: ω·R_s tem dimensão de velocidade. Para torná-lo adimensional precisamos de uma
   velocidade de referência física (ex.: α/R_s, √(σ_y/ρ), ou v). Os testes indicam que a normalização por v e por
   α/R_s **pioram**; vale investigar √(σ_y/ρ) (velocidade "plástica") ou aceitar um **número com unidade + limiar em
   m/s** (mais prático para o operador). Decisão a tomar com o orientador.
5. Próximos testes possíveis: incluir T_solidus/T_liquidus (dados de handbook, a confirmar); índice de calor com
   expoentes fixos de Schmidt mas **sem v**; torque/força a partir de Arora–DebRoy (2011) quando obtivermos o PDF;
   bootstrap por estudo para intervalos dos expoentes.
