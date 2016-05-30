import flask
import os
import json
import uuid
import base64

from cs3320a3 import app

urls_file = 'urls.json'
rooms = dict()
topics = list()

@app.before_request
def setup_rooms():
    if os.path.exists(urls_file):
        with open(urls_file, 'r', encoding="utf8") as the_rooms:
            rooms = json.load(the_rooms)
            print(rooms)


@app.route('/')
def home_page():
    return flask.render_template('index.html')


@app.route('/', methods=['POST'])
def get_topic():
    # If topic empty redirect to index.html else go to next route
    if flask.request.form['topic'] == '':
        return flask.redirect(flask.url_for('home_page'), 303)
    else:
        topics.append(flask.request.form['topic'])
        # Generate room id
        room = base64.urlsafe_b64encode(uuid.uuid4().bytes)[:12].decode('ascii')
    return flask.redirect(flask.url_for('get_name', room=room), 303)


@app.route('/<room>')
def get_name(room):
    topic = topics[0]
    return flask.render_template('join.html', topic=topic)


@app.route('/<room>', methods=['POST'])
def join(room):
    # If nickname empty redirect to get nickname again
    if flask.request.form['nick'] == '':
        return flask.redirect(flask.url_for('get_name'), 303)
    else:
        name = flask.request.form['nick']

        if room not in rooms.keys():
            # If key is not in dictionary, add to dictionary and go to chat page
            topic = topics[0]
            names = [name]
            rooms[room] = {"topic": topics[0], "roster": names}
            with open(urls_file, 'w') as outfile:  # Output dictionary to output file
                json.dump(rooms, outfile)
        else:
            theroom = rooms[room]
            topic = theroom["topic"]
            names = theroom["roster"]
            names.append(name)
            with open(urls_file, 'w') as outfile:  # Output dictionary to output file
                json.dump(rooms, outfile)
        return flask.render_template('chat.html', name=name, room=room, topic=topic, roster=names)
