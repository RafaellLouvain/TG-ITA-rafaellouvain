"""R10 -- Figura da análise dentro dos estudos (lê as tabelas do r09): AUC intra-estudo do índice ω·v^c em função
do expoente relativo c do avanço, com as formas da literatura marcadas."""
import pandas as pd

from dados import SAIDA
from estilo import CM, plt, salvar, virgula

T = SAIDA / "tabelas"
v = pd.read_csv(T / "r09_varredura_c.csv")
r = pd.read_csv(T / "r09_dentro_do_estudo.csv")
lin = r[r["termo"] == "c (ω·v^c)"].iloc[0]
c_ot = float(lin["valor"])
lo, hi = [float(x) for x in str(lin["IC95"]).split(" a ")]

fig, ax = plt.subplots(figsize=(13 * CM, 7 * CM))
ax.axvspan(lo, hi, color="#d6eaf8", label="IC 95 % do expoente ótimo")
ax.plot(v["c"], v["auc_intra"], color="k", lw=1.3)
for c, rot in [(-1.0, r"$\omega/v$"), (-0.5, r"$\omega^2/v$"), (0.0, r"$\omega$")]:
    y = float(v.loc[(v["c"] - c).abs() < 1e-9, "auc_intra"].iloc[0])
    ax.scatter([c], [y], color="#c0392b", zorder=3, s=22)
    ax.annotate(rot, (c, y), textcoords="offset points", xytext=(6, -12), fontsize=9)
ax.axvline(c_ot, color="#2471a3", ls="--", lw=1, label=f"ótimo: c = {c_ot:.2f}".replace(".", ","))
ax.set_xlabel(r"Expoente relativo do avanço, $c$, no índice $\omega\, v^{c}$")
ax.set_ylabel("AUC dentro dos estudos")
virgula(ax)
ax.legend(loc="lower center", fontsize=7.5)
salvar(fig, "fig_r10_auc_intra_avanco")
