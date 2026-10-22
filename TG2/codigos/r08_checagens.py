"""R08 -- Checagens de diagnóstico do modelo B: o desempenho baixo vem de sobreajuste?
(i) mesma lei de potência com regularização L2 (só diagnóstico); (ii) diferença treino × teste."""
from functools import partial

import pandas as pd

from dados import SAIDA, carregar
from modelos import CONJUNTOS_B
from nucleo import LeiPotencia
from validacao import loso, repetidos

d = carregar()
linhas = []
for nome, termos in CONJUNTOS_B.items():
    for l2 in [0.0, 1.0, 10.0, 100.0]:
        fab = partial(LeiPotencia, termos, "acc", "balanceado", l2)
        r = repetidos(fab, d, n=500, processos=3)
        lo, _, _ = loso(fab, d, processos=3)
        linhas.append({"conjunto": nome, "l2": l2, "rep_tr_acc": r["tr_acc"].mean(), "rep_acc": r["acc"].mean(),
                       "gap_treino_teste": r["tr_acc"].mean() - r["acc"].mean(), "rep_bal": r["bal"].mean(),
                       "loso_acc": lo["acc"]})
        print(linhas[-1], flush=True)
pd.DataFrame(linhas).to_csv(SAIDA / "tabelas" / "r08_B_regularizacao.csv", index=False, float_format="%.4f")

# (iii) O problema é a exigência de adimensionalidade? Mesma logística, mas com variáveis dimensionais livres.
dim = {"ln ω + ln R_s (dimensional, expoentes livres)": ["w", "Rs"],
       "10 variáveis brutas (dimensional, expoentes livres)": ["w", "v", "Rs", "Rpr", "Rpt", "t", "alpha", "p",
                                                               "theta", "sy"]}
linhas = []
for nome, termos in dim.items():
    for crit in ["acc", "bal"]:
        fab = partial(LeiPotencia, termos, crit, "balanceado")
        r = repetidos(fab, d, n=500, processos=3)
        lo, _, _ = loso(fab, d, processos=3)
        linhas.append({"modelo": nome, "criterio": crit, "rep_tr_acc": r["tr_acc"].mean(), "rep_acc": r["acc"].mean(),
                       "rep_bal": r["bal"].mean(), "loso_acc": lo["acc"], "loso_bal": lo["bal"]})
        print(linhas[-1], flush=True)
pd.DataFrame(linhas).to_csv(SAIDA / "tabelas" / "r08_dimensional_livre.csv", index=False, float_format="%.4f")
