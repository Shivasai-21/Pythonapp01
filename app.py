from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import datetime

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return "Realtime Python App running in Docker!"

# Example realtime event: send server time every second
@socketio.on('connect')
def handle_connect():
    emit('message', {'data': 'Connected to realtime server!'})

@socketio.on('get_time')
def send_time(_):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    emit('time_update', {'time': now})

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
