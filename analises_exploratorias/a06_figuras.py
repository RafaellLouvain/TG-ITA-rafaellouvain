"""A06 — Figuras exploratórias: rotação por estudo vs. velocidade periférica do ombro (ω·R_s) por estudo.

Mostra (i) que dentro de cada estudo a rotação separa vazio/são e (ii) quanto um índice físico 'alinha' os
estudos sob um único limiar. Paleta: slots 1-2 da paleta categórica de referência (azul = são, laranja = vazio),
com forma do marcador como codificação secundária (círculo = são, x = vazio).
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

from dados_fsw import carregar  # noqa: E402
from metricas import melhor_limiar  # noqa: E402

SUP, TXT, TXT2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df"
SAO, VAZIO = "#2a78d6", "#eb6834"


def painel(d, ordem, y, ylabel, titulo, arquivo, limiar=None, rot_lim=None):
    fig, ax = plt.subplots(figsize=(10, 4.8), facecolor=SUP)
    ax.set_facecolor(SUP)
    rng = np.random.default_rng(0)
    pos = {e: i for i, e in enumerate(ordem)}
    for val, cor, mk, rot in [(0, SAO, "o", "Sem vazio (0)"), (1, VAZIO, "x", "Com vazio (1)")]:
        m = d.void == val
        xs = d.loc[m, "estudo"].map(pos) + rng.uniform(-0.18, 0.18, m.sum())
        ax.scatter(xs, y[m], s=46, marker=mk, c=cor, linewidths=2 if mk == "x" else 0.8,
                   edgecolors=SUP if mk == "o" else None, label=rot, zorder=3)
    if limiar is not None:
        ax.axhline(limiar, color=TXT2, lw=1.2, ls="--", zorder=2)
        ax.text(-0.4, limiar * 1.04, rot_lim, ha="left", va="bottom", color=TXT2, fontsize=9)
    ax.set_yscale("log")
    ax.set_xticks(range(len(ordem)))
    ax.set_xticklabels([f"ref {e}\n{d.loc[d.estudo == e, 'liga'].iloc[0]}" for e in ordem], fontsize=8, color=TXT2)
    ax.set_ylabel(ylabel, color=TXT, fontsize=10)
    ax.set_title(titulo, color=TXT, fontsize=11, loc="left")
    ax.tick_params(colors=TXT2, labelsize=8)
    ax.grid(axis="y", color=GRID, lw=0.8, zorder=0)
    for s in ["top", "right"]:
        ax.spines[s].set_visible(False)
    for s in ["left", "bottom"]:
        ax.spines[s].set_color(GRID)
    ax.legend(frameon=False, fontsize=9, labelcolor=TXT, loc="upper left")
    fig.tight_layout()
    fig.savefig(arquivo, dpi=160, facecolor=SUP)
    plt.close(fig)


def main():
    d = carregar()
    # ordenar estudos pela rotação crítica
    crit = {e: melhor_limiar(s.N.values, s.void.values, -1)[0] for e, s in d.groupby("estudo")}
    ordem = sorted(crit, key=crit.get)
    painel(d, ordem, d.rpm, "Rotação (rpm, escala log)",
           "Rotação por estudo: separa bem dentro de cada estudo, mas o nível crítico muda entre estudos",
           "resultados/fig_a06_rotacao_por_estudo.png")
    vp = d.w * d.Rs
    lim = np.exp(melhor_limiar(np.log(vp.values), d.void.values, -1)[0])
    painel(d, ordem, vp, "ω·R_s — velocidade na borda do ombro (m/s, log)",
           "Índice F1 = ω·R_s: um único limiar universal",
           "resultados/fig_a06_velocidade_periferica_ombro.png", limiar=lim,
           rot_lim=f"limiar ≈ {lim:.2f} m/s (abaixo → vazio previsto)")
    idx = d.w * d.Rs * np.sqrt(d.p / d.sy)
    lim3 = np.exp(melhor_limiar(np.log(idx.values), d.void.values, -1)[0])
    painel(d, ordem, idx, "ω·R_s·(p/σ_y)^0,5 (m/s, log)",
           "Índice F3 = ω·R_s·(p/σ_y)^0,5: confinamento relativo incluído",
           "resultados/fig_a06_indice_F3.png", limiar=lim3, rot_lim=f"limiar ≈ {lim3:.3f} (abaixo → vazio previsto)")
    print("figuras salvas em resultados/")


if __name__ == "__main__":
    main()
