"""Catálogo dos modelos do TG2 (abordagens A, B, C e referências). Ver docs/05_modelagem/plano_capitulos_*.md."""
from functools import partial

from nucleo import Hibrido, Indice, LeiPotencia, Majoritaria, SelecaoConjunto

CONJUNTOS_B = {
    # B1 -- Buckingham completo (TG1): os 7 grupos independentes
    "B1": ["wRs_v", "Pe", "p_sy", "t_Rs", "Rpr_Rs", "Rpt_Rpr", "theta"],
    # B2 -- térmico: geração de calor no ombro + condução (Schmidt; fator ωR_s²/α do Q* de Arora et al. 2011)
    "B2": ["wRs2_a", "Pe", "p_sy", "t_Rs"],
    # B3 -- escoamento/extrusão (Arbegast 2008; Ahmed et al. 2019, 2021)
    "B3": ["wRs_v", "Rpr_Rs", "Rpt_Rpr", "t_Rpr", "p_sy"],
}
CANDIDATOS_C = ["wRs_v", "Pe", "p_sy", "t_Rs", "Rpr_Rs", "Rpt_Rpr", "theta"]
SEM_P_THETA = {"p_sy", "theta"}                     # robustez 1: sem os termos com valores assumidos


def catalogo(criterio, sem_p_theta=False):
    """Dicionário nome -> fábrica (picklável) para um critério de limiar ('acc' ou 'bal')."""
    filtra = (lambda ts: [t for t in ts if t not in SEM_P_THETA]) if sem_p_theta else (lambda ts: list(ts))
    conj = {k: filtra(v) for k, v in CONJUNTOS_B.items()}
    m = {
        "Majoritária": partial(Majoritaria, criterio),
        "A0 (ω)": partial(Indice, "w", criterio),
        "A (ωR_s)": partial(Indice, "wRs", criterio),
        "A' (ωR_s/v)": partial(Indice, "wRs_v", criterio),
        "A'' (ωR_s²/α)": partial(Indice, "wRs2_a", criterio),
    }
    for nome, termos in conj.items():
        m[nome] = partial(LeiPotencia, termos, criterio, "balanceado")
        m[nome + " s/ peso"] = partial(LeiPotencia, termos, criterio, None)
    m["B (seleção)"] = partial(SelecaoConjunto, conj, criterio, "balanceado")
    m["C (híbrido)"] = partial(Hibrido, filtra(CANDIDATOS_C), "wRs", criterio, "balanceado")
    return m
