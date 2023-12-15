from flask import Flask, request, jsonify
from ml_model import placeholder_ml_model

app = Flask(__name__)

@app.route('/')
def index():
    return 'Please use the /prompt endpoint to POST data.', 200

@app.route('/prompt', methods=['POST'])
def handle_prompt():
    data = request.get_json()
    prompt = data.get('prompt', '')
    response = placeholder_ml_model(prompt)
    return jsonify({'response': response}), 200

if __name__ == '__main__':
    app.run(debug=True)