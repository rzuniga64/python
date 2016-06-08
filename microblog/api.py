import datetime
import time
import flask
from init import app, db
import models
from markupsafe import Markup
import markdown

# Call this function to perform security checks.
def check_request():
    token = flask.session['csrf_token']
    if flask.request.form['_csrf_token'] != token:
        print('Invalid csrf token!!!')
        flask.abort(400)
    if 'auth_user' not in flask.session:
        print('Not logged in!!!')
        flask.abort(403)

@app.route('/api/update-follow', methods=['POST'])
def update_post():
#    time.sleep(2) # Uncomment to demonstrate waiting state
    check_request()
    # print('{}'.format(flask.session['csrf_token']))
    # if 'auth_user' not in flask.session:
    #     print('Not logged in.')
    #     flask.abort(403)
    # # reject requests with bad CSRF tokens
    # if flask.request.form['_csrf_token'] != flask.session['csrf_token']:
    #     print('Invalid CSRF token.')
    #     flask.abort(400)

    user_id = flask.session['auth_user']

    # everything's good, extract the follow request
    followee_id = flask.request.form['followee_id']
    followed = flask.request.form['followed']

    if followed == 'true':
        # is followee already followed?
        follow = models.Follow.query.filter_by(followee_id=followee_id,
                                               follower_id=user_id).first()

        if follow:
            # log & return, because followee is already followed
            app.logger.warn('followee %s already followed by %s', followee_id, user_id)
            return flask.jsonify({'result': 'already-followed'})
        else:
            # add the follower
            follow = models.Follow()
            follow.follower_id = user_id
            follow.followee_id = followee_id
            db.session.add(follow)
            db.session.commit()
            # tell client we succeeded
            return flask.jsonify({'result': 'ok'})
    else:
        # we want to unfollow
        unfollow = models.Follow().query.filter_by(followee_id=followee_id, follower_id=user_id).first()
        db.session.delete(unfollow)
        db.session.commit()
        return flask.jsonify({'result': 'ok'})

@app.route('/api/post', methods=['POST'])
def handle_jscript_post():
#    time.sleep(2) # Uncomment to demonstrate waiting state
    check_request()

    postText = flask.request.form['text']
    postURL = flask.request.form['url']

    # create Post object
    post = models.Post()
    post.creator_id = flask.session['auth_user']
    post.timestamp = datetime.datetime.now()
    post.url = postURL
    post.post = Markup(markdown.markdown(postText, output_format='html5'))
    # Add post to db
    db.session.add(post)
    db.session.commit()
    jsonPost = flask.jsonify(post.jsonable)
    return jsonPost
