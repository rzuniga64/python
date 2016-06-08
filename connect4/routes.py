import flask
import os
import json
import uuid
import base64
from flask_socketio import emit, join_room, rooms
import hashlib
import queue
import gameengine

from project5 import app, socketio

# Global dictionary of users.
# key: username
# value: gravatar hash
usernames = dict()


# Waiting room queue.
# When a user enters the waiting room, their username is placed in the queue.
waitingroom = queue.Queue()
waiting_list = {} # Searchable list of users in waitingroom
matches = {} # Matches made in waiting room


@app.before_request
def setup_session():
    if 'sid' not in flask.session:
        sid = base64.b32encode(os.urandom(32)).decode('utf-8')
        flask.session['sid'] = sid


@app.route('/')
def index():
    if 'username' in flask.session:
        username = flask.session['username']
        if username is not None:
            print('User has expired screenname {}. Deleting screenname.'.format(username))
            if username in usernames:
                del usernames[username]
        del flask.session['username']
    return flask.render_template('index.html')


@app.route('/submit-name', methods=['POST'])
def new_user():
    error = None
    user = flask.request.form['username']
    email = flask.request.form['email']
    hash = hashlib.md5()
    hash.update(email.strip().lower().encode('utf8'))
    hash_tag = hash.hexdigest()

    if user and email is None:
        error = "Do Not Leave fields blank!"
        return flask.render_template('index.html', error=error)

    # if key is not in dictionary, add to dictionary
    if user not in usernames.keys():
        usernames[user] = hash_tag
    else:
        error = "Username Already Exists!"
        return flask.render_template('index.html', error=error)

    if 'username' not in flask.session:
        flask.session['username'] = user

    return flask.redirect(flask.url_for('waiting_room', user=user))


@app.route('/waitingroom')
def waiting_room():
    if 'username' in flask.session:
        user = flask.session['username']
        if user in usernames.keys():
            hash_tag = usernames[user]
            return flask.render_template('waitingroom.html', user=user, hash_tag= hash_tag)
        else:
            # Not a valid user. Send them back to index.
            return flask.redirect(flask.url_for('index'))
    else:
        return flask.redirect(flask.url_for('index'))


# URL handler for game room pages.
@app.route('/<key>/')
def game_room(key):
    if 'username' in flask.session:
        user = flask.session['username']
        if user in usernames:
            return flask.render_template('gameroom.html', key=key, user=user)
        else:
            return flask.redirect(flask.url_for('index'))
    else:
        return flask.redirect(flask.url_for('index'))


# On clicking the "Join room" button in the waiting room page, redirects the user to a game room page.
@app.route('/goto-game', methods=['POST'])
def goto_game():
    key = flask.request.form['key']
    user = flask.request.form['user']

    player = gameengine.Player(user)

    if key not in gameengine.games:
        game = gameengine.create_game(player, key)
        gameengine.games[game.key] = game
    else:
        game = gameengine.games[key]
        game.add_player(player)
        print('Player {} joined game {}'.format(user, key))

    if user in matches:
        del matches[user]
    if user in waiting_list:
        del waiting_list[user]

    return flask.redirect(flask.url_for('game_room', key=key, user=user))


@app.route('/quit', methods=['POST'])
def quit_game():
    del flask.session['username']
    username = flask.request.form['user']
    if username in usernames:
        del usernames[username]
        print('Deleted ' + username)
    key = flask.request.form['key']
    if key in gameengine.games:
        game = gameengine.games[key]
        game.remove_player(username)
        if game.is_empty():
            del gameengine.games[key]
            print('Deleted game ' + key)
    return flask.redirect(flask.url_for('index'))


@app.route('/new-game', methods=['POST'])
def new_game():
    username = flask.request.form['user']
    key = flask.request.form['key']
    if key in gameengine.games:
        game = gameengine.games[key]
        game.remove_player(username)
        if game.is_empty():
            del gameengine.games[key]
            print('Deleted game ' + key)
    return flask.redirect(flask.url_for('waiting_room'))


##### SOCKETIO HANDLERS #####


@socketio.on('connect')
def connection():
    print('A client connected.')


# Generic message handler. Helpful for debugging.
@socketio.on('msg')
def msg(msg):
    print(msg)


# Handles a client entering the waiting room.
# After opening a socket, the client sends a 'joinwaitingroom' event.
@socketio.on('joinwaitingroom')
def join_waitingroom(username):
    join_room(username)
    emit('msg', 'joined room', room=username)
    if username in matches:
        key = matches[username]['key']
        other_player = matches[username]['other_user']
        emit('foundmatch', {'key': key, 'user': other_player}, room=username)
        emit('foundmatch', {'key': key, 'user': username}, room=other_player)
    elif not waitingroom.empty() and username not in waiting_list:
        # Grab a user from the queue.
        other_player = waitingroom.get()
        if other_player in waiting_list:
            del waiting_list[other_player]
            print('Found a match for players {} and {}'.format(username, other_player))
            # Generate a game room key.
            key = base64.b32encode(os.urandom(8)).decode('utf-8').replace('=', '')
            match1 = {'this_user': username, 'other_user': other_player, 'key': key}
            match2 = {'this_user': other_player, 'other_user': username, 'key': key}
            matches[username] = match1
            matches[other_player] = match2
            # Emit a 'foundmatch' event to the two users.
            emit('foundmatch', {'key': key, 'user': other_player}, room=username)
            emit('foundmatch', {'key': key, 'user': username}, room=other_player)
            return
        else:
            while not waitingroom.empty():
                other_player = waitingroom.get()
                if other_player in waiting_list:
                    del waiting_list[other_player]
                    print('Found a match for players {} and {}'.format(username, other_player))
                    # Generate a game room key.
                    key = base64.b32encode(os.urandom(8)).decode('utf-8').replace('=', '')
                    match1 = {'this_user': username, 'other_user': other_player, 'key': key}
                    match2 = {'this_user': other_player, 'other_user': username, 'key': key}
                    matches[username] = match1
                    matches[other_player] = match2
                    # Emit a 'foundmatch' event to the two users.
                    emit('foundmatch', {'key': key, 'user': other_player}, room=username)
                    emit('foundmatch', {'key': key, 'user': username}, room=other_player)
                    return
            # waitingroom has no valid users. Join the waitingroom.
            print('{} joined the waitingroom.'.format(username))
            # Put the user in the queue.
            if username not in waiting_list:
                waiting_list[username] = username
                waitingroom.put(username)
    else:
        print('{} joined the waitingroom.'.format(username))
        # Put the user in the queue.
        if username not in waiting_list:
            waiting_list[username] = username
            waitingroom.put(username)


@socketio.on('disconnect')
def on_disconnect():
    for room in rooms():
        print('Disconnecting client was in room ' + room)
        if room in waiting_list:
            del waiting_list[room]
