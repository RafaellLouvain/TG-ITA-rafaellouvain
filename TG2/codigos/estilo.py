"""Estilo único das figuras do TG2 (fonte serifada parecida com a do LaTeX, rótulos em português)."""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import matplotlib.ticker as mticker  # noqa: E402

from dados import SAIDA  # noqa: E402

plt.rcParams.update({
    "font.family": "serif", "font.serif": ["DejaVu Serif"], "mathtext.fontset": "cm",
    "font.size": 10, "axes.titlesize": 10, "axes.labelsize": 10, "legend.fontsize": 8.5,
    "xtick.labelsize": 9, "ytick.labelsize": 9, "axes.grid": True, "grid.alpha": 0.3,
    "savefig.dpi": 300, "savefig.bbox": "tight", "axes.spines.top": False, "axes.spines.right": False,
})
COR_VAZIO, COR_SEM = "#c0392b", "#2471a3"
CM = 1 / 2.54
FIG = SAIDA / "figuras"
FIG.mkdir(parents=True, exist_ok=True)


def salvar(fig, nome):
    fig.savefig(FIG / f"{nome}.png")
    fig.savefig(FIG / f"{nome}.pdf")
    plt.close(fig)


def _fmt(x, _pos=None):
    return f"{x:g}".replace(".", ",")


VIRGULA = mticker.FuncFormatter(_fmt)


def virgula(ax, eixos="xy"):
    """Vírgula decimal nos rótulos dos eixos lineares."""
    if "x" in eixos:
        ax.xaxis.set_major_formatter(VIRGULA)
    if "y" in eixos:
        ax.yaxis.set_major_formatter(VIRGULA)
