#!/usr/bin/env python3
"""Monta os prompts do Google Flow a partir de um episodio.json e valida a fala de cada clipe.

Uso: python3 montar_prompts.py novelas/<slug>/episodio.json
Gera prompts.md na mesma pasta. Sai com código 1 se algum clipe estiver fora da faixa de palavras.
"""
import json
import re
import sys
from pathlib import Path

MIN_PALAVRAS = 18   # abaixo disso o clipe de 10 s fica com silêncio (crédito desperdiçado)
ALVO = (22, 28)
MAX_PALAVRAS = 30   # acima disso a fala não cabe em 10 s
MAX_FALANTES = 2

TEMPLATE = (
    "{estilo}. 10-second clip.\n"
    "Scene: {cenario}.\n"
    "Characters: {personagens}.\n"
    "Camera: {camera}.\n"
    "Action: {acao}.\n"
    "Dialogue in Mexican Spanish, natural lip-sync, dramatic telenovela delivery, "
    "speech starts immediately in the first second and continues until the end, no silent pauses:\n"
    "{falas}\n"
    "No subtitles, no on-screen text, no background music."
)


def contar(texto):
    return len(re.findall(r"[\wáéíóúñü]+", texto, re.IGNORECASE))


def montar_clip(ep, clip):
    pers = "; ".join(f"{n}: {ep['personagens'][n]}" for n in clip["personagens"])
    falas = "\n".join(f'{n} ({emo}): "{txt}"' for n, emo, txt in clip["falas"])
    return TEMPLATE.format(
        estilo=ep["estilo"], cenario=ep["cenarios"][clip["cenario"]], personagens=pers,
        camera=clip["camera"], acao=clip["acao"], falas=falas,
    )


def checar(clip):
    palavras = sum(contar(t) for _, _, t in clip["falas"])
    falantes = {n for n, _, _ in clip["falas"]}
    erros = []
    if palavras < MIN_PALAVRAS:
        erros.append(f"só {palavras} palavras — clipe vazio, adicione fala")
    elif palavras > MAX_PALAVRAS:
        erros.append(f"{palavras} palavras — não cabe em 10 s, corte")
    if len(falantes) > MAX_FALANTES:
        erros.append(f"{len(falantes)} falantes — máximo {MAX_FALANTES}")
    for n in falantes | set(clip["personagens"]):
        if n not in clip["personagens"]:
            erros.append(f"{n} fala mas não está em 'personagens'")
    status = "❌ " + "; ".join(erros) if erros else ("✅" if ALVO[0] <= palavras <= ALVO[1] else "⚠️ fora do alvo 22–28")
    return palavras, status, bool(erros)


def bloco(ep, num, clip):
    palavras, status, _ = checar(clip)
    return f"### Clipe {num} — {palavras} palavras {status}\n\n```\n{montar_clip(ep, clip)}\n```\n"


def main():
    caminho = Path(sys.argv[1])
    ep = json.loads(caminho.read_text(encoding="utf-8"))
    clips = ep["clips"]
    falhas = 0
    out = [f"# {ep['titulo']}\n", f"**Legenda do post:** {ep['legenda']}\n"]

    for s in ep.get("shorts", []):
        out.append(f"\n---\n\n## {s['nome']} (vídeo curto)\n")
        for i, c in enumerate(s.get("clips_novos", []), 1):
            out.append(bloco(ep, f"{s['nome']} / novo {i}", c))
            falhas += checar(c)[2]
        if s.get("clips"):
            out.append(f"Usa os clipes do episódio: **{', '.join(map(str, s['clips']))}** (prompts abaixo, gere uma vez só e reaproveite).\n")
        if s.get("texto_final"):
            out.append(f"Texto na edição, no final: **{s['texto_final']}**\n")

    total = sum(checar(c)[0] for c in clips)
    out.append(f"\n---\n\n## Episódio completo — {len(clips)} clipes (~{len(clips) * 10 // 60} min {len(clips) * 10 % 60} s), {total} palavras\n")
    for i, c in enumerate(clips, 1):
        out.append(bloco(ep, i, c))
        falhas += checar(c)[2]
    if ep.get("texto_final"):
        out.append(f"\nTexto na edição, no final do episódio: **{ep['texto_final']}**\n")

    destino = caminho.with_name("prompts.md")
    destino.write_text("\n".join(out), encoding="utf-8")
    for i, c in enumerate(clips, 1):
        p, st, _ = checar(c)
        print(f"clipe {i:2d}: {p:2d} palavras {st}")
    print(f"\n{destino} gerado. Clipes com erro: {falhas}")
    sys.exit(1 if falhas else 0)


if __name__ == "__main__":
    main()
