"""R03 -- Modelo B: expoentes, sinais, bootstrap por estudo, contribuição por natureza, tornado e retirada de
natureza (seção 4.2). Roda para os três conjuntos (B1, B2, B3); o texto usa o conjunto escolhido.

Os expoentes não dependem do critério de limiar (acc/bal): só o limiar muda. Pesos de classe: balanceados.
"""
from functools import partial

import matplotlib.ticker
import numpy as np
import pandas as pd
from scipy.linalg import null_space

from dados import SIMBOLO_TEX, NATUREZA, NATUREZAS, SAIDA, SIMBOLO, VARIAVEIS, carregar, matriz_grupos
from estilo import CM, plt, salvar
from modelos import CONJUNTOS_B
from nucleo import LeiPotencia, SelecaoConjunto, logistica, metricas, pesos_classe
from validacao import SEMENTE_OFICIAL, loso, repetidos, split

T = SAIDA / "tabelas"
d = carregar()
tr, te = split(d, SEMENTE_OFICIAL)
dtr = d.iloc[tr]
N_BOOT = 1000
# Sinal esperado do expoente no RISCO de vazio (Tabela de síntese, seção 2.9): +1 aumenta, -1 reduz, 0 incerto
ESPERADO = {"w": -1, "v": +1, "Rs": -1, "Rpr": 0, "Rpt": 0, "t": +1, "alpha": +1, "p": -1, "theta": -1, "sy": 0}
LN = np.column_stack([d["ln_" + k] for k in VARIAVEIS])          # ln das variáveis físicas (108 × 10)


def contrib_natureza(e):
    """Desvio-padrão (no dataset) da contribuição de cada natureza ao ln C_void."""
    out = {}
    for nat in NATUREZAS:
        idx = [i for i, k in enumerate(VARIAVEIS) if NATUREZA[k] == nat]
        out[nat] = float(np.std(LN[:, idx] @ e[idx]))
    return out


# --- 0. qual conjunto o protocolo escolhe no treino oficial (para os dois critérios) --------------------------------
escolha = {c: SelecaoConjunto(CONJUNTOS_B, c, "balanceado").ajustar(dtr) for c in ["acc", "bal"]}
for c, m in escolha.items():
    print(f"critério {c}: notas CV interna {np.round(list(m.notas.values()), 3)} -> {m.escolhido}")
pd.DataFrame({c: m.notas for c, m in escolha.items()}).to_csv(T / "r03_selecao_conjunto_oficial.csv")

linhas_exp, linhas_var, linhas_nat, linhas_drop, linhas_rank = [], [], [], [], []
for nome, termos in CONJUNTOS_B.items():
    M = matriz_grupos(termos)
    # --- 1. expoentes (treino oficial), variantes: sem pesos, L2, dados completos ----------------------------------
    m = LeiPotencia(termos, "bal", "balanceado").ajustar(dtr)
    variantes = {
        "treino oficial (pesos bal.)": m.beta,
        "treino oficial (sem pesos)": LeiPotencia(termos, "bal", None).ajustar(dtr).beta,
        "treino oficial (L2, λ=1)": LeiPotencia(termos, "bal", "balanceado", l2=1.0).ajustar(dtr).beta,
        "108 soldas (pesos bal.)": LeiPotencia(termos, "bal", "balanceado").ajustar(d).beta,
    }
    # --- 2. bootstrap por estudo (dados completos) ------------------------------------------------------------------
    estudos = d["estudo"].unique()
    rng = np.random.default_rng(1)
    betas, ranks = [], []
    for _ in range(N_BOOT):
        amostra = rng.choice(estudos, len(estudos), replace=True)
        db = pd.concat([d[d["estudo"] == e] for e in amostra])
        if db["vazio"].nunique() < 2:
            continue
        yb = db["vazio"].to_numpy()
        _, bb = logistica(db[["ln_" + g for g in termos]].to_numpy(), yb, pesos_classe(yb, "balanceado"))
        betas.append(bb)
        cn = contrib_natureza(M @ bb)
        ordem = sorted(cn, key=cn.get, reverse=True)
        ranks.append({nat: ordem.index(nat) + 1 for nat in NATUREZAS if cn[nat] > 0})
    betas = np.array(betas)
    for j, g in enumerate(termos):
        linhas_exp.append({"conjunto": nome, "termo": g, **{k: v[j] for k, v in variantes.items()},
                           "boot_p2.5": np.percentile(betas[:, j], 2.5), "boot_p97.5": np.percentile(betas[:, j], 97.5),
                           "boot_frac_mesmo_sinal": np.mean(np.sign(betas[:, j]) == np.sign(m.beta[j]))})
    # expoentes efetivos das variáveis físicas + sinais
    e = M @ m.beta
    eb = betas @ M.T
    for i, k in enumerate(VARIAVEIS):
        if not np.any(M[i]):
            continue
        esp = ESPERADO[k]
        linhas_var.append({"conjunto": nome, "variavel": SIMBOLO[k], "natureza": NATUREZA[k], "expoente": e[i],
                           "boot_p2.5": np.percentile(eb[:, i], 2.5), "boot_p97.5": np.percentile(eb[:, i], 97.5),
                           "sinal_esperado": {1: "+", -1: "−", 0: "?"}[esp],
                           "confere": "–" if esp == 0 else ("sim" if np.sign(e[i]) == esp else "NÃO"),
                           "boot_frac_sinal_esperado": np.nan if esp == 0 else np.mean(np.sign(eb[:, i]) == esp)})
    # --- 3. contribuição por natureza + frequência de posição no bootstrap -----------------------------------------
    cn = contrib_natureza(e)
    rk = pd.DataFrame(ranks)
    for nat in NATUREZAS:
        linha = {"conjunto": nome, "natureza": nat, "contrib_sd_lnC": cn[nat]}
        if nat in rk:
            for pos in range(1, 6):
                linha[f"freq_pos{pos}"] = np.mean(rk[nat] == pos)
        linhas_nat.append(linha)
    # --- 4. retirada de natureza (restrição: expoentes das variáveis da natureza = 0) ------------------------------
    base_rep = repetidos(partial(LeiPotencia, termos, "bal", "balanceado"), d, n=500)
    base_lo, _, _ = loso(partial(LeiPotencia, termos, "bal", "balanceado"), d)
    for nat in NATUREZAS:
        idx = [i for i, k in enumerate(VARIAVEIS) if NATUREZA[k] == nat]
        if not np.any(M[idx]):
            continue
        Nn = null_space(M[idx])                          # combinações de termos sem a natureza
        dd = d.copy()
        novos = []
        for j in range(Nn.shape[1]):
            dd[f"ln_z{j}"] = dd[["ln_" + g for g in termos]].to_numpy() @ Nn[:, j]
            novos.append(f"z{j}")
        fab = partial(LeiPotencia, list(novos), "bal", "balanceado")
        rep = repetidos(fab, dd, n=500)
        lo, _, _ = loso(fab, dd)
        linhas_drop.append({"conjunto": nome, "natureza_retirada": nat, "termos_restantes": len(novos),
                            "rep_acc": rep["acc"].mean(), "Δrep_acc": rep["acc"].mean() - base_rep["acc"].mean(),
                            "rep_bal": rep["bal"].mean(), "Δrep_bal": rep["bal"].mean() - base_rep["bal"].mean(),
                            "loso_acc": lo["acc"], "Δloso_acc": lo["acc"] - base_lo["acc"],
                            "loso_bal": lo["bal"], "Δloso_bal": lo["bal"] - base_lo["bal"]})
    linhas_drop.append({"conjunto": nome, "natureza_retirada": "(nenhuma)", "termos_restantes": len(termos),
                        "rep_acc": base_rep["acc"].mean(), "rep_bal": base_rep["bal"].mean(),
                        "loso_acc": base_lo["acc"], "loso_bal": base_lo["bal"]})

    # --- 5. tornado (treino oficial): cada variável do p10 ao p90, demais na mediana --------------------------------
    med = np.median(LN, axis=0)
    base = m.lnC0 + med @ e
    barras = []
    for i, k in enumerate(VARIAVEIS):
        if abs(e[i]) < 1e-12:
            continue
        lo10, hi90 = np.percentile(LN[:, i], [10, 90])
        a, b = base + e[i] * (lo10 - med[i]), base + e[i] * (hi90 - med[i])
        barras.append((k, a, b))
    barras.sort(key=lambda x: abs(x[2] - x[1]))
    fig, ax = plt.subplots(figsize=(13 * CM, 0.75 * CM * len(barras) + 2 * CM))
    for y, (k, a, b) in enumerate(barras):
        ax.barh(y, np.exp(b) - np.exp(a), left=np.exp(a), color="#c0392b" if b > a else "#2471a3", alpha=0.85)
        ax.text(max(np.exp(a), np.exp(b)) * 1.08, y, f"{SIMBOLO_TEX[k]}  ({NATUREZA[k].lower()})", va="center",
                fontsize=8.5)
    ax.axvline(1, color="k", lw=1)
    ax.axvline(np.exp(base), color="gray", ls="--", lw=0.8)
    ax.set_xscale("log")
    ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, _: f"{x:g}"))
    ax.xaxis.set_minor_formatter(matplotlib.ticker.FuncFormatter(lambda x, _: f"{x:g}" if str(f"{x:g}")[0] in "25" else ""))
    ax.set_yticks([])
    ax.set_xlabel("$C_{void}$ (variável do percentil 10 ao 90; demais na mediana)")
    ax.grid(axis="y", visible=False)
    lim = ax.get_xlim()
    ax.set_xlim(lim[0], lim[1] * 6)
    salvar(fig, f"fig_r03_tornado_{nome}")
    pd.DataFrame([{"variavel": SIMBOLO[k], "Cvoid_p10": np.exp(a if e[VARIAVEIS.index(k)] else a),
                   "Cvoid_p90": np.exp(b), "cruza_limiar": (a > 0) != (b > 0)} for k, a, b in barras[::-1]]) \
        .to_csv(T / f"r03_tornado_{nome}.csv", index=False, float_format="%.3f")
    print(nome, "C_void na mediana =", round(float(np.exp(base)), 3), "| lnC0 =", round(m.lnC0, 3))

pd.DataFrame(linhas_exp).to_csv(T / "r03_expoentes_termos.csv", index=False, float_format="%.3f")
pd.DataFrame(linhas_var).to_csv(T / "r03_expoentes_variaveis.csv", index=False, float_format="%.3f")
pd.DataFrame(linhas_nat).to_csv(T / "r03_contribuicao_natureza.csv", index=False, float_format="%.3f")
pd.DataFrame(linhas_drop).to_csv(T / "r03_retirada_natureza.csv", index=False, float_format="%.3f")
for f in ["r03_expoentes_termos", "r03_expoentes_variaveis", "r03_contribuicao_natureza", "r03_retirada_natureza"]:
    print("\n==", f)
    print(pd.read_csv(T / f"{f}.csv").to_string(index=False))
