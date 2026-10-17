# Aldanondo et al. (2020) — geometria da ferramenta em juntas sobrepostas Al-Li

**Arquivo:** `referencias/aldanondo_tool_geometry.pdf` (12 p.)

**ABNT:** ALDANONDO, E.; VIVAS, J.; ÁLVAREZ, P.; HURTADO, I. Effect of Tool Geometry and Welding Parameters on Friction
Stir Welded Lap Joint Formation with AA2099-T83 and AA2060-T8E30 Aluminium Alloys. **Metals**, v. 10, n. 7, p. 872,
2020. DOI: 10.3390/met10070872.

## Conteúdo real

- **Junta sobreposta (lap joint)** longarina-revestimento (stringer-skin) aeronáutica: extrudado **AA2099-T83** (2 mm)
  sobre chapa **AA2060-T8E30** (2,5 mm) — ligas Al-Li de 3ª geração. Projeto Clean Sky 2 (ecoTECH).
- Duas ferramentas: ombro plano Ø10 mm, pino Ø4 mm × 2,5 mm; (i) pino cilíndrico rosqueado convencional;
  (ii) pino "3 flats + mixed thread" (3 faces planas, roscas direita/esquerda/neutra).
- Máquina I-STIR PDS 4 (MTS) em **controle de carga** (força axial ajustada antes em controle de posição), **tilt 1,5°**,
  ω = 800/1200 rpm, v = 150/250 mm/min.
- **Nenhum defeito volumétrico (wormhole, cavidade, trinca) foi encontrado** em nenhuma condição. Defeitos estudados:
  **hook** e **cold lap** (típicos de junta sobreposta) e largura efetiva de sobreposição (ELW).
- Resultados: ferramenta convencional → ELW ~30 % maior, mas hook ~138 % maior; 3 flats mantém hook < 0,4 mm
  (critério B da ISO 25239). ω↑ aumenta ELW e hook; v↑ reduz hook.
- **Forças e torque:** forças X e Y crescem em geral com v; **torque aumenta com v e diminui com ω**; torque similar nas
  duas ferramentas → **o ombro é o fator principal do torque**, efeito do pino pouco significativo.
- Huang et al. (citado): cavidades em Al-Li lap fora de 800 rpm / 200 mm/min.

## ⚠️ Divergência com o TG1

O TG1 (relatório §2.3 e slides 22–23) atribui a Aldanondo et al.: "investigação na liga **AA2024-T3**", "controle de
posição vs controle de força", "forças insuficientes geram vazios volumétricos de raiz", "elevação **exponencial** de
F_z com v", "pinos volumosos sob baixa força geram tunneling". **Nada disso está no artigo.** O artigo é em Al-Li,
junta sobreposta, sem vazios; não mede F_z vs v (mede X/Y e torque). Provável alucinação do Gemini.

**Como reaproveitar honestamente no TG final:**
- torque ↑ com v e ↓ com ω → suporta que o **termo cinemático ω/v** (aporte térmico por comprimento) governa a
  "facilidade de fluxo" (ligação com M_T de Du et al.);
- ombro domina torque/calor → suporta R_s com peso alto (coerente com Q ∝ R_s³);
- geometria do pino controla fluxo vertical de material (relevante para preenchimento da cavidade);
- a afirmação "força axial insuficiente → vazio" deve ser citada de **outra fonte** (ex.: Mishra & Ma 2005; Kim et al.
  2006 "Three defect types in FSW"; Arbegast 2008), não de Aldanondo.
