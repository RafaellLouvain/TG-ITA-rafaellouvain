"""R06 -- Comparação entre modelos e com Du et al. (seção 4.5), critério acc × bal, robustez dos dados (4.6).

Lê resultados/tabelas/validacao*.csv e resultados/brutos/*.csv.gz (gerados pelo r02).
"""
import numpy as np
import pandas as pd

from dados import SAIDA
from estilo import CM, plt, salvar, virgula
from r02_validacao import slug

T, B = SAIDA / "tabelas", SAIDA / "brutos"
base = pd.read_csv(T / "validacao.csv")

# Percentil do split oficial dentro da distribuição dos 500 splits (o split oficial foi "fácil"?)
pct = []
for _, r in base.iterrows():
    rep = pd.read_csv(B / f"rep_{r['criterio']}_{slug(r['modelo'])}.csv.gz")
    pct.append((rep["acc"] < r["of_acc"] - 1e-9).mean() + 0.5 * np.isclose(rep["acc"], r["of_acc"]).mean())
base["of_percentil_nos_500"] = pct
base.to_csv(T / "r06_validacao_com_percentil.csv", index=False, float_format="%.4f")

cols = ["modelo", "criterio", "of_acc", "of_bal", "of_percentil_nos_500", "rep_tr_acc_media", "rep_acc_media",
        "rep_acc_p5", "rep_acc_p95", "rep_frac_acc>=70", "rep_bal_media", "rep_sens_media", "rep_espec_media",
        "loso_acc", "loso_bal"]
print(base[cols].round(3).to_string(index=False))

# Robustez dos dados: comparação lado a lado
rob = [base.assign(versao="base")]
for suf, rot in [("_sem_p_theta", "sem p e θ"), ("_sem_84_89", "sem linhas 84–89")]:
    arq = T / f"validacao{suf}.csv"
    if arq.exists():
        rob.append(pd.read_csv(arq).assign(versao=rot))
rob = pd.concat(rob)
piv = rob.pivot_table(index=["modelo", "criterio"], columns="versao",
                      values=["rep_acc_media", "rep_bal_media", "loso_acc"])
piv.to_csv(T / "r06_robustez_dados.csv", float_format="%.4f")
print(piv.round(3).to_string())

# Figura: distribuição da acurácia de teste nos 500 splits (critério acc e bal), com meta e Du et al.
modelos = ["Majoritária", "A0 (ω)", "B1", "B2", "B3", "B (seleção)", "A (ωR_s)", "C (híbrido)"]
rot = {"Majoritária": "Maj.", "A0 (ω)": "$\\omega$", "A (ωR_s)": "2", "B1": "1a", "B2": "1b", "B3": "1c",
       "B (seleção)": "1*", "C (híbrido)": "3"}
NOME_TEXTO = {"A (ωR_s)": "Abordagem 2", "B (seleção)": "Abordagem 1 (seleção)", "C (híbrido)": "Abordagem 3",
              "B1": "1a", "B2": "1b", "B3": "1c"}
fig, axs = plt.subplots(1, 2, figsize=(16 * CM, 7 * CM), sharey=True)
for ax, crit, titulo in zip(axs, ["acc", "bal"], ["Limiar pela acurácia", "Limiar pela acurácia balanceada"]):
    dados = [pd.read_csv(B / f"rep_{crit}_{slug(m)}.csv.gz")["acc"] * 100 for m in modelos]
    bp = ax.boxplot(dados, whis=(5, 95), showfliers=False, patch_artist=True, widths=0.6,
                    medianprops=dict(color="k"))
    for p in bp["boxes"]:
        p.set_facecolor("#d6eaf8")
    ax.scatter(range(1, len(modelos) + 1), [x.mean() for x in dados], marker="D", s=14, c="k", zorder=3,
               label="média")
    ax.axhline(70, color="#c0392b", ls="--", lw=1, label="meta (70 %)")
    ax.axhline(83.3, color="gray", ls=":", lw=1, label="Du et al. (método 1)")
    ax.set_xticks(range(1, len(modelos) + 1))
    ax.set_xticklabels([rot[m] for m in modelos], fontsize=8.5)
    ax.set_title(titulo)
axs[0].set_ylabel("Acurácia de teste (%)")
axs[0].legend(loc="lower right", fontsize=7)
salvar(fig, "fig_r06_comparacao_modelos")

# Figura: sensibilidade × especificidade média (acc vs bal)
fig, ax = plt.subplots(figsize=(13 * CM, 8.5 * CM))
for m in ["A (ωR_s)", "B (seleção)", "C (híbrido)", "B1", "B2", "B3"]:
    pts = base[base["modelo"] == m].set_index("criterio")
    ax.annotate("", xy=(pts.at["bal", "rep_espec_media"], pts.at["bal", "rep_sens_media"]),
                xytext=(pts.at["acc", "rep_espec_media"], pts.at["acc", "rep_sens_media"]),
                arrowprops=dict(arrowstyle="->", color="gray"))
    ax.scatter(pts.at["acc", "rep_espec_media"], pts.at["acc", "rep_sens_media"], c="#2471a3", s=20)
    ax.scatter(pts.at["bal", "rep_espec_media"], pts.at["bal", "rep_sens_media"], c="#c0392b", s=20)
    ax.text(pts.at["bal", "rep_espec_media"] + 0.005, pts.at["bal", "rep_sens_media"] + 0.006, NOME_TEXTO[m], fontsize=7)
ax.scatter([], [], c="#2471a3", s=20, label="limiar pela acurácia")
ax.scatter([], [], c="#c0392b", s=20, label="limiar pela acurácia balanceada")
ax.set_xlabel("Especificidade média")
ax.set_ylabel("Sensibilidade média")
virgula(ax)
ax.legend(fontsize=7, loc="lower left")
salvar(fig, "fig_r06_sens_espec_acc_vs_bal")

# Versão simplificada (texto do TG): um só critério de limiar (acurácia), sem a seleção 1*
mod1 = ["Majoritária", "A0 (ω)", "B1", "B2", "B3", "A (ωR_s)", "C (híbrido)"]
rot1 = {"Majoritária": "Classe\nmajoritária", "A0 (ω)": "Só\nrotação",
        "B1": "Abordagem 1:\nBuckingham\ncompleto", "B2": "Abordagem 1:\nconjunto\ntérmico",
        "B3": "Abordagem 1:\nconjunto\nescoamento", "A (ωR_s)": "Abordagem 2\n($\\omega R_s$)",
        "C (híbrido)": "Abordagem 3"}
fig, ax = plt.subplots(figsize=(16 * CM, 8 * CM))
dados = [pd.read_csv(B / f"rep_acc_{slug(m)}.csv.gz")["acc"] * 100 for m in mod1]
bp = ax.boxplot(dados, whis=(5, 95), showfliers=False, patch_artist=True, widths=0.6, medianprops=dict(color="k"))
for p in bp["boxes"]:
    p.set_facecolor("#d6eaf8")
ax.scatter(range(1, len(mod1) + 1), [x.mean() for x in dados], marker="D", s=16, c="k", zorder=3, label="média")
for i, x in enumerate(dados, start=1):
    ax.text(i + 0.33, x.mean(), f"{x.mean():.1f}".replace(".", ","), fontsize=6.5, va="center", ha="left")
ax.axhline(70, color="#c0392b", ls="--", lw=1, label="meta (70 %)")
ax.axhline(83.3, color="gray", ls=":", lw=1, label="Du et al. (método 1)")
ax.set_xticks(range(1, len(mod1) + 1))
ax.set_xticklabels([rot1[m] for m in mod1], fontsize=6.5)
ax.set_ylim(45, 95)
ax.set_ylabel("Acurácia de teste (%)")
ax.legend(loc="lower right", fontsize=7.5)
salvar(fig, "fig_r06_comparacao_acc")

# Mesmo conjunto de modelos no protocolo de validação de Du et al. (um único sorteio 78/30, semente fixa), no mesmo
# estilo da figura anterior: como há um só valor por modelo, cada caixa se reduz a uma linha
ofic = pd.read_csv(T / "r06_validacao_com_percentil.csv").query("criterio == 'acc'").set_index("modelo")
acc1 = [ofic.at[m, "of_acc"] * 100 for m in mod1]
fig, ax = plt.subplots(figsize=(16 * CM, 8 * CM))
bp = ax.boxplot([[a] for a in acc1], whis=(5, 95), showfliers=False, patch_artist=True, widths=0.6,
                medianprops=dict(color="k", lw=1.5))
for p in bp["boxes"]:
    p.set_facecolor("#d6eaf8")
ax.scatter(range(1, len(mod1) + 1), acc1, marker="D", s=16, c="k", zorder=3, label="acurácia no sorteio único")
for i, a in enumerate(acc1, start=1):
    ax.text(i, a + 1.0, f"{a:.1f}".replace(".", ",") + f"\n({round(a * 0.3):d}/30)", fontsize=6.5, va="bottom",
            ha="center")
ax.axhline(70, color="#c0392b", ls="--", lw=1, label="meta (70 %)")
ax.axhline(83.3, color="gray", ls=":", lw=1, label="Du et al. (método 1)")
ax.set_xticks(range(1, len(mod1) + 1))
ax.set_xticklabels([rot1[m] for m in mod1], fontsize=6.5)
ax.set_ylim(45, 95)
ax.set_ylabel("Acurácia de teste (%)")
ax.legend(loc="lower right", fontsize=7.5)
salvar(fig, "fig_r06_comparacao_protocolo_du")
