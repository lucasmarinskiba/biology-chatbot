from flask import Flask, request, render_template, jsonify
from knowledge_base import biology_knowledge_base
import nltk
from nltk.tokenize import word_tokenize
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

# Descargar recursos de NLTK (solo la primera vez)
nltk.download('punkt')

# Función para procesar preguntas
def process_question(question):
    question = question.lower()
    for q in biology_knowledge_base:
        if question in q.lower():
            return biology_knowledge_base[q]
    return "Lo siento, no tengo información sobre esa pregunta. ¿Puedes intentar con otra?"

# Ruta principal para la interfaz del chatbot
@app.route('/')
def home():
    return render_template('index.html')

# Ruta para manejar las preguntas del chatbot
@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('message')
    response = process_question(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
