# Dataset — `dados/Welding_process_parameters.csv`

**Origem:** Kaggle — <https://www.kaggle.com/datasets/arindambaruah/void-formation-process-data-in-welding>
(arquivo `dados/link_do_dataset_e_projeto_no_kaggle.txt`). É a transcrição da Tabela 1 do *Supplementary Information*
de **Du, Mukherjee & DebRoy (2019)**, *npj Computational Materials* 5:68 (ver [du_2019_benchmark](../02_referencias/du_2019_benchmark.md)).

108 linhas (soldas de topo/butt, 3 ligas de Al), alvo binário: **43 com vazio (1) / 65 sem vazio (0)** → classe
majoritária = 60,2 % (essa é a acurácia de um "chute constante" = baseline trivial; a meta de 70 % precisa ser lida
contra isso, **não** contra 50 %).

## Formato bruto (armadilhas de leitura)

- Arquivo tem **BOM UTF-8** (`encoding='utf-8-sig'`).
- Linha 1 = cabeçalho; **linha 2 = unidades** (pular: `skiprows=[1]`).
- Cabeçalho `Alloy,,Welding speed,...` → a **1ª coluna é o índice (1..108)** e a **2ª é a liga**; o rótulo "Alloy" está
  deslocado.
- Colunas `Axial pressure` e `Tilt angle` têm valores com `*` (ex.: `13.00 *`, `2*`) = **valor estimado/assumido pelos
  autores** (não reportado no artigo de origem). Precisam ser limpos para float e o `*` vira uma flag.

Código de leitura testado (pandas):

```python
df = pd.read_csv('dados/Welding_process_parameters.csv', skiprows=[1], encoding='utf-8-sig')
df.columns = ['id','alloy','v','w','t','Rs','p','Rpr','Rpt','tilt','alpha','sy','void','ref']
for c in ['p','tilt']:
    df[c+'_assumed'] = df[c].astype(str).str.contains(r'\*')
    df[c] = df[c].astype(str).str.replace('*','').str.strip().astype(float)
```

## Colunas

| col | nome original | unidade | símbolo | faixa (min–max) | obs |
|---|---|---|---|---|---|
| id | (sem nome) | – | – | 1–108 | índice |
| alloy | Alloy | – | – | 2024/2219/6061 | **ROTULAGEM ERRADA em 33 linhas — ver abaixo** |
| v | Welding speed | m/s | v | 2,5e-4 – 1,78e-2 (15–1068 mm/min) | ref 15 tem v muito alto (≥ 8,5e-3 m/s) |
| w | Rotation speed | **rps** (rot/s, não rad/s!) | ω / N | 2,5 – 41,67 (150–2500 rpm) | ω em rad/s = 2π·w |
| t | Plate thickness | m | t | 2,1 – 17,5 mm | |
| Rs | Shoulder radius | m | R_s | 5 – 14 mm | |
| p | Axial pressure | **MPa** | p | 7,86 – 26,5 | **72/108 estimados (`*`)**, quase sempre 13 ou 8 |
| Rpr | Pin root radius | m | R_pr | 1,5 – 5,5 mm | |
| Rpt | Pin tip radius | m | R_pt | 0,9 – 4,2 mm | |
| tilt | Tilt angle | grau | θ | **só 2 ou 2,5** | **71/108 estimados (`*`)** → quase sem informação |
| alpha | Thermal diffusivity | m²/s | α | 4,89e-5 / 4,97e-5 / 6,90e-5 | 1 valor por liga |
| sy | Yield strength | MPa | σ_y | 276 / 324 / 352 | 1 valor por liga |
| void | Void-1 void free-0 | – | – | 0/1 | alvo |
| ref | Refs | – | – | 6–18 | nº da referência no artigo de Du et al. |

Observações:
- O dataset **não contém** comprimento do pino (L_p), força axial em N, condutividade k, T_solidus, ρ, c_p, nem tipo de
  pino (rosca/cônico/etc.). O TG1 (slide 26) lista "L_p", "F_z" e "k" — isso está **errado** em relação ao CSV real:
  temos **pressão p (MPa)** e **difusividade α**. Para usar L_p pode-se aproximar L_p ≈ t (penetração total), hipótese a
  declarar.
- α e σ_y são **constantes por liga** → equivalem a uma variável categórica de 3 níveis; não há variação intra-liga.
  Qualquer termo "térmico/material" do modelo só consegue separar ligas entre si.
- Não há duplicatas nas features.

## ACHADO CRÍTICO: coluna `Alloy` está desalinhada

α e σ_y são **perfeitamente consistentes** com a referência de origem (coluna `Refs`) e com propriedades reais:
- α = 4,97e-5 m²/s, σ_y = 324 MPa → **AA2024** (k≈121 W/mK → α≈5,0e-5 ✔)
- α = 4,89e-5 m²/s, σ_y = 352 MPa → **AA2219** (k≈120 W/mK ✔)
- α = 6,90e-5 m²/s, σ_y = 276 MPa → **AA6061-T6** (k≈167, σ_y=276 ✔)

Mas a coluna `Alloy` do Kaggle diz 20×2024, 35×2219, 53×6061 e diverge das propriedades nas linhas
**21–38 e 56–70 (33 linhas)**. Cruzando com as referências do artigo (ref 6–9 são estudos em AA2024, 10–13 em AA2219,
14–19 em AA6061), a rotulagem correta é a **inferida pelas propriedades**:

| liga real (por α, σ_y) | linhas | n | vazios (1) | % vazio |
|---|---|---|---|---|
| AA2024 | 1–38 | 38 | 20 | 53 % |
| AA2219 | 39–70 | 32 | 11 | 34 % |
| AA6061 | 71–108 | 38 | 12 | 32 % |

➡ **Decisão recomendada:** usar `alloy_by_props` (mapear por α) e documentar a correção no TG como etapa de
tratamento de dados (é um ponto metodológico positivo: mostra auditoria do dataset).

## Mapa referência → bloco de ensaios

(nº da ref = numeração do artigo de Du et al. 2019)

| ref | estudo de origem (Du et al.) | linhas | n | vazios | liga (props) | t (mm) | R_s | R_pr/R_pt (mm) | p (MPa) | θ |
|---|---|---|---|---|---|---|---|---|---|---|
| 6 | Carlone & Palazzo 2013 (AA2024-T3) | 1–15 | 15 | 9 | 2024 | 4 | 10 | 3,1/0,9 | 13* | 2 |
| 7 | Anil Kumar et al. 2018 (AA2024) | 16–22 | 7 | 3 | 2024 | 6 | 9 | 3/3 | 7,86 | 2* |
| 7 (?) | idem — **mas com props de 6061** | 84–89 | 6 | 3 | 6061 | 6 | 9 | 3/3 | 7,86 | 2* |
| 8 | Nejad et al. 2017 (AA2024) | 23–25 | 3 | 1 | 2024 | 3 | 10 | 3,1/0,9 | 8* | 2 |
| 9 | Mahmudi & Farhangi 2010 (AA2024-T4) | 26–38 | 13 | 7 | 2024 | 4 | 9 | 3/3 | 13* | 2* |
| 10 | Lakshminarayanan et al. 2011 (AA2219) | 39–44 | 6 | 3 | 2219 | 6,35 | 7,5 | 3/3 | 13* | 2* |
| 11 | Lee et al. (AA2219) | 45–59 | 15 | 3 | 2219 | 8 | 12 | 3,7/2,7 | 26,5 | 2* |
| 12 | Li, Shen & Hu 2011 (AA2219-T6, chapa grossa) | 60–64 | 5 | 3 | 2219 | 17,5 | 14 | 5/3,5 | 13* | 2,5 |
| 13 | Liu et al. 2012 (AA2219-T6) | 65–70 | 6 | 2 | 2219 | 7,5 | 11,25 | 5/2,5 | 13* | 2,5 |
| 14 | Lim et al. 2004 (AA6061-T651) | 71–83 | 13 | 2 | 6061 | 4 | 6,5 | 2/1,3 | 13* | 2* |
| 15 | Balasubramanian 2008 | 90–95 | 6 | 2 | 6061 | 12,7 | 10,8 | 5,5/4,2 | 13* | 2* |
| 16 | Fraser et al. 2018 | 96–103 | 8 | 2 | 6061 | 2,1 | 9 | 3/2 | 23,59 | 2,5 |
| 17 | Ramulu et al. 2013 (Al 6061) | 104–105 | 2 | 1 | 6061 | 6,3 | 13 | 2,95/2,95 | 13* | 2* |
| 18 | Feng et al. 2017 (6061) | 106–108 | 3 | 2 | 6061 | 3 | 5 | 1,5/1,5 | 8* | 2* |

(Refs 4, 5 e 19 do artigo não aparecem na coluna; o bloco 84–89 marcado "ref 7" tem props de 6061 — provavelmente é
outro estudo, possivelmente a ref 19 Kumaravel et al. (Al-6061), ou erro de transcrição. Tratar como 6061.)

## Implicações para a modelagem (importante!)

1. **Dentro de cada referência a geometria é fixa** — só v e ω variam. Logo, quase toda a informação "intra-estudo" é
   sobre (v, ω); a informação de geometria/material vem **entre estudos** (13 grupos). Risco de o modelo aprender
   "qual laboratório" em vez de física → considerar validação **por grupo (leave-one-study-out / GroupKFold)** além do
   split aleatório 78/30 previsto no TG1, ao menos como análise de robustez.
2. **Tendência intra-estudo (verificada em 12/10/2026, varrendo todos os blocos):** com a geometria fixa, o vazio
   ocorre de forma quase monotônica para **ω baixo** e, de forma secundária, para **v alto**. Ex.: ref 6 (AA2024,
   v = 35–140 mm/min): ω ≤ 1200 rpm → vazio, ω ≥ 1400 rpm → são, independentemente de v; ref 9: ω = 700 rpm → sempre
   vazio, ω = 900 rpm → são até 160 mm/min e vazio a 200–250 mm/min; ref 13: vazio só a 300–400 mm/min. Logo, o
   mecanismo dominante no dataset é o **vazio "frio" (aporte térmico/fluxo insuficiente)**, em linha com Du et al.
   ("o vazio desaparece com T alta e τ_max, torque e taxa de deformação baixos"). Não há casos claros de vazio
   "quente" (excesso de calor) — só a anomalia da ref 7 (45 mm/min @ 1200 rpm → vazio, enquanto 75–100 mm/min @ 1200 →
   são), que pode ser excesso de calor ou ruído.
   - Candidatos naturais ao Π cinemático: **ω/v** (rotações por metro, inverso do "weld pitch") e **ω²/v**
     (pseudo heat index de Arbegast), ponderados por geometria (R_s, t) e material (α, σ_y).
   - Ref 15 (Balasubramanian 2008) tem v = 508–1068 mm/min para chapa de 12,7 mm — valores atípicos; suspeita de
     erro de unidade na transcrição (verificar no artigo original se possível).

### Baselines triviais (acurácia em TODA a amostra, limiar ótimo — otimista, apenas referência)

| preditor (1 variável, 1 limiar) | acurácia | regra |
|---|---|---|
| classe majoritária ("nunca vazio") | 60,2 % | – |
| v | 61,1 % | – |
| ω/v | 65,7 % | vazio se < ~3994 rev/m |
| ω·R_s/v | 65,7 % | |
| ω²/v | 69,4 % | |
| **ω (rps) sozinho** | **70,4 %** | vazio se ω < 18,33 rps (1100 rpm) |

➡ **A meta de 70 % do TG1 é atingida (in-sample) só com a rotação.** Porém, **fora da amostra** o quadro muda:
modelos lineares simples ficam em ~62–73 % na validação cruzada e ~60 % deixando um estudo inteiro de fora (ver
[proposta_modelagem](../05_modelagem/proposta_modelagem.md) §4). Reportar sempre a comparação com: classe majoritária,
melhor variável única, regressão logística simples e Du et al. (83,3 % com NN em parâmetros brutos, num único split de
30).
3. p e θ são majoritariamente imputados (p ∈ {7,86; 8; 13; 23,59; 26,5}; θ ∈ {2; 2,5}) → pouco poder discriminante
   real; incluí-los é mais "fenomenológico" do que estatístico. Isso deve ser dito no TG (limitação).
4. Desbalanceamento leve (40/60). Reportar acurácia **e** matriz de confusão / sensibilidade (recall de vazios),
   precisão, F1, e comparar com baseline de classe majoritária (60,2 %).
5. Split do Du et al.: 63 treino (25 vazios) / 15 validação (6 vazios) / 30 teste (≈12 vazios), estratificado. O TG1
   propõe 78 treino / 30 teste (= 63+15 / 30), compatível.
