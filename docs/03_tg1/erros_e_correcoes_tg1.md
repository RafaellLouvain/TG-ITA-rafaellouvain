# Erros e inconsistências do TG1 a corrigir no TG final

Levantamento feito em 12/10/2026 lendo **os PDFs originais** e comparando com o relatório, a apresentação e o chat
com o Gemini. Ordem: do mais grave (pode ser apontado pela banca) ao cosmético.

## A. Atribuições bibliográficas incorretas (graves)

| # | Onde no TG1 | Afirmação | Realidade (fonte) | Correção sugerida |
|---|---|---|---|---|
| A1 | Rel. §2.3; slides 22–23 | Aldanondo et al. (2020) "investigaram AA2024-T3", "força axial insuficiente → vazios de raiz", "F_z cresce exponencialmente com v", controle de posição vs força | Artigo é em **AA2099-T83/AA2060-T8E30, junta sobreposta**, controle de carga, **sem nenhum vazio**; mede forças X/Y e torque (torque ↑ com v, ↓ com ω; ombro domina torque) | Reescrever usando só o que o artigo diz; afirmação "força axial insuficiente → vazio" citar Threadgill et al. (2009), Mishra & Ma (§2.2, profundidade de inserção) ou Kim et al. (2006) |
| A2 | Rel. §2.1; slides 13–14 | "cold voids vs hot voids" atribuídos a Mishra & Ma (2005) | Termos **não aparecem** em Mishra & Ma. A ideia de janela "hot weld / cold weld" está em **Threadgill et al. (2009)** (citado pelo Ângelo) e a de três defeitos (flash/calor excessivo, cavidade/calor insuficiente) em Kim et al. (2006) | Citar Threadgill (2009) e/ou Kim (2006); manter Mishra & Ma só para 0,6–0,9 T_m, auto-regulação (§6.6), câmara de extrusão (§3.1) |
| A3 | Rel. §2.1; slide 6, 12 | "faixa ótima 0,7–0,8 T_m na borda de ataque" (Mishra & Ma) | Não encontrado | Remover ou buscar fonte |
| A4 | Rel. §2.3; slide 25 | Meyghani & Awang (2022): "modelagem CEL", "θ=0 → metal expelido como rebarba → túnel", "ótimo 1,5–3°", "> 4° superaquecimento/afinamento" | Modelo **Euleriano** com Norton modificado; compara **só 0° e 1,5°**; T 389→413 °C; sem tilt, deformação incompleta na raiz do pino → possível vazio; cita literatura com ótimo 1–2° para AA2219 | Reescrever com os achados reais |
| A5 | Rel. §2.2; slide 24 | Ahmed (2021) + Walla (2024): "razão volume dinâmico/estático", "excentricidade como came", "pulsação" | Volume dinâmico/estático: **Thomas et al.** citado em **Mishra & Ma §2.1** (1,1 / 1,8 / 2,6) e Walaa Ahmed et al. (2024, discussão). Excentricidade-came: **em nenhum dos PDFs**. Ahmed 2021 = bobbin tool, modelo de calor por geometria de pino | Atribuir corretamente; remover excentricidade ou achar fonte |
| A6 | Rel. §2.2; texto | "Walla et al. (2024)" | 1ª autora: **Walaa H. Ahmed** → "Ahmed, Kadhum e Salleh (2024)" | Corrigir citação no texto |
| A7 | Slide 27, 29 | Du et al. atingiram 83,33 % "com CFD + RNA" | 83,3 % = **RNA com parâmetros brutos** (Método 1). Com variáveis do modelo analítico: 93,3 % (NN) / 90 % (DT); com CFD: **96,6 %** | Corrigir; destacar que o benchmark justo para o C_void é **83,3 %** (mesmas entradas) |
| A8 | Resumo; slides 10, 26; Rel. §2.3 | "publicado na *Nature*" | ***npj Computational Materials*** 5:68 (Nature Portfolio) | Corrigir |
| A9 | Slide 26 | colunas do dataset incluem "comprimento do pino L_p", "força axial F_z", "condutividade k" | Dataset tem **pressão axial p (MPa)**, **difusividade α (m²/s)**; **não tem L_p** | Corrigir (a Tabela 3.1 do relatório já está correta) |
| A10 | Slides 9, 21 | CFD "demanda dias de processamento" | Nenhuma fonte informa tempo ("milhares de elementos" está ok: Laska usa ~13 mil). Du et al.: "considerable computational work" | Remover "dias"; usar formulação qualitativa citável |

> **Classificação por origem (2026-10-12):** (1) *troca de fonte* — A2 (conceito em Threadgill 2009), A5 parcial
> (volume dinâmico/estático), A11 (SLS no TG do Ângelo), A12; (2) *dado real mal lido/misturado* — A7, A8, A9 (L_p,
> F_z, k vêm da equação analítica de Du et al.), "CEL" em A4; (3) *sem respaldo em nenhuma fonte do repositório
> (provável invenção do Gemini)* — A1 (estudo de Aldanondo descrito não existe), A3, A4 (θ=0→flash, >4°), A5
> (excentricidade-came), A10 ("dias"), Falcon 9, "Du provou interação não linear de α e σ_y" (Rel. §2.3), A13 (não
> verificado).
| A11 | Rel. §1 | "Falcon 9 e SLS/Artemis" | Não está nas referências do TG1. Ângelo cita Carter (2014, NASA), PAR Systems (2022), Hoffman (2022) para SLS; Mishra & Ma: Boeing Delta, C-17, Eclipse 500 | Citar fonte ou trocar por Delta/Space Shuttle/SLS com fonte |
| A12 | Rel. §2.1 | HAZ 200–250 °C + β'' Mg₅Si₆ atribuídos implicitamente a Mishra & Ma | Vem de **Laska (2023)** e é para **AA6082 (6xxx)**; Mishra & Ma: HAZ = T > 250 °C | Atribuir a Laska; para 2xxx falar de θ'/S' |
| A13 | Rel. §2.1 | grãos "1–5 µm" | Mishra & Ma: faixa típica em µm (0,1–18 µm no resumo) | Ajustar ou citar tabela de Mishra & Ma |

## B. Problemas metodológicos

| # | Problema | Por que importa | Encaminhamento |
|---|---|---|---|
| B1 | Π's não definidos no relatório final; forma (aditiva × multiplicativa) não decidida | É o coração do trabalho | Definir no TG2 com derivação (ver [proposta_modelagem](../05_modelagem/proposta_modelagem.md)) |
| B2 | "Blocos adimensionais homogêneos" — versões anteriores tinham Π_Term = ωR_s³/(v t α) que **não é adimensional** (ω[1/s]·m³ / (m/s · m · m²/s) = s⁻¹·m³·s²/m⁴ = s/m) | Banca de engenharia vai checar | Construir Π's verdadeiramente adimensionais (ex.: ωR_s²/α, ωR_s/v, vR_s/α (Péclet), p/σ_y, t/R_s, R_pt/R_pr) |
| B3 | Meta de 70 %: classe majoritária = 60,2 %; ω sozinho dá 70,4 % in-sample | Meta fraca / trivial | Reportar baselines; manter 70 % como mínimo formal, mas mirar ≥ 80 % (Du et al. NN bruto 83,3 %) |
| B4 | Coluna `Alloy` do CSV errada em 33 linhas | Qualquer uso de "liga" fica errado | Corrigir por α/σ_y (ver [dataset](../01_dados/dataset.md)) |
| B5 | p e θ majoritariamente imputados por Du et al. (`*`) | Termos "dinâmicos" quase sem informação | Declarar; testar modelo com e sem eles |
| B6 | Geometria fixa por estudo → risco de o modelo "aprender o laboratório" | Generalização | Validação por grupo (leave-one-study-out) além do split 78/30 |
| B7 | Tabela de sensibilidade do slide 30: linha de v invertida | Erro físico visível | Corrigir |
| B8 | Tabelas de sensibilidade qualitativas sem fonte | Pode ser questionado | No TG final, substituir por sensibilidade **quantitativa** do modelo calibrado (tornado / OAAT / derivadas logarítmicas) |

## C. Formato (ver [04_formato_ita](../04_formato_ita/))

- Usar a **classe LaTeX do ITA** (capa, folha de rosto, ficha CIP, folha de aprovação, resumo + **abstract**, listas de
  figuras/tabelas/abreviaturas/símbolos, FRD no final).
- Referências em **BibTeX** (abnTeX2 / estilo autor-data do ITA), não digitadas à mão.
- Citação no texto: padrão "(Mishra e Ma 2005)" / "Mishra e Ma (2005)", sem itálico.
- Incluir lista de símbolos (há muitos: ω, v, R_s, R_pr, R_pt, θ, α, σ_y, p, Π_i, β_i, C_void, T).
- O `.tex` atual referencia imagens que não estão no repositório (`Imagens/ita-logo.png`, captura de tela).
