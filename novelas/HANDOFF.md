# Passagem de sessão — La Historia Principal (nov/2026)

Página do Facebook com mininovelas de IA feitas no Google Flow (Veo), clipes de até 10 s.
Skill: `.claude/skills/novela-flow/` (SKILL.md + references/ + scripts/montar_prompts.py). Ler SKILL.md inteiro antes de criar.

## Fluxo de trabalho com o usuário
1. Opções de história → 2. roteiro (falas em ES com tradução PT) → 3. UM clipe por vez, JSON completo colado no chat
4. Usuário responde "passou" ou descreve o erro / manda o vídeo (checar via contact sheet com ffmpeg) → 5. "legenda" em blocos copiáveis.
Gerar: `cd novelas/<historia> && python3 ../../.claude/skills/novela-flow/scripts/montar_prompts.py roteiro.json`

## Decisões do usuário (atuais)
- Público ESPANHOL: castelhano da Espanha, âncoras culturais espanholas.
- Elenco com cara de ATORES de série espanhola (Elite, Velvet), não "gente comum" (saía com cara de brasileiro).
- Gancho no seg. 0 com 2+ pessoas no quadro; mistério = curiosidade, não sombrio.
- Histórias realmente NOVAS (não tropos já vistos na internet); cada história com formato diferente da anterior.
- 2 clipes por história. Criança: como quem DESCOBRE/AVISA, não vítima de violência.
- Formato viral "O AVISO" e análise das refs: `references/analise-referencias.md`.

## Em andamento
- `novelas/historia29-ave/` (El AVE, gêmeos separados no nascimento, 2 clipes). Clipe 1 já enviado ao usuário; aguardando "passou". Depois: clipe 2 e legenda.
- `novelas/historia28-piscina/` clipe 1 v3 enviado (formato antigo, usuário trocou para El AVE).

## Próxima tarefa
Analisar por que viralizam os Reels destas páginas (em espanhol), usando o navegador do usuário:
- https://www.facebook.com/Relatosqueensenan/reels/
- https://www.facebook.com/pv026hlfpv026hlf/reels/
Ver os mais vistos, assistir com áudio/transcrever (faster-whisper), e salvar as conclusões na skill.
