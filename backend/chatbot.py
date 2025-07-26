import json
from difflib import get_close_matches

def cargar_faq():
    with open("faq.json", "r", encoding="utf-8") as f:
        return json.load(f)

def responder_usuario(pregunta_usuario):
    faqs = cargar_faq()
    preguntas_originales = list(faqs.keys())
    preguntas_normalizadas = [p.lower() for p in preguntas_originales]

    coincidencias = get_close_matches(pregunta_usuario.lower(), preguntas_normalizadas, n=1, cutoff=0.6)

    if coincidencias:
        indice = preguntas_normalizadas.index(coincidencias[0])
        mejor_pregunta = preguntas_originales[indice]
        return faqs[mejor_pregunta]
    else:
        return "Lo siento, no entiendo tu pregunta. ¿Puedes reformularla?"

