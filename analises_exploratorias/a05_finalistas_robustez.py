"""A05 — Finalistas e testes de robustez.

Índices de 1 número + 1 limiar (vazio se I < I_crit):
  F0  N                                  (baseline: rotação pura)
  F1  ω·R_s                              (velocidade periférica do ombro; expoente vindo da física, sem busca)
  F2  ω·(p/σ_y)^0,5
  F3  ω·R_s·(p/σ_y)^0,5
  F4  ω·R_s^0,5·t·(p/σ_y)·α^-0,5         (melhor da grade com 4 termos — suspeita de sobreajuste)
Testes: split 78/30 estratificado repetido (como Du et al.), LOSO, sensibilidade/especificidade, por liga,
sem a ref. 15 (v suspeito), e substituindo p assumido por um valor único (para ver se o sinal de p é real).
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit

from dados_fsw import carregar
from metricas import avaliar_indice, melhor_limiar

FINALISTAS = {
    "F0  N": lambda d: d.N,
    "F1  ω·R_s": lambda d: d.w * d.Rs,
    "F2  ω·(p/σ_y)^0,5": lambda d: d.w * (d.p / d.sy) ** 0.5,
    "F3  ω·R_s·(p/σ_y)^0,5": lambda d: d.w * d.Rs * (d.p / d.sy) ** 0.5,
    "F4  ω·R_s^0,5·t·(p/σ_y)·α^-0,5": lambda d: d.w * d.Rs**0.5 * d.t * (d.p / d.sy) * d.alpha**-0.5,
}


def split_78_30(x, y, n=500):
    sss = StratifiedShuffleSplit(n_splits=n, test_size=30, random_state=1)
    accs = []
    for tr, te in sss.split(x.reshape(-1, 1), y):
        l, _ = melhor_limiar(x[tr], y[tr], -1)
        accs.append(((-x[te] > -l).astype(int) == y[te]).mean())
    a = np.array(accs)
    return a.mean(), np.percentile(a, 5), np.percentile(a, 95), (a >= 0.70).mean()


def main():
    d = carregar()
    y, g = d.void.values, d.estudo.values
    linhas = []
    for nome, f in FINALISTAS.items():
        x = np.log(f(d).values)
        r = avaliar_indice(x, y, g, -1)
        pred = (x < r["limiar"]).astype(int)
        sens = (pred[y == 1] == 1).mean(); esp = (pred[y == 0] == 0).mean()
        m, p5, p95, frac70 = split_78_30(x, y)
        por_liga = {f"acc_{l}": (pred[d.liga == l] == y[d.liga == l]).mean() for l in ["2024", "2219", "6061"]}
        # sem ref 15
        d2 = carregar(excluir_refs=[15]); x2 = np.log(f(d2).values)
        r2 = avaliar_indice(x2, d2.void.values, d2.estudo.values, -1)
        # p assumido -> valor único (mediana dos assumidos): se o desempenho cai, o sinal vinha das suposições
        d3 = carregar(); d3.loc[d3.p_assumido, "p"] = 13.0; x3 = np.log(f(d3).values)
        r3 = avaliar_indice(x3, y, g, -1)
        linhas.append(dict(indice=nome, limiar=np.exp(r["limiar"]), acc_in=r["acc_in"], acc_cv=r["acc_cv"],
                           acc_loso=r["acc_loso"], sens=sens, espec=esp, split78_30_media=m, split_p5=p5,
                           split_p95=p95, frac_splits_ge70=frac70, **por_liga, loso_sem_ref15=r2["acc_loso"],
                           cv_sem_ref15=r2["acc_cv"], loso_p_assumido_13=r3["acc_loso"]))
    R = pd.DataFrame(linhas)
    R.to_csv("resultados/a05_finalistas.csv", index=False)
    pd.set_option("display.width", 250)
    print(R.T.to_string(float_format=lambda v: f"{v:.3g}"))


if __name__ == "__main__":
    main()
