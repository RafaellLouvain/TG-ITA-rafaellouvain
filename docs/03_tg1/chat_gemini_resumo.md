# Resumo do chat com o Gemini (desenvolvimento do TG1)

**Arquivo:** `TG1/chat-gemini-desenvolvimento-TG1.pdf` (184 p., ~450 KB de texto). Formato: perguntas do Rafael
intercaladas com respostas longas do Gemini; sem marcação de papéis (as mensagens do Rafael são curtas, informais,
geralmente após um "PDF <nome>" de anexo). Lido por blocos em 12/10/2026.

> ⚠️ **Aviso geral:** o Gemini **alucinou bastante** sobre o conteúdo dos PDFs (descrições de artigos que não batem
> com o texto real) e "inventou" resultados (ex.: "Baruah 2023 XGBoost 90 %"). **Nada do chat deve ser usado como
> fonte sem conferir no PDF original.** As notas abaixo separam fatos/decisões do Rafael (confiáveis) de afirmações do
> Gemini (a verificar).

## Linha do tempo das decisões (págs. 1–34)

1. **Ficha de proposta ao Colegiado** (antes do TG1): o Gemini sugeriu temas (fadiga 7xxx, Al-Li, modelagem EF).
   Rafael pediu foco em **processo de fabricação/elemento de máquina, sem elementos finitos**, e depois algo **geral**
   (cinemática, geometria, velocidade…). Título aprovado na ficha ≈ *"Análise da influência de parâmetros de processo
   de fabricação (cinemáticos, de geometria da ferramenta, entre outros) na integridade de juntas soldadas por FSW"* —
   é o título do TG1. **Orientador: Prof. Lindolfo (Moreira Filho)** — confirmado no chat ("ter o Prof. Lindolfo como
   orientador").
2. Rafael mostrou o TG1 do Ângelo como **modelo de formato (~10–12 páginas)**.
3. **Restrição-chave:** *"em vista de limitações do laboratório, eu não conseguirei fazer experimentos"* → trabalho
   passa a ser **analítico/estatístico com dados secundários**.
4. Gemini resumiu o TG final do Ângelo (base Filho 2018, 46–47 ensaios, regressão logística em log Q_eff) e propôs 3
   caminhos: (1) mudar modelo de calor (pino cônico/roscado), (2) trocar o algoritmo (ML: DT, SVM, RF, KNN),
   (3) buscar outra base de dados. **Rafael escolheu a linha 2 + 3** ("aproveitar a base que já temos e fazer outra
   abordagem ou achar uma nova base").
5. Gemini sugeriu 4 opções (ML vs Q_eff na base do Filho; ANN para UTS em 7xxx; RSM + algoritmo genético; validação
   de modelos de torque). Rafael avaliou vários PDFs:
   - `fsw_research1` → Gemini disse que usava dataset no **Mendeley Data** (`data.mendeley.com/datasets/v5bdfz6m86/2`,
     "AA6061-T6") — **falso**: conferido em 2026-10-12, o PDF (Matitopanum et al. 2023, ML para UTS/dureza em AA7075,
     está em `Downloads/` do Windows) não menciona Mendeley em nenhum lugar.
   - `computation-11-00100` (MDPI *Computation* 11:100, 2023) → CNN em **imagens** de cordão FSW dissimilar
     AA5083/AA6061, classes por eficiência de UTS (<70 %, 70–85 %, >85 %); imagens no Kaggle. Não está no repositório.
   - `Adiga_2024` → ⚠️ **o Gemini descreveu errado**: disse AA7075-T651, ANN + algoritmo genético, 17 ensaios
     Box-Behnken (n, v, θ → UTS, HV). **Real:** FSP de AA8090/SiC, 20 ensaios CCD (ω, v, largura do sulco → UTS),
     LR/SVR/ANN/XGBoost. Ver [adiga_2024_e_outros](../02_referencias/adiga_2024_e_outros.md).
6. **Virada: dataset do Kaggle** (`arindambaruah/void-formation-process-data-in-welding`). Rafael: "vamos pra outra
   fonte… esqueça essas outras". Gemini então propôs um **benchmark multi-algoritmo de ML** (SVM, RF, XGBoost, LR
   regularizada, KNN, AdaBoost), split **78 treino / 30 teste** + K-fold, Optuna etc. e um título "Predição de
   descontinuidades volumétricas ... via Machine Learning".
   - ⚠️ O Gemini afirmou que "o autor (Baruah, 2023) desenvolveu XGBoost com GridSearchCV e atingiu **90 %**, superando
     NN e DT (83,3 %)". **Não verificado** — o Kaggle é só um upload do dataset de Du et al. (2019); os 83,3 % são de
     Du et al. (NN com parâmetros brutos). Se for citar algum notebook do Kaggle, conferir antes.
   - ⚠️ Primeiro o Gemini também "descreveu" o dataset com torque/força medidos por sensores — **falso** (o CSV só tem
     os 11 parâmetros + alvo).
7. Rafael colou o cabeçalho do CSV; Gemini mapeou colunas X (2–12) e y (13). (Correto, mas não percebeu o
   desalinhamento da coluna `Alloy` nem os `*` — ver [dataset](../01_dados/dataset.md).)
8. Rafael perguntou se dá para usar a base do **Filho (2018)** junto → Gemini sugeriu **validação cruzada entre
   datasets**: treinar no Kaggle (108) e testar nos 46 do ITA, mapeando "túnel no keyhole" ↔ void, AA2024,
   t = 3,2 mm, R_s = 7,935 mm, R_pr = R_pt = 3,2 mm (pino cilíndrico), tilt 2–3°, α/σ_y do 2024.
   ⚠️ Problemas: na base do Filho **não há pressão axial em MPa** (F = 774 N no script do Ângelo → p ≈ F/(πR_s²)
   ≈ 3,9 MPa, fora da faixa do Kaggle 7,9–26,5), túnel em 83 % dos casos e todas as soldas "quentes"; mistura de
   critérios de defeito (túnel no keyhole ≠ vazio na seção transversal). Ideia interessante, mas arriscada.
9. Rafael questionou se não deveria haver uma fundamentação física (a partir do resumo do Mishra & Ma) → Gemini disse
   que "nenhum modelo analítico conseguirá uma equação fechada com as 11 variáveis" e que o ML seria o motor, com a
   física explicando os resultados. Introduziu **"cold void" (falta de calor) vs "hot void" (excesso de calor → flash →
   falta de material)** — **daqui vem a dicotomia usada no TG1**, atribuída indevidamente a Mishra & Ma.
   Sugeriu buscas no CAPES: fluxo de material/geometria, janelas por **weld pitch v/n**, ML para defeitos.
10. Rafael perguntou sobre cada PDF de referência; o Gemini "justificou" cada coluna do dataset com um artigo:
    - Laska 2023 → pin root/tip, "queda de pressão hidrostática atrás do pino gera vazio" ⚠️ (não está no artigo).
    - Aldanondo 2020 → "monitoraram a força descendente em tempo real e mostraram como reage aos defeitos" ⚠️ (falso:
      controle de carga, mediram forças X/Y e torque, sem vazios). Sugeriu usar como **delimitação de escopo**
      (junta sobreposta / Al-Li fora do escopo) — isso sim é um uso honesto.
    - Ahmed 2021 → BT-FSW como variante; "pino cilíndrico liso, roscado e triangular" ⚠️ (real: cilíndrico, quadrado,
      triangular). Também sugerido para **delimitação de escopo** (BT-FSW fora).
    - Ahmed/Kadhum/Salleh 2024 → defesa de pin root/tip; "pulsação vertical" ⚠️ exagerado.
    - "Arsenal" final: Mishra & Ma (física/calor), Laska + Ahmed 2024 (pino), Aldanondo (forças), Ahmed 2021 (BT-FSW/
      calor), Baruah 2023 (ML) — **Baruah não é um artigo**, é o uploader do Kaggle.

## Págs. 35–60: nasce o C_void e o relatório do TG1

11. Gemini apontou "lacunas" (tilt e diferença entre ligas) → Rafael trouxe **Meyghani & Awang 2022** (tilt) e depois
    achou **Du, Mukherjee & DebRoy 2019** ("achei um benchmark interessante"). Gemini confirmou que Du et al. é a
    **fonte original do dataset** e que a coluna `Refs` = nº da referência no artigo (✔ verdadeiro).
    Gemini disse que o artigo "explica que AA2024/AA2219 são mais duras e difíceis de escoar que AA6061" ⚠️ (Du et al.
    não discute isso; apenas normaliza por liga para remover efeito de composição).
12. **Decisão central do Rafael (pág. 43):** o ponto central é a pesquisa de Du et al. e o dataset; a ideia é criar
    uma **equação/coeficiente analítico-fenomenológico** ("física + calibração estatística") em vez de ML caixa-preta.
    Gemini chamou de "Modelo Analítico-Fenomenológico Híbrido" e propôs o primeiro esboço:
    **C_void = β₁·(termo de energia) + β₂·(R_pt/R_pr) + β₃·cos θ − β₄·(p/σ_y)**, calibração por mínimos quadrados não
    lineares ou algoritmo genético nos 78 de treino, teste nos 30, limiar ex. C_void > 0,5, comparação com 83,3 %;
    **análise de sensibilidade OAAT / diagrama de tornado** (variar uma variável por vez a partir da média);
    verificação externa com a base do Filho (2018).
13. Planejamento do TG1 com estratégia **"underpromise, overdeliver"** (prometer pouco no TG1, entregar no TG2).
    Limite ~10 páginas. Feedbacks do Rafael incorporados: **reduzir o protagonismo de Machine Learning**, fundir
    parágrafos de justificativa, simplificar objetivos, conectar dataset diretamente às equações.
14. Versão do Gemini para a metodologia (pág. 57–59) — **3 blocos**:
    - Π_Term ∝ ω·R_s³/(v·t·α) (Ahmed 2021) — usado **invertido** no C_void (menos calor → mais risco);
    - Π_Geom ∝ R_pt/R_pr (Ahmed 2024);
    - Π_Comp ∝ (p/σ_y)·cos θ (Aldanondo + Meyghani);
    - **C_void = β₁·(Π_Term)⁻¹ + β₂·Π_Geom − β₃·Π_Comp**; pipeline: converter unidades, split 78/30 fixo, mínimos
      quadrados não lineares para β e limiar, matriz de confusão e ROC no teste, comparar com Du et al.
    (O relatório final do TG1 acabou usando **4 blocos** Π_Geom, Π_Cin, Π_Term, Π_Din — ver
    [relatorio_tg1](relatorio_tg1.md).)
15. Gemini gerou o texto completo do relatório (título provisório *"Formulação de um coeficiente analítico
    fenomenológico para predição de vazios no processo FSW"* — o título final manteve o da ficha). Na folha de rosto
    escreveu **"Prof. Dr. Lindolfo Araújo Moreira Filho"** ⚠️ (nome do meio não verificado; o TG do Ângelo traz
    "Prof. Dr. Lindolfo Moreira Filho"). Cronograma TG2 Jul–Dez (o final do TG1 ficou Set–Dez).
    Afirmações do texto gerado que **não têm fonte** nos PDFs: "T de pico 70–90 % de T_fusão" (Mishra & Ma diz
    0,6–0,9 T_m), "Falcon 9", "dias de processamento", "Aldanondo demonstra pressão crítica superior ao limite de
    escoamento", "parâmetros seguros para 6061 geram vazios na 2024".
16. Rafael pediu um "contexto mestre" completo para colar no **NotebookLM** (pág. 60+).

## Págs. 60–184: NotebookLM, título, objetivo de 70 %, slides e versão final do relatório

17. **Contexto mestre para o NotebookLM** (pág. 61–65): resumo do projeto com os 3 blocos
    (Π_Term = ωR_s³/(v t α), Π_Geom = R_pt/R_pr, Π_Comp = (p/σ_y)·cos θ) e
    C_void = β₁(Π_Term)⁻¹ + β₂Π_Geom − β₃Π_Comp; mapeamento "1 artigo ↔ 1 coluna do dataset" (com as alucinações já
    citadas). Sugestão de criar caderno "TG1 - Rafael Louvain" com os 7 PDFs + fonte "0_DIRETRIZ_MESTRA_CONTEXTO".
18. Gemini enquadrou o texto no **template LaTeX** que o Rafael forneceu (o mesmo `report` + TikZ do arquivo `.tex`
    atual).
19. **Título:** discutidas várias opções ("Modelo analítico fundamentado na física do processo...", "Modelagem
    analítica dos fatores de processo e desenvolvimento de índice teórico para predição de vazios em FSW" — usada na
    capa dos slides em rascunho). **O título final do relatório e da apresentação manteve o da ficha aprovada.**
20. **Objetivo específico:** Gemini sugeriu só "avaliar acurácia + matriz de confusão" (underpromise). **Rafael
    decidiu:** "Yang Du alcançaram 83,33 % com a rede neural. Façamos o objetivo específico ser **alcançar 70 % de
    acurácia**". Resumo reescrito com essa meta.
21. **Montagem da apresentação** (págs. 74–166), referência por referência, em Markdown "de alta densidade":
    - Mishra & Ma → janela 0,6–0,9 T_m; "0,7–0,8 T_m na borda de ataque" e faixas de T por zona (nugget 0,7–0,9 T_m,
      TMAZ 0,5–0,7, HAZ 0,3–0,5 T_m; grão 100 µm → 1–5 µm) ⚠️ **valores inventados pelo Gemini**, não estão no PDF;
      cold vs hot voids; auto-regulação; câmara de extrusão; "processo verde, até 60–80 % menos energia" ⚠️ (Mishra &
      Ma dizem "2,5 % da energia de um laser"); a pedido do Rafael, slide com a **equação de Q_total (pág. 18 do PDF)**.
    - Laska → 2 slides (equação de calor do pino + Navier-Stokes/custo do CFD, malha 0,05 mm). Rafael: "não muita
      coisa será aproveitada dessa referência".
    - Aldanondo → ⚠️ "estuda AA2024-T3, controle de posição vs força axial, força baixa → vazio de raiz, efeito de
      escala do pino" — **tudo inventado** (ver [aldanondo_2020](../02_referencias/aldanondo_2020.md)).
    - Ahmed 2021 → ⚠️ "pinos cilíndricos excêntricos, came, pulsação" — **inventado** (o artigo é bobbin tool com pinos
      cilíndrico/quadrado/triangular); sliding/sticking ✔. Rafael pediu para virar 1 slide.
    - "Walla, Ahmed & Shukur (2023)" → razão volume dinâmico/estático e pulsação ✔ (mas é 2024 e o nome é Walaa).
    - Meyghani → ⚠️ "modelo CEL", "θ = 0 → rebarba gigante → túnel", "janela 1,5–3°", "> 4° superaquecimento"
      (não está no artigo).
    - Du et al. → ⚠️ "Nature (Scientific Reports)", "11 colunas incluindo **L_p, F_z, k**", "CFD + RNA = 83,33 %"
      (**errado**: 83,3 % é RNA com parâmetros brutos; colunas reais têm p (MPa) e α, sem L_p).
    - Seção de Metodologia: tabelas de "sensibilidade paramétrica" (comportamento abaixo/acima do ótimo de cada
      variável) — **qualitativas, criadas pelo Gemini** (ex.: "α baixo → retenção → vazio quente") sem fonte.
    - **"Resultados preliminares":** forma multiplicativa **C_void = (Π_Geom·Π_Cin)/(Π_Term·Π_Comp)**.
    - Identidade visual dos slides: azul ITA #0056B3, amarelo #FFCC00, fundo #F9F9FB, texto #1A1A1A (gerou macro VBA
      para PowerPoint).
22. Pergunta de checagem do Rafael: "o ombro responde por 80–90 % do calor está no Mishra?" → Gemini disse "verdadeiro
    com ressalva", atribuindo a Frigaard 2001 / Schmidt 2004 e **citando trechos entre aspas que não existem no PDF**
    ⚠️. (Fonte real com números: Ahmed 2021, 78–88 % em bobbin tool.)
23. Explicações conceituais pedidas pelo Rafael (para a defesa): AS vs RS, "massa viscoplástica", termos de
    Navier-Stokes. Checagem de que todas as colunas do dataset aparecem nos slides (incluiu `Alloy` + σ_y no slide 28).
24. **Apresentação final** (35 slides, ver [apresentacao_tg1](apresentacao_tg1.md)) → Rafael pediu para adaptar o
    relatório a ela. Primeira versão ficou com **18 páginas** (forma multiplicativa, 3 tabelas de sensibilidade) →
    Rafael pediu cortes ("na introdução deixe apenas o 2º e 4º parágrafos"...) → versão final: introdução com 2
    parágrafos, revisão condensada, **C_void aditivo com 4 blocos e β₁..β₄** (equação 3.1), tabela única de variáveis,
    cronograma **Set–Dez** com 6 linhas, figura do Du et al. (print "Captura de tela 2026-06-07 204639.png" → TG1
    finalizado por volta de **junho/2026**).

## Lições para o TG final (do chat como um todo)

- O núcleo da ideia (equação explícita adimensional calibrada no dataset de Du et al., meta ≥ 70 %, hierarquia de
  sensibilidade, foco em chão de fábrica, sem ML caixa-preta) **é do Rafael e está bem definido**.
- A forma do C_void **nunca foi fixada**: três versões coexistiram (aditiva 3 blocos com inverso; multiplicativa 4
  blocos; aditiva 4 blocos com β). Os Π **nunca foram definidos com variáveis reais** na versão final (só nomes).
- A revisão bibliográfica do TG1 herdou várias **afirmações falsas** do Gemini → ver
  [erros_e_correcoes_tg1](erros_e_correcoes_tg1.md). Toda citação no TG final deve ser checada contra o PDF.
- O Rafael tinha a preferência explícita por **reduzir o protagonismo de ML** e por textos **enxutos**.
