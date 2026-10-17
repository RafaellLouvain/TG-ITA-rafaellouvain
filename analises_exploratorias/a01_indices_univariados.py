"""A01 — Índices físicos isolados (1 número + 1 limiar), inspirados nas equações das referências.

Para cada índice: acurácia in-sample, CV (limiar escolhido no treino), LOSO (deixa um estudo inteiro de fora),
AUC global e AUC intra-estudo. Sentido s: -1 = valor baixo -> vazio (falta de calor), +1 = valor alto -> vazio.
"""
import numpy as np
import pandas as pd

from dados_fsw import carregar
from metricas import avaliar_indice

RAD3 = np.sqrt(3)


def geom_calor(d):
    """Termo geométrico da eq. de Schmidt (Mishra & Ma eq. 3): (Rs^3-Rp^3)(1+tan a)+Rp^3+3Rp^2 Hp, a=0 (ombro plano)."""
    return (d.Rs**3 - d.Rp**3) + d.Rp**3 + 3 * d.Rp**2 * d.Hp


def indices(d):
    G = geom_calor(d)
    Q_stick = (2 / 3) * np.pi * (d.sy_Pa / RAD3) * d.w * G          # W, sticking total (delta=1), tau=sy/sqrt3
    Q_slide = (2 / 3) * np.pi * 0.4 * d.p_Pa * d.w * G              # W, sliding (mu=0.4)
    rho_cp = d.rho * d.cp
    area = 2 * d.Rs * d.t                                            # seção "afetada" ~ largura do ombro x espessura
    ipm = d.v_mm_min / 25.4
    T_ah = 0.70 * d.T_liq * (d.rpm**2 / (ipm * 1e4)) ** 0.05        # Arbegast-Hartley (°C), K=0.70, a=0.05
    I = {
        # --- cinemáticos
        "N (rps)": (d.N, -1, "cinemático"),
        "v": (d.v, +1, "cinemático"),
        "ω/v (rot. por m)": (d.w / d.v, -1, "cinemático"),
        "ω²/v (pseudo heat index, Arbegast)": (d.w**2 / d.v, -1, "cinemático"),
        "ωR_s/v (vel. periférica/avanço)": (d.w * d.Rs / d.v, -1, "cinemático"),
        "ωR_p/v (vel. periférica do pino/avanço)": (d.w * d.Rp / d.v, -1, "cinemático"),
        # --- térmicos / energia
        "T/T_sol (Arbegast-Hartley)": (T_ah / d.T_sol, -1, "térmico"),
        "Q/v sticking (J/m, Schmidt δ=1)": (Q_stick / d.v, -1, "térmico"),
        "Q/v sliding (J/m, μp)": (Q_slide / d.v, -1, "térmico"),
        "E* stick = Q/(v ρc_p ΔT_sol 2R_s t)": (Q_stick / (d.v * rho_cp * d.dT_sol * area), -1, "térmico"),
        "E* slide = Q/(v ρc_p ΔT_sol 2R_s t)": (Q_slide / (d.v * rho_cp * d.dT_sol * area), -1, "térmico"),
        "Q* Roy-Nandan-DebRoy = σ_y πR_s² ω/(ρ α v²)": (d.sy_Pa * np.pi * d.Rs**2 * d.w / (d.rho * d.alpha * d.v**2), -1, "térmico"),
        "Péclet vR_s/α": (d.v * d.Rs / d.alpha, +1, "térmico"),
        "Péclet rotacional ωR_s²/α": (d.w * d.Rs**2 / d.alpha, -1, "térmico"),
        "Q_stick/(k t ΔT_sol)": (Q_stick / (d.k * d.t * d.dT_sol), -1, "térmico"),
        # --- geométricos
        "t/R_s": (d.t / d.Rs, +1, "geométrico"),
        "R_pr/R_s": (d.Rpr / d.Rs, +1, "geométrico"),
        "R_pt/R_pr (conicidade)": (d.Rpt / d.Rpr, -1, "geométrico"),
        "R_p/t": (d.Rp / d.t, -1, "geométrico"),
        "V_pino/(πR_s² t)": (np.pi * d.t * (d.Rpr**2 + d.Rpr * d.Rpt + d.Rpt**2) / 3 / (np.pi * d.Rs**2 * d.t), -1, "geométrico"),
        # --- dinâmicos / material
        "p/σ_y": (d.p / d.sy, -1, "dinâmico"),
        "p (MPa)": (d.p, -1, "dinâmico"),
        "tilt": (d.tilt, -1, "dinâmico"),
        "σ_y": (d.sy, +1, "material"),
        "α": (d.alpha, -1, "material"),
    }
    return I


def main():
    d = carregar()
    y, g = d.void.values, d.estudo.values
    linhas = []
    for nome, (x, s, bloco) in indices(d).items():
        r = avaliar_indice(x.values, y, g, s)
        linhas.append(dict(bloco=bloco, indice=nome, sentido=s, **r))
    res = pd.DataFrame(linhas)
    res.to_csv("resultados/a01_indices_univariados.csv", index=False)
    cols = ["bloco", "indice", "sentido", "acc_in", "acc_cv", "acc_loso", "auc", "auc_intra"]
    print(res[cols].sort_values("acc_cv", ascending=False).to_string(index=False, float_format=lambda v: f"{v:.3f}"))


if __name__ == "__main__":
    main()
