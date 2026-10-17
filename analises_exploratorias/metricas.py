"""Métricas para avaliar índices (1 variável + limiar) e modelos lei-de-potência (logística em log).

Convenção: para um índice x com sentido s (+1: x alto -> vazio; -1: x baixo -> vazio), a regra é
vazio  <=>  s*x > s*limiar.
"""
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import RepeatedStratifiedKFold

CV = RepeatedStratifiedKFold(n_splits=5, n_repeats=20, random_state=0)


def melhor_limiar(x, y, s):
    """Limiar que maximiza a acurácia no conjunto dado (pontos médios entre valores ordenados)."""
    z = s * np.asarray(x, float)
    u = np.unique(z)
    cands = np.concatenate([[u[0] - 1], (u[:-1] + u[1:]) / 2, [u[-1] + 1]])
    accs = [((z > c).astype(int) == y).mean() for c in cands]
    i = int(np.argmax(accs))
    return s * cands[i], accs[i]


def avaliar_indice(x, y, grupos, s):
    """Acurácia in-sample, CV repetido (limiar escolhido no treino), LOSO (deixa um estudo fora) e AUCs."""
    x = np.asarray(x, float); y = np.asarray(y)
    lim, acc_in = melhor_limiar(x, y, s)
    acc_cv = []
    for tr, te in CV.split(x.reshape(-1, 1), y):
        l, _ = melhor_limiar(x[tr], y[tr], s)
        acc_cv.append(((s * x[te] > s * l).astype(int) == y[te]).mean())
    acertos = 0
    for g in np.unique(grupos):
        m = grupos == g
        l, _ = melhor_limiar(x[~m], y[~m], s)
        acertos += ((s * x[m] > s * l).astype(int) == y[m]).sum()
    auc = roc_auc_score(y, s * x)
    return dict(limiar=lim, acc_in=acc_in, acc_cv=np.mean(acc_cv), acc_loso=acertos / len(y),
                auc=auc, auc_intra=auc_intra_estudo(x, y, grupos, s))


def auc_intra_estudo(x, y, grupos, s):
    """Concordância só entre pares (vazio, são) do MESMO estudo: mede se o índice ordena bem dentro de cada
    estudo, independente do nível absoluto (que muda entre estudos)."""
    conc = tot = 0.0
    z = s * np.asarray(x, float)
    for g in np.unique(grupos):
        m = grupos == g
        a, b = z[m & (y == 1)], z[m & (y == 0)]
        if len(a) and len(b):
            dif = a[:, None] - b[None, :]
            conc += (dif > 0).sum() + 0.5 * (dif == 0).sum()
            tot += dif.size
    return conc / tot if tot else np.nan


def _logit(C=1e4):
    # C alto ~ sem regularização (queremos expoentes "físicos", não encolhidos)
    return LogisticRegression(C=C, max_iter=5000)


def avaliar_lei_potencia(Xlog, y, grupos, C=1e4):
    """Logística em ln(variáveis) = lei de potência C_void = e^b0 * prod x_i^b_i (vazio se C_void > 1).
    Retorna acurácias CV/LOSO e os expoentes ajustados em todos os dados."""
    X = np.asarray(Xlog, float); y = np.asarray(y)
    acc_cv = []
    for tr, te in CV.split(X, y):
        m = _logit(C).fit(X[tr], y[tr]); acc_cv.append(m.score(X[te], y[te]))
    acertos = 0
    for g in np.unique(grupos):
        msk = grupos == g
        if len(np.unique(y[~msk])) < 2:
            continue
        acertos += (_logit(C).fit(X[~msk], y[~msk]).predict(X[msk]) == y[msk]).sum()
    full = _logit(C).fit(X, y)
    eta = full.decision_function(X)
    return dict(acc_in=full.score(X, y), acc_cv=np.mean(acc_cv), acc_loso=acertos / len(y),
                auc=roc_auc_score(y, eta), auc_intra=auc_intra_estudo(eta, y, grupos, 1),
                b0=full.intercept_[0], expoentes=full.coef_[0])
