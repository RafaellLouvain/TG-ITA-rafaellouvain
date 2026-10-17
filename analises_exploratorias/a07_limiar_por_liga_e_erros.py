"""A07 — (i) Limiar de ω·R_s por liga (tabela de 3 valores) vs. limiar universal; (ii) onde cada índice erra.

LOSO: o limiar da liga do estudo deixado de fora é estimado só com os outros estudos daquela liga.
"""
import numpy as np
import pandas as pd

from dados_fsw import carregar
from metricas import melhor_limiar

INDICES = {
    "F1 ω·R_s": lambda d: d.w * d.Rs,
    "F3 ω·R_s·(p/σ_y)^0,5": lambda d: d.w * d.Rs * np.sqrt(d.p / d.sy),
}


def loso_por_liga(z, y, g, liga):
    pred = np.zeros_like(y)
    for gg in np.unique(g):
        m = g == gg
        mesma = (liga == liga[m][0]) & ~m
        base = mesma if len(np.unique(y[mesma])) == 2 else ~m   # se não houver dados da liga, usa todos
        l, _ = melhor_limiar(z[base], y[base], -1)
        pred[m] = (z[m] < l).astype(int)
    return pred


def main():
    d = carregar()
    y, g, liga = d.void.values, d.estudo.values, d.liga.values
    tab = []
    for nome, f in INDICES.items():
        z = np.log(f(d).values)
        lims = {l: np.exp(melhor_limiar(z[liga == l], y[liga == l], -1)[0]) for l in ["2024", "2219", "6061"]}
        acc_in = np.mean([(z[i] < np.log(lims[liga[i]])) == y[i] for i in range(len(y))])
        p_liga = loso_por_liga(z, y, g, liga)
        # universal LOSO
        p_uni = np.zeros_like(y)
        for gg in np.unique(g):
            m = g == gg; l, _ = melhor_limiar(z[~m], y[~m], -1); p_uni[m] = (z[m] < l).astype(int)
        print(f"{nome}: limiar por liga (in-sample) = " + ", ".join(f"{k}: {v:.3g}" for k, v in lims.items()))
        print(f"   acc in-sample por liga = {acc_in:.3f} | LOSO por liga = {(p_liga == y).mean():.3f} "
              f"| LOSO universal = {(p_uni == y).mean():.3f}")
        for est, s in d.assign(ok=(p_uni == y)).groupby("estudo", sort=False):
            tab.append(dict(indice=nome, estudo=est, liga=s.liga.iloc[0], n=len(s), acertos_LOSO_universal=int(s.ok.sum())))
    T = pd.DataFrame(tab).pivot_table(index=["estudo", "liga", "n"], columns="indice", values="acertos_LOSO_universal")
    T.to_csv("resultados/a07_acertos_por_estudo.csv")
    print("\nAcertos por estudo (LOSO, limiar universal):\n", T.to_string())


if __name__ == "__main__":
    main()
