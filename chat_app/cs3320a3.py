from init import app, socketio

import chat, routes

if __name__ == '__main__':
    socketio.run(app, debug=True)
