from init import app, socketio

import gameengine, routes

if __name__ == '__main__':
    socketio.run(app, debug=True)


