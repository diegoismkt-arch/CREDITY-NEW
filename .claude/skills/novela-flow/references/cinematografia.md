# Guia cinematográfico para novela no Flow

Categorias da biblioteca Melies (melies.co/cinematic-techniques): movimento de câmera, iluminação, composição/enquadramento, lentes, edição, tempo e movimento. Abaixo, as técnicas que usamos e **em que momento da história** cada uma entra. No prompt, o campo `camera` de cada plano deve nomear a técnica em inglês (como o Flow entende) + lente.

## Mapa: momento da história → técnica

| Momento | Técnica (nome no prompt) | Efeito |
|---|---|---|
| Agressão / briga no 1º segundo | **Handheld** + **Whip Pan** para entrar na ação | caos, urgência, "câmera pegou no flagra" |
| Vilão humilhando | **Low Angle** + **Slow Push In**, lente 35–50mm | vilão grande, poderoso, ameaçador |
| Vítima humilhada | **High Angle** (câmera acima), Close-Up 85mm | vítima pequena, frágil |
| Tapa / golpe / objeto caindo | **Snap Zoom** ou **Crash Zoom** + **Slow Motion** curto | impacto |
| Objeto-pista (anel, chave, carta, celular) | **Insert** em **Extreme Close-Up**, lente **macro**, **Rack Focus** do objeto para o rosto | a pista "salta" da tela |
| Revelação / choque | **Dolly Zoom (Vertigo)** ou **Fast Push In** no rosto | mundo desaba |
| Reação de quem descobre | **Extreme Close-Up nos olhos** | emoção máxima, sem fala |
| Diálogo tenso entre dois | **Over-the-Shoulder (OTS)** alternado + **Shot/Reverse Shot** | conflito cara a cara |
| Clima de suspense / segredo | **Dutch Angle** (câmera inclinada) | algo está errado |
| Testemunhas / plateia | **Reaction Shot** de grupo, **Wide Shot** | humilhação pública |
| Entrar em lugar proibido (escritório, quarto) | **Steadicam / Tracking Shot** seguindo por trás, **POV** da porta abrindo | investigação |
| Final / cliffhanger | **Slow Push In** até **Extreme Close-Up** + corte seco (**Smash Cut to black** na edição) | gancho |
| CTA olhando para a câmera | **Breaking the Fourth Wall**, Extreme Close-Up, Slow Push In | conversa direta com o público |

## Edição (entre os planos)
- **Corte seco (Hard Cut)** padrão.
- **Smash Cut**: de um momento calmo direto para um choque (ou para o preto no final).
- **Match Cut**: mesmo objeto/forma ligando dois planos (anel na mão → anel na foto).
- **J-Cut**: o som do próximo plano começa um instante antes (bom para grito/porta batendo).

## Iluminação
- **Practical Lighting / Warm Amber**: festas, restaurantes, casas (velas, lustres, abajur).
- **Golden Hour**: externas de fim de tarde (haciendas, praças).
- **Low-Key / Chiaroscuro**: segredos, escritório trancado, confissão.
- **Cool Blue / Moonlight**: hospital, noite, tristeza.
- **Rim Light**: destacar o vilão no escuro.

## Lentes
- **35mm**: plano aberto/médio, ação, ambiente.
- **50mm**: plano médio, conversa.
- **85mm**: closes de rosto, fundo desfocado.
- **Macro**: objetos-pista.
- **Shallow Focus / Bokeh**: sempre nos closes.

## Regras de uso
1. Cada plano usa **uma técnica principal** nomeada no campo `camera` (não empilhar 4 movimentos num plano de 1 s).
2. Planos de 1 s: só **Insert**, **Snap Zoom** ou **Reaction Shot** (sem movimento longo).
3. Variar: nunca dois planos seguidos com o mesmo enquadramento e ângulo.
4. Vilão = Low Angle; vítima = High Angle; revelação = Push In/Dolly Zoom; pista = Insert macro + Rack Focus.
