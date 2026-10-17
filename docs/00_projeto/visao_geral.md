# Visão geral do projeto (leia primeiro)

## Quem / o quê

- **Aluno:** Rafael Lucas de Albuquerque Louvain — Engenharia Mecânica-Aeronáutica, **ITA**, turma de 2026.
- **Orientador:** Prof. Dr. **Lindolfo Moreira Filho** (ITA) — mesmo orientador do TG do Ângelo Bezerra (2025).
  (O Gemini escreveu "Lindolfo Araújo Moreira Filho" — nome do meio **não confirmado**.)
- **TG** = Trabalho de Graduação (TCC). Duas etapas: **TG1** (proposta, ~10 p. + apresentação — **já feita e
  aprovada**, ~jun/2026) e **TG2/TG final** (2º semestre de 2026, entrega à banca em **dezembro/2026**).
- **Título (ficha aprovada pelo Colegiado):** *Análise da influência de parâmetros de processo de fabricação
  (cinemáticos, de geometria da ferramenta, entre outros) na integridade de juntas soldadas por FSW*.

## O problema

FSW (*Friction Stir Welding*, TWI 1991) une ligas de Al aeronáuticas no estado sólido. Um defeito crítico é o
**vazio/túnel** interno (void/tunneling), invisível por inspeção visual. Prever vazio exige hoje CFD/MEF (caro) ou ML
caixa-preta (Du et al. 2019). **Objetivo do TG:** uma **equação adimensional simples (Coeficiente Analítico de Vazio,
C_void)** que, a partir de parâmetros de máquina, ferramenta e material, diga se haverá vazio — usável no chão de
fábrica, com acurácia "satisfatória" (meta formal: **≥ 70 %** em teste cego), não necessariamente melhor que redes
neurais. Também: **hierarquizar** a influência das naturezas (geometria, cinemática, térmica, dinâmica).

## Restrições

- **Sem experimentos** (limitação de laboratório) → trabalho analítico-estatístico com dados secundários.
- Dados: dataset de **Du, Mukherjee & DebRoy (2019)**, 108 soldas (AA2024/2219/6061), via Kaggle
  (`dados/Welding_process_parameters.csv`). Ver [dataset](../01_dados/dataset.md).
- Preferência do Rafael: **não** fazer um trabalho de "ML"; ML no máximo como comparação.

## Estado em 12/10/2026

- TG1: relatório + apresentação aprovados ([relatorio_tg1](../03_tg1/relatorio_tg1.md),
  [apresentacao_tg1](../03_tg1/apresentacao_tg1.md)).
- Pelo cronograma do TG1: Set = revisão complementar; **Out = consolidar equação + calibrar**; Nov = validação +
  sensibilidade; Dez = redação + entrega. **Ainda não há código nem equação definida** → estamos no ponto crítico.
- Leitura completa de todo o material feita; documentação em `docs/`.

## Achados da leitura que mudam o plano (resumo)

1. **Coluna `Alloy` do CSV está errada em 33 linhas** — usar α/σ_y para rotular a liga.
2. **72/108 pressões e 71/108 tilts são valores assumidos** por Du et al. (`*`) → termos "dinâmicos" fracos.
3. **Meta de 70 %:** trivial in-sample (só ω → 70,4 %), mas **difícil fora da amostra** (Π simples ~62–67 %, 10
   brutas ~73 % em CV; ~60 % deixando um estudo fora). O desafio real é normalizar entre estudos.
4. **Várias citações do TG1 estão erradas** (alucinações do Gemini) — lista em
   [erros_e_correcoes_tg1](../03_tg1/erros_e_correcoes_tg1.md).
5. O Π_Term usado nas versões do TG1 **não é adimensional**; a forma do C_void (aditiva vs multiplicativa) nunca foi
   fixada → proposta de unificação via lei de potência/logística em
   [proposta_modelagem](../05_modelagem/proposta_modelagem.md).
6. O TG do veterano (mesmo orientador) usou regressão logística em log(Q_eff), mas suas acurácias (83 %, 87 %…) são
   **iguais à classe majoritária** → cuidado metodológico que pode diferenciar este TG.
7. Formato do TG final deve seguir a **classe LaTeX do ITA** (ver [04_formato_ita](../04_formato_ita/)).
