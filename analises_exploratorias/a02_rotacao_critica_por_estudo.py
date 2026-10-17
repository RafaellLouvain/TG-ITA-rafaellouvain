"""A02 — Rotação crítica por estudo.

Dentro de cada estudo (ferramenta e liga fixas) a rotação separa quase perfeitamente vazio/são (A01: AUC intra 0,96).
Aqui: (1) estimamos N_crit de cada estudo (limiar ótimo em N, vazio se N < N_crit); (2) vemos que grandezas da
ferramenta/material/processo explicam a variação de N_crit entre estudos. Se N_crit = f(geometria, liga, v, p),
então o C_void natural é C_void = N_crit(·)/N  (vazio se > 1).
"""
import numpy as np
import pandas as pd

from dados_fsw import carregar
from metricas import melhor_limiar


def main():
    d = carregar()
    linhas = []
    for est, s in d.groupby("estudo", sort=False):
        lim, acc = melhor_limiar(s.N.values, s.void.values, -1)
        nvoid = s.void.sum()
        # faixa de indeterminação: maior N com vazio vs menor N sem vazio
        nv_max = s.loc[s.void == 1, "N"].max() if nvoid else np.nan
        ns_min = s.loc[s.void == 0, "N"].min() if nvoid < len(s) else np.nan
        linhas.append(dict(
            estudo=est, liga=s.liga.iloc[0], n=len(s), vazios=int(nvoid), acc_intra_N=acc,
            N_crit_rpm=60 * lim, N_vazio_max_rpm=60 * nv_max, N_sao_min_rpm=60 * ns_min,
            v_med_mm_min=s.v_mm_min.median(), t_mm=1e3 * s.t.iloc[0], Rs_mm=1e3 * s.Rs.iloc[0],
            Rpr_mm=1e3 * s.Rpr.iloc[0], Rpt_mm=1e3 * s.Rpt.iloc[0], p_MPa=s.p.iloc[0], p_assumido=s.p_assumido.iloc[0],
            tilt=s.tilt.iloc[0], sy=s.sy.iloc[0], alpha=s.alpha.iloc[0], T_sol=s.T_sol.iloc[0]))
    E = pd.DataFrame(linhas)
    E.to_csv("resultados/a02_rotacao_critica_por_estudo.csv", index=False)
    print(E.to_string(index=False, float_format=lambda v: f"{v:.3g}"))

    # correlação (em log) entre N_crit e as características do estudo
    print("\nCorrelação de Pearson entre ln(N_crit) e ln(característica) — 14 estudos:")
    L = np.log(E[["N_crit_rpm", "v_med_mm_min", "t_mm", "Rs_mm", "Rpr_mm", "Rpt_mm", "p_MPa", "sy", "alpha", "T_sol"]])
    for c in L.columns[1:]:
        print(f"  {c:14s} r = {np.corrcoef(L.N_crit_rpm, L[c])[0, 1]:+.2f}")
    # velocidade periférica crítica do ombro e do pino (m/s) - candidatas a 'constante universal'
    E["Vp_ombro_crit"] = 2 * np.pi * E.N_crit_rpm / 60 * E.Rs_mm / 1e3
    E["Vp_pino_crit"] = 2 * np.pi * E.N_crit_rpm / 60 * (E.Rpr_mm + E.Rpt_mm) / 2 / 1e3
    for c in ["N_crit_rpm", "Vp_ombro_crit", "Vp_pino_crit"]:
        cv = E[c].std() / E[c].mean()
        print(f"Dispersão relativa (CV) de {c:14s}: {cv:.2f}  (menor = mais 'universal')")


if __name__ == "__main__":
    main()
