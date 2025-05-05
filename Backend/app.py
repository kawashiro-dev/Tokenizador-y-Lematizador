import json
import spacy
from flask import Flask, request, jsonify
from flask_cors import CORS
from langdetect import detect

app = Flask(__name__)
CORS(app)

nlp_es = None
nlp_en = None

def cargar_modelos():
    global nlp_es
    global nlp_en
    try:
        nlp_es = spacy.load("es_core_news_sm")
        nlp_en = spacy.load("en_core_web_sm")
    except OSError:
        print("Error: Asegúrate de haber descargado los modelos de idioma de spaCy.")
        print("python -m spacy download es_core_news_sm")
        print("python -m spacy download en_core_web_sm")
        raise

def tokenizar_lematizar(texto, idioma="es"):
    if idioma == "es":
        doc = nlp_es(texto)
    elif idioma == "en":
        doc = nlp_en(texto)
    else:
        return {"error": "Idioma no soportado", "tokens": [], "lemas": []}

    tokens = [token.text for token in doc]
    caracteres_a_excluir = [",", ".", "(", ")", "*", "&", "^", "%", "$", "#", "@", "!"]
    lemas_filtrados = [
        token.lemma_ for token in doc
        if token.lemma_ not in caracteres_a_excluir and token.is_alpha
    ]
    return {"tokens": tokens, "lemas": lemas_filtrados}

def detectar_idioma(texto):
    try:
        return detect(texto)
    except:
        return "es" # Idioma por defecto en caso de error

@app.route('/procesar_texto', methods=['POST'])
def procesar_texto():
    cargar_modelos()
    data = request.get_json()
    texto = data.get('texto')

    if not texto:
        return jsonify({"error": "No se proporcionó texto para procesar"}), 400

    idioma_detectado = detectar_idioma(texto)
    resultados = tokenizar_lematizar(texto, idioma_detectado)
    return jsonify(resultados)

if __name__ == '__main__':
    app.run(debug=True, port=5000)