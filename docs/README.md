# Documentação do TG — índice

Base de conhecimento do Trabalho de Graduação do Rafael Louvain (ITA, Eng. Mecânica-Aeronáutica, 2026):
**equação adimensional (C_void) para prever vazios em juntas FSW**, calibrada no dataset de Du et al. (2019).
Criada em 2026-10-12 a partir da leitura integral de todos os arquivos do repositório.

**Comece por:** [00_projeto/visao_geral.md](00_projeto/visao_geral.md) → depois
[decisoes_e_pendencias.md](00_projeto/decisoes_e_pendencias.md).

## Mapa

```
docs/
├── README.md                         ← este índice
├── 00_projeto/
│   ├── visao_geral.md                ← contexto, objetivo, estado atual, achados-chave
│   ├── decisoes_e_pendencias.md      ← o que já foi decidido / próximos passos (MANTER ATUALIZADO)
│   └── glossario_fsw.md              ← termos de FSW, defeitos, microestrutura e notação do TG
├── 01_dados/
│   └── dataset.md                    ← CSV: colunas, unidades, armadilhas, Alloy errada, refs→estudos, baselines
├── 02_referencias/
│   ├── indice_referencias.md         ← arquivo ↔ ABNT ↔ status + referências a buscar
│   ├── du_2019_benchmark.md          ← artigo-base (dataset + 83,3/90/93,3/96,6 %)
│   ├── mishra_ma_2005.md             ← revisão clássica; T/T_m vs ω²/v; eq. de Schmidt
│   ├── laska_2023.md                 ← CFD AA6082, pino simples × complexo
│   ├── aldanondo_2020.md             ← lap joint Al-Li (≠ do que o TG1 diz)
│   ├── meyghani_awang_2022.md        ← tilt 0° × 1,5°
│   ├── ahmed_2021_bobbin.md          ← modelos de calor por geometria de pino
│   ├── walla_ahmed_2024_review.md    ← revisão de perfis de pino
│   └── adiga_2024_e_outros.md        ← ML com poucos dados; .bib Derazkola
├── 03_tg1/
│   ├── relatorio_tg1.md              ← o que foi entregue (C_void aditivo 4 blocos, meta 70 %, cronograma)
│   ├── apresentacao_tg1.md           ← 35 slides resumidos
│   ├── chat_gemini_resumo.md         ← histórico das decisões + alucinações do Gemini
│   └── erros_e_correcoes_tg1.md      ← checklist do que corrigir no TG final
├── 04_formato_ita/
│   ├── tg_veterano_angelo.md         ← estrutura/padrão do TG final aprovado (mesmo orientador)
│   └── template_latex.md             ← .tex atual × classe ITA; plano de migração
└── 05_modelagem/
    ├── proposta_modelagem.md         ← análise dimensional, forma do C_void, testes de viabilidade, protocolo
    └── analises_exploratorias_2026-10-12.md ← verificação dos dados + índices testados (ω·R_s etc.)

analises_exploratorias/ (na raiz do repo) ← código Python dos testes exploratórios + resultados/ (CSV, PNG)
```

## Regras de uso desta documentação

1. **Fonte da verdade = PDFs originais.** O chat do Gemini contém muitas alucinações; nunca citar algo só porque
   aparece no TG1 ou no chat — conferir no resumo da referência (`02_referencias/`) ou no PDF.
2. Ao decidir algo com o Rafael, registrar em `00_projeto/decisoes_e_pendencias.md` (com data).
3. Resultados numéricos novos (calibração, acurácias) → `05_modelagem/` com data e o script que os gerou.
4. Idioma: português (o TG é em português); termos técnicos em inglês em itálico no texto final.
