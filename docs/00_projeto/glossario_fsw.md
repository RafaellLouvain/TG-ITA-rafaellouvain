# Glossário e símbolos (FSW + notação do TG)

## Processo

- **FSW (Friction Stir Welding)** — soldagem por fricção e mistura mecânica; estado sólido; TWI (UK), 1991 (Wayne
  Thomas). **FSP** — processamento por fricção (variante para modificar microestrutura). **BT-FSW** — bobbin tool
  (dois ombros, sem placa de apoio).
- **Ombro (shoulder)** — parte de maior diâmetro; gera a maior parte do calor (∝ R_s³) e confina o material.
- **Pino (pin/probe)** — penetra a junta; mistura/extruda o material; raio na raiz R_pr e na ponta R_pt (cônico se
  R_pt < R_pr).
- **Lado de avanço (AS)** — onde a velocidade tangencial da ferramenta tem o mesmo sentido do avanço; **lado de recuo
  (RS)** — sentido oposto. Material passa preferencialmente pelo RS; vazios tendem a ficar no **AS**.
- **Borda de ataque / de fuga (leading / trailing edge)** — frente / traseira da ferramenta.
- **Tilt (θ)** — inclinação do eixo da ferramenta para trás (tipicamente 1–3°) → forja na traseira.
- **Weld pitch** — avanço por rotação = v/ω (mm/rot). Inverso: rotações por mm.
- **Pseudo heat index** — ω²/v (Arbegast & Hartley); T/T_m = K(ω²/(v·10⁴))^α, K 0,65–0,75, α 0,04–0,06.
- **Sticking / sliding** — adesão total (calor por deformação, τ = σ_y/√3) / escorregamento (atrito, τ = μp);
  δ = fração de sticking.
- **Câmara de extrusão (Reynolds)** — ombro (teto) + placa de apoio (piso) + metal frio (paredes) + pino; vazio =
  falha no balanço de massa.
- **Hot weld / cold weld** — janela de processo limitada por excesso de calor (flash, fusão incipiente) e falta de
  calor (mistura insuficiente, vazios) — Threadgill et al. (2009).

## Defeitos

- **Vazio / túnel / wormhole** — cavidade volumétrica interna longitudinal (alvo do dataset).
- **Flash (rebarba)** — material expelido sob o ombro (calor/penetração excessivos).
- **Kissing bond / joint line remnant** — linha de óxido/ligação fraca; **falta de penetração (root flaw)**.
- **Hook / cold lap** — típicos de junta sobreposta (Aldanondo 2020).

## Microestrutura

- **Nugget / SZ / DXZ** — zona de mistura, recristalização dinâmica, grão fino equiaxial, anéis de cebola.
- **TMAZ** — zona termomecanicamente afetada: grãos deformados, sem recristalização.
- **HAZ (ZAC)** — só ciclo térmico; superenvelhecimento → menor dureza; fratura em tração costuma ocorrer aí.
- Precipitados: 6xxx → β'' (Mg₅Si₆), β'; 2xxx → θ' (Al₂Cu), S/S' (Al₂CuMg).

## Notação do TG (proposta — manter consistente no texto)

| Símbolo | Significado | Unidade (dataset) |
|---|---|---|
| v | velocidade de avanço | m/s |
| ω | rotação | rps no CSV (rad/s = 2π·rps) |
| t | espessura da chapa | m |
| R_s | raio do ombro | m |
| R_pr, R_pt | raio do pino na raiz / ponta | m |
| p | pressão axial | MPa |
| θ | ângulo de inclinação | ° |
| α | difusividade térmica | m²/s |
| σ_y | limite de escoamento (temp. ambiente) | MPa |
| Π_i | grupos adimensionais | – |
| β_i | expoentes/pesos calibrados | – |
| C_void | Coeficiente Analítico de Vazio | – |
| T (ou C*) | limiar de decisão | – |
| T_m, T_s | temperatura de fusão / solidus | K ou °C |
