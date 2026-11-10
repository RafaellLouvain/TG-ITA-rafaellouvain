# Plano da apresentação final do TG2 (estilo A, Beamer 16:9) — versão 2

Premissas: um slide por seção da revisão que interessa, **um slide por subseção da metodologia** e um por
resultado relevante → 43 slides + 4 de reserva. Bullets em frases completas (3 a 5 por slide), com a palavra-chave
em negrito no início, para servirem de roteiro de fala. Figuras e tabelas sempre retiradas do relatório
(numeração atual, 77 p.). Tempo estimado: ~35–40 min a ~50 s por slide (ajustável).

---

## Parte 1 — Introdução (6 slides)

### 1. Capa
Título oficial, subtítulo do C_void, autor, orientador, TG2 · Eng. Mecânica-Aeronáutica · ITA · 2026.

### 2. O processo FSW e sua relevância
- **Mensagem:** o FSW une metais sem fundi-los e viabilizou a soldagem de ligas aeronáuticas antes consideradas não soldáveis.
- **Bullets:**
  - **Princípio:** uma ferramenta rotativa (ombro + pino) gera calor por atrito e deformação, amolece o metal e o mistura mecanicamente ao longo da junta.
  - **Estado sólido:** como não há fusão, evitam-se trincas de solidificação e porosidade típicas da soldagem a arco.
  - **Aplicações:** ligas 2xxx e 7xxx de alumínio, difíceis de soldar por fusão; uso aeroespacial, naval e automotivo.
- **Visual:** Fig. 2.1 (esquema do processo).

### 3. O problema: vazios volumétricos
- **Mensagem:** o vazio é o defeito mais crítico porque é interno, não aparece na superfície e reduz a resistência mecânica.
- **Bullets:**
  - **O que é:** uma cavidade no interior da junta, em geral no lado de avanço, formada quando o material não preenche o espaço deixado pelo pino.
  - **Por que preocupa:** atua como concentrador de tensão e reduz a resistência à tração e à fadiga.
  - **Difícil de detectar:** exige ensaios não destrutivos (ultrassom, raio X) ou corte da peça.
  - **Consequência:** escolher parâmetros por tentativa e erro é caro; é preciso prever o defeito antes de soldar.
- **Visual:** Fig. 2.14 (macrografias com vazio grande, pequeno e sem vazio, de Du et al.).

### 4. Como se prevê hoje
- **Mensagem:** os métodos atuais são precisos, mas caros (simulação) ou pouco interpretáveis (aprendizado de máquina).
- **Bullets:**
  - **Simulação:** modelos CFD e de elementos finitos exigem muito esforço computacional para cada condição.
  - **Du, Mukherjee e DebRoy (2019):** compilaram 108 soldas da literatura e treinaram redes neurais e árvores de decisão.
  - **Resultados deles:** 83,3% com os 10 parâmetros brutos; 90% a 96,6% com variáveis causais calculadas por modelos analíticos e numéricos.
  - **Lacuna:** nenhum desses métodos fornece uma relação explícita, calculável à mão, entre os parâmetros e o defeito.
- **Visual:** Tab. 2.3 (métodos e acurácias de Du et al.).

### 5. A linha de pesquisa no ITA
- **Mensagem:** este trabalho continua uma sequência de trabalhos do grupo sobre FSW.
- **Bullets:**
  - **Cintra (2018):** 47 soldas de AA2024-T3; defeitos de soldas quentes, frias e mistas; força de forjamento como parâmetro primordial.
  - **Gomes (2019), Esaki (2022):** modelagem térmica e por elementos finitos da temperatura de soldagem.
  - **Batista Filho e Tanaka (2020), Alcoforado (2021):** caracterização mecânica e metalográfica de juntas.
  - **Bezerra (2025):** regressão logística da energia efetiva sobre os ensaios de Cintra; a energia isolada não basta.
  - **Este trabalho:** passa de uma liga e uma ferramenta para uma base com várias ligas, ferramentas e espessuras.
- **Visual:** nenhum (ou Fig. 2.17, curva de Bezerra).

### 6. Objetivos
- **Mensagem:** propor uma expressão explícita, testá-la com rigor e entender quais variáveis importam.
- **Bullets:**
  - **Objetivo 1:** propor o Coeficiente Analítico de Vazio (C_void), expressão simples que prevê vazio a partir dos parâmetros de processo, da ferramenta e do material.
  - **Meta:** mais de 70% de acurácia na base de 108 soldas de Du et al.
  - **Objetivo 2:** hierarquizar a influência das naturezas das variáveis: cinemática, geométrica, térmica, dinâmica e metalúrgica.
- **Visual:** nenhum (slide limpo, só com os três itens).

---

## Parte 2 — Revisão da literatura (7 slides)

### 7. Ferramenta e variáveis do processo (Seção 2.1)
- **Mensagem:** as variáveis do problema se agrupam em naturezas, e o ombro é a principal fonte de calor.
- **Bullets:**
  - **Ferramenta:** o ombro (raio R_s) gera a maior parte do calor; o pino (raios R_pr e R_pt) arrasta e mistura o material.
  - **Lados:** no lado de avanço a velocidade da ferramenta soma-se à do avanço; no de recuo, subtrai-se; a solda é assimétrica.
  - **Variáveis:** rotação ω e avanço v (cinemáticas); R_s, R_pr, R_pt, t (geométricas); p e θ (dinâmicas); α (térmica); σ_y (metalúrgica).
- **Visual:** Fig. 2.2 (ferramenta) ou Fig. 2.3 (lados de avanço e recuo).

### 8. Geração de calor e temperatura (Seção 2.2)
- **Mensagem:** a temperatura máxima é função forte da rotação; o avanço governa mais a taxa de aquecimento.
- **Bullets:**
  - **Origem do calor:** atrito e deformação plástica na interface; o calor local é proporcional à velocidade de deslizamento ωr, máxima na borda do ombro.
  - **O ombro domina:** ferramentas com e sem pino produzem praticamente a mesma temperatura de pico.
  - **Faixa típica:** a temperatura de pico fica entre 0,6 e 0,9 da temperatura de fusão; os vazios se associam a temperaturas baixas.
  - **Correlações:** Arbegast–Hartley (T/T_m ∝ (ω²/v)^α, com α pequeno) e Arora et al. (aporte de calor adimensional Q*).
- **Visual:** Fig. 2.6 (temperatura de pico com e sem pino).

### 9. Escoamento do material (Seção 2.3)
- **Mensagem:** o vazio surge quando o material arrastado pela frente da ferramenta não retorna para preencher o espaço atrás do pino.
- **Bullets:**
  - **Extrusão:** o material é extrudado ao redor do pino, sobretudo pelo lado de recuo, e forjado atrás da ferramenta pelo ombro.
  - **Balanço de massa (Arbegast):** se o material que sai da frente não for igual ao que retorna atrás, sobra uma cavidade.
  - **Geometria do pino:** pinos cônicos e com canais facilitam o transporte de material para baixo.
- **Visual:** Fig. 2.9 (zonas de deformação do modelo de Arbegast).

### 10. Defeitos e a janela de processo (Seção 2.5)
- **Mensagem:** há defeitos de solda fria e de solda quente; o vazio está no lado frio.
- **Bullets:**
  - **Lado frio (rotação baixa, avanço alto):** pouco calor e escoamento insuficiente → vazio, falta de preenchimento.
  - **Lado quente (rotação alta, avanço baixo):** excesso de calor → rebarba, arrancamento superficial, colapso do núcleo.
  - **Janela de processo:** a região intermediária gera soldas sãs; o aumento da força axial amplia essa janela.
- **Visual:** Fig. 2.12 (defeitos e janela de Arbegast).

### 11. Influência dos parâmetros (Seção 2.6)
- **Mensagem:** a literatura combina rotação e avanço em índices empíricos, mas cada um atribui pesos diferentes às duas velocidades.
- **Bullets:**
  - **Rotação:** aumenta o calor e reduz o torque, com efeito que tende a saturar.
  - **Avanço:** reduz o calor por comprimento e aumenta os esforços.
  - **Combinações clássicas:** ω/v (avanço por rotação), ω²/v (pseudoíndice de calor), energia por comprimento.
  - **Raio do ombro:** principal fator geométrico do calor gerado.
- **Visual:** Fig. 2.7 (temperatura de pico × razão ω/v).

### 12. Modelagem e predição: Du et al. (Seção 2.7)
- **Mensagem:** a referência do trabalho mostra que as variáveis causais predizem bem, mas exigem modelos prévios.
- **Bullets:**
  - **Variáveis causais:** temperatura, taxa de deformação, torque e tensão de cisalhamento máxima no pino.
  - **Limites de decisão:** soldas com temperatura normalizada abaixo de 0,93 tenderam a ter vazio.
  - **Hierarquia deles:** temperatura e tensão de cisalhamento > torque > taxa de deformação.
  - **Abertura para este trabalho:** obter algo parecido diretamente dos parâmetros, sem simulação.
- **Visual:** Fig. 2.18 (as quatro variáveis causais).

### 13. Síntese: o que esperar de cada variável (Seção 2.9)
- **Mensagem:** a revisão gera uma "previsão" do sinal de cada variável, usada depois para checar os modelos.
- **Bullets:**
  - **Reduzem o risco:** rotação, raio do ombro, pressão, inclinação (mais calor, mais forjamento).
  - **Aumentam o risco:** avanço, espessura (menos calor por comprimento, raiz mais fria).
  - **Incertos:** geometria do pino e limite de escoamento.
- **Visual:** Tab. 2.4 (síntese dos efeitos esperados).

---

## Parte 3 — Metodologia (12 slides, um por subseção)

### 14. Visão geral (Seção 3.1)
- **Mensagem:** a metodologia segue um fluxo único, aplicado igualmente a todas as abordagens.
- **Bullets:**
  - **Etapas:** auditoria da base → análise dimensional → três abordagens → calibração → validação → diagnóstico e robustez.
  - **Ordem das abordagens:** cada uma nasceu do resultado da anterior.
  - **Extra:** aplicação do índice final aos ensaios de Cintra (2018).
- **Visual:** Fig. 3.1 (fluxograma).

### 15. Base de dados (Seção 3.2)
- **Mensagem:** dados reais e públicos, mas compilados de estudos diferentes.
- **Bullets:**
  - **Origem:** 108 soldas de topo compiladas por Du et al. (2019), de 14 estudos independentes, em AA2024, AA2219 e AA6061.
  - **Variáveis:** 10 entradas (ω, v, R_s, R_pr, R_pt, t, p, θ, α, σ_y) e uma saída binária: 43 com vazio, 65 sem.
  - **Característica-chave:** dentro de cada estudo só a rotação e o avanço variam; as outras oito variáveis são constantes.
  - **Propriedades:** α e σ_y assumem um único valor por liga.
- **Visual:** Tab. 3.1 (variáveis, unidades e naturezas).

### 16. Tratamento dos dados (Seção 3.3)
- **Mensagem:** a base foi auditada, e três problemas foram tratados antes de qualquer modelo.
- **Bullets:**
  - **Coluna de liga:** diverge das propriedades em 33 linhas; a liga passou a ser identificada pelo par (α, σ_y), que é coerente com o estudo de origem.
  - **Valores assumidos:** p e θ foram assumidos por Du et al. em cerca de dois terços das soldas; θ tem só os valores 2° e 2,5°.
  - **Soldas duvidosas:** as linhas 84 a 89 foram mantidas, mas testadas na análise de robustez.
  - **Unidades:** tudo convertido para o SI.
- **Visual:** nenhum (ou um recorte da Tab. 4.1, estudos).

### 17. Análise dimensional e grupos adimensionais (Seção 3.4)
- **Mensagem:** pelo teorema Π, as 10 variáveis se reduzem a 7 grupos com significado físico.
- **Bullets:**
  - **Teorema Π:** 10 variáveis e 3 dimensões (massa, comprimento, tempo) → 7 grupos independentes.
  - **Grupos:** ωR_s/v, vR_s/α (Péclet), p/σ_y, t/R_s, R_pr/R_s, R_pt/R_pr e θ.
  - **Restrição 1:** a rotação só pode entrar dividida por uma velocidade de referência (o avanço ou α/R_s).
  - **Restrição 2:** p e σ_y só entram juntos, como p/σ_y; as naturezas dinâmica e metalúrgica não se separam.
- **Visual:** Tab. 3.2 (grupos adimensionais).

### 18. Abordagem 1: produto de grupos adimensionais (Seção 3.5.1)
- **Mensagem:** a proposta original do TG1 é uma lei de potência dos grupos, com expoentes calibrados.
- **Bullets:**
  - **Forma:** C_void = C₀ ∏ Π_i^β_i; prevê-se vazio quando C_void > 1.
  - **Três conjuntos, por mecanismo:** Buckingham completo (os 7 grupos), térmico (geração e condução de calor) e escoamento (extrusão ao redor do pino).
  - **Interpretação:** cada expoente indica o peso e o sentido da influência do grupo.
- **Visual:** Eq. 3.1 + Tab. 3.3 (conjuntos de grupos).

### 19. Abordagem 2: índice físico único (Seção 3.5.2)
- **Mensagem:** uma única grandeza física, comparada a um valor crítico.
- **Bullets:**
  - **Forma:** C_void = V_crit/(ωR_s); prevê-se vazio quando a velocidade periférica do ombro é menor que V_crit.
  - **Por que ωR_s:** é a velocidade de deslizamento na borda do ombro, onde o calor por área é máximo, e a velocidade do material arrastado.
  - **Só um parâmetro:** V_crit, sem expoentes ajustados.
  - **Comparações:** versões adimensionais ωR_s/v e ωR_s²/α, e o índice só com a rotação.
- **Visual:** Eq. 3.2.

### 20. Abordagem 3: núcleo físico com termos complementares (Seção 3.5.3)
- **Mensagem:** testar se algum grupo adimensional acrescenta informação ao núcleo ωR_s.
- **Bullets:**
  - **Forma:** ωR_s multiplicado por grupos escolhidos pelos dados.
  - **Seleção progressiva:** um grupo entra só se aumentar a acurácia da validação interna em pelo menos 1 ponto percentual.
  - **Sem olhar o teste:** a seleção usa só as soldas de treinamento.
- **Visual:** Eq. 3.3.

### 21. Calibração (Seção 3.6)
- **Mensagem:** a regressão logística é o método natural para calibrar uma lei de potência com resposta sim/não.
- **Bullets:**
  - **Equivalência:** o logaritmo da chance de vazio é linear nos logaritmos dos grupos, ou seja, a chance é uma lei de potência.
  - **Classes equilibradas:** 43 com vazio e 65 sem; as duas classes recebem o mesmo peso no ajuste.
  - **Limiar:** escolhido no treinamento para maximizar a acurácia.
  - **Métricas:** acurácia, sensibilidade (vazios detectados) e especificidade (soldas sãs aprovadas).
- **Visual:** Eq. 3.4 (logística) e Eq. 3.5 (métricas).

### 22. Protocolo de validação (Seção 3.7)
- **Mensagem:** três esquemas complementares, do mais comparável ao mais exigente.
- **Bullets:**
  - **Protocolo de Du et al.:** um único sorteio estratificado, 78 soldas de treino e 30 de teste; comparável à referência.
  - **500 sorteios:** o mesmo procedimento repetido 500 vezes; a média é a medida principal, mais robusta.
  - **Validação por estudo:** cada um dos 14 estudos sai inteiro para teste; simula máquina, ferramenta e chapa novas.
  - **Regra geral:** nenhuma decisão de modelagem usa os dados de teste.
- **Visual:** nenhum (ou um esquema simples 78/30 desenhado no próprio slide).

### 23. Hierarquia de influência e robustez (Seção 3.8)
- **Mensagem:** a hierarquia vem de evidências simples, cada uma ligada a uma natureza, e não de um modelo.
- **Bullets:**
  - **Cinemática:** AUC dentro dos estudos (pares de soldas do mesmo estudo) e expoente do avanço em ω·v^c.
  - **Geométrica:** ganho de acurácia ao passar de ω para ωR_s.
  - **Demais naturezas:** retirada de p e θ, frequência de escolha na abordagem 3 e versões com a difusividade.
  - **Robustez:** repetir tudo sem p e θ e sem as linhas duvidosas.
- **Visual:** Tab. 3.4 (análises usadas na hierarquia).

### 24. Aplicação aos ensaios de Cintra (Seção 3.9)
- **Mensagem:** testar o índice fora da base de calibração.
- **Bullets:**
  - **Ensaios:** 47 soldas de AA2024-T3, chapa de 3,2 mm, uma única ferramenta; só rotação e avanço variam; defeito registrado: túnel.
  - **Só a abordagem 2 se aplica:** as outras exigiriam pressão, inclinação e ponta do pino, não registradas.
  - **Dois testes:** índice calibrado em Du et al. aplicado diretamente; e limiar recalibrado nos próprios ensaios.
  - **Ferramentas:** Python (NumPy, pandas, SciPy, scikit-learn), código no repositório público (Seção 3.10).
- **Visual:** nenhum.

---

## Parte 4 — Resultados e discussão (15 slides)

### 25. Caracterização da base (Seção 4.1)
- **Mensagem:** os estudos são muito diferentes entre si; o nível crítico de rotação muda de estudo para estudo.
- **Bullets:**
  - **Diversidade:** espessura de 2,1 a 17,5 mm, raio do ombro de 5 a 14 mm, rotações de 150 a 2500 rpm.
  - **Dentro de cada estudo:** os vazios aparecem nas rotações mais baixas.
  - **Entre estudos:** o nível de rotação em que o vazio some é diferente, porque a ferramenta e a chapa mudam.
- **Visual:** Fig. 4.1 (rotação das soldas por estudo).

### 26. Abordagem 1: desempenho (Seção 4.2.1)
- **Mensagem:** no protocolo de Du, os grupos adimensionais atingem a meta e igualam a rede neural; no protocolo rigoroso, não.
- **Bullets:**
  - **Protocolo de Du:** 70,0% a 83,3%; o Buckingham completo igualou a rede neural (83,3%) com uma expressão explícita.
  - **500 sorteios:** 60,7% a 64,0%, abaixo da meta.
  - **Pista:** ficaram abaixo do índice formado só pela rotação (66,7%), sinal de que a informação estava na rotação.
- **Visual:** Tab. 4.2.

### 27. Por que: o regime de condução (Seção 4.2.2)
- **Mensagem:** nas soldas da base, a temperatura depende da potência gerada, e não da energia por comprimento.
- **Bullets:**
  - **Número de Péclet:** vR_s/α < 1 em 93% das soldas (mediana 0,30).
  - **Significado:** o calor se difunde à frente da ferramenta mais depressa do que ela avança; o campo de temperatura é quase estacionário.
  - **Consequência:** dividir a rotação pelo avanço (ωR_s/v) ou por α/R_s piora o índice.
- **Visual:** Tab. 4.3 (ωR_s 72,9% × ωR_s/v 60,9% × ωR_s²/α 63,7%).

### 28. Rotação × avanço dentro dos estudos (Seção 4.2.2)
- **Mensagem:** comparando soldas do mesmo estudo, a rotação explica quase tudo e o avanço quase nada.
- **Bullets:**
  - **AUC:** a rotação ordena corretamente 96% dos pares com e sem vazio; o avanço, 54% (quase um sorteio).
  - **Expoente do avanço:** em ω·v^c, o melhor c é −0,10, cerca de um décimo do peso da rotação.
  - **Literatura descartada:** o intervalo de c exclui ω/v (c = −1) e ω²/v (c = −0,5).
- **Visual:** Fig. 4.2.

### 29. Coerência física dos expoentes (Seção 4.2.3)
- **Mensagem:** mesmo sem atingir a meta no protocolo rigoroso, o conjunto térmico tem expoentes fisicamente coerentes.
- **Bullets:**
  - **Coerentes:** rotação, raio do ombro, pressão e difusividade no sentido esperado; avanço também, com peso pequeno (+0,26).
  - **Exceção:** a espessura sai com sinal oposto ao esperado.
  - **Explicação:** a espessura só varia entre estudos, que diferem também em ferramenta e rotação.
- **Visual:** Eq. 4.2 + Tab. 4.4.

### 30. Abordagem 2: velocidade periférica crítica (Seção 4.3)
- **Mensagem:** um único limiar de velocidade periférica prevê o vazio frio.
- **Bullets:**
  - **Índice:** C_void = V_crit/(ωR_s); vazio previsto quando ωR_s < V_crit, isto é, quando falta calor junto ao ombro.
  - **Limiar calibrado:** V_crit = 0,84 m/s, ou rotação (rpm) × raio do ombro (mm) ≈ 8.000.
  - **Desempenho:** 90,0% no protocolo de Du (27 de 30 soldas) e 72,9% na média de 500 sorteios.
  - **Simplicidade:** um único parâmetro, sem simulação; o avanço e a pressão não entram.
- **Visual:** Fig. 4.3. (slide de exemplo já pronto)

### 31. Como usar na prática (Seção 4.3)
- **Mensagem:** o índice vira uma regra direta de chão de fábrica.
- **Bullets:**
  - **Exemplo (R_s = 10 mm):** a 600 rpm, ωR_s ≈ 0,63 m/s → vazio; a 1.200 rpm, ≈ 1,26 m/s → solda sã.
  - **Rotação mínima:** cerca de 800 rpm para essa ferramenta.
  - **Limiar conservador (1,05 m/s, ≈ 10.000 rpm·mm):** detecta 75% dos vazios, mantendo 70,3% de acurácia.
  - **Raio do ombro:** um ombro maior atinge a mesma velocidade com menos rotação.
- **Visual:** Tab. 4.5.

### 32. Abordagem 3 (Seção 4.4)
- **Mensagem:** acrescentar grupos ao ωR_s quase não ajuda.
- **Bullets:**
  - **Ganho pequeno:** de 72,9% para 74,0% em média; nenhum ganho na validação por estudo.
  - **Instabilidade:** em média só 1,3 termo entra, e o conjunto escolhido muda de sorteio para sorteio.
  - **Mais escolhido:** a conicidade do pino (57%), seguida de p/σ_y (30%).
  - **Conclusão:** não justifica a complexidade adicional.
- **Visual:** Tab. 4.6.

### 33. Comparação com Du et al. — mesmo protocolo (Seção 4.5)
- **Mensagem:** com uma expressão, o desempenho é da mesma ordem dos métodos complexos.
- **Bullets:**
  - **Abordagem 2 (90,0%):** acima da rede neural com os mesmos parâmetros (83,3%).
  - **Igual à árvore de decisão** com variáveis causais de modelo analítico (90,0%).
  - **A cerca de 6 pontos** dos métodos com variáveis de simulação numérica (96,6%).
  - **Ressalva:** os conjuntos de teste são diferentes; a leitura é "mesma ordem de grandeza".
- **Visual:** Fig. 4.5 (protocolo de Du).

### 34. Comparação no protocolo rigoroso (Seção 4.5)
- **Mensagem:** a abordagem 2 se mantém acima da meta; um único sorteio pode enganar.
- **Bullets:**
  - **Médias:** abordagem 2 com 72,9%, abordagem 3 com 74,0%, abordagem 1 entre 60,7% e 64,0%.
  - **Dispersão:** um único sorteio varia de cerca de 60% a 83% para o mesmo modelo.
  - **Generalização:** 66,7% na validação por estudo, a 3,3 pontos da meta em condições inteiramente novas.
- **Visual:** Fig. 4.4 (boxplots) + Tab. 4.7.

### 35. Hierarquia das naturezas (Seção 4.6)
- **Mensagem:** cinemática > geométrica > dinâmica e metalúrgica > térmica.
- **Bullets:**
  - **Cinemática:** rotação ordena 96% dos pares; avanço, 54%.
  - **Geométrica:** acrescentar o raio do ombro leva de 66,7% para 72,9%.
  - **Dinâmica e metalúrgica:** p/σ_y escolhida em 30% dos sorteios, mas retirá-la quase não muda o desempenho.
  - **Térmica:** incluir α piora o índice (72,9% → 63,7%).
  - **Ressalva:** efeito não detectado não é o mesmo que efeito desprezível.
- **Visual:** nenhum (ou Tab. 3.4).

### 36. Robustez (Seção 4.7)
- **Mensagem:** as conclusões não dependem dos dados mais incertos.
- **Bullets:**
  - **Sem p e θ:** abordagem 2 inalterada; abordagem 3 −0,3 ponto; abordagem 1 −0,7 a −2,2 pontos.
  - **Sem as linhas 84–89:** as abordagens 2 e 3 melhoram ligeiramente (74,1% e 76,8%).
- **Visual:** Tab. 4.8.

### 37. Vazios de origem fria na base de Du (Seção 4.8)
- **Mensagem:** os vazios desta base são de calor insuficiente, e por isso a velocidade periférica basta.
- **Bullets:**
  - **Fonte:** Du et al. atribuem os vazios a aporte de calor insuficiente.
  - **Dados:** nenhum vazio acima de 1,3 m/s; a fração de vazios cai à medida que ωR_s aumenta.
  - **Dentro dos estudos:** em 96% dos pares, a solda com vazio é a de menor rotação.
- **Visual:** Tab. 4.10 (fração de vazios por faixa de ωR_s).

### 38. Ensaios de Cintra: um mecanismo diferente (Seção 4.8)
- **Mensagem:** o índice delimita a fronteira fria; os defeitos de Cintra parecem limitados pelo forjamento.
- **Bullets:**
  - **Aplicação direta:** todas as soldas abaixo do limiar (≈ 1.010 rpm com essa ferramenta); 83% com túnel.
  - **Mas:** a fração com túnel não cai com a rotação, e nenhuma recalibração separa as soldas.
  - **Leitura:** soldas quentes ou mistas, atribuídas pelo próprio Cintra à variação da força de forjamento.
  - **Implicação:** nesse regime, pressão axial e inclinação tendem a ser mais relevantes.
- **Visual:** Tab. 4.9.

### 39. Limitações (Seção 4.9)
- **Mensagem:** os limites vêm dos dados disponíveis, e não do método.
- **Bullets:**
  - **Estudos compilados:** oito variáveis só variam entre 14 condições.
  - **Dados incertos:** p e θ assumidos; α e σ_y com um valor por liga.
  - **Casos inseparáveis:** estudos 6 e 8, mesma liga e ferramenta, comportamentos opostos.
  - **Domínio:** índice válido para a fronteira fria; nenhuma base permite estudar a quente.
- **Visual:** nenhum.

---

## Parte 5 — Conclusão (4 slides)

### 40. Conclusões (1/2): o resultado
- **Bullets:**
  - **Meta atingida:** C_void = 0,84 m/s / (ωR_s); vazio previsto abaixo de 0,84 m/s (≈ 8.000 rpm·mm).
  - **Desempenho:** 90,0% no protocolo de Du, comparável a métodos com simulação; 72,9% na média de 500 sorteios.
  - **Abordagem 1:** também atingiu a meta no protocolo de Du (83,3%, igual à rede neural).
  - **Uso industrial:** limiar conservador de 1,05 m/s (≈ 10.000 rpm·mm).
- **Visual:** Eq. 4.4 em destaque.

### 41. Conclusões (2/2): o que se aprendeu
- **Bullets:**
  - **Física:** no regime de condução, a temperatura junto ao ombro depende da potência; por isso o avanço e a pressão não entram.
  - **Hierarquia:** cinemática > geométrica > dinâmica e metalúrgica > térmica.
  - **Domínio:** o índice descreve a fronteira entre regime frio e adequado.
  - **Método:** um único sorteio pode superestimar o desempenho; muitos sorteios e validação por estudo são essenciais.
- **Visual:** nenhum.

### 42. Trabalhos futuros
- **Bullets:**
  - **Base nova:** soldas com defeitos frios e quentes no mesmo estudo, com força axial, inclinação e propriedades das ligas medidas.
  - **Etapa 1:** confirmar o limiar de ωR_s como fronteira entre regime frio e adequado.
  - **Etapa 2:** encontrar a expressão da fronteira entre regime adequado e quente, provavelmente com variáveis dinâmicas e da liga.
  - **Generalização:** expressar V_crit em função das propriedades do material, tornando o índice adimensional.
- **Visual:** Fig. 2.13 (janela de processo).

### 43. Obrigado
Agradecimento, contato, repositório (github.com/RafaellLouvain/TG-ITA-rafaellouvain).

---

## Reserva (após o slide 43)
- **B1** Expoentes dos três conjuntos da abordagem 1 (Eqs. 4.1–4.3).
- **B2** Protocolo de Du × rigoroso lado a lado (Figs. 4.4 e 4.5).
- **B3** Validação por estudo: erros concentrados nos estudos 6, 8, 10, 12 e 13.
- **B4** Cintra: recalibração (limiar fora da faixa; expoentes livres +1,6 para ω e −1,6 para v).
