import flask
from flask_socketio import send, emit, join_room, leave_room
# we need both app and socketio
from cs3320a3 import app, socketio


@socketio.on('connect')
def on_connect():
    app.logger.info('client connected')


@socketio.on('joined')
def joined(data):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    name = data['name']
    room = data['room']
    join_room(room)
    emit('status', {'msg': name + ' has entered the room.'}, room=room)


# socketio.on says 'call function when this kind of event comes in'
@socketio.on('message')
def message(data):
    # flask_socketio.send sends a message to all connected clients
    msg = data['message']
    room = data['room']
    name = data['name']
    emit('message', {'msg': name + ': ' + msg}, room=room)


@socketio.on('disconnect')
def on_disconnect(data):
    room = data['room']
    leave_room(room)
    app.logger.info('client disconnected')
