from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from orchestrator import Orchestrator, socketio

app = Flask(__name__)
socketio.init_app(app, cors_allowed_origins="*")
orchestrator = Orchestrator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-app', methods=['POST'])
def generate_app():
    data = request.json
    user_prompt = data.get('prompt')
    print("Received prompt:", user_prompt)  # Debugging-Anweisung
    
    if not user_prompt:
        return jsonify({'error': 'Prompt is missing'}), 400
    
    try:
        result = orchestrator.process_request(user_prompt)
        print("Generated result:", result)  # Debugging-Anweisung
        return jsonify(result)
    except Exception as e:
        print("Error:", str(e))  # Debugging-Anweisung
        return jsonify({'error': str(e)}), 500

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    emit('connection_response', {'status': 'connected'})

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0')
