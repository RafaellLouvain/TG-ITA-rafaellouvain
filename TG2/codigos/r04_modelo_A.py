"""R04 -- Modelo A (índice único ωR_s + limiar): limiar crítico, robustez do limiar e figura (seção 4.3)."""
import numpy as np
import pandas as pd

from dados import SAIDA, carregar
from estilo import CM, COR_SEM, COR_VAZIO, plt, salvar, virgula
from nucleo import Indice, escolher_limiar, metricas
from validacao import N_SPLITS, SEMENTE_OFICIAL, split

T = SAIDA / "tabelas"
d = carregar()
tr, te = split(d, SEMENTE_OFICIAL)
y = d["vazio"].to_numpy()
N_BOOT = 1000

linhas = []
for crit in ["acc", "bal"]:
    m = Indice("wRs", crit).ajustar(d.iloc[tr])
    V = m.I_crit
    # bootstrap do limiar (por linha e por estudo), sempre nos 108
    rng = np.random.default_rng(2)
    est = d["estudo"].unique()
    bl, be = [], []
    for _ in range(N_BOOT):
        i = rng.integers(0, len(d), len(d))
        bl.append(np.exp(-escolher_limiar(-d["ln_wRs"].to_numpy()[i], y[i], crit)))
        db = pd.concat([d[d["estudo"] == e] for e in rng.choice(est, len(est))])
        if db["vazio"].nunique() == 2:
            be.append(np.exp(-escolher_limiar(-db["ln_wRs"].to_numpy(), db["vazio"].to_numpy(), crit)))
    # robustez: limiar do treino oficial multiplicado por 0,9 / 1,0 / 1,1, avaliado no teste oficial e nos 500 splits
    for fator in [0.9, 1.0, 1.1]:
        prev = (d["wRs"].to_numpy() < V * fator).astype(int)
        of = metricas(y[te], prev[te])
        reps = []
        for s in range(N_SPLITS):
            trs, tes = split(d, s)
            Vs = Indice("wRs", crit).ajustar(d.iloc[trs]).I_crit * fator
            reps.append(metricas(y[tes], (d["wRs"].to_numpy()[tes] < Vs).astype(int)))
        reps = pd.DataFrame(reps)
        linhas.append({"criterio": crit, "V_crit_treino_m_s": V, "fator_limiar": fator,
                       "of_acc": of["acc"], "of_bal": of["bal"], "rep_acc": reps["acc"].mean(),
                       "rep_bal": reps["bal"].mean(), "rep_sens": reps["sens"].mean(),
                       "rep_espec": reps["espec"].mean(),
                       "V_boot_linha_p2.5": np.percentile(bl, 2.5), "V_boot_linha_p97.5": np.percentile(bl, 97.5),
                       "V_boot_estudo_p2.5": np.percentile(be, 2.5), "V_boot_estudo_p97.5": np.percentile(be, 97.5),
                       "N_rpm_x_Rs_mm_crit": V * fator * 60 / (2 * np.pi) * 1e3})
res = pd.DataFrame(linhas)
res.to_csv(T / "r04_limiar_A.csv", index=False, float_format="%.4f")
print(res.to_string(index=False))

# Curva acurácia × limiar (nos 108, só ilustrativa) e figura do índice por estudo
Vs = np.linspace(0.3, 1.6, 300)
acc = [metricas(y, (d["wRs"].to_numpy() < v).astype(int))["acc"] for v in Vs]
bal = [metricas(y, (d["wRs"].to_numpy() < v).astype(int))["bal"] for v in Vs]
pd.DataFrame({"V": Vs, "acc_108": acc, "bal_108": bal}).to_csv(T / "r04_curva_limiar.csv", index=False,
                                                                 float_format="%.4f")

V_acc = res.query("criterio=='acc' and fator_limiar==1.0")["V_crit_treino_m_s"].iat[0]
V_bal = res.query("criterio=='bal' and fator_limiar==1.0")["V_crit_treino_m_s"].iat[0]
ordem = sorted(d["estudo"].unique(), key=lambda s: (int(s.rstrip("b")), s))
x = {e: i for i, e in enumerate(ordem)}
rng = np.random.default_rng(0)
fig, ax = plt.subplots(figsize=(15 * CM, 7 * CM))
for vz, cor, rot, mk in [(0, COR_SEM, "Sem vazio", "o"), (1, COR_VAZIO, "Com vazio", "x")]:
    g = d[d["vazio"] == vz]
    ax.scatter(g["estudo"].map(x) + rng.uniform(-0.12, 0.12, len(g)), g["wRs"], c=cor, marker=mk, s=22,
               label=rot, linewidths=1.2)
ax.axhline(V_acc, color="k", lw=1, label=f"limiar de máxima acurácia = {V_acc:.2f} m/s".replace(".", ",") + "")
if not np.isclose(V_acc, V_bal):
    ax.axhline(V_bal, color="k", lw=1, ls="--", label=f"limiar conservador = {V_bal:.2f} m/s".replace(".", ",") + "")
ax.set_xticks(range(len(ordem)))
ax.set_xticklabels([f"{e}\n{d.loc[d.estudo == e, 'liga'].iat[0][2:]}" for e in ordem], fontsize=8)
ax.set_xlabel("Estudo de origem (numeração de Du et al., 2019) e liga")
ax.set_ylabel(r"$\omega R_s$ (m/s)")
virgula(ax, "y")
ax.legend(loc="lower center", bbox_to_anchor=(0.5, 1.0), fontsize=7.5, ncol=2, frameon=False)
salvar(fig, "fig_r04_indice_wRs_por_estudo")
