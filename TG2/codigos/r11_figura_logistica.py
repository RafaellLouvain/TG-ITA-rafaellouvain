"""R11 -- Figura ilustrativa da regressão logística: probabilidade de vazio em função da velocidade periférica do
ombro (108 soldas), com os limiares da abordagem 2."""
import numpy as np

from dados import carregar
from estilo import CM, COR_SEM, COR_VAZIO, plt, salvar, virgula
from nucleo import logistica, pesos_classe

d = carregar()
y = d["vazio"].to_numpy()
x = d["wRs"].to_numpy()
b0, b = logistica(np.log(x)[:, None], y, pesos_classe(y, "balanceado"))

rng = np.random.default_rng(0)
fig, ax = plt.subplots(figsize=(14 * CM, 7 * CM))
for vz, cor, rot, mk in [(0, COR_SEM, "Sem vazio", "o"), (1, COR_VAZIO, "Com vazio", "x")]:
    m = y == vz
    ax.scatter(x[m], vz + rng.uniform(-0.04, 0.04, m.sum()), c=cor, marker=mk, s=18, label=rot, linewidths=1.1,
               zorder=3)
xs = np.linspace(x.min() * 0.95, x.max() * 1.05, 300)
ax.plot(xs, 1 / (1 + np.exp(-(b0 + b[0] * np.log(xs)))), color="k", lw=1.4, label="regressão logística")
ax.axvline(0.84, color="gray", lw=1, label="limiar 0,84 m/s")
ax.axvline(1.05, color="gray", lw=1, ls="--", label="limiar 1,05 m/s")
ax.set_xlabel(r"Velocidade periférica do ombro, $\omega R_s$ (m/s)")
ax.set_ylabel("Probabilidade de vazio")
virgula(ax)
ax.legend(loc="center right", fontsize=7.5)
salvar(fig, "fig_r11_logistica_wRs")
print("expoente de ωR_s:", round(b[0], 2))
