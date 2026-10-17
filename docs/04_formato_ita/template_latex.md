# Template LaTeX — situação atual e plano para o TG final

## O que existe hoje: `TG1/TG1_relatorio_formato_latex.tex`

- `\documentclass[12pt,openany]{report}`, `babel` brazilian, `geometry` A4 **(sup 3 cm, inf 2 cm, esq 3 cm, dir 2 cm)**,
  `lmodern`, `onehalfspacing`, recuo de parágrafo 1,25 cm, `titlesec` (capítulo \Huge bold "1  Título"), `booktabs`,
  `tabularx`, `amsmath`, `tikz` (moldura da capa a 20 mm da borda), `hyperref[hidelinks]`.
- Capa manual em `titlepage` (TikZ): "INSTITUTO TECNOLÓGICO DE AERONÁUTICA" / logo `Imagens/ita-logo.png` (8,2 cm) /
  nome / título em caixa alta negrito / "Trabalho de Graduação" / "2026" / "Curso de Engenharia
  Mecânica-Aeronáutica".
- Resumo e Sumário manuais (`\@starttoc{toc}`), numeração arábica começando em 4.
- Referências digitadas à mão (sem BibTeX); citações como `\textit{Mishra \& Ma (2005)}`.
- Arquivos de imagem **ausentes** do repositório: `Imagens/ita-logo.png`,
  `Imagens/Captura de tela 2026-06-07 204639.png` (figura de Du et al. com as 4 variáveis causais).
- Equação do C_void com `\tag{3.1}` manual.

Serve como base rápida, mas **não atende o padrão do TG final** (ver abaixo).

## O padrão do TG final (do TG do Ângelo, aprovado em nov/2025)

Ver [tg_veterano_angelo](tg_veterano_angelo.md) para a ordem completa. Itens que o `report` atual **não tem**:
folha de rosto, ficha catalográfica CIP (com "REFERÊNCIA BIBLIOGRÁFICA" e "CESSÃO DE DIREITOS"), folha de aprovação,
dedicatória/agradecimentos/epígrafe (opcionais), **Abstract**, **Lista de Figuras**, Lista de Tabelas, **Lista de
Abreviaturas e Siglas**, (Lista de Símbolos), cabeçalho "CAPÍTULO n. TÍTULO", legendas "FIGURA n.m –" /
"TABELA n.m –", referências ABNT com back-references, **Folha de Registro do Documento (FRD)**.

## Plano recomendado

1. **Obter a classe oficial do ITA** (o TG do Ângelo foi gerado com ela — legendas, cabeçalhos, FRD e CIP são
   idênticos ao modelo institucional). Caminhos: pedir o `.tex`/projeto Overleaf ao Ângelo ou ao Prof. Lindolfo, ou
   procurar o template institucional do ITA para teses/TG (Overleaf/Biblioteca do ITA). **Não inventar a FRD à mão.**
2. Migrar o conteúdo do TG1 para a classe, separando em arquivos: `capitulos/01_introducao.tex`, ...,
   `referencias.bib`.
3. Montar `referencias.bib` a partir de [indice_referencias](../02_referencias/indice_referencias.md) (todas as
   entradas já estão em formato ABNT lá).
4. Estrutura-alvo dos capítulos do TG final (proposta, ~40–60 p., no padrão do Ângelo):
   1. Introdução (motivação, objetivo geral/específicos, organização do texto)
   2. Revisão da literatura (fundamentos FSW; geração de calor e temperatura; fluxo de material e defeitos de vazio;
      parâmetros de ferramenta e processo; modelos de predição de defeitos — Du et al., índices empíricos, análise
      dimensional)
   3. Metodologia (dataset e tratamento; derivação dos grupos adimensionais; forma do C_void; calibração; validação;
      sensibilidade)
   4. Resultados e discussão (calibração, acurácia vs baselines e vs Du et al., matriz de confusão, sensibilidade,
      mapas de processo ω × v, limitações)
   5. Conclusão (e trabalhos futuros)
   Referências · Apêndices (código, tabela completa do dataset corrigido) · FRD.
5. Compilar sempre no Overleaf/`latexmk`; manter figuras geradas por script em `figuras/`.
