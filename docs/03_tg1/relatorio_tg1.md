# Relatório do TG1 (entregue e aprovado)

**Arquivos:** `TG1/TG1___Relatório_Rafael_Louvain.pdf` (11 p.) e fonte `TG1/TG1_relatorio_formato_latex.tex`
(conteúdo idêntico; o PDF foi compilado no Overleaf — a imagem `Imagens/ita-logo.png` e
`Imagens/Captura de tela 2026-06-07 204639.png` (figura de Du et al.) **não estão no repositório**).

- **Autor:** Rafael Lucas de Albuquerque Louvain — Engenharia Mecânica-Aeronáutica, ITA, 2026.
- **Título:** *Análise da influência de parâmetros de processo de fabricação (cinemáticos, de geometria da
  ferramenta, entre outros) na integridade de juntas soldadas por FSW* (= título da ficha aprovada pelo Colegiado).
- **Orientador:** Prof. Lindolfo Moreira Filho (não aparece no relatório; vem do chat e do TG do Ângelo).
- **Palavras-chave:** FSW, Coeficiente Analítico, Vazios, Ligas Aeronáuticas, Análise Dimensional.

## Estrutura (págs.)

Capa (1) · Resumo (2) · Sumário (3) · **1 Introdução e contextualização** (4) — 1.1 Objetivo ·
**2 Revisão da literatura** (5–7) — 2.1 Fundamentos termomecânicos e balanço térmico; 2.2 Mecânica de escoamento e
modelagem computacional; 2.3 Parâmetros operacionais e forças de restrição; Fig. 2.1 (4 variáveis causais de Du et al.)
· **3 Metodologia** (8–9) — eq. 3.1 + Tabela 3.1 · **4 Cronograma** (10) · Referências (11; 7 itens, digitadas à mão).

## Conteúdo essencial

**Resumo/Objetivo:** desenvolver um modelo matemático-fenomenológico na forma de um **Coeficiente Analítico de Vazio
(C_void)** que agrupe parâmetros de naturezas cinemática, geométrica, dinâmica e térmica numa expressão adimensional;
calibrar e validar nos **108 ensaios** (AA2024, AA2219, AA6061) de Du, Mukherjee & DebRoy (2019); **meta: > 70 % de
acurácia global em teste cego**; estruturar **hierarquia de sensibilidade** das variáveis governantes; mitigar a
dependência de simulações numéricas no chão de fábrica.

**Equação proposta (3.1), "análise inicial e passível de alteração":**

$$C_{void} = \beta_1\,\Pi_{Geom} + \beta_2\,\Pi_{Cin} + \beta_3\,\Pi_{Term} + \beta_4\,\Pi_{Din}$$

Π_Geom (geometria do ferramental), Π_Cin (cinemática), Π_Term (térmico), Π_Din (dinâmica de forjamento); β_i ajustados.
**Os Π não são definidos explicitamente no relatório final.** (Em versões anteriores — slides/chat —
Π_Term = ωR_s³/(v·t·α), Π_Geom = R_pr/R_pt ou R_pt/R_pr, Π_Comp = (p/σ_y)·cos θ.)

**Calibração:** split **78 treino / 30 teste cego**; o processo "convergirá para um threshold T": C_void > T → vazio
(1); C_void ≤ T → sã (0). Meta 70 %.

**Tabela 3.1 — variáveis (natureza):** Alloy (metalúrgica), v (cinemática), ω (cinemática), t (geométrica),
R_s (geométrica), p (dinâmica), R_pr (geométrica), R_pt (geométrica), θ (dinâmica), α (térmica), σ_y (metalúrgica).

**Cronograma TG2:** Set — revisão bibliográfica complementar; **Out — consolidação da equação analítica +
calibração dos coeficientes e expoentes**; Nov — validação/acurácia + análise de sensibilidade; Dez — redação final
e entrega à banca.
➡ **Hoje (12/10/2026) estamos no mês de "consolidar a equação e calibrar"** — e nada foi implementado ainda.

## Pontos fortes a manter

- Problema claro e bem motivado (CFD caro × necessidade de critério rápido no chão de fábrica).
- Benchmark público e de prestígio (Du et al.), mesmo split que o artigo, meta numérica explícita.
- Ideia de **grupos adimensionais** ↔ analogia de Reynolds que o próprio Du et al. sugere.

## Pontos fracos / a corrigir no TG final

Ver lista consolidada em [erros_e_correcoes_tg1](erros_e_correcoes_tg1.md). Resumo:
1. Várias atribuições bibliográficas falsas (Aldanondo, Meyghani, Mishra & Ma, Ahmed/Walla) vindas do Gemini.
2. "Publicado na *Nature*" → é *npj Computational Materials*.
3. Π's não definidos; forma aditiva vs multiplicativa indefinida; "homogêneos/adimensionais" ainda não demonstrado.
4. Meta de 70 % é atingível só com ω (70,4 % in-sample) → precisa ser contextualizada contra baselines.
5. Formatação: não usa a classe ITA (falta ficha CIP, folha de aprovação, abstract, listas, FRD); referências sem
   BibTeX; citações "*Autor (ano)*" em itálico em vez do padrão autor-data da classe.
