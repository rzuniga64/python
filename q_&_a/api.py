import flask
from init import app, db
import models


@app.route('/api/update-upvote', methods=['POST'])
def update_upvote():
    if 'auth_user' not in flask.session:
        flask.abort(401)
    user_id = flask.session['auth_user']
    print('from api, user id is {}'.format(user_id))
    # reject requests with bad CSRF tokens
    if flask.request.form['_csrf_token'] != flask.session['csrf_token']:
        flask.abort(400)

    answer_id = flask.request.form['answer_id']
    want_upvote = flask.request.form['want_upvote'] == 'true'

    upvote = models.Upvote.query.filter_by(answer_id=answer_id,
                                             creator_id=user_id).first()
    downvote = models.Downvote.query.filter_by(answer_id=answer_id,
                                             creator_id=user_id).first()

    if want_upvote:
        if upvote is None:
            # add the upvote
            upvote = models.Upvote()
            upvote.creator_id = user_id
            upvote.answer_id = answer_id
            db.session.add(upvote)
            db.session.commit()
            if downvote is not None:
                db.session.delete(downvote)
                db.session.commit()
            return flask.jsonify({'result': 'ok'})
        else:
            app.logger.warn('answer %s already upvoted by %s', answer_id, user_id)
            return flask.jsonify({'result': 'already-upvoted'})
    else:
        if upvote is not None:
            db.session.delete(upvote)
            db.session.commit()
            return flask.jsonify({'result': 'ok'})
        else:
            return flask.jsonify({'result': 'not-starred'})

@app.route('/api/update-downvote', methods=['POST'])
def update_downvote():
    if 'auth_user' not in flask.session:
        flask.abort(401)
    user_id = flask.session['auth_user']
    print('from api, user id is {}'.format(user_id))
    # reject requests with bad CSRF tokens
    if flask.request.form['_csrf_token'] != flask.session['csrf_token']:
        flask.abort(400)

    answer_id = flask.request.form['answer_id']
    want_downvote = flask.request.form['want_downvote'] == 'true'

    downvote = models.Downvote.query.filter_by(answer_id=answer_id,
                                             creator_id=user_id).first()
    upvote = models.Upvote.query.filter_by(answer_id=answer_id,
                                             creator_id=user_id).first()

    if want_downvote:
        if downvote is None:
            # add the upvote
            downvote = models.Downvote()
            downvote.creator_id = user_id
            downvote.answer_id = answer_id
            db.session.add(downvote)
            db.session.commit()
            if upvote is not None:
                db.session.delete(upvote)
                db.session.commit()
            return flask.jsonify({'result': 'ok'})
        else:
            app.logger.warn('answer %s already downvoted by %s', answer_id, user_id)
            return flask.jsonify({'result': 'already-downvoted'})
    else:
        if downvote is not None:
            db.session.delete(downvote)
            db.session.commit()
            return flask.jsonify({'result': 'ok'})
        else:
            return flask.jsonify({'result': 'not-starred'})