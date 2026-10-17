# Du, Mukherjee & DebRoy (2019) — artigo-base / benchmark

**Arquivo:** `referencias/yang_du_original_reserach_main_source.pdf` (8 p.)

**ABNT:** DU, Y.; MUKHERJEE, T.; DEBROY, T. Conditions for void formation in friction stir welding from machine
learning. **npj Computational Materials**, v. 5, n. 68, 2019. DOI: 10.1038/s41524-019-0207-y.

> ⚠️ O periódico é a **npj Computational Materials** (grupo Nature, parceria com o Shanghai Institute of Ceramics),
> **não a revista *Nature***. O TG1 (resumo, slides 10/26) diz "publicado na Nature" — corrigir no TG final para
> "npj Computational Materials (Nature Portfolio)".
> Autores: Yang Du (Penn State + Tianjin Univ.), Tuhin Mukherjee, Tarasankar DebRoy (Penn State). Recebido 15/02/2019,
> aceito 06/06/2019. Acesso aberto (CC BY 4.0).

## O que fizeram

- 108 conjuntos de dados experimentais independentes da literatura (refs 4–19 do artigo) para FSW de **AA2024,
  AA2219, AA6061**; **43 com vazio**, 65 sem. Presença de vazio decidida pela seção transversal da solda.
  Alvo: 1 = vazio, 0 = sem vazio.
- Justificativa para juntar dados de máquinas diferentes: não há evidência de que a marca/modelo da máquina afete vazio.
- Escolheram NN e DT (dizem que KNN precisa de muitos dados, SVM "não dá modelo reutilizável", RF é para saídas
  multivariáveis — justificativas fracas, podem ser discutidas no TG).
- Para p e θ não reportados, adotaram "valores razoáveis comumente usados" → marcados com `*` (no CSV).
- **Observação dos autores (importante para nós):** "se qualquer um dos parâmetros brutos é mantido constante, ajustar
  os outros pode resultar em juntas com e sem vazio" → todos os parâmetros brutos têm influência parecida; por isso
  **não** fizeram DT nos parâmetros brutos, só NN.
- **Analogia com o número de Reynolds** (p. 2): o comportamento de sistemas complexos é melhor descrito por *grupos* de
  variáveis do que por variáveis brutas. ➡ **Este é exatamente o gancho conceitual do nosso C_void adimensional** —
  citar explicitamente no TG.
- Variáveis "causais" (computadas por modelos mecanísticos): **temperatura local T** (perto da ponta do pino, lado de
  avanço, onde o vazio se forma), **taxa de deformação relativa ε_r = ε̇/rps**, **torque total no pino M_T**,
  **tensão de cisalhamento máxima no pino τ_m**. Normalizadas pelo **máximo de cada liga** (para remover efeito de
  composição).
- Vazio ↔ **T baixa**, **τ_m, M_T, ε_r altos**. Fluxo inadequado/descontínuo ao redor do pino = causa. Fluxo inadequado
  vem de aporte térmico insuficiente (ω baixo para dado v), diâmetro de ombro inadequado, chapa espessa etc.
- Fig. 2 (dados de Doude et al. 2015, v = 100 mm/min constante): ω = 2,5 rps → vazio grande (T=596,6 K, τ=70,5 MPa);
  3,33 rps → vazio pequeno (614,1 K; 56,3 MPa); 6,67 rps → sem vazio (654,5 K; 31,9 MPa).
- Fig. 1: T monitorada 298 → 608 K; τ no pino é senoidal com máximo no lado de retrocesso (θ = 90° da direção de
  soldagem); torque cai com aumento do aporte de calor (v↓ ou ω↑).
- Literatura citada: pico de temperatura deve estar entre **80–90 % de T_solidus** para evitar vazio (Qian et al. 2013,
  ref 25).

## Modelo analítico "back-of-the-envelope" (Métodos)

Temperatura local (condução em chapa grossa, fonte pontual — Grong 1994):

$$T - T_0 = \frac{Q}{\rho C_p (4\pi\alpha t)^{1.5}}\exp\!\left(-\frac{R^2}{4\alpha t}\right)$$

Calor total gerado:

$$Q = \tfrac{2}{3}\pi\,[\delta\tau + (1-\delta)\mu_f P_N]\,\omega\,[(r_s^3 - r^3)(1+\tan\phi) + r^3 + 2r^2 l_p]$$

com α = k/(ρC_p), R² = x²+y²+z²; τ = tensão de cisalhamento no escoamento; δ = coef. de escorregamento (slip);
μ_f = coef. de atrito; P_N = força axial; r_s, r = raios do ombro e pino; l_p = comprimento do pino; ω = rotação;
φ = ângulo (chamado "tilt" no texto — na formulação original de Nandan/Schmidt é o **ângulo de concavidade do ombro**);
t = tempo para atingir regime. ➡ **Base direta para construir Π_Term / Π_Geom**: Q ∝ ω·(σ_y/√3 ou μp)·R_s³.

Velocidades/strain rate: 12 pontos de monitoramento (AS, RS, frente, trás × 3 alturas: ponta, meio, raiz do pino).
Propriedades e coeficientes assumidos independentes de T no modelo analítico.

## Resultados (Tabela 1 do artigo)

| Método | ML | Entradas | Treino | Validação | **Teste** |
|---|---|---|---|---|---|
| 1 | NN | 10 parâmetros brutos (v, ω, R_s, t, p, R_pt, R_pr, θ, α, σ_y) | 98,4 % | 86,6 % | **83,3 %** |
| 2 | NN | T*, ε_r*, M_T*, τ_m* (modelo analítico) | 92 % | 86,6 % | **93,3 %** |
| 3 | DT | idem (analítico) | 88,8 % | 80 % | **90 %** |
| 4 | NN | idem (modelo numérico CFD) | 95,2 % | 93,3 % | **96,6 %** |
| 5 | DT | idem (numérico) | 92 % | 86,6 % | **96,6 %** |

Limiares do DT: Método 3 — T* = 0,93; τ_m* = 0,94; ε_r* = 0,65; M_T* = 0,90; importância τ_m* > T* > ε_r* = M_T*.
Método 5 — T* = 0,94; τ_m* = 0,83 e 0,77; ε_r* = 0,72; M_T* = 0,67; importância T* > τ_m* > ε_r* = M_T*.
Ex.: "soldas com T* < 0,93 são suscetíveis a vazio".
Matrizes de confusão (Fig. 5, teste n=30): método 1 → 2 FP/3 FN aprox. (25/30 corretos); métodos 4/5 → 29/30.

**Split:** 63 treino (25 vazios) / 15 validação (6 vazios) / 30 teste (12 vazios), aleatório estratificado.
NN: tanh, 4–8 nós ocultos, Bayesiana com regularização; escolhe o modelo de menor *log predictive error*.
Limiar dos DT: busca do valor em [0,1] com menos erros por variável.

**Ranking final de influência:** T > τ_m > M_T > ε_r (conclusão 1 do artigo).

## Como usar no TG

- **Benchmark direto:** nosso C_void usa **as mesmas entradas do Método 1** (parâmetros brutos) → comparação justa é com
  **83,3 %** (NN caixa-preta). Os 90–96,6 % exigem modelo analítico/CFD prévio.
- ⚠️ **Erro no TG1:** os slides 27 e 29 dizem que Du et al. atingiram 83,33 % "através da arquitetura acoplada CFD + RNA".
  **Errado**: 83,3 % é a NN só com parâmetros brutos; com CFD + RNA foi 96,6 %. Corrigir no TG final.
- O nosso diferencial: equação explícita, transparente, sem CFD/NN, usando grupos adimensionais (ideia do Reynolds que
  os próprios autores sugerem). Podemos inclusive tentar **aproximar T*, τ_m*** com fórmulas fechadas (ex.: correlação
  adimensional de pico de temperatura de Roy, Nandan & DebRoy 2006 — ref 41; "back-of-the-envelope" de Arora, DebRoy &
  Bhadeshia 2011 — ref 40) e usá-los dentro do C_void.
- Referências secundárias úteis do artigo para buscar: 25 (Qian 2013, modelo analítico ω-v sem defeito), 27 (Arbegast
  2008, modelo de zona de deformação e defeitos), 39 (Arora 2011, ombro ótimo), 40, 41, 43.
