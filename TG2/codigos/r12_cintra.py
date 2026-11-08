"""R12 -- Aplicação do índice da abordagem 2 aos 47 ensaios de Cintra (2018) e fração de vazios por faixa de ωR_s.

Dados: dados/cintra_2018_ensaios.csv, transcrito das Tabelas 3.3 a 3.5 de Bezerra (2025), que consolidam os ensaios de
Cintra (2018): Alclad AA2024-T3, chapa de 3,2 mm, ferramenta única (ombro de 15,87 mm, pino de 6,4 mm); só a rotação e
o avanço variam. Alvo: "túnel no keyhole". Só a abordagem 2 é aplicável (as abordagens 1 e 3 exigiriam pressão,
inclinação e raio da ponta do pino, não registrados ensaio a ensaio).

(i) índice calibrado nas 108 soldas de Du et al. aplicado ao Cintra; (ii) limiar recalibrado no próprio Cintra, em 500
sorteios estratificados 33/14, com os critérios de acurácia e de acurácia balanceada; (iii) logística com ω e v livres.
"""
import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import StratifiedShuffleSplit

from dados import RAIZ, SAIDA, carregar
from nucleo import escolher_limiar, logistica, pesos_classe

T = SAIDA / "tabelas"
c = pd.read_csv(RAIZ / "dados" / "cintra_2018_ensaios.csv")
RS = 15.87e-3 / 2
c["wRs"] = 2 * np.pi * c["rpm"] / 60 * RS
y = c["tunel"].to_numpy()

# Fração com túnel por rotação
por_rot = c.groupby("rpm").agg(wRs=("wRs", "first"), n=("tunel", "size"), tunel=("tunel", "sum"))
por_rot["fracao"] = por_rot["tunel"] / por_rot["n"]
por_rot.to_csv(T / "r12_cintra_por_rotacao.csv")
print(por_rot.round(3))

# (i) Índice calibrado em Du et al. (V_crit nas 108 soldas, critério de acurácia)
du = carregar()
V_du = np.exp(-escolher_limiar(-du["ln_wRs"].to_numpy(), du["vazio"].to_numpy(), "acc"))
yh = (c["wRs"] < V_du).astype(int).to_numpy()
res = {"V_crit_du": V_du, "rpm_equivalente": V_du / (2 * np.pi / 60 * RS), "prev_vazio": yh.sum(),
       "acc": (yh == y).mean(), "acc_tunel_ou_preench": (yh == (c["tunel"] | c["sem_preench"])).mean(),
       "auc_rotacao": roc_auc_score(y, -c["rpm"])}

# (ii) Limiar recalibrado nos ensaios de Cintra
esc = -np.log(c["wRs"].to_numpy())
sss = StratifiedShuffleSplit(n_splits=500, test_size=14, random_state=2026)
for crit in ("acc", "bal"):
    res[f"V_crit_cintra_{crit}"] = np.exp(-escolher_limiar(esc, y, crit))
    m = []
    for tr, te in sss.split(esc, y):
        p = (esc[te] > escolher_limiar(esc[tr], y[tr], crit)).astype(int)
        se, es = p[y[te] == 1].mean(), 1 - p[y[te] == 0].mean()
        m.append(((p == y[te]).mean(), (se + es) / 2))
    res[f"teste_acc_{crit}"], res[f"teste_bal_{crit}"] = np.mean(m, axis=0)

# (iii) Logística com ω e v livres
b0, b = logistica(np.c_[np.log(c["rpm"]), np.log(c["v_mm_min"])], y, pesos_classe(y, "balanceado"))
res["expoente_w"], res["expoente_v"] = b
pd.Series(res).to_csv(T / "r12_cintra_resultados.csv", header=["valor"])
print(pd.Series(res).round(3))

# Fração de soldas com vazio por faixa de ωR_s na base de Du et al.
du["faixa"] = pd.cut(du["wRs"], [0, 0.5, 0.84, 1.05, 1.3, 1.8])
faixas = du.groupby("faixa", observed=True)["vazio"].agg(n="size", vazios="sum")
faixas["fracao"] = faixas["vazios"] / faixas["n"]
faixas.to_csv(T / "r12_du_faixas_wRs.csv")
print(faixas.round(3), "\nmaior ωR_s com vazio:", du.loc[du["vazio"] == 1, "wRs"].max().round(3))
