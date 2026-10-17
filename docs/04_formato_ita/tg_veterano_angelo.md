# TG do veterano — Ângelo Chaves Souza Bezerra (ITA, 2025)

**Arquivos:** `referencias/TG1_E_TG_FINAL_DE_ALUNO_DE_OUTRO_ANO_PARA_REFERENCIA/`
- `TG_1_FSW (1).pdf` — TG1 (14 p.), título "Modelagem termomecânica do processo FSW", 9/jun/2025.
- `TG_Angelo_Bezerra_vEnvio (Updt)_2.pdf` — TG final (59 p.), título **"Análise da energia efetiva por comprimento e
  ocorrência de defeitos no processo FSW (Friction Stir Welding)"**, aprovado 12/nov/2025, registro
  **DCTA/ITA/TC-065/2025**, CDU 621.791, 56 folhas.

**Orientador: Prof. Dr. Lindolfo Moreira Filho (ITA)** — mesmo orientador do Rafael (a confirmar com o usuário).
No TG1 dele aparece "Coordenador do Curso de Engenharia Mecânica: Prof. Dr. Leandro Rodrigues Cunha" (o TG final,
de Mecânica-Aeronáutica, não traz coordenador na folha de aprovação).

## Estrutura do TG final (modelo a seguir)

Pré-textuais (ordem exata):
1. **Capa** — "INSTITUTO TECNOLÓGICO DE AERONÁUTICA", nome, TÍTULO EM CAIXA ALTA, "Trabalho de Graduação", ano,
   "Curso de Engenharia Mecânica-Aeronáutica".
2. **Folha de rosto** — CDU, nome, título, "Orientador / Prof. ... (ITA)", "ENGENHARIA MECÂNICA-AERONÁUTICA",
   "São José dos Campos / instituto tecnológico de aeronáutica / ano".
3. **Ficha catalográfica (CIP)** — "Dados Internacionais de Catalogação-na-Publicação (CIP) / Divisão de Informação e
   Documentação"; sobrenome, nome; título; local, ano; nº de folhas ("56f."); "Trabalho de Graduação – Curso de
   Engenharia Mecânica-Aeronáutica– Instituto Tecnológico de Aeronáutica, 2025. Orientador: Prof. ..."; palavras-chave
   numeradas; "I. Instituto Tecnológico de Aeronáutica. II. Título."; **REFERÊNCIA BIBLIOGRÁFICA** (como citar o TG);
   **CESSÃO DE DIREITOS** (nome, título, tipo/ano, texto padrão de permissão, endereço do autor).
4. **Folha de aprovação** — "Essa publicação foi aceita como Relatório Final de Trabalho de Graduação"; autor;
   orientador; local e data.
5. Dedicatória · 6. Agradecimentos · 7. Epígrafe · 8. **Resumo** · 9. **Abstract** · 10. **Lista de Figuras** ·
   11. Lista de Abreviaturas e Siglas · 12. **Sumário**.

Textuais:
1. Introdução e contextualização (1.1 Motivação, 1.2 Objetivo)
2. Revisão da literatura (2.1 Fundamentos — utilidade em Al, ferramentas, princípio físico/assimetria, geração de
   calor, janela de processo, defeitos; 2.2 Energia por comprimento; 2.3 Aplicações industriais)
3. Metodologia (3.1 Base experimental; 3.2 Modelo analítico; 3.3 Modelo computacional; 3.4 Código Matlab)
4. Resultados e Discussões
5. Conclusão

Pós-textuais: **Referências** (ABNT, com páginas de citação ao final de cada entrada — "back-references" do pacote
hyperref/abnTeX/ITA class), **Folha de Registro do Documento** (FRD: classificação TC, data, registro nº, nº de
páginas, título, autor, instituição, palavras-chave do autor e de indexação, apresentação Nacional/Internacional,
resumo, grau de sigilo OSTENSIVO).

## Padrões de formatação observados

- Gerado claramente com a **classe LaTeX do ITA (ITA-LaTeX / `abntex2`-like)**: legendas "FIGURA 2.1 –", "TABELA 3.1 –"
  em caixa alta; cabeçalho "CAPÍTULO 2. REVISÃO DA LITERATURA" + nº da página; numeração de pré-textuais em romano.
- **Citações no texto em formato autor-data com parênteses**: "(Mishra e Ma 2005)", "(Threadgill et al. 2009)",
  "(Colegrove e Shercliff 2005)", "(Filho 2018)". (Sem vírgula entre autor e ano — estilo da classe ITA.)
- Referências ABNT: SOBRENOME, Iniciais.; ... Título. **Periódico**, v., n., p., ano. Lista em ordem alfabética.
- Equações numeradas por capítulo "(3.7)". Listings de código numerados ("Listing 3.1 – Script em matlab").
- Nota de rodapé usada para esclarecer nomenclatura.
- Tabela de nomenclatura (símbolo / unidade / descrição) no início da metodologia — **boa prática para copiar**.

⚠️ O `TG1_relatorio_formato_latex.tex` do Rafael **não usa a classe do ITA**: é `report` + `titlesec` + capa em TikZ e
referências digitadas à mão (sem BibTeX). Para o TG final, **recomenda-se migrar para a classe oficial do ITA
(abnTeX2/ITA) com BibTeX** para obter automaticamente ficha CIP, folha de aprovação, FRD, listas e citações autor-data.
Ver [template_latex](template_latex.md).

## Conteúdo técnico (relevante para nós)

- Base experimental: dissertação de mestrado do próprio orientador — **FILHO, J. A. P. C. (2018)** *Análise de
  integridade estrutural de uma junta tipo topo soldada em liga de alumínio Alclad AA2024-T3 por FSW na indústria
  aeroespacial*, ITA (172 p.). 47 soldas (CPs A–J), chapas 3,2 mm, ferramenta: pino Ø6,4 × 2,9 mm, ombro Ø15,87 mm;
  n = 520–980 rpm, f = 18–50 mm/min; profundidade p = 2,75–2,93 mm; defeitos: solda quente (todos!), solda fria
  (nenhum), rebarbas, superfície sem preenchimento, variação do cordão, superfície áspera, túnel no keyhole.
  (Obs.: "J. A. P. C. Filho" — possivelmente o próprio Prof. Lindolfo? Não: o orientador é Lindolfo **Moreira** Filho;
  o autor da dissertação é J. A. P. C. Filho. Verificar.)
- Modelo: torque/calor por atrito puro, τ = μ F_f / A_c, ombro + lateral + ponta do pino;
  **Q_wl = (ω μ F_f / v)[ (2/3)((r_s³ − r_bp³)/(r_s − r_bp) + r_bp) + h_p/2 ]**, **Q_eff = (h_p/t)·Q_wl**
  (correção pela penetração); correlação T_w/T_s (Hamilton & Dymek 2008).
  ⚠️ A integração dele tem inconsistências dimensionais (divide por (r_s − r_bp), Q₂ = ωμF h/2...) — não copiar
  as equações sem rederivar.
- Análise: **regressão logística univariada p = 1/(1+e^−(b₀+b₁ log₁₀ Q_eff))** por tipo de defeito (Matlab
  `glmfit`), limiar de 50 % → Q_eff crítico; "banda segura" = interseção dos limiares.
- Resultados reportados: túnel 83,0 %, rebarbas 63,8 %, sem preenchimento 87,2 %, áspera 66,0 %, variação 72,3 %.
  Banda segura global **vazia**. Túnel "cresce com a energia" (contraintuitivo).

### ⚠️ Lição metodológica crítica (verificado em 12/10/2026)

Recalculando as prevalências da Tabela 3.4/3.5 (n = 47): túnel 39/47 → **classe majoritária = 83,0 %**; sem
preenchimento 41/47 → **87,2 %**; rebarbas 30/47 → **63,8 %**; áspera → 63,8 %; variação → 70,2 %.
**As acurácias do veterano são idênticas (ou +1 acerto) ao classificador trivial "sempre a classe majoritária"**, e
foram medidas **dentro da amostra** (sem teste). Ou seja, Q_eff praticamente não discriminou nada.
➡ No nosso TG: **sempre** reportar baseline majoritário (60,2 % no dataset de Du), matriz de confusão, sensibilidade/
especificidade, e acurácia **fora da amostra** (teste cego + validação cruzada). Isso diferencia o trabalho e é algo
que a banca (mesmo orientador) pode valorizar. Também mostra que um índice de energia **único** pode ser insuficiente
→ justificativa para um C_void multi-termo.

## Referências úteis citadas pelo veterano (para reaproveitar)

- THREADGILL, P. L.; LEONARD, A. J.; SHERCLIFF, H. R.; WITHERS, P. J. Friction stir welding of aluminium alloys.
  **International Materials Reviews**, v. 54, n. 2, p. 49-93, 2009. → **Fonte ideal para "hot welds vs cold welds",
  janela de processo, efeito da força axial ampliando a janela, causas de vazio (pressão de forja insuficiente, v alto +
  ω baixo = poucas rotações por mm, folga)**. Também é a ref. 3 de Du et al. Não temos o PDF — vale obter.
- COLEGROVE, P. A.; SHERCLIFF, H. R. Three-dimensional CFD modelling of flow round a threaded friction stir welding
  tool profile. **J. Mater. Process. Technol.** / STWJ, 2005.
- HAMILTON, C.; DYMEK, S. (2008) modelo térmico, T/T_solidus vs energia.
- KASHAEV, N. et al. (2018) — revisão LBW/FSW na indústria aeronáutica (também citado por Aldanondo).
- CARTER, B. (2014) NASA Glenn — apresentação "Introduction to FSW" (fonte p/ Delta II, SLS).
- PAR Systems (2022) — FSW no SLS/Artemis; HOFFMAN et al. (2022) NASA ALMF.
- ABNAR, B. et al. (2015) — efeito do heat input em AA3003 (E_l baixo → vazios; alto → crescimento de grão).
- THOMAS, W. M. et al. (1991) patente; THOMAS et al. (2001) razão volume dinâmico/estático.
- TWI (2000, 2002, 2006, 2023) — notas técnicas.
