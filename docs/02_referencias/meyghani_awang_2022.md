# Meyghani & Awang (2022) — influência do ângulo de inclinação (tilt)

**Arquivo:** `referencias/bahman_meyghany_tilt_angle.pdf` (23 p.)

**ABNT:** MEYGHANI, B.; AWANG, M. The Influence of the Tool Tilt Angle on the Heat Generation and the Material
Behavior in Friction Stir Welding (FSW). **Metals**, v. 12, n. 11, p. 1837, 2022. DOI: 10.3390/met12111837.

## Conteúdo real

- Modelo de elementos finitos 3D **Euleriano (CSM)** com **lei de atrito de Norton modificada** (inovação do artigo:
  fórmula fechada da área de contato do ombro inclinado e componentes de velocidade com tilt). AA6061-T6, chapa 6 mm,
  ombro Ø15 mm, pino Ø6 × 6 mm, **800 rpm, 120 mm/min**, penetração 0,1 mm. Johnson-Cook para plasticidade.
- Compara **apenas θ = 0° vs θ = 1,5°**.
- Equações úteis:
  - fluxo de calor por atrito: q̇_f = τ·Δv_g; Norton: τ = −P·g(Δv_g)·Δv_g/|Δv_g|;
  - **P = F/A** com A = 2[R² cos⁻¹(S₂/2R) − (S₂²/4)·tan(cos⁻¹(S₂/2R))] (área de contato do ombro inclinado);
  - **velocidade do material na periferia do ombro = ω·R_s** (ω em rad/s) — e componentes V_x = ωR_s sinβ cosα,
    V_y = ωR_s cosβ, V_z = −ωR_s sinβ sinα (α = tilt);
  - calor por deformação plástica q̇_pl = η σ:ε̇_pl.
- Resultados: sem tilt, T_máx no centro da solda = **389 °C**; com 1,5°, **413 °C** (pico desloca para a parte de trás
  da ferramenta). Lado de avanço ~350–400 °C, retrocesso ~300–350 °C. Com tilt: maior fluxo de calor, deformação
  plástica mais ampla, linhas de corrente mais densas, aquecimento à frente (pré-aquecimento) mais suave.
  **Sem tilt, deformação incompleta na raiz do pino → possível vazio** (Fig. 14).
- Revisão citada: tilt ↑ → torque e forças ↑; tilt ótimo para **AA2219 = 1–2°** (ref [16] do artigo); outros estudos
  usaram 0/1/2°, 1,5/3° e 2–4°. O tilt gera força de forjamento adicional na borda de fuga → "aplicar tilt na prática
  é obrigatório".
- O ombro concentra a maior parte do calor (perfil "V" em T na seção transversal; perfil "M" ao longo da largura).

## ⚠️ Divergência com o TG1

O TG1 afirma: "modelagem CEL", "θ = 0 → metal expelido livremente como rebarba, gerando túnel", "janela ótima
**1,5°–3°**", "desvios > 4° concentram tensões, superaquecimento e afinamento". O artigo:
- é Euleriano (não exatamente CEL — Coupled Eulerian-Lagrangian); dizer "modelo Euleriano de elementos finitos";
- não estuda > 1,5°, não fala em > 4°, nem em rebarba como mecanismo do vazio sem tilt (fala em deformação
  incompleta na raiz do pino → vazio);
- a faixa 1–2° (AA2219) vem de referência citada por eles.

**Uso honesto no TG final:** tilt aumenta forja na traseira, T de pico e mistura → reduz vazio; ombro domina calor;
v_material ≈ ω·R_s (justifica o grupo **ω·R_s/v** como razão entre velocidade periférica e de avanço — candidato
direto a Π cinemático). No dataset θ ∈ {2; 2,5} e 66 % é imputado → efeito praticamente não identificável; tratar o
termo de tilt como fator fenomenológico fixo ou discutir como limitação.
