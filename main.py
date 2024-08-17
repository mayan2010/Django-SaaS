from flask import   Flask, render_template, request, session, redirect
from flask_socketio import join_room, leave_room, send, SocketIO

app = Flask(__name__)
app.config["SecretKey"] = "Goyan"
socketio = SocketIO(app)




if __name__ == "__main__":
    socketio.run(app, debug = True)
