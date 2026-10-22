"""R02 -- Avalia todos os modelos pelo protocolo: split oficial 78/30, 500 splits 78/30 e LOSO.

Uso: python r02_validacao.py [--sem-p-theta] [--sem-duvidosas] [--n 500]
Saídas: resultados/tabelas/validacao<sufixo>.csv (resumo) e resultados/brutos/*.csv.gz (por split).
"""
import argparse
import re
import time
import unicodedata

import pandas as pd

from dados import SAIDA, carregar
from modelos import catalogo
from nucleo import wilson
from validacao import N_SPLITS, loso, oficial, repetidos, resumo_repetidos


def slug(nome):
    a = unicodedata.normalize("NFKD", nome).encode("ascii", "ignore").decode()
    return re.sub(r"[^A-Za-z0-9]+", "_", a).strip("_")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sem-p-theta", action="store_true")
    ap.add_argument("--sem-duvidosas", action="store_true")
    ap.add_argument("--n", type=int, default=N_SPLITS)
    ap.add_argument("--so", default=None, help="roda só os modelos cujo nome contém este texto")
    a = ap.parse_args()
    sufixo = ("_sem_p_theta" if a.sem_p_theta else "") + ("_sem_84_89" if a.sem_duvidosas else "")
    df = carregar(excluir_duvidosas=a.sem_duvidosas)
    (SAIDA / "brutos").mkdir(parents=True, exist_ok=True)
    (SAIDA / "tabelas").mkdir(parents=True, exist_ok=True)

    linhas, loso_estudos = [], []
    for criterio in ["acc", "bal"]:
        for nome, fab in catalogo(criterio, a.sem_p_theta).items():
            if a.so and a.so not in nome:
                continue
            t0 = time.time()
            of, m, tr, te, prev = oficial(fab, df)
            lo, lo_est, _ = loso(fab, df)
            rep = repetidos(fab, df, n=a.n)
            rep.to_csv(SAIDA / "brutos" / f"rep{sufixo}_{criterio}_{slug(nome)}.csv.gz", index=False)
            lo_est.insert(0, "modelo", nome)
            lo_est.insert(1, "criterio", criterio)
            loso_estudos.append(lo_est)
            acertos = of["tp"] + of["tn"]
            lo_ic, hi_ic = wilson(acertos, of["n"])
            linhas.append({
                "modelo": nome, "criterio": criterio,
                "of_acc": of["acc"], "of_acc_IC95": f"{lo_ic:.2f}-{hi_ic:.2f}", "of_bal": of["bal"],
                "of_sens": of["sens"], "of_espec": of["espec"], "of_tr_acc": of["tr_acc"], "of_tr_bal": of["tr_bal"],
                "of_matriz(tp,fn,fp,tn)": f"{of['tp']},{of['fn']},{of['fp']},{of['tn']}",
                "of_info": {k: v for k, v in of.items() if k in ("escolhido", "termos", "I_crit")},
                **resumo_repetidos(rep),
                "loso_acc": lo["acc"], "loso_bal": lo["bal"], "loso_sens": lo["sens"], "loso_espec": lo["espec"],
            })
            print(f"{criterio} {nome:22s} of={of['acc']:.3f}/{of['bal']:.3f} rep={rep['acc'].mean():.3f}"
                  f"/{rep['bal'].mean():.3f} loso={lo['acc']:.3f}/{lo['bal']:.3f}  ({time.time() - t0:.0f}s)",
                  flush=True)
    res = pd.DataFrame(linhas)
    nome_arq = f"validacao{sufixo}" + (f"_{a.so}" if a.so else "")
    res.to_csv(SAIDA / "tabelas" / f"{nome_arq}.csv", index=False, float_format="%.4f")
    pd.concat(loso_estudos).to_csv(SAIDA / "tabelas" / f"loso_por_estudo{sufixo}.csv", index=False)


if __name__ == "__main__":
    main()
