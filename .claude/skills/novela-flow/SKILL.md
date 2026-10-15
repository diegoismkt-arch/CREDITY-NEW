---
name: novela-flow
description: Cria mininovelas dramáticas em espanhol (estilo "Relatos que Enseñan") para Facebook, geradas no Google Flow em clipes de até 10 s com fala do começo ao fim. Gera história, roteiro dividido em clipes, prompts prontos para colar no Flow, versão curta (2 clipes, 15–20 s) e textos do post. Use quando o usuário pedir novela, episódio, roteiro, vídeo curto/Reel, prompts do Flow ou "parte 2".
---

# Novela Flow

Produz episódios de novela em espanhol (sotaque mexicano) feitos 100% no **Google Flow**, no formato das páginas de "relatos" que crescem no Facebook. Base: análise de vídeos da página *Relatos que Enseñan* (ver `references/analise-referencias.md`).

## Regras de ouro do Flow (créditos)

1. **Cada clipe tem 10 s e fala do primeiro ao último segundo.** Clipe sem fala = crédito jogado fora.
   - Alvo: **22–28 palavras faladas por clipe** (espanhol dramático ≈ 2,7 palavras/s).
   - Mínimo 18 (abaixo disso o clipe fica vazio). Máximo 30 (acima disso a fala é cortada ou acelerada demais).
2. **No máximo 2 personagens falando por clipe** (3 bagunça a sincronia labial). Até 3 falas alternadas por clipe.
3. **A fala começa no primeiro segundo** — o prompt sempre pede "speech starts immediately, no silent pause".
4. **Personagem com descrição e roupa FIXAS**, copiadas palavra por palavra em todo prompt. É isso que mantém o rosto consistente. Se possível, gere antes uma imagem de referência de cada personagem e use como *ingrediente* no Flow.
5. **Visual em inglês, falas em espanhol entre aspas.** Sem legenda, sem texto, sem música no Flow — texto ("CONTINUARÁ...", "Parte 2") entra na edição.
6. Corte na edição: dentro de um clipe de 10 s dá para intercalar reações de outros clipes do mesmo cenário, mas **nunca gere clipe só de reação** — use as reações que já aparecem nos clipes falados.

## Formatos

### Curto — 1 a 2 clipes (10–20 s) → fase de crescimento da página
O curto **não conta a história**: ele mostra **um único momento de choque e corta antes da resposta**. Ver `references/analise-referencias.md` (curtos A e B).
- **Primeiro frame já é a imagem absurda/injusta** (criança esfregando o chão aos pés da madrasta com taça de vinho; mulher "morta" na mesa do necrotério abrindo os olhos). Quem rola o feed entende a situação sem som.
- **Clipe 1: situação + revelação.** Algo escondido aparece (celular escondido no laço do vestido; a "morta" está viva e sabe quem a envenenou).
- **Clipe 2: o vilão chega / é pego** — termina no **rosto de choque** ou na **fala do vilão que ainda não sabe** ("Doctor, ¿ya puede firmar la cremación?"). **Sem resolução.**
- Personagens arquetípicos reconhecíveis em 1 segundo pela roupa: vilã de preto com vinho, pai/herói de terno, vítima frágil (criança, mulher), vilão de terno vermelho.
- Termina com texto na edição: *"Parte 2 en mi página"*, *"¿Qué harías tú? 👇"*.
- A base é sempre uma história longa: o curto é o momento mais forte dela. Uma história longa rende **3 a 5 curtos**, cada um com um gancho diferente.

### Longo — 30 a 40 clipes (5–7 min) → monetização
Estrutura obrigatória:
1. **Gancho (clipe 1–2):** já começa no conflito ou plantando o conflito.
2. **Humilhação crescente:** vilão(ã) ataca pobreza/profissão do(a) humilde.
3. **Tentação:** vilão oferece dinheiro/luxo em troca de abandonar alguém.
4. **Falsa derrota:** o humilde quase cede ("acepta, yo no quiero ser un estorbo").
5. **Virada:** discurso emocional de dignidade ("mi dignidad no tiene precio").
6. **Final:** alternar entre
   - **cliffhanger + "CONTINUARÁ..."** (gera seguidores), plantando o mistério antes (objeto, nome, segredo);
   - **moral explícita** na última fala (gera compartilhamento).

## Linguagem dos diálogos
- Frases curtas, diretas, emocionais. Personagens caricatos: vilão sem nuance, humilde digno.
- **Repetir o conflito** nas falas (quem chega no meio entende): "simple carpintero", "20 años", "empleaducha".
- Respostas em pergunta: **"¿Cómo que…?"**, "¿En serio…?".
- Vocabulário: *Dios, mi niña, padrecito, lárguese, descarada, mi dignidad no tiene precio, ¿qué va a pensar la gente?*
- Temas que funcionam: rico × pobre, profissão humilde (lavandeira, pedreiro, vendedor de empanadas, carpinteiro, faxineira), abandono, sogra má, herança, milionário disfarçado, gratidão aos pais/avós.
- **Histórias sempre originais.** Usar a fórmula, nunca copiar história, nome ou cena de outra página.

## Fluxo de trabalho

1. Definir a premissa (1 frase), personagens (com descrição visual fixa e roupa) e cenários.
2. Escrever o episódio em `novelas/<slug>/episodio.json` (formato abaixo), com clipes longos em `clips` e os curtos em `shorts`.
3. Rodar o montador, que valida as palavras de cada clipe e gera os prompts prontos:
   ```bash
   python3 .claude/skills/novela-flow/scripts/montar_prompts.py novelas/<slug>/episodio.json
   ```
   Gera `novelas/<slug>/prompts.md`. Corrigir todo clipe marcado ❌ (curto/longo demais) e rodar de novo até não sobrar nenhum.
4. Entregar ao usuário: link/arquivo `prompts.md`, título, legenda e indicação de quais clipes viram curtos.

## Formato do `episodio.json`

```json
{
  "titulo": "Título do post em espanhol",
  "legenda": "Legenda do post com pergunta no final",
  "estilo": "Vertical 9:16, photorealistic Mexican telenovela look, warm natural light, shallow depth of field",
  "personagens": {
    "ERNESTO": "Don Ernesto, 72-year-old Mexican man, short white hair, ... (descrição + roupa fixa, em inglês)"
  },
  "cenarios": {
    "TALLER": "small humble carpentry workshop in a Mexican neighborhood, ..."
  },
  "clips": [
    {
      "cenario": "TALLER",
      "personagens": ["MARIANA", "ERNESTO"],
      "camera": "medium two-shot, slow push-in",
      "acao": "Mariana runs in excited showing a ring; Ernesto puts down his chisel",
      "falas": [["MARIANA", "excited", "¡Abuelito, ...!"], ["ERNESTO", "moved", "Ay, mi niña..."]]
    }
  ],
  "shorts": [
    {"nome": "Curto 1 — A humilhação", "clips": [8, 10], "texto_final": "¿Qué harías tú? 👇"}
  ],
  "texto_final": "CONTINUARÁ..."
}
```

`shorts[].clips` usa a numeração dos clipes do episódio (1 = primeiro). Um curto também pode ter clipes próprios em `shorts[].clips_novos` (mesmo formato de `clips`) quando precisar de fala exclusiva.
