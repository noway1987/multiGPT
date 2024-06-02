from flask import Flask, request, jsonify
from orchestrator import Orchestrator

app = Flask(__name__)
orchestrator = Orchestrator()

@app.route('/generate-app', methods=['POST'])
def generate_app():
    data = request.json
    user_prompt = data.get('prompt')
    
    result = orchestrator.process_request(user_prompt)
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
