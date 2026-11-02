"""R09 -- Efeito de ω e v DENTRO de cada estudo (sem confusão entre estudos).

Só ω e v variam dentro dos estudos; as demais variáveis são constantes em cada estudo. Usa-se a AUC intra-estudo
(compara apenas pares vazio × sem vazio do mesmo estudo) para achar o expoente relativo c do avanço no índice ω·v^c,
com IC por bootstrap de estudos. Formas da literatura: ω/v (avanço por rotação, c = −1) e ω²/v (Arbegast–Hartley,
c = −0,5). A logística condicional não converge (quase-separação pela rotação dentro dos estudos).
"""
import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score

from dados import SAIDA, carregar

d = carregar()
g = d["estudo"].to_numpy()
y = d["vazio"].to_numpy()
linhas = []

# 1) AUC intra-estudo (média ponderada pelos pares vazio × sem vazio de cada estudo)
def auc_intra(escore):
    num = den = 0.0
    for e in np.unique(g):
        m = g == e
        if 0 < y[m].sum() < m.sum():
            pares = y[m].sum() * (m.sum() - y[m].sum())
            num += roc_auc_score(y[m], escore[m]) * pares
            den += pares
    return num / den

for nome, esc in {"ω (−ln ω)": -d["ln_w"], "v (+ln v)": d["ln_v"], "ω/v (−)": -(d["ln_w"] - d["ln_v"]),
                  "ω²/v (−)": -(2 * d["ln_w"] - d["ln_v"])}.items():
    linhas.append({"analise": "AUC intra-estudo", "termo": nome, "valor": auc_intra(esc.to_numpy())})

# 2) Varredura do expoente relativo de v: escore de risco = −(ln ω + c·ln v); c = −1 ↔ ω/v; c = −0,5 ↔ ω²/v.
#    (A logística condicional não converge: dentro dos estudos a rotação quase separa as classes, AUC 0,96.)
cs = np.round(np.arange(-1.5, 1.01, 0.05), 2)
auc_c = np.array([auc_intra(-(d["ln_w"] + c * d["ln_v"]).to_numpy()) for c in cs])
c_otimo = cs[np.argmax(auc_c)]
rng = np.random.default_rng(3)
estudos = np.unique(g)
c_boot = []
for _ in range(1000):
    amostra = rng.choice(estudos, len(estudos))
    idx = np.concatenate([np.flatnonzero(g == e) for e in amostra])
    gg, yy = np.repeat(np.arange(len(amostra)), [np.sum(g == e) for e in amostra]), y[idx]
    lw, lv = d["ln_w"].to_numpy()[idx], d["ln_v"].to_numpy()[idx]
    def auc_b(esc):
        num = den = 0.0
        for k in np.unique(gg):
            m = gg == k
            if 0 < yy[m].sum() < m.sum():
                pares = yy[m].sum() * (m.sum() - yy[m].sum())
                num += roc_auc_score(yy[m], esc[m]) * pares
                den += pares
        return num / den if den else np.nan
    a = np.array([auc_b(-(lw + c * lv)) for c in cs])
    if np.all(np.isnan(a)):
        continue
    c_boot.append(cs[np.nanargmax(a)])
linhas.append({"analise": "expoente relativo de v que maximiza a AUC intra-estudo", "termo": "c (ω·v^c)",
               "valor": c_otimo, "IC95": f"{np.percentile(c_boot, 2.5):.2f} a {np.percentile(c_boot, 97.5):.2f}"})
for c in [-1.0, -0.5, 0.0]:
    linhas.append({"analise": "AUC intra-estudo na varredura", "termo": f"c = {c}", "valor": auc_c[cs == c][0]})
pd.DataFrame({"c": cs, "auc_intra": auc_c}).to_csv(SAIDA / "tabelas" / "r09_varredura_c.csv", index=False,
                                                   float_format="%.4f")

out = pd.DataFrame(linhas)
out.to_csv(SAIDA / "tabelas" / "r09_dentro_do_estudo.csv", index=False, float_format="%.4f")
print(out.to_string(index=False))
