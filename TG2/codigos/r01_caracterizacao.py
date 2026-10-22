"""R01 -- Caracterização do dataset (seção 4.1): tabelas por estudo e por liga; rotação por estudo."""
import matplotlib.ticker
import numpy as np
import pandas as pd

from dados import SAIDA, carregar
from estilo import CM, COR_SEM, COR_VAZIO, plt, salvar

d = carregar()
T = SAIDA / "tabelas"
T.mkdir(parents=True, exist_ok=True)


def faixa(s, fmt="{:.0f}"):
    a, b = s.min(), s.max()
    return fmt.format(a) if np.isclose(a, b) else f"{fmt.format(a)}–{fmt.format(b)}"


ordem = sorted(d["estudo"].unique(), key=lambda s: (int(s.rstrip("b")), s))
linhas = []
for e in ordem:
    g = d[d["estudo"] == e]
    linhas.append({
        "estudo": e, "liga": g["liga"].iat[0], "n": len(g), "vazios": int(g["vazio"].sum()),
        "t_mm": faixa(g["t"] * 1e3, "{:.1f}"), "Rs_mm": faixa(g["Rs"] * 1e3, "{:.1f}"),
        "Rpr/Rpt_mm": f"{faixa(g['Rpr'] * 1e3, '{:.1f}')}/{faixa(g['Rpt'] * 1e3, '{:.1f}')}",
        "rpm": faixa(g["rpm"]), "v_mm_min": faixa(g["v_mm_min"]),
        "p_MPa": faixa(g["p_MPa"], "{:.1f}") + ("*" if g["p_assumido"].all() else ""),
        "theta": faixa(g["theta"], "{:.1f}") + ("*" if g["theta_assumido"].all() else ""),
    })
pd.DataFrame(linhas).to_csv(T / "r01_estudos.csv", index=False)

por_liga = d.groupby("liga")["vazio"].agg(n="size", vazios="sum")
por_liga["pct_vazio"] = 100 * por_liga["vazios"] / por_liga["n"]
por_liga.to_csv(T / "r01_ligas.csv")

desc = pd.DataFrame({
    "variavel": ["v (mm/min)", "ω (rad/s)", "rpm", "t (mm)", "R_s (mm)", "R_pr (mm)", "R_pt (mm)", "p (MPa)",
                 "θ (°)", "α (m²/s)", "σ_y (MPa)", "Pe = vR_s/α"],
    "min": [d.v_mm_min.min(), d.w.min(), d.rpm.min(), d.t.min() * 1e3, d.Rs.min() * 1e3, d.Rpr.min() * 1e3,
            d.Rpt.min() * 1e3, d.p_MPa.min(), d.theta.min(), d.alpha.min(), d.sy_MPa.min(), np.exp(d.ln_Pe.min())],
    "mediana": [d.v_mm_min.median(), d.w.median(), d.rpm.median(), d.t.median() * 1e3, d.Rs.median() * 1e3,
                d.Rpr.median() * 1e3, d.Rpt.median() * 1e3, d.p_MPa.median(), d.theta.median(), d.alpha.median(),
                d.sy_MPa.median(), np.exp(d.ln_Pe.median())],
    "max": [d.v_mm_min.max(), d.w.max(), d.rpm.max(), d.t.max() * 1e3, d.Rs.max() * 1e3, d.Rpr.max() * 1e3,
            d.Rpt.max() * 1e3, d.p_MPa.max(), d.theta.max(), d.alpha.max(), d.sy_MPa.max(), np.exp(d.ln_Pe.max())],
})
desc.to_csv(T / "r01_descritiva.csv", index=False, float_format="%.4g")
print(pd.DataFrame(linhas).to_string(index=False))
print(por_liga)
print(desc.to_string(index=False))
print("fração com Pe < 1:", (d.ln_Pe < 0).mean().round(3), "| p assumido:", d.p_assumido.sum(),
      "| θ assumido:", d.theta_assumido.sum())

# Figura: rotação por estudo (o nível crítico muda de estudo para estudo)
fig, ax = plt.subplots(figsize=(15 * CM, 7 * CM))
x = {e: i for i, e in enumerate(ordem)}
rng = np.random.default_rng(0)
for vz, cor, rot, mk in [(0, COR_SEM, "Sem vazio", "o"), (1, COR_VAZIO, "Com vazio", "x")]:
    g = d[d["vazio"] == vz]
    ax.scatter(g["estudo"].map(x) + rng.uniform(-0.12, 0.12, len(g)), g["rpm"], c=cor, marker=mk, s=22,
               label=rot, linewidths=1.2)
ax.set_yscale("log")
ax.set_yticks([150, 200, 300, 500, 700, 1000, 1500, 2500])
ax.yaxis.set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.yaxis.set_minor_locator(matplotlib.ticker.NullLocator())
ax.set_xticks(range(len(ordem)))
ax.set_xticklabels([f"{e}\n{d.loc[d.estudo == e, 'liga'].iat[0][2:]}" for e in ordem], fontsize=8)
ax.set_xlabel("Estudo de origem (numeração de Du et al., 2019) e liga")
ax.set_ylabel("Rotação (rpm)")
ax.legend(loc="lower right")
salvar(fig, "fig_r01_rotacao_por_estudo")
