"""Leitura e tratamento do dataset de Du, Mukherjee e DebRoy (2019) para o TG2.

Decisões (docs/05_modelagem/protocolo_metodologia.md, seção 3):
- CSV com BOM; linha 2 = unidades (descartada); 1ª coluna = índice;
- coluna Alloy NÃO é usada (desalinhada em 33 linhas); quando é preciso agrupar por liga, a liga é identificada
  pelo par (alpha, sigma_y), que é 1:1 com a liga;
- tudo em SI: omega em rad/s, p e sigma_y em Pa, comprimentos em m, v em m/s, alpha em m²/s; theta em graus
  (adimensional);
- valores com '*' (assumidos por Du et al.) viram número + marcador p_assumido / theta_assumido;
- estudo de origem = coluna Refs; as linhas 84-89 (ref. 7 com propriedades de 6061) formam o grupo '7b'.
"""
from pathlib import Path

import numpy as np
import pandas as pd

RAIZ = Path(__file__).resolve().parents[2]
CSV = RAIZ / "dados" / "Welding_process_parameters.csv"
SAIDA = Path(__file__).resolve().parents[1] / "resultados"

LIGA_POR_ALPHA = {4.97e-05: "AA2024", 4.89e-05: "AA2219", 6.90e-05: "AA6061"}
LINHAS_DUVIDOSAS = list(range(84, 90))          # ref. 7 com propriedades de 6061

# Variáveis físicas usadas no modelo (SI) e sua natureza (Tabela 3.1 do TG1, 5 naturezas)
VARIAVEIS = ["w", "v", "Rs", "Rpr", "Rpt", "t", "alpha", "p", "theta", "sy"]
NATUREZA = {
    "w": "Cinemática", "v": "Cinemática",
    "Rs": "Geométrica", "Rpr": "Geométrica", "Rpt": "Geométrica", "t": "Geométrica",
    "alpha": "Térmica",
    "p": "Dinâmica", "theta": "Dinâmica",
    "sy": "Metalúrgica",
}
NATUREZAS = ["Cinemática", "Geométrica", "Térmica", "Dinâmica", "Metalúrgica"]
SIMBOLO = {"w": "ω", "v": "v", "Rs": "R_s", "Rpr": "R_pr", "Rpt": "R_pt", "t": "t", "alpha": "α",
           "p": "p", "theta": "θ", "sy": "σ_y"}

SIMBOLO_TEX = {"w": r"$\omega$", "v": r"$v$", "Rs": r"$R_s$", "Rpr": r"$R_{pr}$", "Rpt": r"$R_{pt}$", "t": r"$t$",
               "alpha": r"$\alpha$", "p": r"$p$", "theta": r"$\theta$", "sy": r"$\sigma_y$"}

# Grupos adimensionais: expoente de cada variável física (matriz dimensional da análise de Buckingham)
GRUPOS = {
    "wRs_v":    {"w": 1, "Rs": 1, "v": -1},           # avanço por rotação adimensional (cinemático)
    "Pe":       {"v": 1, "Rs": 1, "alpha": -1},       # Péclet de avanço
    "wRs2_a":   {"w": 1, "Rs": 2, "alpha": -1},       # Péclet rotacional (= wRs_v * Pe)
    "p_sy":     {"p": 1, "sy": -1},                   # pressão relativa
    "t_Rs":     {"t": 1, "Rs": -1},                   # espessura relativa ao ombro
    "Rpr_Rs":   {"Rpr": 1, "Rs": -1},                 # razão pino/ombro
    "Rpt_Rpr":  {"Rpt": 1, "Rpr": -1},                # conicidade do pino
    "t_Rpr":    {"t": 1, "Rpr": -1},                  # profundidade relativa do pino
    "theta":    {"theta": 1},                         # inclinação (já adimensional)
    "wRs":      {"w": 1, "Rs": 1},                    # velocidade periférica do ombro (m/s) -- dimensional
    "w":        {"w": 1},                             # só rotação (rad/s) -- dimensional
}
ROTULO = {
    "wRs_v": "ωR_s/v", "Pe": "vR_s/α", "wRs2_a": "ωR_s²/α", "p_sy": "p/σ_y", "t_Rs": "t/R_s",
    "Rpr_Rs": "R_pr/R_s", "Rpt_Rpr": "R_pt/R_pr", "t_Rpr": "t/R_pr", "theta": "θ", "wRs": "ωR_s", "w": "ω",
}


def carregar(excluir_duvidosas=False):
    df = pd.read_csv(CSV, skiprows=[1], encoding="utf-8-sig")
    df.columns = ["id", "alloy_csv", "v", "N", "t", "Rs", "p_MPa", "Rpr", "Rpt", "theta", "alpha", "sy_MPa",
                  "vazio", "ref"]
    df = df.drop(columns="alloy_csv")                       # coluna Alloy descartada
    for c, flag in [("p_MPa", "p_assumido"), ("theta", "theta_assumido")]:
        s = df[c].astype(str)
        df[flag] = s.str.contains(r"\*")
        df[c] = s.str.replace("*", "", regex=False).str.strip().astype(float)
    df["liga"] = df["alpha"].round(7).map({round(a, 7): l for a, l in LIGA_POR_ALPHA.items()})
    assert df["liga"].notna().all()
    df["estudo"] = df["ref"].astype(str)
    df.loc[df["id"].isin(LINHAS_DUVIDOSAS), "estudo"] = "7b"
    if excluir_duvidosas:
        df = df[~df["id"].isin(LINHAS_DUVIDOSAS)].reset_index(drop=True)
    # SI
    df["w"] = 2 * np.pi * df["N"]                            # rad/s
    df["p"] = df["p_MPa"] * 1e6                              # Pa
    df["sy"] = df["sy_MPa"] * 1e6                            # Pa
    df["rpm"] = 60 * df["N"]
    df["wRs"] = df["w"] * df["Rs"]                          # velocidade periférica do ombro (m/s)
    df["v_mm_min"] = df["v"] * 6e4
    df["vazio"] = df["vazio"].astype(int)
    for k in VARIAVEIS:
        df["ln_" + k] = np.log(df[k])
    for g, exps in GRUPOS.items():
        df["ln_" + g] = sum(e * df["ln_" + k] for k, e in exps.items())
    return df


def matriz_grupos(termos):
    """Matriz M (variáveis × termos): expoente de cada variável física em cada termo."""
    return np.array([[GRUPOS[g].get(k, 0) for g in termos] for k in VARIAVEIS], dtype=float)


if __name__ == "__main__":
    d = carregar()
    print(d.shape, "vazios:", d["vazio"].sum())
    print(d.groupby("liga")["vazio"].agg(["size", "sum"]))
    print(d.groupby("estudo")["vazio"].agg(["size", "sum"]))
    print(d[["ln_" + g for g in GRUPOS]].describe().T.round(2))
