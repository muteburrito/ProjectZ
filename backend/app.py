from flask import Flask, request, jsonify
from flask_cors import CORS
from backend.backend_logic import search

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return '''
    <html>
        <body style="background-color: black; color: white; font-family: monospace;">
            Please use the /prompt endpoint to POST data.
        </body>
    </html>
    ''', 200

@app.route('/<path:path>', methods=['GET', 'POST'])
def catch_all(path):
    if request.method == 'POST':
        return jsonify({'error': 'This endpoint "{}" does not exist'.format(path)}), 404
    else:
        return '''
        <html>
            <body style="background-color: black; color: white; font-family: monospace;">
                This page "{}" does not exist
            </body>
        </html>
        '''.format(path), 404

@app.route('/prompt', methods=['POST'])
def handle_prompt():
    data = request.get_json()
    prompt = data.get('prompt', '')
    response = search(prompt)
    print(len(response))
    return jsonify({'response': response}), 200

if __name__ == '__main__':
    app.run(debug=True)