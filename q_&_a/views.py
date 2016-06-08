import flask
import os
import uuid
import base64
import json
import bcrypt
import models
import markdown
from markupsafe import Markup
from datetime import date
from sqlalchemy import desc
import math

from flask import Flask
from init import app, db
from markupsafe import Markup
from sqlalchemy.orm import joinedload


# # Uncomment to add a dummy user to the db
# user = models.User()
# user.login = "some_dude"
# user.pw_hash = "12345"
# db.session.add(user)
# db.session.commit()

@app.before_request
def setup_user():
    """
    Figure out if we have an authorized user, and look them up.
    This runs for every request, so we don't have to duplicate code.
    """
    if 'auth_user' in flask.session:
        user = models.User.query.get(flask.session['auth_user'])
        flask.g.user = user
        # save the user in `flask.g`, which is a set of globals for this request

@app.before_request
def setup_token():
    if 'csrf_token' not in flask.session:
        flask.session['csrf_token'] = base64.b64encode(os.urandom(32)).decode('ascii')

@app.route('/')
def index():
    # Load list of questions
    questions = models.Question.query.all()
    # Sort questions in descending order by ID
    questions.sort(key=lambda question: question.id, reverse=True)
    # Create dictionary of marked-up questions mapping question id to content
    marked_questions = {}
    num_questions = len(questions)
    upper_bound = num_questions
    if upper_bound > 25:
        upper_bound = 25
    for i in range(0, upper_bound):
        if questions[i].question is None:
            marked_question = ""
        else:
            marked_question = Markup(markdown.markdown(questions[i].question, output_format='html5'))
        marked_questions[questions[i].id] = marked_question
    last_page = math.ceil(num_questions / 25)
    print("last page: {}".format(last_page))
    return flask.render_template("index.html", questions=questions[0:25],
                                 content=marked_questions, pid=1, lastpage=last_page)  # Flask will look for templates in the templates folder

@app.route('/<int:pid>')
def additional_index(pid):
    if pid is 1:
        return flask.redirect(flask.url_for('index'))
    if pid < 1: # invalid page number
        flask.abort(404)
    # Load list of questions
    questions = models.Question.query.all()
    num_questions = len(questions)
    last_page = math.ceil(num_questions / 25)
    if pid > last_page: # page number is too big, abort
        flask.abort(404)
    # Sort questions in descending order by ID
    questions.sort(key=lambda question: question.id, reverse=True)
        # Create dictionary of marked-up questions mapping question id to content
    marked_questions = {}
    if pid < last_page:
        upper_bound = 25 * pid
    else:
        upper_bound = num_questions
    lower_bound = 25 * (pid - 1)
    for i in range(lower_bound, upper_bound):
        if questions[i].question is None:
            marked_question = ""
        else:
            marked_question = Markup(markdown.markdown(questions[i].question, output_format='html5'))
        marked_questions[questions[i].id] = marked_question
    return flask.render_template("index.html", questions=questions[lower_bound:upper_bound],
                                 content=marked_questions, pid=pid, lastpage=last_page)


@app.route('/question-form')
def ask_question():
    return flask.render_template("question_form.html")


@app.route('/add-question', methods=['POST'])
def add_question():
    if flask.request.form['_csrf_token'] != flask.session['csrf_token']:
        app.logger.debug('invalid CSRF token in question form!')
        flask.abort(400)
    subject = flask.request.form['subject']
    content = flask.request.form['content']
    tag_str = flask.request.form['tags']
    # Check for bad input
    if len(subject) > 50:
        return flask.render_template("question_form.html", state='bad-subject')
    if len(content) > 1000:
        return flask.render_template("question_form.html", state='bad-question')
    if subject == '':
        subject = 'No subject'
    if content == '':
        content = 'No content'
    # Assemble date string
    today = date.today()
    month = str(today.month)
    day = str(today.day)
    year = str(today.year)
    date_asked = month + '/' + day + '/' + year
    # Create question object
    question = models.Question()
    question.subject = subject
    question.question = content
    question.date_asked = date_asked
    question.creator_id = flask.session['auth_user']

    for tag in tag_str.split(','):
        # skip all empty tags
        # strip whitespace. then empty tag is false. so 'if not' skips empty

        if not tag.strip():
            continue
        if len(tag.strip()) > 50:
            continue # tag is too long, throw it out

        # create object
        tag_obj = models.QuestionTag()
        # set tag
        tag_obj.tag = tag.strip()
        # add to question
        question.tags.append(tag_obj)
    # Add question to db
    db.session.add(question)
    db.session.commit()
    return flask.redirect(flask.url_for('view_question', qid=question.id), 303)


@app.route('/questions/<int:qid>')
def view_question(qid):
    question = models.Question.query.get(qid)
    if question is None:
        flask.abort(404)
    if question.question is None:
        marked_question = ""
    else:
        marked_question = Markup(markdown.markdown(question.question, output_format='html5'))
    marked_answers = {}
    for answer in question.answers:
        if answer.answer is None:
            marked_answer = ""
        else:
            marked_answer = Markup(markdown.markdown(answer.answer, output_format='html5'))
        marked_answers[answer.id] = marked_answer
    upvoted = {} # dictionary of answers user has upvoted
    downvoted = {}
    # Determine which answers a user has upvoted or downvoted
    if 'auth_user' in flask.session:
        for answer in question.answers:
            upvote = models.Upvote.query.filter_by(answer_id=answer.id,
                                                  creator_id=flask.session['auth_user']).first()
            downvote = models.Downvote.query.filter_by(answer_id=answer.id,
                                                  creator_id=flask.session['auth_user']).first()
            # Has the user upvoted it?
            upvoted[answer.id] = upvote is not None
            downvoted[answer.id] = downvote is not None
    # Get number of upvotes/downvotes
    answers=[]
    for answer in question.answers:
        answer_dict = {}
        answer_dict['answer'] = answer
        answer_dict['id'] = answer.id
        upvotes = models.Upvote.query.filter_by(answer_id=answer.id).all()
        answer_dict['upvotes'] = 0
        for u in upvotes:
            answer_dict['upvotes'] += 1
        downvotes = models.Downvote.query.filter_by(answer_id=answer.id).all()
        for d in downvotes:
            answer_dict['upvotes'] -= 1
        answers.append(answer_dict)
    return flask.render_template('question.html', question=question, content=marked_question,
                                 marked_answers=marked_answers, upvoted=upvoted, downvoted=downvoted, answers=answers)


@app.route('/add-answer', methods=['POST'])
def add_answer():
    if flask.request.form['_csrf_token'] != flask.session['csrf_token']:
        app.logger.debug('invalid CSRF token in answer form!')
        flask.abort(400)
    qid = flask.request.form['qid']
    creator_id = flask.session['auth_user']
    content = flask.request.form['content']
    # Check for bad input
    if len(content) > 1000:
        return flask.redirect(flask.url_for('bad_answer', qid=qid))
    if content == '':
        content = 'No content'
    # create answer object
    answer = models.Answer()
    answer.creator_id = creator_id
    answer.question_id = qid
    answer.answer = content
    # add answer to db
    db.session.add(answer)
    db.session.commit()
    return flask.redirect(flask.url_for('view_question', qid=qid), 303)

@app.route('/answer-problem/<int:qid>')
def bad_answer(qid):
    return flask.render_template('bad_answer.html', qid=qid)


@app.route('/login')
def login_form():
    # GET request to /login - send the login form
    return flask.render_template('login.html')


@app.route('/login', methods=['POST'])
def handle_login():
    # POST request to /login - check user
    login = flask.request.form['user']
    password = flask.request.form['password']
    # try to find user
    user = models.User.query.filter_by(login=login).first()
    if user is not None:
        # hash the password the user gave us
        # for verifying, we use their real hash as the salt
        pw_hash = bcrypt.hashpw(password.encode('utf8'), user.pw_hash)
        # is it good?
        if pw_hash == user.pw_hash:
            # yay!
            flask.session['auth_user'] = user.id
            # And redirect to '/', since this is a successful POST
            return flask.redirect(flask.request.form['url'], 303)

    # if we got this far, either username or password is no good
    # For an error in POST, we'll just re-show the form with an error message
    return flask.render_template('login.html', state='bad')


@app.route('/create_user', methods=['POST'])
def create_user():
    login = flask.request.form['user']
    password = flask.request.form['password']
    # do the passwords match?
    if password != flask.request.form['confirm']:
        return flask.render_template('login.html', state='password-mismatch')
    # is the login ok?
    if len(login) > 20:
        return flask.render_template('login.html', state='bad-username')
    # search for existing user
    existing = models.User.query.filter_by(login=login).first()
    if existing is not None:
        # oops
        return flask.render_template('login.html', state='username-used')

    # create user
    user = models.User()
    user.login = login
    # hash password
    user.pw_hash = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt(15))

    # save user
    db.session.add(user)
    db.session.commit()

    flask.session['auth_user'] = user.id
    print("From user creation, id is {}".format(flask.session['auth_user']))

    return flask.redirect(flask.request.form['url'], 303)


@app.route('/user/<name>')
def show_user(name):
    user = models.User.query.filter_by(login=name).first()
    if user is None:
        flask.abort(404)

    return flask.render_template('user.html', user=user)


@app.route('/logout')
def handle_logout():
    # user wants to say goodbye, just forget about them
    del flask.session['auth_user']
    # redirect to specfied source URL, or / if none is present
    return flask.redirect(flask.request.args.get('url', '/'))


@app.route('/tags/<tag>')
def show_tag(tag):
    # find question-tag instances with specified tag
    # 'joinedload' tells it to fetch associated questions right away
    q = models.QuestionTag.query.options(joinedload(models.QuestionTag.question))
    question_tags = q.filter_by(tag=tag).all();
    # this quick syntax lets us convert the question_tags into a list of questions
    questions = [at.question for at in question_tags]
    marked_questions = {}
    for question in questions:
        if question.question is None:
            marked_question = ""
        else:
            marked_question = Markup(markdown.markdown(question.question, output_format='html5'))
        marked_questions[question.id] = marked_question
    return flask.render_template('tag.html', tag=tag, questions=questions, content=marked_questions)

# function handles 404 URL
@app.errorhandler(404)
def page_not_found(err):
    return flask.render_template('404.html', path=flask.request.path), 404
