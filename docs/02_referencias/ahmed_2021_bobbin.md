# Ahmed et al. (2021) — modelos de geração de calor, bobbin tool, geometrias de pino

**Arquivo:** `referencias/mohammed_ahemd_mat_heat_tools.pdf` (18 p.)

**ABNT:** AHMED, M. M. Z.; HABBA, M. I. A.; JOUINI, N.; ALZAHRANI, B.; SELEMAN, M. M. E.-S.; EL-NIKHAILY, A. Bobbin Tool
Friction Stir Welding of Aluminum Using Different Tool Pin Geometries: Mathematical Models for the Heat Generation.
**Metals**, v. 11, n. 3, p. 438, 2021. DOI: 10.3390/met11030438.

(O TG1 lista como "AHMED, M. M. Z. et al." — ok.)

## Conteúdo

- **Bobbin tool FSW** (BT-FSW: dois ombros, superior e inferior, sem placa de apoio), AA1050-H14 (σ_y = 60 MPa),
  5–10 mm, junta sobreposta; ω = 600 rpm constante, v = 200–1000 mm/min; pinos **cilíndrico, quadrado, triangular**
  (círculo inscrito Ø10 mm), ombros Ø25 mm côncavos (~6°). Temperatura medida por infravermelho.
- **Modelo de calor** (adaptado de Schmidt/Hattel, Colligan & Mishra, Ðurđanović, Nandan):
  - Q_total = Q_ombro_sup + Q_ombro_inf + Q_pino; cada parcela Q = (1−δ)Q_atrito + δ·Q_deformação (δ = grau de
    aderência; δ_ombro = 0,2, δ_pino = 0,1; literatura: δ ~ 0,1);
  - dQ = ω dM = ω R τ_s dA; **τ_s = μ p** (escorregamento) ou τ_s = σ_y/√3 (aderência);
  - **μ = μ₀[1 − exp(−δ ω R_m / (ω₀ R_s))]**, μ₀ = 0,45, μ entre 0,4–0,5 (cai com T);
  - **σ_y(T) = σ_y [1 − (T − T_R)/(T_m − T_R)]** (amolecimento linear com T homóloga);
  - ombro: **Q_s = 2πωτ_s (R_s³ − R_p³)/(3 cos α)** (α = ângulo de concavidade do ombro);
  - pino cilíndrico: **Q_p = 2πω l_p R_p² τ_s**;
  - pino quadrado: Q_p = 2√2 ζ ω a² l_p τ_s; triangular: √3 ω a² l_p τ_s;
  - **energia por unidade de comprimento: Q_El = (2πμωp / v) · [(R_s³ − R_p³)/(3cos α) + l_p R_p²]**
    ➡ forma exatamente do tipo "ω·p·R_s³ / v" — **base física direta para o C_void**.
- **Correlação empírica temperatura–energia (AA1050):** T_w/T_m = 0,247 + 0,0002·Q_El − 2,9×10⁻⁸·Q_El²
  (Q_El em J/mm; R² = 0,929).
- Resultados: ombro gera **78 % (quadrado), 83 % (cilíndrico), 88 % (triangular)** do calor. Pino quadrado → maior
  calor/temperatura (área de pino maior). Q_El vai de ~3,4 kJ/mm (200 mm/min) a ~0,9 kJ/mm (1000 mm/min).
  T medida 240–385 °C.
- Calor ∝ ω, μ, espessura, R_s, concavidade do ombro, área do pino; **∝ 1/v**.
- Razão ótima ombro/pino reportada: **2,5:1 a 3:1** (ref [20] do artigo). Pino deve resistir às forças mas ser
  pequeno o bastante para mexer o material; comprimento do pino ~ espessura.
- Revisão interna cita: pino excêntrico gera **menos** calor (Essa et al.); pinos poligonais aumentam T de pico com o
  nº de lados (Mehat et al.); calor por atrito ~95,6 % do total (Bastier et al.).

## Uso no TG

- Fonte primária para a **equação de Q (ombro + pino)** e para o argumento "**ombro domina o aporte térmico**
  (R_s³)". Também para a dependência **σ_y(T)** e para **Q_El ∝ ω p R_s³ / v**.
- ⚠️ No TG1 (§2.2 e slide 24) atribui-se a Ahmed (2021) e Walla et al. (2024) a "Razão entre Volume Dinâmico e
  Estático do pino", "pulsação" de perfis poligonais e "excentricidade como came". Ahmed **não** discute volume
  dinâmico/estático nem pulsação; só menciona de passagem pinos excêntricos (menos calor) e poligonais (mais T). Essas
  ideias vêm da revisão de Walla/Ahmed 2024 — ver [walla_ahmed_2024_review](walla_ahmed_2024_review.md).
- Cuidado: é BT-FSW em AA1050 (liga mole), não FSW convencional em ligas aeronáuticas; usar como modelo de calor,
  não como dado de vazio.
