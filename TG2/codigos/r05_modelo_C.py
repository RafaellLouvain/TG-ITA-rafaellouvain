"""R05 -- Modelo C (núcleo ωR_s + termos adimensionais aceitos por ganho de acurácia de teste na CV interna):
trajetória da seleção no treino oficial, frequência de seleção nos 500 splits, equação final e tornado (seção 4.4)."""
import matplotlib.ticker
import numpy as np
import pandas as pd

from dados import SIMBOLO_TEX, GRUPOS, NATUREZA, ROTULO, SAIDA, SIMBOLO, VARIAVEIS, carregar, matriz_grupos
from estilo import CM, plt, salvar
from modelos import CANDIDATOS_C
from nucleo import Hibrido
from validacao import SEMENTE_OFICIAL, split

T = SAIDA / "tabelas"
B = SAIDA / "brutos"
d = carregar()
tr, te = split(d, SEMENTE_OFICIAL)
LN = np.column_stack([d["ln_" + k] for k in VARIAVEIS])

traj, eqs = [], []
for crit in ["acc", "bal"]:
    m = Hibrido(CANDIDATOS_C, "wRs", crit, "balanceado").ajustar(d.iloc[tr])
    for passo, (termo, nota) in enumerate(m.trajetoria):
        traj.append({"criterio": crit, "passo": passo, "termo": ROTULO[termo], "nota_cv_interna": nota})
    lm = m.modelo
    e = matriz_grupos(lm.termos) @ lm.beta
    eqs.append({"criterio": crit, "termos": " + ".join(ROTULO[t] for t in lm.termos),
                "lnC0": lm.lnC0, **{f"β[{ROTULO[t]}]": b for t, b in zip(lm.termos, lm.beta)},
                **{f"e[{SIMBOLO[k]}]": e[i] for i, k in enumerate(VARIAVEIS) if abs(e[i]) > 1e-12}})
    if crit == "bal":
        mod_bal, e_bal = lm, e
pd.DataFrame(traj).to_csv(T / "r05_trajetoria_oficial.csv", index=False, float_format="%.4f")
pd.DataFrame(eqs).to_csv(T / "r05_equacao_oficial.csv", index=False, float_format="%.4f")
print(pd.DataFrame(traj).to_string(index=False))
print(pd.DataFrame(eqs).T.to_string())

# Frequência com que cada termo entra no modelo nos 500 splits (e ordem média de entrada)
linhas = []
for crit in ["acc", "bal"]:
    arq = B / f"rep_{crit}_C_hibrido.csv.gz"
    if not arq.exists():
        continue
    r = pd.read_csv(arq)
    listas = r["termos"].fillna("wRs").str.split("+")
    n_termos = listas.apply(len) - 1
    for c in CANDIDATOS_C:
        pos = [lst.index(c) for lst in listas if c in lst]
        linhas.append({"criterio": crit, "termo": ROTULO[c],
                       "natureza": ", ".join(sorted({NATUREZA[k] for k in GRUPOS[c]})),
                       "freq_selecao": len(pos) / len(r), "posicao_media": np.mean(pos) if pos else np.nan})
    linhas.append({"criterio": crit, "termo": "(nº médio de termos além do núcleo)", "freq_selecao": n_termos.mean()})
    linhas.append({"criterio": crit, "termo": "(fração só com o núcleo)", "freq_selecao": (n_termos == 0).mean()})
freq = pd.DataFrame(linhas)
freq.to_csv(T / "r05_frequencia_selecao.csv", index=False, float_format="%.3f")
print(freq.to_string(index=False))

# Tornado ilustrativo da equação final (critério balanceado)
med = np.median(LN, axis=0)
base = mod_bal.lnC0 + med @ e_bal
barras = []
for i, k in enumerate(VARIAVEIS):
    if abs(e_bal[i]) < 1e-12:
        continue
    lo10, hi90 = np.percentile(LN[:, i], [10, 90])
    barras.append((k, base + e_bal[i] * (lo10 - med[i]), base + e_bal[i] * (hi90 - med[i])))
barras.sort(key=lambda x: abs(x[2] - x[1]))
fig, ax = plt.subplots(figsize=(13 * CM, 0.75 * CM * len(barras) + 2 * CM))
for yv, (k, a, b) in enumerate(barras):
    ax.barh(yv, np.exp(b) - np.exp(a), left=np.exp(a), color="#c0392b" if b > a else "#2471a3", alpha=0.85)
    ax.text(max(np.exp(a), np.exp(b)) * 1.08, yv, f"{SIMBOLO_TEX[k]}  ({NATUREZA[k].lower()})", va="center",
            fontsize=8.5)
ax.axvline(1, color="k", lw=1)
ax.set_xscale("log")
ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, _: f"{x:g}".replace(".", ",")))
ax.xaxis.set_minor_formatter(matplotlib.ticker.FuncFormatter(lambda x, _: f"{x:g}".replace(".", ",") if f"{x:g}".lstrip("0.")[:1] in ("2", "5") else ""))
ax.set_yticks([])
ax.grid(axis="y", visible=False)
ax.set_xlabel("$C_{void}$ (variável do percentil 10 ao 90; demais na mediana)")
lim = ax.get_xlim()
ax.set_xlim(lim[0], lim[1] * 6)
salvar(fig, "fig_r05_tornado_C")
