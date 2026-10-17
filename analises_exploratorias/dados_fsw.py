"""Carregamento e tratamento do dataset de Du, Mukherjee & DebRoy (2019) + grandezas derivadas.

Exploratório (não é o código oficial do TG). Ver docs/01_dados/dataset.md para as armadilhas do CSV.
"""
from pathlib import Path

import numpy as np
import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
CSV = RAIZ / "dados" / "Welding_process_parameters.csv"

# Propriedades por liga. k, rho, cp reproduzem exatamente o alpha do CSV (k/(rho*cp)), o que indica que
# Du et al. usaram esses valores de handbook. T_solidus/T_liquidus: valores típicos (ASM) -- CONFIRMAR com fonte
# antes de usar no texto final.
LIGAS = {
    "2024": dict(k=121.0, rho=2780.0, cp=875.0, T_sol=502.0, T_liq=638.0),
    "2219": dict(k=120.0, rho=2840.0, cp=864.0, T_sol=543.0, T_liq=643.0),
    "6061": dict(k=167.0, rho=2700.0, cp=896.0, T_sol=582.0, T_liq=652.0),
}
ALPHA_PARA_LIGA = {4.97e-05: "2024", 4.89e-05: "2219", 6.90e-05: "6061"}
T0 = 25.0  # temperatura ambiente (°C)


def carregar(excluir_refs=()):
    df = pd.read_csv(CSV, skiprows=[1], encoding="utf-8-sig")
    df.columns = ["id", "alloy_csv", "v", "N", "t", "Rs", "p", "Rpr", "Rpt", "tilt", "alpha", "sy", "void", "ref"]
    for c in ["p", "tilt"]:
        s = df[c].astype(str)
        df[c + "_assumido"] = s.str.contains(r"\*")
        df[c] = s.str.replace("*", "", regex=False).str.strip().astype(float)
    # liga corrigida pelas propriedades (a coluna do Kaggle está desalinhada em 33 linhas)
    df["liga"] = df["alpha"].round(7).map({round(a, 7): l for a, l in ALPHA_PARA_LIGA.items()})
    assert df["liga"].notna().all()
    for nome in ["k", "rho", "cp", "T_sol", "T_liq"]:
        df[nome] = df["liga"].map({l: d[nome] for l, d in LIGAS.items()})
    # grupo = estudo de origem (ref 7 tem dois blocos com ligas diferentes)
    df["estudo"] = df["ref"].astype(str)
    df.loc[df["id"].between(84, 89), "estudo"] = "7b"
    df = df[~df["estudo"].isin([str(r) for r in excluir_refs])].reset_index(drop=True)
    return derivar(df)


def derivar(df):
    """Grandezas derivadas em SI. omega em rad/s; p e sy em Pa."""
    d = df
    d["w"] = 2 * np.pi * d["N"]                      # rad/s
    d["rpm"] = 60 * d["N"]
    d["v_mm_min"] = d["v"] * 6e4
    d["p_Pa"] = d["p"] * 1e6
    d["sy_Pa"] = d["sy"] * 1e6
    d["Rp"] = (d["Rpr"] + d["Rpt"]) / 2              # raio médio do pino
    d["Hp"] = d["t"]                                 # hipótese: pino ~ espessura (não há L_p no dataset)
    d["F"] = d["p_Pa"] * np.pi * d["Rs"] ** 2        # força axial equivalente (N)
    d["dT_sol"] = d["T_sol"] - T0
    return d


if __name__ == "__main__":
    df = carregar()
    print(df.groupby("liga")[["void"]].agg(["size", "sum"]))
    print(df.head().T)
