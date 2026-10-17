# TG — C_void para vazios em FSW (ITA 2026)

Trabalho de Graduação do Rafael Louvain: equação adimensional simples (Coeficiente Analítico de Vazio, C_void)
para prever vazios em juntas FSW, calibrada no dataset de Du, Mukherjee & DebRoy (2019) — 108 soldas.

- **Toda a base de conhecimento está em `docs/`** — comece por `docs/README.md` e `docs/00_projeto/visao_geral.md`.
- Registre decisões em `docs/00_projeto/decisoes_e_pendencias.md` (com data).
- Responda ao usuário em português.
- Não confie no TG1 nem no chat do Gemini como fonte: várias citações estão erradas
  (`docs/03_tg1/erros_e_correcoes_tg1.md`). Confira sempre no PDF em `referencias/`.
- Dataset: `dados/Welding_process_parameters.csv` — linha 2 é de unidades; 1ª coluna é índice; coluna `Alloy`
  errada em 33 linhas (use α/σ_y); `*` = valor assumido. Detalhes em `docs/01_dados/dataset.md`.
- PDFs não têm `pdftotext` no sistema; use PyMuPDF em um venv no scratchpad.
