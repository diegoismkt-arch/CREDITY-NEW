# Análise das referências — página "Relatos que Enseñan"

Página do Facebook com ~12 milhões de seguidores (facebook.com/Relatosqueensenan). Dois vídeos longos analisados (frames, cortes e transcrição completa).

| | Vídeo 1 — "La patrona y la lavandera" | Vídeo 2 — "El vendedor de empanadas" |
|---|---|---|
| Duração | 7min19 | 6min09 |
| Cortes detectados | ~236 | ~342 |
| Duração média de plano | 1,6 s | 1,3 s |
| Final | Mistério + "CONTINUARÁ..." | Moral explícita |

## Produção
- 100% IA (estilo Veo/Flow), personagens falando com sincronia labial, **sem narrador**.
- 9:16, luz quente, cenários de novela mexicana (lavanderia, obra, rua de bairro, casa simples).
- Cada personagem usa **a mesma roupa do começo ao fim** (consistência).
- Sem legenda, sem texto na tela, exceto "CONTINUARÁ..." no fim.

## Diálogos
- Uma fala curta por plano, 2–4 s; os planos são muito curtos (cortes a cada ~1,5 s).
- Conflito repetido o tempo todo ("simple lavandera", "vendedor de empanadas", "20 años").
- "¿Cómo que…?" usado dezenas de vezes como resposta.
- Vilã rica e arrogante, humilde digno, coro de amigas fofoqueiras.
- Nome "Camila" reaparece nos dois vídeos (moldes reutilizados).

## Estrutura
1. Gancho imediato (já na humilhação).
2. Humilhação crescente.
3. Tentação com dinheiro (apartamento, Cancún, "vas a vivir como una reina").
4. Falsa derrota ("quizás merece algo mejor", "ándate, mi niña").
5. Virada com discurso ("esas empanadas pagaron cada libro de mi escuela").
6. Cliffhanger ("hay algo sobre mí que nunca te he contado") ou moral ("padre es el que se queda").

## Efeito no espectador
Raiva da vilã (retenção até o fim) → identificação (público latino 35–65) → catarse/justiça → comentários tomando partido → compartilhamento da moral → seguir a página pela "Parte 2".

## Vídeos curtos (referências de 10–16 s)

**Curto A (16 s): "¿De dónde salió ese teléfono?"**
- Frame 1: menina de vestido azul esfregando o chão de mármole da mansão; madrasta de preto, sentada, com taça de vinho; o pai entra.
- O pai se ajoelha: "Mírame, ¿por qué estás llorando?". A menina chora sem responder.
- Close: a mão do pai encontra um **celular escondido no laço do vestido** da menina.
- Corte para o rosto da madrasta em **choque**, boca aberta. Fim: pai olhando o celular, madrasta com a mão na boca. **Não mostra o que tem no celular.**
- Quase sem fala: o visual conta tudo. 4 cortes em 16 s.

**Curto B (10,5 s): "¡Está viva!"**
- Frame 1: médico legista com bisturi sobre uma mulher na mesa do necrotério.
- Ela abre os olhos. Ele grita. Ela: "¡No diga nada! El hombre que me envenenó está detrás de esa puerta".
- Entra o vilão de terno vermelho, sorrindo: "Doctor, ¿ya puede firmar la cremación?". **Fim.**
- 5 falas em 10 s, muito denso (combina com a regra de clipe cheio de fala).

### Por que os curtos viralizam
1. **Imagem-choque no 1º segundo**, que se entende sem som (o feed do Facebook começa mudo).
2. **Injustiça contra vítima indefesa** (criança, mulher envenenada) → raiva imediata.
3. **Segredo revelado pela metade** (celular, "sei quem me envenenou") → curiosidade.
4. **O vilão não sabe que foi descoberto** → o espectador sabe mais que o vilão (ironia dramática) e quer ver ele cair.
5. **Corta no ápice, sem resolução** → comentários ("¿qué había en el teléfono?", "parte 2!!"), reassistir (loop) e seguir a página.
6. **Duração de 10–16 s** → alta taxa de conclusão e de replay, que é o principal sinal do algoritmo de Reels.
7. Personagens com **cara de novela de TV** (Televisa/Telemundo) → parece novela "real", o que gera confiança.

## Diferença para a nossa produção
No Flow cada geração custa créditos, então **cada clipe de 10 s precisa estar cheio de fala**. Os cortes rápidos das referências são feitos DENTRO do clipe: 2 a 4 planos com cortes secos, um falante por plano (modelo de prompt JSON da casa).

## Aprendizados dos testes no Flow
- **Teste 1 (Parte 1, clipe 1):** a timeline calculada bateu — cortes gerados em 3,7 s e 7,0 s (previsto 3,9 s e 7,1 s), falas completas, roupas consistentes. Erro: a personagem falou olhando para o pai em vez do irmão, porque o campo `face` mandava olhar para o pai. Correção: campos `para`/`posicoes` obrigatórios (eyeline + blocking).
- **Teste 2 (Parte 1, clipe 1 refeito):** com `para`/`posicoes`, cada um falou com a pessoa certa; cortes em 3,9 s e 7,0 s. Aprendizado: não existe "frame do quarto sozinho" nem "do Don sozinho" — o plano 1 mostra Don deitado + Valeria ao fundo + quarto. Os frames pedidos têm que sair dos planos planejados (com o segundo exato) e a descrição tem que bater com a composição real.
- **Teste 3 (Parte 1, clipe 2):** reprovado. O clipe já começava com Don de olhos abertos: faltou mostrar os filhos saindo, a enfermeira entrando e ele acordando devagar. Correção: regra de continuidade — cada mudança de situação acontece na tela; dividido em clipe 2 (saída + entrada) e clipe 3 (acorda + CTA).
- **Decisão do usuário:** curto = 2 clipes. Transições (saída/entrada/acordar) cabem no mesmo clipe de 10 s com 4–5 cortes e um plano mudo de ~1 s.

## Curto C (11 s, 1 clipe): "Cierra todas las salidas"
- P1 (0–1,7 s): mulher de vestido dourado, close de perfil, celular no ouvido, sussurra a ordem ("Papá, cierra todas las salidas").
- P2 (1,7–3,4 s): vilão de smoking branco caminha sorridente pela festa de gala.
- P3 (3,4–3,8 s): insert rapidíssimo do olho dela.
- P4 (3,8–~5 s): plano aberto simétrico das grandes portas do salão se fechando, seguranças.
- P5 (~5–7,7 s): vilão vira para trás, o sorriso some — percebe a armadilha.
- P6 (7,7–11 s): ela cara a cara com ele, fria: "Esas puertas no fueron construidas para mantener el peligro afuera… sino para que hombres como tú no salgan."
- Mecânica: armadilha preparada em segredo → vilão confiante → a porta fecha (imagem forte, sem fala) → percepção → frase de efeito da heroína. Inverte o poder em 11 s.

## Curto D (20 s, 2 clipes): "Papá, mamá está sentada allí"
- Clipe 1: pai e filho andando à noite numa rua; o menino aponta: "Papá, mamá está sentada allí." Pai, com dor: "No, querido, tu madre ya no está." O menino solta a mão e corre até uma mulher sem-teto sentada na calçada e a abraça. Ela, chorando: "Mi hijo más querido."
- Clipe 2: o pai, em choque: "Sofía, pero yo te enterré." Ela: "Entonces te has equivocado de persona." O pai se ajoelha e abraça os dois: "Nunca más te dejaré ir."
- Mecânica: criança reconhece quem o adulto acha que morreu → adulto nega → corrida + abraço (imagem forte) → adulto reconhece → reencontro (catarse). Emoção de lágrima, não de raiva. 6 cortes, ~3 s cada.

## Curto E — VIRAL (2 milhões de views, muitos pedidos de Parte 2): "La heredera" (90 s, 41 cortes)
**História:** casamento de luxo num pátio colonial. A noiva (vilã, vestido de cetim) agride a empregada idosa ("¡Suéltame!" / "Baja la mano"). Cai um medalhão do pescoço da empregada. O mordomo idoso abre: foto antiga do casal → "¿De quién era eso?" "De mi esposo." "¿Cómo se llamaba?" "Arturo Salcedo." → a empregada é a viúva verdadeira → "Entonces tú no eres la heredera." A matriarca de vinho entra na briga ("Está vieja está mintiendo" / "No vuelvas a tocarla" / "Yo soy la dueña" / "Enséñame los papeles"). Chave antiga: "Llevas cerrado 28 años. Anoche alguien entró." Vídeo no celular mostra a invasão. Puxa-puxa da pasta, agarrar pulso. Corte para o escritório trancado: gaveta vazia, foto de casamento, "aquí estaba el testamento". "Enséñame tu bolso." Dentro: a última página do testamento. Elas começam a ler e uma voz GRITA de fora do quadro: "Fui yo." Todos olham para a porta e ninguém aparece; ninguém sabe quem é. FIM (sem CTA falado). (Correção do usuário: não tem cena de assinatura; quem confessa não aparece.)

**O que é diferente do que estávamos fazendo:**
1. **Falas MUITO curtas (1–6 palavras), muitas por clipe** — pingue-pongue rápido (pergunta → resposta de 2 palavras). Nós fazíamos 3 falas longas por clipe.
2. **Começa na AGRESSÃO FÍSICA, não numa fala** — mão levantada, braço agarrado no 1º segundo.
3. **Ação física o tempo todo:** tapa, pisar na mão, agarrar pulso, arrancar pasta, revirar bolsa, abrir porta. Ninguém fica parado falando.
4. **Objetos-pista em insert a cada ~10 s:** medalhão com foto, chave antiga, vídeo no celular, pasta, gaveta vazia, foto de casamento, envelope, bolsa, página do testamento. ~25% dos planos são INSERTS de mãos/objetos (sem rosto).
5. **Cadeia de revelações:** cada resposta abre outra pergunta (quem é o marido → ela é a herdeira → quem entrou no escritório → onde está o testamento → quem foi?). Nunca resolve. Termina numa CONFISSÃO gritada por uma voz fora do quadro ("Fui yo"): todos olham, ninguém aparece.
6. **Plateia/testemunhas:** convidados olhando, 5 personagens ativos, todos reagem. A humilhação é pública.
7. **Muda de cenário no meio** (pátio → corredor → escritório trancado): sensação de "investigação" avançando.
8. **Sem CTA falado:** o cliffhanger sozinho gera os pedidos de Parte 2.
9. **Close extremo de olhos/rosto na reação** e **planos de 1–2 s**.

**Por que viralizou:** injustiça física contra idosa humilde (raiva) + Cinderela invertida (a empregada é a dona) + mistério de detetive com pistas visíveis + escalada a cada 10 s + final com confissão sem explicação → pessoa assiste até o fim, reassiste para entender as pistas e comenta teorias e "parte 2".

- **La Enfermera, clipe 1:** falas, ordem, tapa e insert da pulseira saíram certos. Erro: o Flow escreveu "CAMILA / 30 y- Camila" na tela, no close da Camila (letreiro de apresentação inventado a partir da ficha com nome + idade); o crachá da Rosa saiu com "ROSA". Correção: negativos fixos contra nome/idade escritos e letreiro de apresentação.
- **La Enfermera, clipe 4 (reprovado):** a Camila trocou o vestido azul por um bege de alcinha (frame de referência fraco para a roupa); o close final de 'olhos da Camila' saiu com a Isabel (Extreme Close-Up nos olhos sem rosto inteiro confunde quem é); áudio embolado e '¡Mientes!' repetido. Correção: frame com a roupa bem visível, último plano = close de rosto inteiro com cabelo/roupa descritos, negativo 'X no último plano', regra 'fala dita uma única vez' para falas de 1 palavra; 5 referências com personagem só de fundo atrapalham — usar só quem aparece.
- **La Enfermera, clipe 4 (2ª versão):** áudio e falas certos, Camila de azul, close final certo. Erros: o letreiro "CAMILA… 30 Year" voltou (veio da imagem de referência que tinha texto) e no '¡Mientes!' a Isabel apareceu com o vestido azul da Camila. Regra: frame com texto nunca vira referência; negativo 'roupa de uma personagem em outra'.
- **El Anillo, clipe 4 (Frames to Video):** a continuidade com o clipe 3 funcionou (começou no Ramiro sentado). Erros: closes isolados sem relação espacial (Esteban falava com o pai olhando para frente), nenhuma reação, e o rosto do Esteban ficou grisalho no último close (misturou com o Ramiro). Correção: decupagem OTS/plano-contraplano, direção de tela fixa, two-shot de perfil para quem está do mesmo lado, negativo 'esteban com barba grisalha'.
- **El Anillo, clipe 4 (Ingredients + último frame como imagem 1):** FUNCIONOU — abriu com o Ramiro sentado, OTS e contraplano mostrando com quem cada um fala, close de reação, two-shot de perfil no sussurro. Detalhes: neon com letras ao fundo (por isso o estilo agora diz 'neon sem letras'), camiseta do Esteban saiu preta.
- **El Anillo, clipe 5 (reprovado):** 3,8 s sem fala no começo (a fala do Esteban, dita enquanto o Ramiro andava de costas, sumiu + insert de 2,5 s), falas calmas, neon com letras (copiado do frame de referência). Correção: regra de no máx ~1,5 s mudo, 1º plano com fala de frente, emoção física na voz/corpo, fechar na reação do vilão, frames sem letreiro.

## Referência "El Príncipe y la Fiona" (86 s, enviada pelo usuário)
Estrutura: conto de fadas (Cinderela) + justiça física. Anúncio do príncipe → ela, chorando, esbarra e mancha
de vinho o smoking BRANCO dele (a mancha vira marca visual até o fim) → "¿Sabes quién soy?" "No, y no quiero
saberlo." → "Entonces eres tú… la mujer que estaba buscando" → ele seca as lágrimas dela (close com toque)
→ "¿Por qué llora?" "Me dijo que era fea." "Entonces está ciego. Dime quién es." → o valentão se apresenta
("Fui yo") e repete a ofensa com humor cruel → "Dilo otra vez, pero mírame a mí" → briga coreografada na pista,
plateia em volta → "Eso es para que respetes a las damas" → sino da meia-noite, ela foge → ele corre atrás,
ela entra num carro → ele acha a bolsa dela com documento → "Ahora sé dónde encontrarte."
O que funciona: arquétipo conhecido (o público entende sem explicação), romance + vingança no mesmo vídeo,
herói que defende sem ser pedido, toque carinhoso em close, mancha/objeto como continuidade visual,
plateia, perseguição + objeto perdido, final que PROMETE continuação (não CTA falado). Falas curtíssimas,
muitos closes alternados com OTS, choro intenso dela.

## Recusa do Flow: "pessoas famosas" (La Costurera, clipe 1)
Descrições glamourosas e genéricas (loira platinada, coque alto, vestido prata, diamantes, "muito bonita")
fizeram o Flow recusar por parecer celebridade. Correção: rosto comum com traços marcantes e imperfeitos
(sardas, pinta, nariz largo, sobrancelhas grossas, queixo pontudo), cabelo menos "de tapete vermelho",
"pessoas desconhecidas, rostos com imperfeições reais" no estilo. NÃO escrever "celebridade/famoso" nem no negativo (o filtro lê as palavras).

## Perseguição (La Costurera, clipe 7)
Com "VALERIA descendo e MATEO descendo atrás dela", o Flow pôs os dois correndo JUNTOS. Em fuga/perseguição:
quem fugiu já está LONGE (no fim do caminho) quando o outro aparece; nunca os dois no mesmo plano, exceto um
Wide Shot que mostre a DISTÂNCIA; cada um "SOZINHO no quadro"; negativos "os dois correndo juntos", "X alcançando Y".

## Voz de telefone (La Costurera, cena do carro)
Voz saindo do celular sobre plano sem boca: o Flow falhou 2x (fala incompleta / voz não saiu). Para ligação
curta, MOSTRAR quem fala do outro lado (rosto na sombra, só a boca num fio de luz) — com boca visível o Flow
gera a fala. E trocar roupa/cabelo de um personagem (óculos, cabelo solto) fez o rosto não bater com o baile:
manter penteado e acessório-marca (coque ruivo, colar) quando mudar a roupa.

## Referência "¿Papá?" (15 s, enviada pelo usuário)
Mansão à noite. A avó rica expulsa uma mulher pobre e a menina: "Váyanse antes de que alguien las vea." O dono
entra com seguranças → a menina: "¿Papá?" → "La abuela dijo que estabas muerto." → a mãe: "Me dijo que habías
muerto… y que el dinero dejó de llegar." → avó: "Andrés, esto no es lo que parece." → ele: "Abre la caja fuerte."
"No." → INSERT do cofre com pastas/documentos (a prova) → "Tres años… robando el dinero que les enviaba." → ele
se ajoelha ao lado da filha → "¡Que nadie se vaya!" (fim seco, sem resolução).
O que funciona: segredo de família revelado em 2 s por uma palavra ("¿Papá?"); vilã da própria família com motivo
(dinheiro); prova física num insert (cofre); herói muda de lado no meio do vídeo; plateia de seguranças; ~10 falas
em 15 s, todas curtas; termina numa ORDEM que promete punição. Obs.: usa criança — no nosso Flow, evitar
(filtro); trocar por filha/filho adulto ou mãe idosa.

## Objeto que pula de personagem (Los Tamales, clipes 1 e 2)
Os OCULOS ESCUROS na cabeça da PAOLA apareceram na cabeça da DONA LUPE nos dois clipes, mesmo com negativo
"dona lupe de oculos". O negativo citando o objeto parece até reforçar. Regra: não dar acessório "solto"
(óculos na cabeça, chapéu, lenço) a um personagem quando outro está em close; se o objeto pular, TIRAR o objeto
da descrição de todo mundo em vez de proibir no negativo.
