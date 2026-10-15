---
name: novela-flow
description: Cria mininovelas dramáticas em espanhol (estilo "Relatos que Enseñan") para Facebook, geradas no Google Flow em clipes de até 10 s com fala do começo ao fim. Gera história, roteiro em planos, prompts JSON no modelo da casa (Ingredients to Video, timeline, atuação, negative prompt), vídeos curtos (2–3 clipes) com CTA falado e textos do post. Use quando o usuário pedir novela, episódio, roteiro, vídeo curto/Reel, prompts do Flow ou "parte 2".
---

# Novela Flow

Produz novelas em espanhol (sotaque mexicano) 100% no **Google Flow**, no formato das páginas de "relatos" que viralizam no Facebook. Por que viralizam e como as referências são feitas: `references/analise-referencias.md`.

## Regras de ouro (créditos do Flow)

1. **Clipe de até 10 s com fala do primeiro ao último segundo.** Clipe vazio = crédito jogado fora. O script recusa clipe com menos de 75% de fala.
2. **Um falante por plano, cortes secos dentro do clipe.** Cada clipe tem 2 a 4 planos; em cada plano só o rosto de quem fala aparece e só ele mexe a boca. A fala começa no primeiro instante do plano.
3. **Tempo da fala = palavras ÷ 2,7 s** (medido nas referências). O script calcula a timeline sozinho; nunca escrever os tempos à mão.
4. **Imagem de referência só quando precisa.** O **clipe 1 é Text to Video, sem imagem**: cria os personagens pela descrição (vai no campo `consistency`). Depois de gerar, **salvar os frames** dos personagens e do cenário (`salvar_frames`). Os clipes seguintes usam esses frames como referência (Ingredients to Video, `input_image`). Personagem que ainda não apareceu entra descrito por texto e tem o frame salvo no clipe em que aparece. Roupa e rosto FIXOS sempre.
5. **Prompt em português, falas em espanhol.** Sem legenda, sem texto, sem música — texto ("Comenta PARTE 2 👇") entra na edição.
6. **Toda fala tem destinatário e todo clipe tem posições.** Cada plano falado leva `"para"` (com quem fala, ou `"CAMERA"` no CTA) e o clipe leva `"posicoes"` (onde cada um está no cenário). O script gera `addressee`, `eyeline` ("fala PARA X e olha para X, que está…; NÃO olha para Y") e `blocking`. **Nunca** escrever em `rosto`/`corpo` um olhar para outra pessoa que não o destinatário — no 1º teste a Valeria falou com o pai em vez do irmão porque o rosto dizia "olhar de cima para o pai".
7. **Frames de referência = o que o clipe REALMENTE mostra.** Nunca inventar frame "do quarto vazio" ou "do personagem sozinho". A descrição de cada frame diz de qual plano e de qual segundo ele sai e descreve a composição real daquele plano, incluindo quem mais aparece. Se o frame tiver alguém que não entra no próximo clipe, o prompt avisa que essa pessoa NÃO aparece e que o frame serve só para o rosto X e o cenário. Um frame pode servir para personagem + cenário ao mesmo tempo. Ao planejar o clipe 1, garantir que cada personagem que volta depois tenha um plano em que o rosto apareça bem. O usuário não manda o vídeo toda vez (gasta crédito): o pedido de frames sai do plano de planos, com o segundo exato.
8. **Atuação no máximo:** `ATUACAO_PRIORIDADE_MAXIMA` e os campos voice/face de cada plano descrevem emoção forte (voz falhando, lágrimas, desprezo, choque). Nada neutro.

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
      ]
    }
  ]
}
```

- `imagens` vazio/ausente = clipe sem referência (Text to Video). Com `imagens`, o personagem cujo `frame` está na lista vira "O MESMO da imagem N"; os demais são descritos por texto.
- Nos textos, citar imagens pelo NOME (`imagem FRAME_DON`); o script troca pelo número certo de cada clipe ("imagem 2").
- Plano sem `fala` = plano mudo de reação (use pouco, no máximo ~0,8 s, só no fim).
- O negative prompt padrão (tela dividida, legendas, fala repetida, dois rostos nos planos de fala, etc.) já vem no script.
