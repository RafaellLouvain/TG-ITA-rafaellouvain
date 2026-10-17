# Apresentação do TG1 (aprovada)

**Arquivo:** `TG1/TG1-Apresentacao-Rafael Louvain.pdf` — 35 slides, 16:9, identidade visual azul ITA (#0056B3) +
amarelo (#FFCC00), fundo off-white. Feita a partir do roteiro gerado com o Gemini (ver
[chat_gemini_resumo](chat_gemini_resumo.md)).

## Roteiro (slide → conteúdo)

| # | Título | Ideia principal / fonte atribuída |
|---|---|---|
| 1 | Capa | título da ficha; TG1 Eng. Mec.-Aer. 2026 |
| 2 | Parte 01 — Introdução | |
| 3 | FSW — surgimento e relevância | TWI 1991; 2xxx/7xxx "não soldáveis"; sustentabilidade |
| 4 | Anatomia — ombro | maior parcela do calor; confinamento hidrostático (evita flash) |
| 5 | Anatomia — pino | calor secundário; mistura 3D |
| 6 | Dinâmica do fluxo | borda de ataque (0,7–0,8 T_m ⚠️), transporte, borda de fuga, AS vs RS, forjamento |
| 7 | Defeitos e impacto estrutural | flash, sulcos, raiz; concentradores de tensão/fadiga |
| 8 | O defeito de vazio (tunneling) | ruptura do balanço de massa; AS; precisa US/RX |
| 9 | Complexidade e limite numérico | multifatorialidade; CFD/MEF "dias" ⚠️ |
| 10 | **Objetivos** | C_void; **meta > 70 %** nos 108 ensaios ("Nature" ⚠️); **hierarquia** cinemática/geometria/dinâmica/térmica |
| 11 | Parte 02 — Revisão | |
| 12 | Janela térmica (Mishra & Ma) | 0,6–0,9 T_m ✔; 0,7–0,8 T_m na borda ⚠️; 400–480 °C |
| 13–14 | Cold vs hot voids (Mishra & Ma) | ⚠️ termos não estão em Mishra & Ma; auto-regulação ✔ (§6.6) |
| 15 | Câmara de extrusão (Mishra & Ma) | ✔ (Reynolds, via Mishra & Ma) |
| 16 | **Equacionamento térmico global** | eq. de Schmidt: Q = (2/3)π[δσ_y/√3 + (1−δ)μp]ω[(R_s³−R_p³)(1+tan α)+R_p³+3R_p²H_p] ✔ |
| 17–19 | Microestrutura: nugget / TMAZ / HAZ | ✔ em geral; faixas de T por zona e "1–5 µm" ⚠️ |
| 20 | Termomecânica e viscosidade (Laska) | eq. de calor no pino; viscosidade f(T, ε̇) ✔; β'' Mg₅Si₆ ✔ (AA6082) |
| 21 | Custo computacional CFD (Laska) | Navier-Stokes ✔; malha fina ✔; "dias" ⚠️ |
| 22 | Força axial e confinamento (Aldanondo) | ⚠️ **conteúdo não corresponde ao artigo** |
| 23 | Interdependência e escala do pino (Aldanondo) | ⚠️ idem; insight útil: "um mesmo parâmetro pode aparecer em mais de um termo" |
| 24 | Regimes de interface e pulsação (Ahmed + Walla) | sliding/sticking ✔; excentricidade ⚠️; pulsação/volume dinâmico ✔ (Walla 2024 / Mishra) |
| 25 | Tilt e rampa de forjamento (Meyghani) | parcialmente ✔; "1,5–3°", ">4°", "θ=0 → flash" ⚠️ |
| 26 | Dataset (Du et al.) | lista L_p, F_z, k ⚠️ (real: p em MPa, α; sem L_p) |
| 27 | Modelagem híbrida (Du et al.) | ⚠️ "CFD + RNA = 83,33 %" — errado (83,3 % = RNA c/ parâmetros brutos; CFD + RNA = 96,6 %) |
| 28 | Parte 03 — Metodologia | |
| 29 | Modelo fenomenológico: ganhos e limitações | Du et al. "caixa-preta"; equação explícita, menos acurada, mais simples |
| 30–32 | **Sensibilidade paramétrica** (tabelas) | para cada variável: efeito "abaixo do ótimo" vs "acima do ótimo" (qualitativo, sem fonte) |
| 33 | Estratégia, calibração e meta | blocos adimensionais que **multiplicam/dividem**; subamostra para ajustar **expoentes inteiros** e coeficientes; threshold; ≥ 70 %; sensibilidade por natureza |
| 34 | **Formulação analítica unificada** | C_void = β₁Π_Geom + β₂Π_Cin + β₃Π_Term + β₄Π_Din (β₁ geométrica, β₂ cinemática, β₃ térmica, β₄ mecânica) |
| 35 | Obrigado | |

## Tabelas de sensibilidade (slides 30–32) — conteúdo

| Parâmetro | Abaixo do ótimo | Acima do ótimo |
|---|---|---|
| v | subaquecimento → cold void | superaquecimento → hot void ⚠️ (invertido: v **baixo** = mais calor) |
| ω | plastificação deficiente | ejeção de massa |
| t | concentração térmica | dissipação severa |
| R_s | déficit térmico | fricção exagerada |
| p (F_z) | falha de vedação | desgaste e afinamento |
| R_pr | cisalhamento pobre | estrangulamento |
| R_pt | déficit hidrodinâmico | atrito no suporte |
| θ | perpendicularidade | concentração elíptica |
| α | retenção energética | dissipação severa |
| σ_y | baixo escoamento | elevado escoamento |

⚠️ **Inconsistência:** no slide 30 a linha de *Welding speed* diz "abaixo do ótimo → subaquecimento/cold voids;
acima → superaquecimento/hot voids". Fisicamente é o contrário (v alto = menos energia por comprimento = frio). Na
versão do chat a tabela estava correta; houve troca na diagramação. Corrigir no TG final.

## Observação: duas formas do C_void na história do TG1

- Slide 33 fala em blocos que "se **multiplicam ou dividem**" e "expoentes inteiros" (forma de **lei de potência**,
  como num número de Reynolds): C_void = (Π_Geom·Π_Cin)/(Π_Term·Π_Comp) (versão "resultados preliminares" do chat).
- Slide 34 e relatório: forma **aditiva ponderada** com β's.
- Ambas são compatíveis se trabalharmos em **log**: log C_void = Σ βᵢ log Πᵢ (lei de potência ↔ soma linear em log,
  β = expoentes). Essa é a ponte natural — ver [proposta_modelagem](../05_modelagem/proposta_modelagem.md).
