# Laska et al. (2023) — temperatura, fluxo e propriedades vs geometria (AA6082, CFD)

**Arquivos:** `referencias/Laska_temp_evolution.pdf` **e** `referencias/s11665-023-08671-1 (1).pdf` — **são o mesmo
arquivo** (md5 idêntico; o nome do segundo é o DOI). Pode-se apagar um deles.

**ABNT:** LASKA, A.; SADEGHI, B.; SADEGHIAN, B.; TAHERIZADEH, A.; SZKODO, M.; CAVALIERE, P. Temperature Evolution,
Material Flow, and Resulting Mechanical Properties as a Function of Tool Geometry during Friction Stir Welding of
AA6082. **Journal of Materials Engineering and Performance**, v. 32, n. 23, p. 10655-10668, 2023.
DOI: 10.1007/s11665-023-08671-1.

## Conteúdo

- AA6082-T651, chapa **3 mm**, fresadora convencional, **1000 rpm, 250 mm/min, tilt 2°**. Duas ferramentas com o
  mesmo ombro: **pino cônico liso ("simple")** e **pino hexagonal com ranhuras ("complex")**.
- Modelo **COMSOL 5.3**: transferência de calor em regime permanente com advecção (ρC_p U·∇T = ∇·(k∇T) + Q̇),
  calor no pino por integrais (μ p (ωr − U_w sinθ)), atrito misto sliding/sticking
  F = (1−S)τ_s + S[δτ_s + (1−δ)μP_N]; **CFD: continuidade + Navier-Stokes, fluido não-Newtoniano** (viscosidade
  função de T e taxa de deformação — Nandan et al.); termo-mecânico para tensão residual.
  **Malha triangular de 0,05 a 5 mm** (mais fina sob a ferramenta); **12 868 elementos** triangulares + 992 de aresta.
- Resultados: T_máx **406 °C** (pino complexo, ~5 % maior); calor do pino complexo ~**20 % maior** (cantos → mais
  cisalhamento); velocidade de fluxo ~40 % maior na região hexagonal; tensão residual ~13 % maior no complexo
  (237 vs 210 MPa). T maior no lado de avanço (AS); HAZ maior no AS; **T máx. sob o ombro**; gradiente térmico maior
  à frente da ferramenta.
- Pino cônico: zona de mistura mais larga (8,25 vs 6,80 mm) — a conicidade facilita o fluxo ao redor do pino; pino
  complexo "aprisiona" material em níveis.
- **Defeitos:** soldas com pino simples mostraram "cavitation loses" superficiais atribuídas a **plastificação
  insuficiente por menor aporte térmico** ➡ suporte direto para "vazio por calor insuficiente".
  "Fatores-chave da qualidade: aporte térmico adequado + mistura adequada do material plastificado."
- Microestrutura: grão na ZM 11 µm (complexo) vs 14 µm (simples); Hall-Petch; dureza ZM 89,5 vs 84,5 HV; metal base
  96 HV; **mínimo na HAZ do lado de avanço (62–67 HV)**; fratura na HAZ-AS; eficiência 72,5 % vs 55,8 %
  (UTS base 371 MPa).
- **Precipitação AA6082:** β'' (Mg₅Si₆) dissolve a **200–250 °C** (atingidos na HAZ); β' (Mg₁.₇Si) forma a ~300 °C →
  superenvelhecimento e amolecimento da HAZ.

## ⚠️ Divergências com o TG1

- TG1: "malhas finíssimas ... **0,05 mm**" ✔ (é o tamanho mínimo). Mas os slides dizem "milhares de elementos e matrizes
  densas, demandando **dias** de processamento" — o artigo **não informa tempo de processamento** e usa só ~13 mil
  elementos. Reformular: "exige malha refinada (até 0,05 mm) e acoplamento térmico-fluido-mecânico", sem afirmar
  "dias" com base nesta fonte. (Du et al. dizem apenas "considerable computational work".)
- TG1 menciona "fase β'' (Mg₅Si₆)" no contexto geral de ligas 2xxx/6xxx — é específico de Al-Mg-Si (6xxx). Para
  2024/2219 os precipitados são S (Al₂CuMg) / θ' (Al₂Cu).
- O slide 20 diz "validando o uso da difusividade no termo térmico do TG" — inferência nossa, não do artigo.
