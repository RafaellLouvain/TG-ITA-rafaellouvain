# Índice de referências (arquivo ↔ citação ABNT ↔ status)

Legenda de status: ✅ lida integralmente e resumida · 🔎 citada por outra fonte, **PDF não disponível** (vale obter).

## PDFs no repositório (`referencias/`)

| Arquivo | Referência ABNT | Resumo | Uso principal no TG |
|---|---|---|---|
| `yang_du_original_reserach_main_source.pdf` | DU, Y.; MUKHERJEE, T.; DEBROY, T. Conditions for void formation in friction stir welding from machine learning. **npj Computational Materials**, v. 5, n. 68, 2019. DOI: 10.1038/s41524-019-0207-y. | ✅ [du_2019_benchmark](du_2019_benchmark.md) | Dataset + benchmark (83,3 % / 90–96,6 %) |
| `Mishra_Ma_fundamentos.pdf` | MISHRA, R. S.; MA, Z. Y. Friction stir welding and processing. **Materials Science and Engineering: R: Reports**, v. 50, n. 1-2, p. 1-78, 2005. DOI: 10.1016/j.mser.2005.07.001. | ✅ [mishra_ma_2005](mishra_ma_2005.md) | Fundamentos, T/T_m vs ω²/v, eq. de Schmidt, câmara de extrusão |
| `Laska_temp_evolution.pdf` (= `s11665-023-08671-1 (1).pdf`, **duplicado**) | LASKA, A.; SADEGHI, B.; SADEGHIAN, B.; TAHERIZADEH, A.; SZKODO, M.; CAVALIERE, P. Temperature Evolution, Material Flow, and Resulting Mechanical Properties as a Function of Tool Geometry during Friction Stir Welding of AA6082. **Journal of Materials Engineering and Performance**, v. 32, n. 23, p. 10655-10668, 2023. DOI: 10.1007/s11665-023-08671-1. | ✅ [laska_2023](laska_2023.md) | CFD (custo), pino e calor, HAZ |
| `aldanondo_tool_geometry.pdf` | ALDANONDO, E.; VIVAS, J.; ÁLVAREZ, P.; HURTADO, I. Effect of Tool Geometry and Welding Parameters on Friction Stir Welded Lap Joint Formation with AA2099-T83 and AA2060-T8E30 Aluminium Alloys. **Metals**, v. 10, n. 7, p. 872, 2020. DOI: 10.3390/met10070872. | ✅ [aldanondo_2020](aldanondo_2020.md) | Torque vs ω, v; delimitação de escopo (lap joint, Al-Li) |
| `bahman_meyghany_tilt_angle.pdf` | MEYGHANI, B.; AWANG, M. The Influence of the Tool Tilt Angle on the Heat Generation and the Material Behavior in Friction Stir Welding (FSW). **Metals**, v. 12, n. 11, p. 1837, 2022. DOI: 10.3390/met12111837. | ✅ [meyghani_awang_2022](meyghani_awang_2022.md) | Tilt, P = F/A, v_material = ωR_s |
| `mohammed_ahemd_mat_heat_tools.pdf` | AHMED, M. M. Z.; HABBA, M. I. A.; JOUINI, N.; ALZAHRANI, B.; SELEMAN, M. M. E.-S.; EL-NIKHAILY, A. Bobbin Tool Friction Stir Welding of Aluminum Using Different Tool Pin Geometries: Mathematical Models for the Heat Generation. **Metals**, v. 11, n. 3, p. 438, 2021. DOI: 10.3390/met11030438. | ✅ [ahmed_2021_bobbin](ahmed_2021_bobbin.md) | Q_El ∝ μωpR_s³/v; ombro 78–88 % do calor |
| `walla_ahmed_review_on_tool_geometry.pdf` | AHMED, W. H.; KADHUM, A. H.; SALLEH, M. S. A Review on Tool Pin Geometry of Friction Stir Welding. **Al-Khwarizmi Engineering Journal**, v. 20, n. 2, p. 39-55, 2024. DOI: 10.22153/kej.2024.02.001. | ✅ [walla_ahmed_2024_review](walla_ahmed_2024_review.md) | Perfis de pino, volume dinâmico/estático |
| `Adiga_2024_Mater._Res._Express_11_076517.pdf` | ADIGA, K.; HERBERT, M. A.; RAO, S. S.; SHETTIGAR, A. K.; SHRIVATHSA, T. V. Development of machine learning regression models for the prediction of tensile strength of friction stir processed AA8090/SiC surface composites. **Materials Research Express**, v. 11, n. 7, p. 076517, 2024. DOI: 10.1088/2053-1591/ad62ba. | ✅ [adiga_2024_e_outros](adiga_2024_e_outros.md) | ML com poucos dados (LR ≈ XGBoost > ANN) |
| `Periodicos-CAPES-BibTex (1).bib` | AGHAJANI DERAZKOLA, H.; SIMCHI, A. Experimental and thermomechanical analysis of the effect of tool pin profile on the friction stir welding of poly(methyl methacrylate) sheets. **Journal of Manufacturing Processes**, v. 34, p. 412-423, 2018. DOI: 10.1016/j.jmapro.2018.06.015. | só metadados | Baixa relevância (PMMA) |
| `TG1_E_TG_FINAL_.../TG_1_FSW (1).pdf` e `TG_Angelo_Bezerra_vEnvio (Updt)_2.pdf` | BEZERRA, Â. C. S. **Análise da energia efetiva por comprimento e ocorrência de defeitos no processo FSW (Friction Stir Welding)**. 2025. 56 f. Trabalho de Conclusão de Curso (Graduação) – Instituto Tecnológico de Aeronáutica, São José dos Campos, 2025. | ✅ [tg_veterano_angelo](../04_formato_ita/tg_veterano_angelo.md) | Formato; trabalho correlato (Q_eff × defeitos) |

## Referências citadas nas fontes que valem buscar (CAPES/CAFe) 🔎

Prioridade alta (preenchem lacunas do TG1):
- THREADGILL, P. L.; LEONARD, A. J.; SHERCLIFF, H. R.; WITHERS, P. J. Friction stir welding of aluminium alloys.
  **International Materials Reviews**, v. 54, n. 2, p. 49-93, 2009. → hot/cold welds, janela de processo, efeito da
  força axial, causas de vazios (substitui as atribuições erradas a Aldanondo e Mishra & Ma).
- ARBEGAST, W. J. A flow-partitioned deformation zone model for defect formation during friction stir welding.
  **Scripta Materialia**, v. 58, p. 372-376, 2008. → modelo de zonas de metalworking + balanço de massa → defeitos.
- KIM, Y. G.; FUJII, H.; TSUMURA, T.; KOMAZAKI, T.; NAKATA, K. Three defect types in friction stir welding of aluminum
  die casting alloy. **Materials Science and Engineering: A**, v. 415, p. 250-254, 2006. → flash (calor excessivo),
  cavidade/sulco (calor insuficiente), pressão anormal. *(referência conhecida da literatura; conferir dados ao obter)*
- ARORA, A.; DEBROY, T.; BHADESHIA, H. K. D. H. Back-of-the-envelope calculations in friction stir welding—Velocities,
  peak temperature, torque, and hardness. **Acta Materialia**, v. 59, p. 2020-2028, 2011. → fórmulas fechadas para
  T_pico e torque (ref. 40 de Du et al.) — **muito útil para o Π_Term**.
- ROY, G. G.; NANDAN, R.; DEBROY, T. Dimensionless correlation to estimate peak temperature during friction stir
  welding. **Science and Technology of Welding and Joining**, v. 11, p. 606-608, 2006. → correlação **adimensional**
  de T_pico (ref. 41 de Du et al.) — **diretamente alinhada com a proposta do TG**.
- QIAN, J. et al. An analytical model to optimize rotation speed and travel speed of friction stir welding for
  defect-free joints. **Scripta Materialia**, v. 68, p. 175-178, 2013. → critério analítico ω–v sem defeito
  (ref. 25 de Du et al.; T_pico 80–90 % de T_solidus).
- ARORA, A.; DE, A.; DEBROY, T. Toward optimum friction stir welding tool shoulder diameter. **Scripta Materialia**,
  v. 64, p. 9-12, 2011. (ref. 39) · SCHMIDT, H.; HATTEL, J.; WERT, J. An analytical model for the heat generation in
  friction stir welding. **Modelling Simul. Mater. Sci. Eng.**, v. 12, p. 143-157, 2004.

Prioridade média: NANDAN, R.; DEBROY, T.; BHADESHIA, H. Recent advances in friction-stir welding. **Prog. Mater.
Sci.**, v. 53, p. 980-1023, 2008 · COLEGROVE & SHERCLIFF (2005) · HAMILTON & DYMEK (2008) · KASHAEV et al. (2018) ·
FILHO, J. A. P. C. (2018) dissertação ITA (dados do Ângelo) · CARTER (2014, NASA) para aplicações aeroespaciais.

As 13 fontes primárias do dataset (refs. 6–18 de Du et al.) estão listadas em [dataset](../01_dados/dataset.md).
