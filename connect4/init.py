import os.path
import flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

app = flask.Flask(__name__)
app.config.from_pyfile('settings.py')
app.secret_key = app.config['SECRET_KEY']
socketio = SocketIO(app)
recip_sockets = {}
