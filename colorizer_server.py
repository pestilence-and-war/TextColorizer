from flask import Flask, request, jsonify
from flask_cors import CORS
import spacy

nlp = spacy.load('en_core_web_sm')

app = Flask(__name__)

CORS(app)  #This will enable CORS for all routes

@app.route('/process', methods=['POST'])
def process_text():
    text = request.get_json().get('text')
    doc = nlp(text)
    result = [{'text': str(token), 'pos': token.pos_} for token in doc]
    return jsonify(result)

if __name__ == '__main__':
    app.run(port=5000)