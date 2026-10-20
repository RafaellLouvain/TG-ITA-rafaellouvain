# Referências V2 (baixadas em 2026-10-19) — resumos verificados

PDFs em `referencias/V2/`. Lidos integralmente. Também em V2: `fox_mecanica_dos_fluidos.md` (livro-texto, sem PDF).

Descartados (baixados, mas fora de escopo): dois artigos de Ahmed, Wynne, Rainforth e Threadgill sobre
**textura cristalográfica** (Scripta Materialia 2008 e 2010) — relevância baixa para vazios.
Não obtidos: Threadgill et al. (2009, *Int. Mater. Rev.*) e Roy, Nandan e DebRoy (2006) — este último tem a
correlação reproduzida e melhorada por Arora et al. (2011), abaixo.

---

## 1. Arbegast (2008) — modelo de zonas de deformação e formação de defeitos

**ABNT:** ARBEGAST, W. J. A flow-partitioned deformation zone model for defect formation during friction stir
welding. **Scripta Materialia**, v. 58, n. 5, p. 372-376, 2008. DOI: 10.1016/j.scriptamat.2007.10.031.
Arquivo: `referencias/V2/arbegast_2008_flow_partitioned_defects.pdf` (5 p., *Viewpoint paper*, só conceito — a
validação experimental "está em andamento").

- FSW como processo de conformação com zonas sequenciais: pré-aquecimento, deformação inicial, **extrusão**,
  **forjamento** e resfriamento. Na zona de extrusão o fluxo é cíclico, em padrão de "limpeza" (*wiping*).
- Material inicial = área projetada do pino; "material em excesso" é adicionado na zona de extrusão conforme
  projeto da ferramenta, tensão de escoamento, temperatura e parâmetros.
- "Isoterma crítica": onde a tensão é menor que a de escoamento → limite da ZTMA.
- **Defeitos (Fig. 2):** geométricos (falta de penetração/fusão — penetração ou alinhamento incorretos) e de
  **fluxo**, que ocorrem **fora da janela de processo, em condições muito quentes ou muito frias**:
  - **Quente (condição de *stick*)**: fluxo excessivo → rebarba (*flash*), *galling* superficial, colapso do nugget.
  - **Frio (condição de *slip*)**: fluxo insuficiente → falta de preenchimento superficial, **wormhole (vazio)** ou
    falta de consolidação **no lado de avanço** (em ordem crescente de força de forja).
  - Ótimo: temperatura em que ocorre fluxo *stick–slip* e o material que sai da frente é **exatamente igual** ao que
    volta para a região atrás do pino.
- Zonas de fluxo: I (lado de avanço), II (lado de recuo, desce e contorna o pino), III (sob o ombro, arrastada do
  recuo para o avanço e bombeada para baixo para preencher a zona I), IV (sob a ponta do pino), V (recirculação em
  condição muito quente). **Perda de material das zonas II, III ou IV** (por rebarba, coroa elevada, separação de
  chapas) → material insuficiente na zona I → **falta de preenchimento, wormhole ou falta de consolidação**.
- Efeito da rotação (ferramenta e avanço fixos, Fig. 3): ω↑ → mais material gira sob o ombro, mais material passa
  pelo lado de recuo que pelo de avanço, zonas de extrusão mais estreitas (T maior), mais material sob a ponta;
  ω excessivo → condição *stick*, fluxo pelo ombro domina.
- **Balanço de massa (eq. 1):** fluxo crítico de massa por revolução para evitar vazio
  **M_cr = ρ (a · b · φ²)⁻¹**, com a = fator de forma do pino (mm⁻¹), b = fator de forma do ombro (mm⁻²) e
  **φ = ω/ν** (rotação/avanço, mm⁻¹). **Vazio quando a massa que chega à zona de forjamento é menor que M_cr**;
  a diferença é a "deficiência de massa do wormhole" M_wh (eq. 6).
  ➡ φ = ω/v ao **quadrado** — mesma combinação do pseudoíndice de calor ω²/v.

**Uso no TG:** fonte primária da janela quente/fria e do mecanismo do vazio (substitui os "cold/hot voids" sem
fonte do TG1); base conceitual do "vazio = falha no balanço de massa" (seções 2.3 e 2.5); motivação para um índice
que combine geometria do pino, do ombro e ω/v.

---

## 2. Arora, DebRoy e Bhadeshia (2011) — cálculos "back-of-the-envelope"

**ABNT:** ARORA, A.; DEBROY, T.; BHADESHIA, H. K. D. H. Back-of-the-envelope calculations in friction stir welding
– Velocities, peak temperature, torque, and hardness. **Acta Materialia**, v. 59, n. 5, p. 2020-2028, 2011.
DOI: 10.1016/j.actamat.2010.12.001.
Arquivo: `referencias/V2/arora_debroy_bhadeshia_2011_back_of_envelope.pdf`. (Ref. 40 de Du et al.)

- Motivação: modelos numéricos (Navier-Stokes + energia + constitutivas) são "complexos e computacionalmente
  intensivos"; faltam métodos analíticos simples como os de Rosenthal na soldagem por fusão — **mesmo argumento do
  TG**.
- **Campo de velocidade:** escoamento de fluido incompressível entre um disco rotativo (ombro) e um estacionário;
  u = rωF, v = rωG, w = dωH; escorregamento parcial na interface δ = 0,2 + 0,8[1 − exp(−δ₀ (ω/ω₀)(R_M/R_S))].
  Velocidade máxima na interface ombro–peça, decrescendo com a profundidade; erro de 10–17% vs. modelo numérico.
- **Temperatura de pico — correlação adimensional** (de Roy, Nandan e DebRoy, 2006, recalibrada):
  - T* = (T_P − T_in)/(T_S − T_in) (T_S = solidus);
  - **Q\* = σ₈ A ω C_P φ / (k U²)** — σ₈: tensão de escoamento a 0,8 T_S; A: área da seção do ombro; ω: rotação;
    C_P: calor específico; k: condutividade; U: velocidade de avanço; φ = [(kρC_P)_peça/(kρC_P)_ferramenta]^{1/2};
  - **T\* = 0,151 log₁₀(Q\*) + 0,097**, válida para 4×10² < Q\* < 3,7×10⁵, desvio-padrão 0,01;
  - verificada contra temperaturas de pico medidas vs. *weld pitch* (rotações/mm) para AA2024, 5083, 7075 (erros 3–9%).
- **Torque:** τ = Y/√3 (Y na temperatura média ≈ 0,95 T_P); τ_t = (1−δ)τ + δμ_f P_N; **T = 2πR_S³τ_t/3**; torque
  diminui com o aumento da rotação (material mais macio). Boa concordância para AA2524 e Ti-6Al-4V.
- Dureza da ZTMA correlacionada com a composição química (eq. 13).

**Uso no TG:**
- Seção 2.2 (temperatura) e 2.8 (índices adimensionais): **é um índice adimensional publicado para FSW** — precedente
  direto para o C_void.
- Metodologia: candidato a Π_Term com base física. ⚠ Nas análises exploratórias, um índice parecido com Q\*
  (σ_y πR_s² ω/(ρ α v²), sem σ₈ nem φ) teve desempenho fraco (≈59% CV), porque o termo U² dá peso grande à
  velocidade de avanço, que no dataset quase não discrimina vazio. Vale testar a versão completa (com σ₈ estimado
  e T* em relação a 80–90% da solidus).

---

## 3. Ahmed, Wynne, Rainforth, Addison, Martin e Threadgill (2019) — geometria da ferramenta em chapa grossa

**ABNT:** AHMED, M. M. Z.; WYNNE, B. P.; RAINFORTH, W. M.; ADDISON, A.; MARTIN, J. P.; THREADGILL, P. L. Effect of
tool geometry and heat input on the hardness, grain structure, and crystallographic texture of thick-section
friction stir-welded aluminium. **Metallurgical and Materials Transactions A**, v. 50, n. 1, p. 271-284, 2019.
DOI: 10.1007/s11661-018-4996-2. Arquivo: `referencias/V2/ahmed_threadgill_2019_tool_geometry_thick_section.pdf`.
(Citar como "AHMED et al., 2019" — atenção para não confundir com AHMED, M. M. Z. et al., 2021 e AHMED, W. H. et
al., 2024.)

- AA6082-T6, 38 mm, penetração 32 mm, TWI. Pino **cônico** (TPT, conicidade 28,8°) vs. pino **paralelo** (PPT,
  Ø19 e Ø12 mm), ombros Ø40/Ø30 mm; 400–600 rpm, 62,5–125 mm/min.
- **Pino cônico → taxa de deformação e tamanho de grão variam ao longo da espessura** (grão ~11 µm no topo vs. ~5 µm
  na base); pino paralelo → uniformes. Taxa de deformação estimada 217–362 s⁻¹ (velocidade de cisalhamento
  V_s = 2ωP_r; γ̇ = V_s/S_x; ε̇ = γ̇/√3), relação com Zener–Hollomon.
- Temperatura no topo maior que na base do nugget (560–634 °C no topo, 530–577 °C na base); calor por comprimento e
  largura da ZAC aumentam com a redução da velocidade de avanço; torque 200–329 N·m.
- Razão profundidade do pino / largura do ombro acima de 0,8 resultou em juntas sem defeitos; uma região não
  consolidada apareceu em uma das soldas (PPT2, menor velocidade).
- Revisão citada: Elangovan e Balasubramanian (AA2219, 6 mm) — pino quadrado deu zona livre de defeitos em
  1500–1700 rpm.

**Uso no TG:** seção 2.3/2.6 — justifica fisicamente a variável **conicidade (R_pt/R_pr)** do dataset (a
conicidade altera a taxa de deformação e a temperatura ao longo da espessura); temperatura maior no topo (ombro).
