import os
from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS  # Importing CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the API key from the environment
api_key = os.getenv("GOOGLE_GENERATIVEAI_KEY")
genai.configure(api_key=api_key)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get('prompt', '')

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return jsonify({'reply': response.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
