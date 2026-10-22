"""Protocolo de validação: split oficial 78/30, splits 78/30 repetidos e deixa-um-estudo-de-fora (LOSO)."""
import os
from concurrent.futures import ProcessPoolExecutor

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from nucleo import metricas

SEMENTE_OFICIAL = 2026          # fixada antes de rodar qualquer modelo (protocolo, seção 5)
N_TESTE = 30
N_SPLITS = 500


def split(df, semente, n_teste=N_TESTE):
    idx = np.arange(len(df))
    tr, te = train_test_split(idx, test_size=n_teste, stratify=df["vazio"], random_state=semente)
    return np.sort(tr), np.sort(te)


def _info(m):
    """Informações extras do modelo ajustado (conjunto escolhido, termos, limiar...)."""
    out = {}
    for atr in ["escolhido", "termos", "I_crit", "limiar"]:
        if hasattr(m, atr):
            v = getattr(m, atr)
            out[atr] = "+".join(v) if isinstance(v, list) else v
    if hasattr(m, "modelo") and hasattr(m.modelo, "termos"):
        out["termos"] = "+".join(m.modelo.termos)
    return out


def avaliar_split(fabrica, df, tr, te):
    m = fabrica().ajustar(df.iloc[tr])
    y = df["vazio"].to_numpy()
    r_te = metricas(y[te], m.prever(df.iloc[te]))
    r_tr = metricas(y[tr], m.prever(df.iloc[tr]))
    linha = {**{k: v for k, v in r_te.items()}, **{"tr_" + k: r_tr[k] for k in ["acc", "bal", "sens", "espec"]}}
    linha.update(_info(m))
    return linha, m, te, m.prever(df.iloc[te])


def _tarefa_repetida(args):
    fabrica, df, semente = args
    tr, te = split(df, semente)
    linha, _, te, prev = avaliar_split(fabrica, df, tr, te)
    linha["semente"] = semente
    erros = df["id"].to_numpy()[te][prev != df["vazio"].to_numpy()[te]]
    linha["ids_teste"] = " ".join(map(str, df["id"].to_numpy()[te]))
    linha["ids_erro"] = " ".join(map(str, erros))
    return linha


def repetidos(fabrica, df, n=N_SPLITS, processos=None):
    processos = processos or max(1, (os.cpu_count() or 2) - 1)
    args = [(fabrica, df, s) for s in range(n)]
    with ProcessPoolExecutor(processos) as ex:
        linhas = list(ex.map(_tarefa_repetida, args, chunksize=max(1, n // (4 * processos))))
    return pd.DataFrame(linhas)


def oficial(fabrica, df):
    tr, te = split(df, SEMENTE_OFICIAL)
    linha, m, te, prev = avaliar_split(fabrica, df, tr, te)
    return linha, m, tr, te, prev


def _tarefa_loso(args):
    fabrica, df, estudo = args
    te = np.flatnonzero(df["estudo"].to_numpy() == estudo)
    tr = np.flatnonzero(df["estudo"].to_numpy() != estudo)
    m = fabrica().ajustar(df.iloc[tr])
    return estudo, te, m.prever(df.iloc[te]), _info(m)


def loso(fabrica, df, processos=None):
    processos = processos or max(1, (os.cpu_count() or 2) - 1)
    estudos = sorted(df["estudo"].unique(), key=lambda s: (len(s), s))
    with ProcessPoolExecutor(processos) as ex:
        res = list(ex.map(_tarefa_loso, [(fabrica, df, e) for e in estudos]))
    prev = np.zeros(len(df), int)
    por_estudo = []
    for estudo, te, p, info in res:
        prev[te] = p
        y = df["vazio"].to_numpy()[te]
        por_estudo.append({"estudo": estudo, "n": len(te), "vazios": int(y.sum()),
                           "acertos": int((p == y).sum()), **info})
    total = metricas(df["vazio"].to_numpy(), prev)
    return total, pd.DataFrame(por_estudo), prev


def resumo_repetidos(r):
    return {
        "rep_acc_media": r["acc"].mean(), "rep_acc_p5": r["acc"].quantile(0.05),
        "rep_acc_p95": r["acc"].quantile(0.95), "rep_frac_acc>=70": (r["acc"] >= 0.70 - 1e-9).mean(),
        "rep_bal_media": r["bal"].mean(), "rep_sens_media": r["sens"].mean(), "rep_espec_media": r["espec"].mean(),
        "rep_tr_acc_media": r["tr_acc"].mean(),
    }
