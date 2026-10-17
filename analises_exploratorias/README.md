# Análises exploratórias (não oficiais)

Testes rápidos de relações entre variáveis para orientar a escolha do C_void. **Não é o código final do TG.**
Conclusões e tabelas comentadas: [`docs/05_modelagem/analises_exploratorias_2026-10-12.md`](../docs/05_modelagem/analises_exploratorias_2026-10-12.md).

## Como rodar

```bash
python -m venv .venv && .venv/bin/pip install -r requirements.txt
cd analises_exploratorias
../.venv/bin/python a01_indices_univariados.py      # ~10 s
../.venv/bin/python a02_rotacao_critica_por_estudo.py
../.venv/bin/python a03_lei_potencia_blocos.py      # ~1 min
../.venv/bin/python a04_grade_expoentes.py          # ~2 min
../.venv/bin/python a05_finalistas_robustez.py      # ~1 min
../.venv/bin/python a06_figuras.py
../.venv/bin/python a07_limiar_por_liga_e_erros.py
```

Saídas (CSV e PNG) em `resultados/`.

## Arquivos

| Arquivo | O que faz |
|---|---|
| `dados_fsw.py` | lê o CSV (pula linha de unidades, limpa `*`, **corrige a liga por α**), adiciona k/ρ/c_p/T_solidus por liga e grandezas derivadas |
| `metricas.py` | índice + limiar (in-sample, CV 5×20, LOSO, AUC, AUC intra-estudo); logística em log = lei de potência |
| `a01` | ~25 índices físicos isolados (cinemáticos, térmicos, geométricos, dinâmicos) |
| `a02` | rotação crítica de cada estudo e o que a explica |
| `a03` | leis de potência por blocos (expoentes livres) |
| `a04` | grade de expoentes "redondos" + 1 limiar; CV aninhada |
| `a05` | finalistas: split 78/30 repetido, sensibilidade/especificidade, por liga, sem ref. 15, p assumido |
| `a06` | figuras |
| `a07` | limiar por liga vs universal; acertos por estudo |
