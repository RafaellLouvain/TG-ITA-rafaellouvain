"""Núcleo de cálculo: regressão logística em ln(Π) (= lei de potência), escolha do limiar e métricas.

Convenção: 'escore' s cresce com o risco de vazio; vazio previsto se s > limiar.
Para as leis de potência, s = ln C_void + const; C_void = exp(s - limiar) e vazio se C_void > 1.
"""
import numpy as np
from scipy.special import expit
from sklearn.model_selection import RepeatedStratifiedKFold

from dados import GRUPOS, VARIAVEIS, matriz_grupos


# ----------------------------------------------------------------------------------------------------------------
# Regressão logística (Newton-Raphson / IRLS com busca em linha) -- ajusta os expoentes da lei de potência
# ----------------------------------------------------------------------------------------------------------------
def logistica(X, y, pesos=None, l2=0.0, max_iter=100, tol=1e-9):
    """Retorna (b0, beta). X já em ln(Π). l2 > 0 aplica penalidade nos coeficientes padronizados (só checagem).
    Em subconjuntos perfeitamente separáveis (raros, ~2 % das amostras pequenas) os coeficientes crescem sem limite
    até o fim das iterações; a previsão (sinal do escore) continua válida."""
    with np.errstate(over="ignore", invalid="ignore"):
        return _logistica(X, y, pesos, l2, max_iter, tol)


def _logistica(X, y, pesos, l2, max_iter, tol):
    X = np.asarray(X, float)
    y = np.asarray(y, float)
    n, k = X.shape
    w = np.ones(n) if pesos is None else np.asarray(pesos, float)
    mu_x = X.mean(0) if k else np.zeros(0)
    sd_x = X.std(0) if k else np.zeros(0)
    sd_x = np.where(sd_x > 0, sd_x, 1.0)
    Z = (X - mu_x) / sd_x                                     # padronizado (condicionamento numérico)
    A = np.column_stack([np.ones(n), Z])
    R = np.eye(k + 1) * (l2 + 1e-8)                          # 1e-8: só estabilidade numérica
    R[0, 0] = 0.0
    b = np.zeros(k + 1)
    p0 = np.clip(np.average(y, weights=w), 1e-6, 1 - 1e-6)
    b[0] = np.log(p0 / (1 - p0))

    def objetivo(bb):
        eta = A @ bb
        return np.sum(w * (y * eta - np.logaddexp(0, eta))) - 0.5 * bb @ R @ bb

    f = objetivo(b)
    for _ in range(max_iter):
        eta = A @ b
        mu = expit(eta)
        g = A.T @ (w * (y - mu)) - R @ b
        H = A.T @ (A * (w * mu * (1 - mu))[:, None]) + R
        passo = np.linalg.solve(H, g)
        t = 1.0
        while True:
            b_novo = b + t * passo
            f_novo = objetivo(b_novo)
            if f_novo >= f - 1e-12 or t < 1e-6:
                break
            t /= 2
        b, f_antigo, f = b_novo, f, f_novo
        if np.max(np.abs(t * passo)) < tol or abs(f - f_antigo) < 1e-12:
            break
    beta = b[1:] / sd_x
    b0 = b[0] - np.sum(beta * mu_x)
    return b0, beta


def pesos_classe(y, modo):
    y = np.asarray(y)
    if modo is None:
        return None
    n1, n0 = y.sum(), len(y) - y.sum()
    return np.where(y == 1, len(y) / (2 * n1), len(y) / (2 * n0))


# ----------------------------------------------------------------------------------------------------------------
# Métricas e limiar
# ----------------------------------------------------------------------------------------------------------------
def metricas(y, yhat):
    y = np.asarray(y).astype(int)
    yhat = np.asarray(yhat).astype(int)
    tp = int(np.sum((y == 1) & (yhat == 1)))
    tn = int(np.sum((y == 0) & (yhat == 0)))
    fp = int(np.sum((y == 0) & (yhat == 1)))
    fn = int(np.sum((y == 1) & (yhat == 0)))
    sens = tp / (tp + fn) if tp + fn else np.nan
    espec = tn / (tn + fp) if tn + fp else np.nan
    return dict(acc=(tp + tn) / len(y), bal=np.nanmean([sens, espec]), sens=sens, espec=espec,
                tp=tp, tn=tn, fp=fp, fn=fn, n=len(y))


def escolher_limiar(s, y, criterio):
    """Limiar sobre o escore s que maximiza a acurácia ('acc') ou a acurácia balanceada ('bal') no treino.
    Empates: mediana dos limiares empatados."""
    s = np.asarray(s, float)
    y = np.asarray(y).astype(int)
    u = np.unique(s)
    cand = np.concatenate([[u[0] - 1.0], (u[:-1] + u[1:]) / 2, [u[-1] + 1.0]])
    prev = s[None, :] > cand[:, None]
    tp = (prev & (y == 1)).sum(1)
    fp = (prev & (y == 0)).sum(1)
    P, N = y.sum(), len(y) - y.sum()
    tn = N - fp
    if criterio == "acc":
        val = (tp + tn) / len(y)
    else:
        val = 0.5 * (tp / P + tn / N)
    melhores = np.flatnonzero(np.isclose(val, val.max()))
    return cand[melhores[len(melhores) // 2]]


def wilson(acertos, n, z=1.96):
    p = acertos / n
    den = 1 + z ** 2 / n
    c = (p + z ** 2 / (2 * n)) / den
    h = z * np.sqrt(p * (1 - p) / n + z ** 2 / (4 * n ** 2)) / den
    return c - h, c + h


# ----------------------------------------------------------------------------------------------------------------
# Modelos (todos com: ajustar(df) -> self ; escore(df) ; prever(df))
# ----------------------------------------------------------------------------------------------------------------
class Majoritaria:
    nome = "Classe majoritária"

    def __init__(self, criterio="acc"):
        self.criterio = criterio

    def ajustar(self, df):
        self.classe = int(df["vazio"].mean() > 0.5)
        return self

    def escore(self, df):
        return np.full(len(df), float(self.classe))

    def prever(self, df):
        return np.full(len(df), self.classe)


class Indice:
    """Abordagem A: um índice físico I (produto de potências fixas) + limiar. Risco cresce quando I diminui.
    C_void = I_crit / I ; vazio se C_void > 1."""

    def __init__(self, grupo, criterio="acc", nome=None):
        self.grupo, self.criterio = grupo, criterio
        self.nome = nome or grupo

    def escore(self, df):
        return -df["ln_" + self.grupo].to_numpy()

    def ajustar(self, df):
        self.limiar = escolher_limiar(self.escore(df), df["vazio"].to_numpy(), self.criterio)
        self.I_crit = np.exp(-self.limiar)
        return self

    def prever(self, df):
        return (self.escore(df) > self.limiar).astype(int)


class LeiPotencia:
    """Abordagens B e C: C_void = C0 * prod(Π_i^beta_i), calibrada por regressão logística em ln Π."""

    def __init__(self, termos, criterio="acc", pesos="balanceado", l2=0.0, nome=None):
        self.termos, self.criterio, self.pesos, self.l2 = list(termos), criterio, pesos, l2
        self.nome = nome or "+".join(termos)

    def _X(self, df):
        return df[["ln_" + g for g in self.termos]].to_numpy() if self.termos else np.zeros((len(df), 0))

    def ajustar(self, df):
        y = df["vazio"].to_numpy()
        self.b0, self.beta = logistica(self._X(df), y, pesos_classe(y, self.pesos), self.l2)
        self.limiar = escolher_limiar(self.escore(df), y, self.criterio)
        self.lnC0 = self.b0 - self.limiar                    # ln C_void = lnC0 + sum(beta ln Π)
        return self

    def escore(self, df):
        return self.b0 + self._X(df) @ self.beta

    def ln_cvoid(self, df):
        return self.lnC0 + self._X(df) @ self.beta

    def prever(self, df):
        return (self.escore(df) > self.limiar).astype(int)

    def expoentes_variaveis(self):
        """Expoente efetivo de cada variável física (soma sobre os termos)."""
        return dict(zip(VARIAVEIS, matriz_grupos(self.termos) @ self.beta))


def _cv_interna(df, fabrica, criterio, n_rep, semente):
    """Média da métrica (acc ou bal) em CV estratificada 5-fold repetida, dentro do treino."""
    y = df["vazio"].to_numpy()
    rskf = RepeatedStratifiedKFold(n_splits=5, n_repeats=n_rep, random_state=semente)
    vals = []
    for tr, te in rskf.split(np.zeros(len(y)), y):
        m = fabrica().ajustar(df.iloc[tr])
        vals.append(metricas(y[te], m.prever(df.iloc[te]))[criterio])
    return float(np.mean(vals))


class SelecaoConjunto:
    """Modelo B final: escolhe, só com o treino (CV interna), o melhor entre os conjuntos B1, B2, B3."""

    def __init__(self, conjuntos, criterio="acc", pesos="balanceado", n_rep=4, semente=0):
        self.conjuntos, self.criterio, self.pesos = conjuntos, criterio, pesos
        self.n_rep, self.semente = n_rep, semente
        self.nome = "B (seleção)"

    def ajustar(self, df):
        self.notas = {}
        for nome, termos in self.conjuntos.items():
            fab = lambda t=termos: LeiPotencia(t, self.criterio, self.pesos)
            self.notas[nome] = _cv_interna(df, fab, self.criterio, self.n_rep, self.semente)
        melhor = max(self.notas.values())
        empatados = [n for n, v in self.notas.items() if np.isclose(v, melhor)]
        self.escolhido = min(empatados, key=lambda n: len(self.conjuntos[n]))
        self.modelo = LeiPotencia(self.conjuntos[self.escolhido], self.criterio, self.pesos).ajustar(df)
        return self

    def escore(self, df):
        return self.modelo.escore(df)

    def prever(self, df):
        return self.modelo.prever(df)


class Hibrido:
    """Abordagem C: núcleo físico fixo (ln ωR_s com um coeficiente) + termos adimensionais adicionados um a um
    (seleção progressiva), aceitos só se aumentarem a métrica de teste da CV interna em >= ganho_min."""

    def __init__(self, candidatos, nucleo="wRs", criterio="acc", pesos="balanceado", ganho_min=0.01,
                 n_rep=4, semente=0):
        self.candidatos, self.nucleo, self.criterio, self.pesos = list(candidatos), nucleo, criterio, pesos
        self.ganho_min, self.n_rep, self.semente = ganho_min, n_rep, semente
        self.nome = "C (híbrido)"

    def ajustar(self, df):
        atuais = [self.nucleo]
        fab = lambda t: (lambda: LeiPotencia(t, self.criterio, self.pesos))
        nota = _cv_interna(df, fab(atuais), self.criterio, self.n_rep, self.semente)
        self.trajetoria = [(self.nucleo, nota)]
        restantes = list(self.candidatos)
        while restantes:
            notas = {c: _cv_interna(df, fab(atuais + [c]), self.criterio, self.n_rep, self.semente)
                     for c in restantes}
            c_best = max(notas, key=notas.get)
            if notas[c_best] < nota + self.ganho_min:
                break
            atuais.append(c_best)
            restantes.remove(c_best)
            nota = notas[c_best]
            self.trajetoria.append((c_best, nota))
        self.termos = atuais
        self.modelo = LeiPotencia(atuais, self.criterio, self.pesos).ajustar(df)
        return self

    def escore(self, df):
        return self.modelo.escore(df)

    def prever(self, df):
        return self.modelo.prever(df)
