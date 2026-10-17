# Adiga et al. (2024) + outras referências avulsas

## Adiga et al. (2024) — ML de regressão para UTS em FSP

**Arquivo:** `referencias/Adiga_2024_Mater._Res._Express_11_076517.pdf` (16 p.) — **não é citado no TG1.**

**ABNT:** ADIGA, K.; HERBERT, M. A.; RAO, S. S.; SHETTIGAR, A. K.; SHRIVATHSA, T. V. Development of machine learning
regression models for the prediction of tensile strength of friction stir processed AA8090/SiC surface composites.
**Materials Research Express**, v. 11, n. 7, p. 076517, 2024. DOI: 10.1088/2053-1591/ad62ba.

- FSP (processamento por fricção, variante do FSW) de AA8090 (Al-Li) + SiC; 20 ensaios (planejamento CCD: ω 800/1100/
  1400 rpm, v 25/50/75 mm/min, largura do sulco 1,0/1,4/1,8 mm); alvo = UTS (regressão).
- Modelos: regressão linear (LR), SVR, ANN (Keras, Adam, MSE), XGBoost; split 80/20; métricas R², RMSE, MAE.
- Resultados teste: XGBoost R² = 97,84 %, LR 97,65 %, SVR 96,2 %, **ANN 86,08 % (pior)**.
- Mensagem útil para nós: **com datasets pequenos, modelos simples (LR, SVR, árvores) generalizam melhor que ANN**;
  ANN precisa de muitos dados. Também: RSM só é preciso numa faixa limitada de parâmetros.

**Uso no TG:** justificar que um modelo simples/explicito pode competir com NN em dataset pequeno (108 pontos);
metodologia de split treino/teste e métricas; contexto de ML em processos de fricção. Os "You may also like" do PDF
apontam revisões relevantes: El-Zathry et al. (ML em técnicas de fricção — revisão), Loganathan et al. (ML para
qualidade superficial em FSW).

## Derazkola & Simchi (2018) — só no arquivo .bib

**Arquivo:** `referencias/Periodicos-CAPES-BibTex (1).bib` (exportado do Periódicos CAPES; **não há o PDF**).

AGHAJANI DERAZKOLA, H.; SIMCHI, A. Experimental and thermomechanical analysis of the effect of tool pin profile on the
friction stir welding of poly(methyl methacrylate) sheets. **Journal of Manufacturing Processes**, v. 34, p. 412-423,
2018. DOI: 10.1016/j.jmapro.2018.06.015.

(No .bib o campo journal está como "Elsevier ScienceDirect Journals" e o tipo como `@Artigo` — corrigir se for usar
BibTeX: `@article`, `journal = {Journal of Manufacturing Processes}`, `pages = {412--423}`.) É sobre FSW de **PMMA**
(polímero) — relevância baixa para ligas de Al; possivelmente útil só para geometria do pino. Não citado no TG1.
