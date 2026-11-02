# Códigos do TG2 — modelos A, B e C do C_void

Implementam o protocolo de `docs/05_modelagem/protocolo_metodologia.md` e o plano de
`docs/05_modelagem/plano_capitulos_metodologia_resultados.md`. Saídas em `../resultados/` (tabelas CSV, figuras
PNG/PDF e resultados brutos por split em `brutos/`).

Requisitos: Python ≥ 3.11 com numpy, pandas, scipy, scikit-learn e matplotlib.

## Ordem de execução

```bash
cd TG2/codigos
python3 r01_caracterizacao.py                  # seção 4.1 (tabelas por estudo/liga, figura rotação × estudo)
python3 r02_validacao.py                       # todos os modelos: split oficial, 500 splits, LOSO (~10 min)
python3 r02_validacao.py --sem-p-theta         # robustez 1 (sem os termos com p e θ assumidos)
python3 r02_validacao.py --sem-duvidosas       # robustez 2 (sem as linhas 84–89)
python3 r03_sensibilidade_B.py                 # seção 4.2: expoentes, bootstrap, naturezas, tornado, retirada
python3 r04_modelo_A.py                        # seção 4.3: limiar crítico de ωR_s e sua robustez
python3 r05_modelo_C.py                        # seção 4.4: seleção dos termos, equação final, tornado
python3 r06_comparacao.py                      # seções 4.5–4.6: comparação, acc × bal, robustez dos dados
python3 r07_erros.py                           # seção 4.7: erros por solda e por estudo
python3 r08_checagens.py                       # diagnóstico: sobreajuste do B (L2) e modelo dimensional livre
python3 r09_dentro_do_estudo.py                # efeito de ω e v só dentro dos estudos (AUC intra, expoente de v)
```

## Módulos

| Arquivo | Conteúdo |
|---|---|
| `dados.py` | leitura do CSV, SI, coluna Alloy descartada, marcadores de `*`, estudos, grupos adimensionais (matriz dimensional) |
| `nucleo.py` | regressão logística em ln Π (= lei de potência), escolha do limiar (acc/bal), métricas, modelos `Indice` (A), `LeiPotencia` (B), `SelecaoConjunto` (B final), `Hibrido` (C) |
| `modelos.py` | catálogo: conjuntos B1–B3, candidatos do C, referências |
| `validacao.py` | split oficial (semente 2026, fixada antes de rodar), 500 splits 78/30 estratificados, LOSO |
| `estilo.py` | estilo das figuras |
