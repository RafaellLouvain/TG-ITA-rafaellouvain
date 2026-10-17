# Mishra & Ma (2005) — revisão clássica de FSW/FSP

**Arquivo:** `referencias/Mishra_Ma_fundamentos.pdf` (78 p.)

**ABNT:** MISHRA, R. S.; MA, Z. Y. Friction stir welding and processing. **Materials Science and Engineering: R:
Reports**, v. 50, n. 1-2, p. 1-78, 2005. DOI: 10.1016/j.mser.2005.07.001.

Estrutura: 1 Intro · 2 Parâmetros (ferramenta, soldagem, junta) · 3 Modelagem (fluxo de metal, temperatura) ·
4 Microestrutura (nugget, TMAZ, HAZ) · 5 Propriedades (tensão residual, dureza, tração, fadiga, tenacidade, corrosão) ·
6 Materiais (Cu, Ti, aço, Mg, MMC, dissimilares) · 7 Aplicações (aeroespacial, blindagem) · 8 FSP · 9 Questões em aberto
· 10 Resumo. Para o TG importam sobretudo §2, §3, §4, §7.1 e §9–10 (lidos integralmente); §5, §6, §8 lidos por
varredura.

## Pontos-chave com localização (para citar com segurança)

### §1 / §7.1 — contexto
- FSW inventado no **TWI (UK) em 1991**; ligas 2XXX e 7XXX "não soldáveis" por fusão (microestrutura de
  solidificação ruim, porosidade, trinca a quente). Ferramenta: (a) aquece, (b) move o material.
- Tabela 1: benefícios — processo em fase sólida, baixa distorção, sem perda de elementos de liga, sem gás de
  proteção, **"apenas 2,5 % da energia de uma solda a laser"**.
- Aeroespacial: Eclipse 500, **Boeing — tanques do foguete Delta** e estruturas internas do C-17; "milhas de solda sem
  defeitos". (Falcon 9 / SLS citados no TG1 **não estão** nesta fonte — precisam de outra referência.)

### §2.1 — geometria da ferramenta
- "Geometria da ferramenta é o aspecto mais influente no desenvolvimento do processo"; **o maior componente de
  aquecimento vem do atrito ombro–peça**; "do ponto de vista térmico, o tamanho relativo pino/ombro é o que importa".
  O ombro também **confina** o volume aquecido.
- **Razão volume dinâmico / volume estático** (Thomas et al.): cilíndrico 1,1:1; Whorl™ 1,8:1; MX Triflute™ 2,6:1
  ➡ **esta é a fonte original** do conceito citado no TG1 (atribuído lá a Ahmed/Walla).
- Pinos tronco-cônicos (Whorl, Triflute) deslocam 60–70 % menos material, reduzem força, facilitam fluxo e o
  "augering" para baixo. A-skew™ (eixo do pino levemente inclinado → ação orbital de forjamento na raiz).

### §2.2 — parâmetros de soldagem
- Mais importantes: **rotação ω (rpm)** e **velocidade de avanço v (mm/min)**. ω↑ → mais atrito, T maior, mais
  mistura; mas o aumento de calor com ω **não é monotônico**, pois μ muda.
- **Tilt** para trás garante que o ombro segure o material e o mova da frente para trás do pino.
- **Profundidade de inserção:** rasa demais → ombro não toca → **"inner channel" (canal/túnel interno) ou sulco
  superficial**; funda demais → rebarba (flash) excessiva e afinamento.
- Pré-aquecimento para materiais de alto ponto de fusão/alta condutividade (calor insuficiente → difícil obter solda
  contínua sem defeito).

### §3.1 — fluxo de material
- Reynolds (marker insert, 2195Al): fluxo assimétrico; material vai para trás (até 1 diâmetro do pino); no AS
  material é empurrado para baixo, no RS para cima; **deslocamento vertical inversamente proporcional ao "weld pitch"
  (v/ω = avanço por rotação)**; transporte aumenta com o diâmetro do pino.
  ➡ **"Câmara de extrusão" (Reynolds):** ombro (teto) + pino + placa de apoio (piso) + metal frio (paredes) formam uma
  câmara de extrusão que se move. (TG1 slide 15 ✔ — é de Reynolds, citado em Mishra & Ma.)
- Guerra et al.: zona rotacional que avança com o pino + material extrudado pelo RS. Colligan: grande parte do
  material é simplesmente **extrudado pelo lado de retrocesso** e depositado atrás. London et al.: tilt de 3° causa
  "plowing" à frente.
- **Arbegast (2008) — modelo de zonas de metalworking:** pré-aquecimento, deformação inicial, **extrusão**,
  **forjamento** (material forçado para a cavidade deixada pelo pino sob pressão hidrostática; ombro aplica força de
  forja) e resfriamento. Modelo de **balanço de massa da zona de extrusão** relaciona geometria, parâmetros e tensão
  de escoamento ➡ base para o argumento "vazio = falha no balanço de massa / preenchimento da cavidade".
- Modelos: Goetz & Jata: taxas de deformação 2–12 s⁻¹, deformações 2–5; Colegrove & Shercliff (CFD 2D, slip).

### §3.2 — temperatura (MUITO relevante para o C_void)
- Pico na zona de mistura 400–500 °C (7075: 400–480 °C; 6061: ~400–450 °C). T máx. no topo (ombro). Gradiente na
  espessura pequeno dentro da zona de mistura.
- Tang et al.: T↑ com ω e com pressão; o aumento de T com ω satura (+40 °C de 300→650 rpm; +20 °C de 650→1000).
  **O ombro domina a geração de calor** (área e pressão maiores e maior velocidade linear).
- **Hashimoto et al.: T de pico cresce com a razão ω/v** (2024-T6, 5083-O, 7075-T6).
- **Frigaard et al.:** potência média **q₀ = (4/3) π² μ P ν R³** (ν em rot/s, R raio da ferramenta) — rotação e raio do
  ombro são as variáveis principais; **P não pode exceder a tensão de escoamento** na temperatura de operação.
- **Arbegast & Hartley — pseudo heat index w = ω²/v:**
  **T/T_m = K · (ω²/(v·10⁴))^α**, com **α = 0,04–0,06** e **K = 0,65–0,75** (ω em rpm, v em pol/min no original;
  T em °C). **T_máx. em FSW de ligas de Al fica entre 0,6·T_m e 0,9·T_m** (faixa de trabalho a quente e de
  solubilização). ➡ fórmula fechada para estimar T* sem CFD — candidata forte para o Π_Term.
- **Schmidt et al. (2004) — calor total (W):**
  Q = (2/3)π [δ σ_y/√3 + (1−δ) μ p] ω [(R_s³ − R_p³)(1 + tan α) + R_p³ + 3R_p² H_p]
  (α = ângulo de cone do ombro; δ = variável de estado de contato: 1 = sticking, 0 = sliding). Validado em 2024-T3.
  ➡ **é a equação do slide 16 do TG1** (lá aparece "Q_total ... (1 + tan α)").
- Conclusões da seção: T < T_fusão; ombro domina; **T↑ com ω, T↓ com v, T↑ com ω/v**; T máx. no topo. Diferentes
  "pseudo heat index" existem e **não há tendência geral** ao correlacionar datasets distintos (aviso honesto dos
  autores — relevante para nós!). Sharma & Mishra: atrito muda de "stick" (ω baixo) para "stick/slip" (ω alto).

### §4 — microestrutura
- **Nugget / zona de mistura (DXZ):** recristalização dinâmica, grãos finos equiaxiais, tipicamente na faixa de
  **micrômetros** (resumo: **0,1–18 µm**; UFG < 1 µm com resfriamento). Forma "basin" (ω baixo) ou elíptica (ω alto);
  anéis de cebola. Interface nugget/metal base nítida no AS e difusa no RS. Mecanismos: CDRX, DDRX, GDRX.
  Precipitados: dissolução + coarsening + reprecipitação (T 400–550 °C no nugget).
- **TMAZ:** grãos deformados em fluxo ascendente ao redor do nugget, **sem recristalização** (deformação
  insuficiente), alguma dissolução de precipitados, muitos sub-contornos.
- **HAZ:** só ciclo térmico (definida por Mahoney como T > 250 °C em liga tratável); mesma estrutura de grão do metal
  base; **coarsening de precipitados e alargamento da PFZ** (zona livre de precipitados, ×5 em 7050).

### §6.6 — "auto-regulação" térmica
- Fusão significativa não se sustenta: líquido não transmite cisalhamento → se ω alto superaquecer e fundir
  parcialmente a superfície, **o acoplamento ferramenta-peça cai, limitando T**. Fusão parcial define o **limite
  superior de ω**. (TG1 slide 13–14 ✔ — mas a fonte está na seção de dissimilares.)
- "Cold weld" (pouca interpenetração) citado em 2024/D357.

### §6 — outros materiais (evidência de "vazio por pouco calor")
- Latão 60/40: frequência de **vazio tipo sulco aumenta com v↑ ou ω↓** (Park et al.).
- AZ91D: **v maior ou ω menor que o ótimo → vazios internos / falta de ligação.**
- Dissimilares: costura não soldada, grandes zonas abertas (vazios), óxidos na raiz.

### §9–10 — lacunas
- Fluxo de material "complicado e pouco compreendido"; projeto de ferramenta ainda intuitivo; ferramentas
  proprietárias → generalização difícil sem saber a ferramenta (relevante: o dataset não tem perfil do pino).

## ⚠️ Divergências com o TG1

| Afirmação no TG1 | O que a fonte diz |
|---|---|
| "janela 0,6–0,9 T_m" ✔ | §3.2, de Arbegast & Hartley |
| "faixa ótima 0,7–0,8 T_m na borda de ataque" | **não encontrado** em Mishra & Ma |
| "cold voids vs hot voids" (slides 13–14, relatório §2.1) | **termos não aparecem** em Mishra & Ma. Existe a ideia (calor insuficiente → vazio; excesso → flash/fusão parcial), mas a dicotomia "cold/hot" vem de outras fontes (ex.: Kim et al. 2006, *Three defect types in friction stir welding of aluminum die casting alloy*, MSE A 415: flash por calor excessivo, cavidade/sulco por calor insuficiente; Arbegast 2008). **Citar a fonte correta no TG final.** |
| "liquefação local ... ejeção de massa como rebarba → hot voids" | parcialmente: auto-regulação e fusão parcial (§6.6); flash por inserção profunda (§2.2) |
| Grãos do nugget "1–5 µm" | Mishra & Ma: típico na faixa de µm, 0,1–18 µm no resumo. Valor "1–5" não é citação literal |
| HAZ "200–250 °C", β'' Mg₅Si₆ | vem de **Laska et al. (2023)** para AA6082; Mishra & Ma: HAZ = T > 250 °C |
| "ombro responde por boa parte do calor pelo braço de momento cúbico R³" ✔ | §2.1 e §3.2 (Schmidt; Frigaard; Tang) |
| equação Q_total do slide 16 ✔ | §3.2, eq. (3c), Schmidt et al. |
| "câmara de extrusão" ✔ | §3.1.1.1 (Reynolds) |

## Ideias diretamente aproveitáveis para o C_void

1. Π térmico baseado em **T/T_m ≈ K(ω²/v)^α** (Arbegast–Hartley) ou em **Q/v** (energia por comprimento, Schmidt/
   Frigaard): ambos usam só parâmetros de máquina + geometria.
2. Expoentes pequenos (α ≈ 0,05) ⇒ T depende muito fracamente de ω²/v → trabalhar com **logaritmos**
   (log(ω²/v)) é natural; um C_void log-linear (lei de potência) é coerente com a física.
3. **Weld pitch v/ω** governa o fluxo vertical (Reynolds) → candidato a Π cinemático.
4. **P ≤ σ_y(T)** (Frigaard) e τ = σ_y/√3 no sticking → normalizar pressão por σ_y: **p/σ_y** é um adimensional
   natural para o bloco dinâmico.
