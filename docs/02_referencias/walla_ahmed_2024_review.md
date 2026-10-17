# Ahmed, Kadhum & Salleh (2024) — revisão sobre geometria de pino

**Arquivo:** `referencias/walla_ahmed_review_on_tool_geometry.pdf` (17 p.)

**ABNT:** AHMED, W. H.; KADHUM, A. H.; SALLEH, M. S. A Review on Tool Pin Geometry of Friction Stir Welding.
**Al-Khwarizmi Engineering Journal**, v. 20, n. 2, p. 39-55, 2024. DOI: 10.22153/kej.2024.02.001.

> ⚠️ "Walla" é o **prenome** da 1ª autora (Walaa H. Ahmed). No texto do TG1 aparece "Walla et al. (2024)" — o correto
> em ABNT é **"Ahmed, Kadhum e Salleh (2024)"** (ou "Ahmed et al. (2024)", que colide com Ahmed et al. (2021) → usar
> "AHMED, W. H. et al., 2024" vs "AHMED, M. M. Z. et al., 2021" para desambiguar). A lista de referências do TG1 já
> está correta.

## Conteúdo

Revisão narrativa (revista iraquiana, menor impacto) de ~24 estudos de perfis de pino: cilíndrico, rosqueado, cônico,
quadrado, triangular, hexagonal, com faces planas, etc. Tabela 1 com eficiência de junta, méritos e desvantagens.
- Parâmetros **primários**: v, ω, geometria da ferramenta; **secundários**: perfil do pino, material da ferramenta,
  espessura, material da peça.
- **O ombro produz a maior parte do calor e confina o material plastificado**; pino + ombro governam o fluxo.
- Conclusão: **pino quadrado** → melhores propriedades (eficiência até 94 %), atribuído à **maior razão
  volume dinâmico/estático** nos cantos ("more driving force") e à **ação pulsante** das faces planas (mais calor,
  mais plastificação). Triangular: menor UTS (54 %), demora a atingir T máx., recristalização insuficiente.
- Gopi & Mohan (2021): pulsos por segundo = nº de arestas × rotação; **105–110 pulsos/s** ótimo para solda sem defeito.
- Su, Xue & Wu (2020, CFD): mais faces planas → maior zona plástica, velocidade, T e calor; perfil do pino altera o
  torque < 4,7 %.
- Galvão et al. (2013): **vazio de túnel a v baixa (14 mm/min)** em Al-aço. Doos et al. (2014): túnel com menor aporte.
- Shammari (2019): por ANOVA, **tilt teve o maior impacto** e geometria do pino o menor (AA2024/6061).
- Al-kubaisy (2016): v foi a variável mais importante para resistência (66 %).
- Fluxo de material concentrado no lado de retrocesso (RS) — material se move mais no RS.

## Uso no TG

- Fonte para "razão volume dinâmico/estático" e "efeito pulsante" de pinos poligonais (citado no TG1 §2.2).
  ⚠️ "Excentricidade do pino como came" **não** está nesta revisão (nem em Ahmed 2021 de forma desenvolvida) — se for
  usar, buscar fonte própria (ex.: Essa et al.; Mehta/Reynolds).
- O dataset **não tem perfil do pino** — só R_pr e R_pt (conicidade). Então a geometria do pino entra só via raios:
  volume varrido ~ π·t·(R_pr² + R_pr R_pt + R_pt²)/3 (tronco de cone), razão R_pt/R_pr (conicidade), R_s/R_pr
  (razão ombro/pino; ótimo citado 2,5–3).
