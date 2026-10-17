"""A03 — Leis de potência por blocos (logística em ln das variáveis).

C_void = e^b0 * prod(x_i^b_i)  <=>  logit P(vazio) = b0 + sum b_i ln x_i ; vazio previsto se C_void > 1.
Comparamos conjuntos de variáveis organizados pelos blocos do TG1 (cinemático, térmico, geométrico, dinâmico)
e grupos adimensionais. Métricas: CV estratificado 5x20 e LOSO (deixa um estudo inteiro de fora).
Os expoentes são normalizados pelo de N (rotação) para leitura: C_void ∝ (N * prod x_i^(b_i/b_N))^(b_N).
"""
import numpy as np
import pandas as pd

from dados_fsw import carregar
from metricas import avaliar_lei_potencia


def conjuntos(d):
    L = lambda s: np.log(s.values)  # noqa: E731
    base = {"N": L(d.N), "v": L(d.v), "t": L(d.t), "R_s": L(d.Rs), "R_pr": L(d.Rpr), "R_pt": L(d.Rpt),
            "p": L(d.p), "σ_y": L(d.sy), "α": L(d.alpha), "tilt": L(d.tilt), "ΔT_sol": L(d.dT_sol)}
    adim = {"ωR_s²/α": L(d.w * d.Rs**2 / d.alpha), "vR_s/α": L(d.v * d.Rs / d.alpha), "p/σ_y": L(d.p / d.sy),
            "t/R_s": L(d.t / d.Rs), "R_pr/R_s": L(d.Rpr / d.Rs), "R_pt/R_pr": L(d.Rpt / d.Rpr),
            "ωR_s/v": L(d.w * d.Rs / d.v)}
    V = {**base, **adim}
    S = {
        # cinemático
        "K1  N": ["N"],
        "K2  N, v": ["N", "v"],
        # cinemático + geometria do ombro
        "G1  N, R_s": ["N", "R_s"],
        "G2  N, R_s, t": ["N", "R_s", "t"],
        "G3  N, R_s, R_pr, R_pt, t": ["N", "R_s", "R_pr", "R_pt", "t"],
        # + material (térmico/metalúrgico)
        "M1  N, α": ["N", "α"],
        "M2  N, R_s, α": ["N", "R_s", "α"],
        "M3  N, R_s, σ_y": ["N", "R_s", "σ_y"],
        "M4  N, R_s, α, σ_y": ["N", "R_s", "α", "σ_y"],
        "M5  N, R_s, t, α": ["N", "R_s", "t", "α"],
        # + dinâmico
        "D1  N, R_s, α, p": ["N", "R_s", "α", "p"],
        "D2  N, R_s, α, p, tilt": ["N", "R_s", "α", "p", "tilt"],
        "D3  N, R_s, α, v": ["N", "R_s", "α", "v"],
        # tudo
        "T1  todas as 10 brutas": ["N", "v", "t", "R_s", "R_pr", "R_pt", "p", "σ_y", "α", "tilt"],
        # versões adimensionais
        "A1  ωR_s²/α (Péclet rot.)": ["ωR_s²/α"],
        "A2  ωR_s²/α, vR_s/α": ["ωR_s²/α", "vR_s/α"],
        "A3  ωR_s²/α, t/R_s": ["ωR_s²/α", "t/R_s"],
        "A4  ωR_s²/α, p/σ_y": ["ωR_s²/α", "p/σ_y"],
        "A5  ωR_s²/α, t/R_s, p/σ_y, R_pr/R_s": ["ωR_s²/α", "t/R_s", "p/σ_y", "R_pr/R_s"],
        "A6  7 grupos adimensionais": ["ωR_s²/α", "vR_s/α", "p/σ_y", "t/R_s", "R_pr/R_s", "R_pt/R_pr"],
    }
    return V, S


def main():
    d = carregar()
    y, g = d.void.values, d.estudo.values
    V, S = conjuntos(d)
    linhas = []
    for nome, cols in S.items():
        X = np.column_stack([V[c] for c in cols])
        r = avaliar_lei_potencia(X, y, g)
        e = r["expoentes"]
        ref = e[0]  # normalizar pelo 1º termo (N ou o Péclet rotacional)
        expo = ", ".join(f"{c}^{ei / ref:+.2f}" for c, ei in zip(cols, e))
        linhas.append(dict(modelo=nome, k=len(cols), acc_in=r["acc_in"], acc_cv=r["acc_cv"], acc_loso=r["acc_loso"],
                           auc=r["auc"], auc_intra=r["auc_intra"], expoentes_rel=expo, escala=ref))
    R = pd.DataFrame(linhas)
    R.to_csv("resultados/a03_lei_potencia_blocos.csv", index=False)
    pd.set_option("display.width", 250); pd.set_option("display.max_colwidth", 120)
    print(R.to_string(index=False, float_format=lambda v: f"{v:.3f}"))


if __name__ == "__main__":
    main()
