"""R07 -- Análise dos erros (seção 4.7): frequência de erro de cada solda nos 500 splits e acerto por estudo (LOSO)."""
import pandas as pd

from dados import SAIDA, carregar
from r02_validacao import slug

T, B = SAIDA / "tabelas", SAIDA / "brutos"
d = carregar().set_index("id")

linhas = []
for modelo in ["A (ωR_s)", "B (seleção)", "C (híbrido)"]:
    for crit in ["acc", "bal"]:
        r = pd.read_csv(B / f"rep_{crit}_{slug(modelo)}.csv.gz")
        vezes_teste = pd.Series(" ".join(r["ids_teste"]).split()).astype(int).value_counts()
        vezes_erro = pd.Series(" ".join(r["ids_erro"].fillna("")).split()).astype(int).value_counts()
        taxa = (vezes_erro.reindex(vezes_teste.index, fill_value=0) / vezes_teste).rename("taxa_erro")
        x = d.join(taxa)
        x["modelo"], x["criterio"] = modelo, crit
        linhas.append(x.reset_index()[["modelo", "criterio", "id", "estudo", "liga", "rpm", "v_mm_min", "Rs", "t",
                                       "wRs", "vazio", "taxa_erro"]])
err = pd.concat(linhas)
err.to_csv(T / "r07_erro_por_solda.csv", index=False, float_format="%.3f")
por_estudo = err.groupby(["modelo", "criterio", "estudo"]).agg(n=("id", "size"), vazios=("vazio", "sum"),
                                                                taxa_erro_media=("taxa_erro", "mean"))
por_estudo.to_csv(T / "r07_erro_por_estudo.csv", float_format="%.3f")
print(por_estudo.unstack(["modelo", "criterio"])["taxa_erro_media"].round(2).to_string())
sempre = err[err["taxa_erro"] >= 0.8].sort_values(["modelo", "criterio", "estudo"])
print("\nSoldas erradas em >= 80 % das vezes em que caem no teste:")
print(sempre.groupby(["modelo", "criterio"])["id"].apply(lambda s: " ".join(map(str, s))).to_string())

lo = pd.read_csv(T / "loso_por_estudo.csv")
lo["acerto"] = lo["acertos"] / lo["n"]
print("\nLOSO: acerto por estudo")
print(lo[lo["modelo"].isin(["A (ωR_s)", "B (seleção)", "C (híbrido)"])]
      .pivot_table(index="estudo", columns=["modelo", "criterio"], values="acerto").round(2).to_string())
