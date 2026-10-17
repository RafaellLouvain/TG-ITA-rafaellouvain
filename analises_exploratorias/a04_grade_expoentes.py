"""A04 — Busca em grade de índices com expoentes "redondos" + UM limiar universal (formato chão de fábrica).

I = ω · R_s^a · t^b · (p/σ_y)^c · α^e · v^f       (vazio se I < I_crit)
Expoentes em passos de 0,5 (f em 0,25). Avaliação: acurácia CV (limiar escolhido no treino) e LOSO.
ATENÇÃO: escolher o melhor da grade usando a própria CV/LOSO é otimista (seleção de modelo nos mesmos dados).
Por isso também reportamos uma CV ANINHADA para o procedimento "escolher expoentes + limiar".
"""
import itertools

import numpy as np
import pandas as pd

from dados_fsw import carregar
from metricas import CV, avaliar_indice, melhor_limiar

GRADE = dict(a=np.arange(0, 3.01, 0.5), b=np.arange(-1, 1.01, 0.5), c=np.arange(-1, 1.01, 0.5),
             e=np.arange(-2, 1.01, 0.5), f=np.arange(-0.5, 0.51, 0.25))


def lnI(d, a, b, c, e, f):
    return (np.log(d.w) + a * np.log(d.Rs) + b * np.log(d.t) + c * np.log(d.p / d.sy)
            + e * np.log(d.alpha) + f * np.log(d.v)).values


def acc_limiar(z, y, idx_tr, idx_te):
    l, _ = melhor_limiar(z[idx_tr], y[idx_tr], -1)
    return ((-z[idx_te] > -l).astype(int) == y[idx_te]).mean()


def main():
    d = carregar()
    y, g = d.void.values, d.estudo.values
    combos = list(itertools.product(*GRADE.values()))
    Z = {cmb: lnI(d, *cmb) for cmb in combos}

    # 1) avaliação de todos os combos (in-sample e LOSO rápidos; CV completa só no top)
    linhas = []
    for cmb, z in Z.items():
        _, acc_in = melhor_limiar(z, y, -1)
        acertos = 0
        for gg in np.unique(g):
            m = g == gg
            l, _ = melhor_limiar(z[~m], y[~m], -1)
            acertos += ((-z[m] > -l).astype(int) == y[m]).sum()
        linhas.append(dict(zip("abcef", cmb), acc_in=acc_in, acc_loso=acertos / len(y),
                           n_termos=sum(abs(x) > 0 for x in cmb)))
    R = pd.DataFrame(linhas).sort_values(["acc_loso", "acc_in"], ascending=False)
    top = R.head(25).copy()
    top["acc_cv"] = [avaliar_indice(lnI(d, r.a, r.b, r.c, r.e, r.f), y, g, -1)["acc_cv"] for r in top.itertuples()]
    top.to_csv("resultados/a04_grade_top.csv", index=False)
    print(f"{len(combos)} combinações avaliadas. Top 25 por LOSO:")
    print(top.to_string(index=False, float_format=lambda v: f"{v:.3f}"))

    # melhor por número de termos (parcimônia)
    print("\nMelhor por nº de termos além de ω (LOSO):")
    print(R.groupby("n_termos").head(1).sort_values("n_termos").to_string(index=False, float_format=lambda v: f"{v:.3f}"))

    # 2) CV aninhada honesta: em cada fold, escolher combo+limiar só no treino (por acc in-sample do treino)
    accs = []
    cv_rapida = list(CV.split(np.zeros(len(y)), y))[:30]  # 30 folds para custo razoável
    sub = combos[::3]  # subamostra da grade para custo
    for tr, te in cv_rapida:
        best, bacc, bl = None, -1, None
        for cmb in sub:
            z = Z[cmb]; l, a = melhor_limiar(z[tr], y[tr], -1)
            if a > bacc:
                best, bacc, bl = cmb, a, l
        accs.append(((-Z[best][te] > -bl).astype(int) == y[te]).mean())
    print(f"\nCV aninhada (seleção de expoentes dentro do treino, {len(cv_rapida)} folds, grade/3): "
          f"acc = {np.mean(accs):.3f} ± {np.std(accs):.3f}")


if __name__ == "__main__":
    main()
