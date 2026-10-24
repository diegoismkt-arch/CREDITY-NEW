---
name: novela-flow
description: Cria mininovelas dramáticas em espanhol (estilo "Relatos que Enseñan") para Facebook, geradas no Google Flow em clipes de até 10 s com fala do começo ao fim. Gera história, roteiro em planos, prompts JSON no modelo da casa (Ingredients to Video, timeline, atuação, negative prompt), vídeos curtos (2–3 clipes) com CTA falado e textos do post. Use quando o usuário pedir novela, episódio, roteiro, vídeo curto/Reel, prompts do Flow ou "parte 2".
---

# Novela Flow

Produz novelas em espanhol da ESPANHA (castelhano, sotaque peninsular; público principal: Espanha. Projetos antigos em espanhol do México têm `"idioma": "mexico"` no roteiro.json) 100% no **Google Flow**, no formato das páginas de "relatos" que viralizam no Facebook. Por que viralizam e como as referências são feitas: `references/analise-referencias.md`. Identidade da página (nome, bio, CTA, medidas): `references/pagina.md`. **Linguagem de câmera (técnicas cinematográficas por momento da história): `references/cinematografia.md` — usar SEMPRE no campo `camera` de cada plano.**

## Regras de ouro (créditos do Flow)

1. **Clipe de até 10 s com fala do primeiro ao último segundo.** Clipe vazio = crédito jogado fora. O script recusa clipe com menos de 80% de fala, com mais de 1,6 s de planos mudos ou que TERMINE num plano mudo. (Feedback do usuário em La camarera: os closes mudos de reação/"susto" no fim de cada clipe foram todos cortados na edição e 9 clipes de 90 s viraram 60 s.) O último plano é SEMPRE uma fala; o script segura 0,4 s depois dela dentro do mesmo plano para a palavra não ser cortada. Reação vai DENTRO do plano falado (o ouvinte reage enquanto o outro fala, ou o falante reage antes de falar), nunca num plano mudo separado.
2. **Um falante por plano, cortes secos dentro do clipe.** Cada clipe tem 2 a 4 planos; em cada plano só o rosto de quem fala aparece e só ele mexe a boca. A fala começa no primeiro instante do plano.
3. **Tempo da fala = palavras ÷ 2,7 s** (medido nas referências). O script calcula a timeline sozinho; nunca escrever os tempos à mão.
4. **Imagem de referência só quando precisa.** O **clipe 1 é Text to Video, sem imagem**: cria os personagens pela descrição (vai no campo `consistency`). Depois de gerar, **salvar os frames** dos personagens e do cenário (`salvar_frames`). Os clipes seguintes usam esses frames como referência (Ingredients to Video, `input_image`). Personagem que ainda não apareceu entra descrito por texto e tem o frame salvo no clipe em que aparece. Roupa e rosto FIXOS sempre. **Até 5 imagens de referência por clipe, UMA por personagem** (nunca duas imagens do mesmo personagem — escolher o frame mais recente e limpo) (personagens que aparecem + cenário + objeto-pista que está em cena).
   **Quem extrai os frames é o Claude** (pedido do usuário): quando o usuário manda o vídeo aprovado, extrair com ffmpeg os frames limpos (um personagem por imagem; recortar se houver outro rosto), conferir visualmente, salvar em `novelas/<projeto>/frames/FRAME_X.png`, fazer commit e SEMPRE ENVIAR os arquivos ao usuário pelo chat (SendUserFile) junto com o próximo clipe — o usuário NÃO tem acesso à pasta do repositório.
5. **Prompt em português, falas em espanhol.** Sem legenda, sem texto, sem música — texto ("Comenta PARTE 2 👇") entra na edição.
6. **Toda fala tem destinatário e todo clipe tem posições.** Cada plano falado leva `"para"` (com quem fala, ou `"CAMERA"` no CTA) e o clipe leva `"posicoes"` (onde cada um está no cenário). O script gera `addressee`, `eyeline` ("fala PARA X e olha para X, que está…; NÃO olha para Y") e `blocking`. **Nunca** escrever em `rosto`/`corpo` um olhar para outra pessoa que não o destinatário — no 1º teste a Valeria falou com o pai em vez do irmão porque o rosto dizia "olhar de cima para o pai".
7. **Nunca usar como referência um frame que tenha TEXTO escrito** (letreiro, legenda): o Flow copia o texto para o vídeo novo, mesmo com aviso no prompt. Trocar por outro frame limpo do mesmo personagem.
   **Frames de referência = o que o clipe REALMENTE mostra.** Nunca inventar frame "do quarto vazio" ou "do personagem sozinho". A descrição de cada frame diz de qual plano e de qual segundo ele sai e descreve a composição real daquele plano, incluindo quem mais aparece. Se o frame tiver alguém que não entra no próximo clipe, o prompt avisa que essa pessoa NÃO aparece e que o frame serve só para o rosto X e o cenário. Um frame pode servir para personagem + cenário ao mesmo tempo. Ao planejar o clipe 1, garantir que cada personagem que volta depois tenha um plano em que o rosto apareça bem. O usuário não manda o vídeo toda vez (gasta crédito): o pedido de frames sai do plano de planos, com o segundo exato.
8. **Continuidade dentro do clipe, com cortes.** Toda mudança de situação (alguém sai, alguém entra, alguém acorda) tem que ACONTECER na tela — nunca pular direto para o estado seguinte. Resolver DENTRO do mesmo clipe com cortes rápidos: falas curtas (1–3 s) e, para transições, um plano mudo de ~1 s (ex.: a enfermeira entrando). O vídeo curto tem **2 clipes**; não criar clipe extra sem o usuário pedir.
9. **Filtro do Flow:** nunca mostrar bebês, crianças ou berços, nem escrever "bebê/recém-nascido" no prompt — o Flow recusa ("conteúdo relacionado a menores"). Contar a história com adultos e objetos (ficha, foto de adultos, pulseira).
10. **Atuação forte, mas com contraste:** `ATUACAO_PRIORIDADE_MAXIMA` e os campos voice/face descrevem emoção clara (voz falhando, lágrimas, desprezo, choque). Nada neutro — mas nem todo mundo grita e chora o tempo todo: contenção (voz baixa, olhar firme, silêncio de 1 s) também é emoção e faz o pico pesar mais.

## Decupagem da conversa (cobertura de câmera) — OBRIGATÓRIO
Erro do clipe 4 de El Anillo: closes "sozinhos no quadro" em todo plano deixam cada um falando para o nada — o público não vê com quem a pessoa fala, não há troca de câmera de verdade nem reação.
1. **Plano/contraplano com Over-the-Shoulder (OTS):** fala dirigida a alguém = OTS por cima do ombro do OUVINTE (ombro/nuca desfocados em primeiro plano, rosto do falante nítido). O próximo falante ganha o OTS invertido. Assim cada fala mostra para quem é.
2. **Direção de tela fixa (regra dos 180°):** definir no clipe quem fica à ESQUERDA e quem à DIREITA do quadro e manter: quem está à esquerda olha para a DIREITA do quadro e vice-versa. Escrever isso no `eyeline` ("olha para a DIREITA do quadro, para X").
3. **Close de reação:** depois da fala mais forte do clipe, ~0,8 s no rosto de quem OUVIU (boca fechada). Pelo menos 1 por clipe quando couber.
4. **Variar o tamanho:** abrir com plano médio/dois personagens (situa o espaço), depois OTS, depois close no pico. Nunca 4 closes iguais seguidos.
5. **Duas pessoas do mesmo lado do balcão** (ex.: pai e filho): para um falar com o outro, plano de perfil dos dois (two-shot de perfil) ou OTS de um sobre o outro — nunca o falante olhando para a lente/frente.
6. **"SOZINHO no quadro"** só em close de reação ou de choque. Nos planos de fala usar OTS ou two-shot.

## Ritmo e emoção (erro do clipe 5 de El Anillo: 3,8 s sem fala e cena morna)
- **Nunca mais de ~1,5 s seguidos sem fala.** Nunca dois planos mudos em sequência. Insert de leitura: 1,5–2 s (2,5 s só se for celular/documento com muita coisa para ver).
- **O 1º plano do clipe já tem fala + ação.** Fala dita por alguém de COSTAS ou andando para longe o Flow costuma pular — quem fala no 1º plano está de frente/perfil para a câmera.
- **Emoção alta = reação física + voz quebrando:** mão na boca, soluço, passo para trás, segurar o braço do outro, voz que falha ou sobe. Escrever isso em `voz`/`rosto`/`corpo`, não só "emocionado".
- **Feche o clipe na reação de quem tem mais a perder** (o vilão empalidecendo, a vítima desabando), não no rosto de quem acabou de falar calmo.
- **Frames de referência com letreiro/neon com letras também contaminam** (igual ao letreiro de nome): preferir frames sem texto no fundo.

## Construção da história (incorporado do "Prompt Mestre", v2)
1. **Vínculo com o protagonista nas primeiras 2–3 cenas:** logo depois do gancho, mostrar um gesto concreto de dignidade, cuidado, lealdade ou sacrifício (ex.: ela ajuda alguém mesmo humilhada, protege um objeto, não revida). O público precisa TORCER por ele, não só sentir pena.
2. **Virada preparada:** planejar o final ANTES do clipe 1. Toda revelação tem 1–2 pistas discretas já mostradas antes; a solução nasce de ações, objetos ou relações estabelecidas — nunca de segredo inventado no último segundo nem de salvador aleatório.
3. **Cada clipe avança a trama:** uma decisão, consequência, descoberta ou obstáculo por clipe. Proibido repetir a mesma humilhação com frases diferentes.
4. **Antagonista com motivo reconhecível** (medo de perder a herança, ciúme, orgulho), não vilão vazio. Protagonista com vontade própria, que participa da solução.
5. **Continuidade escrita no roteiro:** para cada clipe, registrar quem segura o quê, em qual mão, onde cada um está, roupa e luz. Objetos não surgem nem somem; troca de lugar ou roupa só com ação na tela.
6. **2 a 4 personagens principais.** Não repetir a combinação de conflito + profissão + cenário + final das últimas histórias (ver `novelas/`).
7. **Fechamento:** história fechada paga a expectativa da abertura e termina numa consequência emocional visível; série termina em suspense com resolução plausível já planejada. CTA ("Comenta PARTE 2 👇") só depois do ápice, uma vez.
8. **Checagem antes de entregar cada clipe:** o gancho se entende sem contexto? O público sabe o que está em jogo? A virada foi preparada? Rostos, roupas, posições, mãos e objetos batem com o clipe anterior?

## Estilo VIRAL (aprendido com o vídeo de 2 milhões de views — prioridade)
- **Falas curtas:** 1 a 6 palavras por fala, 4 a 6 falas por clipe, em pingue-pongue (pergunta curta → resposta curta). Evitar fala longa de 10+ palavras, exceto na revelação.
- **1º segundo = ação física**, não fala: agarrar o braço, mão levantada, empurrão, objeto caindo. Agressão (tapa) vem ANTES de qualquer fala, num plano mudo próprio (~1,6 s, slow motion no impacto) com MUITOS efeitos sonoros: passos, whoosh, estalo alto com eco, boom grave, zumbido de ouvido, batida de coração (pedido do usuário: "isso chama atenção").
- **Ninguém fala parado:** cada plano tem uma ação de corpo (agarrar, puxar, abrir, mostrar, recuar).
- **Objeto-pista a cada ~10 s** em INSERT de mão/objeto (medalhão, chave, celular com vídeo, documento, assinatura, bolsa). Insert de objeto simples (anel caindo, chave na mão): ~1 s. **Insert de algo que o público precisa LER ou ASSISTIR (tela de celular, documento, foto, assinatura): mínimo 2,5 s**, com Slow Zoom In até a tela/papel ocupar o quadro.
- **Cadeia de revelações:** cada resposta abre nova pergunta; nunca resolver. Terminar numa frase-bomba curta ou numa revelação sem explicação. Final mais forte: uma VOZ fora do quadro grita "¡Fui yo!", todos se viram para a porta e NINGUÉM aparece (no plano: `"quem": "VOZ (fora do quadro)"`, `"bocas"`, e tirar "voz sem rosto na tela" dos negativos). **A voz fora do quadro toca sobre um plano SEM NENHUM ROSTO (porta escura, corredor vazio)** — no teste, com o grupo na tela durante o grito, o Flow pôs a boca da Victoria gritando; e com a porta abrindo, apareceu um vulto. Porta IMÓVEL, corredor preto; versão preferida do usuário: os personagens num ÚNICO plano de grupo SEM CORTE, de perfil; a pergunta, o grito fora do quadro (vindo de onde está a câmera) e todos VIRAM O ROSTO para a lente, bocas fechadas. **A frase-bomba tem que RESPONDER a uma pergunta feita logo antes** (ex.: "¿Quién mató a mi Rafael?" → "¡Fui yo!").
- **Plateia:** testemunhas reagindo; humilhação pública. 4–5 personagens ativos.
- **Trocar de cenário** no meio de um vídeo longo para dar sensação de investigação.
- **CTA falado é opcional:** se o gancho final for forte, terminar na última FALA-bomba (não num rosto mudo) e pôr o CTA só como texto na edição.
- A regra de ocupação de fala continua: falas curtas, mas MUITAS, mais inserts de ~1 s — o clipe nunca fica parado.

## Formatos

### Curto — 2 a 3 clipes (20–30 s) → fase de crescimento da página
O curto **não conta a história**: mostra **um único momento de choque e corta antes da resposta**.
- **1º frame já é a imagem absurda/injusta** (entendível sem som).
- **Segredo revelado pela metade** + **vilão que não sabe que foi descoberto**.
- **CTA falado no último plano do último clipe** (não gasta clipe extra): close no último personagem que fala, ele olha DIRETO para a lente e diz *"Si quieres saber qué va a pasar, comenta parte dos."* No roteiro: `"olha_para_camera": true` nesse plano (o script tira "personagem olhando para a camera" do negative prompt e avisa no `mouths`).
- Texto na edição, no final: **Comenta PARTE 2 👇**.
- A Parte 2 continua do ponto exato e termina com novo gancho + CTA.

### Longo — 30 a 40 clipes (5–7 min) → monetização
1. Gancho já no conflito → 2. Humilhação crescente → 3. Tentação (dinheiro/luxo) → 4. Falsa derrota → 5. Virada com discurso de dignidade → 6. Final com "CONTINUARÁ..." + mistério **ou** moral explícita.
Um longo rende 3 a 5 curtos (cada um com um gancho diferente).

## Linguagem dos diálogos
- Frases curtas e emocionais; vilão sem nuance, humilde digno.
- Repetir o conflito nas falas ("simple carpintero", "tres meses en coma").
- Respostas em pergunta: "¿Cómo que…?", "¿En serio…?".
- Vocabulário: *Dios, mi niña, hija, padrecito, lárguese, descarada, mi dignidad no tiene precio*.
- Temas: rico × pobre, profissão humilde, filhos ingratos, herança, abandono, segredo de família, milionário disfarçado.
- **Histórias sempre originais** — usar a fórmula, nunca copiar história de outra página.

## Fluxo de trabalho

> **UM CLIPE POR VEZ.** Entregar só o prompt do próximo clipe. O seguinte só depois que o usuário disser que o anterior saiu bom e tiver salvo os frames. Se ele mandar o vídeo gerado, analisar (frames, cortes, transcrição) antes de seguir; se saiu errado, corrigir o prompt desse mesmo clipe. Nunca adiantar clipes ou partes seguintes. Prompts sempre colados no chat, nunca como arquivo.

1. Ideia em 1 frase + personagens + cenários.
2. Escrever `novelas/<slug>/roteiro.json` (formato abaixo).
3. Rodar:
   ```bash
   python3 .claude/skills/novela-flow/scripts/montar_prompts.py novelas/<slug>/roteiro.json
   ```
   Gera `clipe_01.json`, `clipe_02.json`… (cada um é o prompt para colar no Flow) e `prompts.md` com tudo junto + lista de imagens de referência. Corrigir todo ❌ (passou de 10 s → cortar palavras; pouca fala → acrescentar fala) e rodar de novo.
4. Entregar: imagens de referência a gerar, os JSON dos clipes, título, legenda e texto da edição.

## Formato do `roteiro.json`

```json
{
  "titulo_post": "Título do post em espanhol",
  "legenda": "Legenda com pergunta + Comenta PARTE 2 👇",
  "texto_final": "Comenta PARTE 2 👇",
  "titulo_interno": "NOME DA CENA",
  "estilo": "Novela dramatica de luxo. Fotografia cinematografica hiper-realista... luz...",
  "imagens": { "FRAME_DON": "frame salvo do clipe 1: DON deitado, rosto bem visivel", "FRAME_QUARTO": "..." },
  "personagens": {
    "DON": {
      "descricao": "senhor de 75 anos, cabelo grisalho..., roupa FIXA.",
      "voz": "Voz grave e rouca de homem de 75 anos.",
      "frame": "FRAME_DON"
    }
  },
  "clips": [
    {
      "nome": "Nome curto do clipe",
      "atuacao": "texto do ATUACAO_PRIORIDADE_MAXIMA",
      "imagens": ["FRAME_QUARTO", "FRAME_DON"],
      "salvar_frames": ["FRAME_..."],
      "personagens": ["DON"],
      "posicoes": { "DON": "deitado na cama", "VALERIA": "em pe do lado ESQUERDO da cama" },
      "preservar_extra": ["O mesmo quarto da imagem FRAME_QUARTO."],
      "cenario": "setting do clipe",
      "estilo": "(opcional) estilo/luz próprio deste clipe, quando muda de cenário",
      "som": "sons ambiente",
      "negativos_extra": ["coisas proibidas só neste clipe"],
      "remover_negativos": ["item da lista padrão que não vale neste clipe"],
      "regras_extra": ["regra de diálogo extra"],
      "planos": [
        {
          "quem": "DON", "para": "VALERIA", "fala": "Frase em espanhol.", "emocao": 10,
          "intencao": "...", "voz": "...", "rosto": "...", "corpo": "...",
          "camera": "Close-Up de DON SOZINHO no quadro, lente 85mm...",
          "olha_para_camera": false
        },
        { "rosto": "plano mudo de reação", "corpo": "...", "camera": "Corte seco...", "segundos": 0.8 }
        (plano COM fala tambem aceita "segundos": vira a duracao MINIMA do plano — use quando a acao, ex. levantar da cadeira, precisa de mais tempo que a fala)
      ]
    }
  ]
}
```

- `imagens` vazio/ausente = clipe sem referência (Text to Video). Com `imagens`, o personagem cujo `frame` está na lista vira "O MESMO da imagem N"; os demais são descritos por texto.
- `frames` (por clipe, opcional): `{"VICTORIA": "FRAME_VICTORIA_PAPEL"}` troca o frame de referência do personagem só naquele clipe (quando um frame mais novo mostra melhor o rosto).
- `descricoes` (por clipe, opcional): troca a descrição do personagem só naquele clipe (ex.: perdeu a bolsa, rasgou o vestido).
- Quando o clipe CONTINUA a ação do último plano do anterior (alguém sentado se levanta etc.): se TODOS os personagens do clipe estão nesse último frame, usar `primeiro_frame: true` (Frames to Video). Se algum personagem que aparece no clipe NÃO está no frame (Frames to Video não aceita outras referências e o rosto dele se perde), usar Ingredients com o último frame como imagem 1 + os frames dos outros, e escrever no plano 1 que o vídeo ABRE na mesma composição da imagem 1, com a ação continuando dali.
- `primeiro_frame: true` (por clipe): a imagem 1 vira o PRIMEIRO FRAME do vídeo (Frames to Video), para continuar exatamente de um frame bom de um clipe que errou depois.
- `sem_fala: true` (por clipe): libera a regra de 65% de fala — só quando o usuário pedir um clipe mudo (ex.: reação final; a fala entra na edição, tirada de outro clipe).
- `estrutura` (por clipe): troca o texto do campo `structure` (ex.: plano único contínuo sem corte).
- `bocas` (por plano, opcional): troca o texto padrão do campo `mouths` (ex.: voz fora do quadro).
- Nos textos, citar imagens pelo NOME (`imagem FRAME_DON`); o script troca pelo número certo de cada clipe ("imagem 2").
- Plano sem `fala` = plano mudo: só insert de objeto-pista (~1 s) ou o tapa/ação de abertura (marcar `"acao_abertura": true`). NUNCA no fim do clipe.
- O negative prompt padrão (tela dividida, legendas, fala repetida, dois rostos nos planos de fala, etc.) já vem no script.

## Público: ESPANHA (desde a historia11)
- Campo `"idioma"` no roteiro.json: `"espanha"` (padrão) ou `"mexico"` (projetos antigos).
- Falas em castelhano: "camarera" (não mesera), "ladrona" (não ratera), "vosotros/os", "coger", "vale", "¿qué coño…?" (evitar palavrões fortes), "mamá" ok.
- Nomes e cenários espanhóis: Pilar, Carmen, Lucía, Álvaro, Javier, Mercedes; fincas/cortijos andaluzes, pisos em Madrid, cafeterias, chiringuitos, bodas e "pedidas de mano".
- Rostos: espanhóis comuns (pele clara/morena mediterrânea).

## Câmera de cinema SEMPRE (pedido do usuário)
Todo clipe usa pelo menos 3 técnicas DIFERENTES de `references/cinematografia.md`, escritas pelo nome no campo `camera` (Low Angle no vilão, High Angle na vítima, Insert + Rack Focus no objeto-pista, Crash Zoom In em choque/tapa, Slow Dolly In em tensão, Extreme Close-Up nos olhos em reação, Dutch Angle no segredo, Dolly Zoom 1x por vídeo na revelação máxima). Não repetir "Close-up SOLO" em todos os planos: o "SOLO" (só quem fala no quadro) continua obrigatório, mas o enquadramento e o movimento variam.

## Continuidade de espaço (pedido do usuário, desde La camarera clipe 4)
- Os personagens da cena ficam JUNTOS e PERTO (menos de 1 m), sempre nas MESMAS posições e com o MESMO fundo descrito em todos os planos do clipe e dos clipes seguintes.
- (ATUALIZADO) Nada de plano mudo de abertura nem de close mudo final: o clipe já ABRE com fala (num Two/Three Shot ou OTS que mostre todos juntos) e TERMINA com fala. A continuidade vem das posições fixas e do mesmo fundo.
- Nas falas: OVER-THE-SHOULDER fechado — ombro/nuca do ouvinte DESFOCADO em primeiro plano, de COSTAS, sem rosto e sem boca visíveis; quem fala nítido em close. Isso mantém a continuidade sem reabrir o problema de troca de voz (só uma boca visível por plano).
- (pedido do usuário) O clipe SEGUINTE pode usar o ÚLTIMO FRAME do anterior como primeiro frame (`primeiro_frame: true`, imagem `FRAME_FIM<n>`, Frames to Video) — esse frame agora é o fim de uma fala, não um close mudo. Só usar Ingredients se entrar personagem que não está nesse frame.
- (pedido do usuário) Os personagens se mexem em todos os planos (avançam, recuam, viram, gesticulam enquanto falam); nada de estátua. O último plano (falado) muda de ângulo em relação ao primeiro frame.

## Prompt Mestre (padrão consolidado)
O fluxo completo, o cardápio de ganchos (VARIAR a cada história; o tapa não é padrão), as regras de fala até o fim e o checklist de entrega estão em `references/prompt-mestre.md` (cópia em PDF para o usuário em `prompts/Prompt_Mestre_Novelas_Espanha.pdf`). Seguir esse documento em toda nova história.

## Fluxo sem mandar vídeo (pedido do usuário: mandar vídeo gasta muitos créditos)
- O usuário NÃO manda mais o vídeo. Ele responde "passou" ou descreve o erro em texto; quando precisar, manda só um PRINT (frame) tirado por ele.
- Continuidade: o usuário usa o próprio Flow — "Estender/Extend" no Scenebuilder (continua do último frame) ou print do último quadro em Frames to Video.
- Referência de rosto: o usuário tira print do rosto de cada personagem no player do Flow e sobe em Ingredients. Claude diz NO TEXTO qual print tirar (personagem, plano, segundo aproximado) e em que ordem subir.
- Claude só analisa vídeo se o usuário pedir explicitamente.

## Cenas dentro de CARRO (lição de El taxista)
- O motorista está DIRIGINDO: sempre de frente para o para-brisa, mãos no volante; NUNCA virado para trás. Só os olhos procuram o passageiro pelo RETROVISOR.
- NÃO usar Over-the-Shoulder pela nuca do motorista para filmar o banco de trás (o Flow vira o motorista de costas). Para o passageiro: câmera no lugar do passageiro da frente apontada para trás, com só o encosto de cabeça na borda; ou pelo retrovisor. Para o motorista: perfil (do banco do passageiro) ou frontal pelo para-brisa.
- Nada de travar portas / passageiro preso / medo de ser levado: o Flow recusa como conteúdo prejudicial.
- NUNCA descrever criança (idade, "menina") em cena de dor, culpa ou crime: o Flow recusa como "prejudicial a menores". Foto de filho(a) falecido(a) = jovem adulto(a) 18+ ou sem foto.
