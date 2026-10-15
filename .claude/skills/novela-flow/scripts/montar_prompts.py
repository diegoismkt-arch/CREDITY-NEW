#!/usr/bin/env python3
"""Gera os prompts JSON do Google Flow (modelo da casa) a partir de um roteiro.json.

Uso: python3 montar_prompts.py novelas/<slug>/roteiro.json
Cria novelas/<slug>/clipe_01.json, clipe_02.json... e prompts.md (todos juntos para copiar).
Calcula o tempo de cada plano pelas palavras e sai com código 1 se algum clipe
passar do limite de duração ou ficar vazio demais (crédito desperdiçado).
"""
import json
import re
import sys
from pathlib import Path

PALAVRAS_POR_SEG = 2.7   # medido nas referências: "Esse anel era da minha filha" = 6 palavras em 2,2 s
FOLGA_POR_FALA = 0.2     # respiro antes do corte seco
MIN_PLANO_FALA = 1.2
DURACAO_MAX = 10.0
OCUPACAO_MIN = 0.75      # pelo menos 75% do clipe com fala

NEGATIVO_BASE = [
    "texto ou letras em qualquer lugar",
    "palavra inventada no ultimo plano",
    "fala repetida",
    "fala adiantada ou atrasada para outro plano",
    "personagem falando ou olhando para quem nao e o destinatario da fala",
    "fala neutra ou monotona",
    "rosto neutro ou expressao vazia",
    "atuacao contida",
    "dois rostos visiveis nos planos de fala",
    "voz sem rosto na tela",
    "tela dividida",
    "colagem",
    "formato horizontal",
    "bordas pretas",
    "palavras em ingles",
    "palavras em portugues",
    "duas vozes simultaneas",
    "movimento labial do ouvinte",
    "fala cortada, encurtada ou incompleta",
    "personagem olhando para a camera",
    "mudanca de rosto",
    "mudanca de roupa",
    "legendas",
    "logotipo",
    "marca-d'agua",
    "trilha sonora",
]


def contar(texto):
    return len(re.findall(r"[\wáéíóúñü]+", texto or "", re.IGNORECASE))


def seg(x):
    m, s = divmod(round(x, 2), 60)
    return f"{int(m):02d}:{s:05.2f}"


def montar(rot, n, clip):
    planos = clip["planos"]
    t = 0.0
    timeline, falantes, avisos = [], [], []
    erro_para = False
    for p in planos:
        fala = p.get("fala")
        if fala:
            dur = max(MIN_PLANO_FALA, contar(fala) / PALAVRAS_POR_SEG + FOLGA_POR_FALA)
        else:
            dur = p.get("segundos", 0.8)
        ini, t = t, t + dur
        item = {"time": f"{seg(ini)}-{seg(t)}", "speaker": p["quem"] if fala else "NONE",
                "dialogue": fala or None}
        if fala:
            falantes.append(p["quem"])
            alvo = p.get("para")
            if not alvo:
                avisos.append(f"❌ plano de {p['quem']} sem 'para' (com quem fala)")
                erro_para = True
            item["addressee"] = alvo
            pos = clip.get("posicoes", {})
            if alvo == "CAMERA":
                item["eyeline"] = f"{p['quem']} olha DIRETO para a lente."
            elif alvo:
                onde = f", que esta {pos[alvo]}" if alvo in pos else ""
                outros = [k for k in clip["personagens"] if k not in (p["quem"], alvo)]
                item["eyeline"] = (f"{p['quem']} fala PARA {alvo} e olha para {alvo}{onde}, fora do quadro."
                                   + (f" NAO olha para {', '.join(outros)}." if outros else ""))
            item.update({
                "emotion_level": p.get("emocao", 9),
                "intention": p["intencao"],
                "voice": p["voz"],
            })
        item.update({"face": p["rosto"], "body": p["corpo"]})
        cam = p["camera"]
        if fala and "primeiro instante" not in cam:
            cam += " A fala comeca no primeiro instante do plano."
        item["camera"] = cam
        if fala:
            olha_camera = p.get("olha_para_camera", False)
            item["mouths"] = (f"Somente {p['quem']} movimenta os labios."
                              + (" Olha DIRETO para a lente, quebrando a quarta parede." if olha_camera else ""))
        else:
            item["mouths"] = "Bocas FECHADAS. Ninguem fala."
        timeline.append(item)

    total = t
    fala_seg = sum(max(MIN_PLANO_FALA, contar(p["fala"]) / PALAVRAS_POR_SEG + FOLGA_POR_FALA)
                   for p in planos if p.get("fala"))
    erro = erro_para
    if total > DURACAO_MAX:
        avisos.append(f"❌ {total:.1f}s — passa de {DURACAO_MAX:.0f}s, corte palavras")
        erro = True
    if fala_seg / DURACAO_MAX < OCUPACAO_MIN:
        avisos.append(f"❌ só {fala_seg:.1f}s de fala em {DURACAO_MAX:.0f}s — clipe vazio, gaste o crédito com mais fala")
        erro = True

    ultima_fala = max((i for i, p in enumerate(planos) if p.get("fala")), default=-1)
    fim_fala = sum(max(MIN_PLANO_FALA, contar(p["fala"]) / PALAVRAS_POR_SEG + FOLGA_POR_FALA) if p.get("fala")
                   else p.get("segundos", 0.8) for p in planos[:ultima_fala + 1])

    usados = clip["personagens"]
    negativos = [x for x in NEGATIVO_BASE if x not in clip.get("remover_negativos", [])]
    if any(p.get("olha_para_camera") for p in planos):
        negativos.remove("personagem olhando para a camera")
    negativos = clip.get("negativos_extra", []) + negativos

    nomes_fala = list(dict.fromkeys(falantes))
    imagens = clip.get("imagens", [])
    pers = rot["personagens"]
    fichas, preservar = {}, []
    for k in usados:
        d = pers[k]
        o, fic = ("A MESMA", "ficticia") if d.get("feminino") else ("O MESMO", "ficticio")
        if d.get("frame") in imagens:
            # personagem já existe num frame salvo de clipe anterior
            fichas[k] = f"{o} da imagem {d['frame']}. Personagem {fic}. {d['voz']}"
            preservar.append(f"{k}: o MESMO rosto da imagem {d['frame']}, {d['descricao']}")
        else:
            # primeira aparição: criado só pela descrição
            fichas[k] = f"{d['descricao']} Personagem {fic}. {d['voz']}"
            preservar.append(f"{k}: {d['descricao']}")
    prompt = {"ATUACAO_PRIORIDADE_MAXIMA": clip["atuacao"]}
    if imagens:
        prompt["input_image"] = {
            "required": False,
            "mode": "Ingredients to Video, sem primeiro frame.",
            "additional_references": True,
            "reference_images": [f"Imagem {i} — {rot['imagens'][k]}" for i, k in enumerate(imagens, 1)],
            "preserve_exactly": preservar + clip.get("preservar_extra", []),
        }
    prompt.update({
        "scene": {
            "title": rot["titulo_interno"],
            "duration_seconds": min(DURACAO_MAX, round(total + 0.05, 1)),
            "aspect_ratio": "9:16 vertical, um unico quadro cheio, sem divisoes",
            "structure": (f"{len(planos)} planos de cinema em tela cheia, ligados por cortes secos. "
                          f"{len(falantes)} falas, cada uma dita UMA UNICA VEZ, comecando no primeiro instante "
                          "do plano de quem fala e terminando antes do corte."),
            "style": rot["estilo"],
            "setting": clip["cenario"],
            **({"blocking": [f"{k}: {v}" for k, v in clip["posicoes"].items()]} if clip.get("posicoes") else {}),
            "characters": fichas,
        },
        "timeline": timeline,
        "dialogue_rules": {
            "language": "Espanol de Mexico, acento mexicano natural, TODAS as palavras em espanhol.",
            "performance": "Novela: cada fala com a entonacao do campo voice e a expressao do campo face.",
            "total_dialogue_lines": len(falantes),
            "exact_order": falantes,
            "rules": [
                f"So existem {len(falantes)} falas, cada uma dita UMA UNICA VEZ, no plano do seu dono.",
                f"Depois de {fim_fala:.1f} segundos ninguem fala." if ultima_fala < len(planos) - 1
                else "A ultima fala termina junto com o video.",
                "Cada fala e dirigida a: " + "; ".join(
                    f"{p['quem']} -> {p.get('para')}" for p in planos if p.get("fala")) + ".",
                "Quem fala olha para o destinatario da fala (campo eyeline), nunca para outra pessoa.",
                "Nao repetir, misturar, traduzir ou acrescentar palavras.",
                "Cada frase e dita INTEIRA, do comeco ao fim.",
            ] + clip.get("regras_extra", []),
        },
        "audio": {
            "single_voice_at_a_time": True,
            "sound": clip["som"],
            "music": "Nenhuma.",
            "narration": "Nenhuma.",
            "subtitles": "Nao gerar.",
        },
        "negative_prompt": negativos,
    })
    if not imagens:
        # clipe que cria os personagens: aparência fixa logo depois da atuação
        prompt = {"ATUACAO_PRIORIDADE_MAXIMA": prompt.pop("ATUACAO_PRIORIDADE_MAXIMA"),
                  "consistency": preservar + clip.get("preservar_extra", []), **prompt}
    # "imagem DON" -> "imagem 2", conforme a ordem das referências deste clipe
    numeros = {k: i for i, k in enumerate(imagens, 1)}
    prompt = json.loads(re.sub(r"imagem ([A-Z_]+)\b",
                               lambda m: f"imagem {numeros.get(m.group(1), m.group(1))}",
                               json.dumps(prompt, ensure_ascii=False)))
    faltando = set(re.findall(r"imagem ([A-Z_]{2,})\b", json.dumps(prompt, ensure_ascii=False)))
    if faltando:
        avisos.append(f"❌ cita imagem que não está em 'imagens' do clipe: {', '.join(sorted(faltando))}")
        erro = True
    status = " ".join(avisos) if avisos else "✅"
    resumo = (f"clipe {n}: {total:.1f}s, {fala_seg:.1f}s de fala "
              f"({sum(contar(p.get('fala')) for p in planos)} palavras, {len(planos)} planos, "
              f"falantes: {', '.join(nomes_fala)}) {status}")
    return prompt, resumo, erro


def main():
    caminho = Path(sys.argv[1])
    rot = json.loads(caminho.read_text(encoding="utf-8"))
    pasta = caminho.parent
    md = [f"# {rot['titulo_post']}\n", f"**Legenda:** {rot['legenda']}\n",
          f"**Texto na edição (final):** {rot.get('texto_final', '')}\n"]
    erros = 0
    for n, clip in enumerate(rot["clips"], 1):
        prompt, resumo, erro = montar(rot, n, clip)
        erros += erro
        print(resumo)
        txt = json.dumps(prompt, ensure_ascii=False, indent=2)
        (pasta / f"clipe_{n:02d}.json").write_text(txt + "\n", encoding="utf-8")
        refs = clip.get("imagens", [])
        uso = ("Sem imagem de referência (Text to Video)." if not refs else
               "Referências, nesta ordem: " + "; ".join(f"{i}) {k}" for i, k in enumerate(refs, 1)))
        md.append(f"\n## Clipe {n} — {clip['nome']}\n\n{resumo}\n\n{uso}\n\n```json\n{txt}\n```\n")
        if clip.get("salvar_frames"):
            md.append("**Depois de gerar este clipe, salve os frames:**\n" +
                      "\n".join(f"- **{k}:** {rot['imagens'][k]}" for k in clip["salvar_frames"]))
    (pasta / "prompts.md").write_text("\n".join(md), encoding="utf-8")
    print(f"\n{pasta}/prompts.md gerado. Clipes com erro: {erros}")
    sys.exit(1 if erros else 0)


if __name__ == "__main__":
    main()
