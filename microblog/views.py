import io

import flask
import os
import uuid
import base64
import json
import bcrypt
import models
import markdown
from datetime import date
from sqlalchemy import desc
import math
import time
import datetime
import re

from flask import Flask
from init import app, db
from markupsafe import Markup
from sqlalchemy.orm import joinedload
from api import check_request


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
        # You can reference this variable in a jinja template as g.user
        # example:
        # <p>Logged in as {{ g.user.name }}</p>


@app.before_request
def setup_token():
    # This runs before every request.
    # Creates a csrf_token for the user's session if they do not already have one.
    if 'csrf_token' not in flask.session:
        flask.session['csrf_token'] = base64.b64encode(os.urandom(32)).decode('ascii')



# Main page that shows 20 most recent posts from people the user follows when logged in
@app.route('/')
def main_page():
    # load list of posts
    marked_posts = dict()

    # if the user is not logged in show teh20 most recent posts across all users and allow the user to register an
    # account.
    if 'auth_user' not in flask.session.keys():
        # load list of posts
        marked_posts = dict()
        posts = models.Post.query.all()
        # Sort questions in descending order by ID
        posts.sort(key=lambda post: post.timestamp, reverse=True)
        upper_bound = len(posts)
        if upper_bound > 20:
            upper_bound = 20
        if posts is not None:
            posts = posts[0:upper_bound]
            for i in range(0, upper_bound):
                if posts[i].post is None:
                    marked_post = ""
                else:
                    marked_post = Markup(markdown.markdown(posts[i].post, output_format='html5'))
                marked_posts[posts[i].id] = marked_post
        return flask.render_template('index.html', posts=posts, marked_posts=marked_posts)
    else:
        user = models.User.query.get(flask.session['auth_user'])

        # If the user is logged in, show the 20 most recent posts from the users they follow.
        followed_posts = db.session.query(models.Post, models.Follow) \
            .filter(models.Post.creator_id == models.Follow.followee_id, models.Follow.follower_id == models.User.id).\
                                                order_by(models.Post.timestamp).all()

        # Sort questions in descending order by ID
        followed_posts.sort(key=lambda post: post.Post.id, reverse=True)
        upper_bound = len(followed_posts)
        if upper_bound > 20:
            upper_bound = 20
        if followed_posts is not None:
            for i in range(0, upper_bound):
                if followed_posts[i].Post.post is None:
                    marked_post = ""
                else:
                    marked_post = Markup(markdown.markdown(followed_posts[i].Post.post, output_format='html5'))
                marked_posts[followed_posts[i].Post.id] = marked_post
        return flask.render_template('index.html', user=user, posts=followed_posts, marked_posts=marked_posts)


@app.route('/post')
def post_page():
    return flask.render_template('post.html')

@app.route('/post/photo-send', methods=['POST'])
def photo_send():
    # validate CSRF
    if flask.request.form['_csrf_token'] != flask.session['csrf_token']:
        print('Invalid csrf token.')
        flask.abort(400)
    # check for logged in user
    if flask.g.user is None:
        flask.abort(403)  # forbidden

    file = flask.request.files['image']

    # check that we think the file is an image file
    if not file.mimetype.startswith('image/'):
        print('Incorrect file type.')
        flask.abort(400)

    post = models.Post()
    post.photo_type = file.mimetype

    photo_data = io.BytesIO()
    file.save(photo_data)
    post.photo = photo_data.getvalue()
    post.post = flask.request.form['post']
    post.creator_id = flask.session['auth_user']
    post.timestamp = datetime.datetime.now()
    post.url = flask.request.form['url']
    db.session.add(post)
    db.session.commit()

    return flask.redirect(flask.url_for('main_page'), 303)

    # a URL handler to return the photo data


@app.route('/post/<int:photo_id>/photo')
def photo_sender(photo_id):

    photo = models.Post.query.get_or_404(photo_id)

    return flask.send_file(io.BytesIO(photo.photo))

@app.route('/login')
def login_page():
    return flask.render_template('login.html')


@app.route('/login', methods=['POST'])
def handle_login():
    # POST request to /login - check user
    name = flask.request.form['name']
    password = flask.request.form['password']
    # try to find user
    user = models.User.query.filter_by(name=name).first()
    if user is not None:
        # hash the password the user gave us
        # for verifying, we use their real hash as the salt
        pw_hash = bcrypt.hashpw(password.encode('utf8'), user.pw_hash)
        # is it good?
        if pw_hash == user.pw_hash:
            # yay!
            flask.session['auth_user'] = user.id
            flask.g.user = user
            return flask.redirect(flask.request.form['url'], 303)

    # if we got this far, either username or password is no good
    # For an error in POST, we'll just re-show the form with an error message
    return flask.render_template('login.html', state='bad')


@app.route('/edit_profile')
def edit_page():
    return flask.render_template('edit_profile.html')


@app.route('/edit_profile', methods=['POST'])
def edit_profile():
    check_request()
    location = flask.request.form['location']
    bio = flask.request.form['bio']
    user = flask.g.user

    user.location = location
    user.bio = bio

    # save user
    db.session.commit()
    return flask.redirect(flask.url_for('show_profile', name=user.name), 303)


@app.route('/create_user', methods=['POST'])
def create_user():
    name = flask.request.form['name']
    email = flask.request.form['email']
    password = flask.request.form['password']
    if re.match("^[a-zA-Z0-9_-]+$", name) is None:
        return flask.render_template('login.html', state='bad-username')
    # do the passwords match?
    if password != flask.request.form['confirm']:
        return flask.render_template('login.html', state='password-mismatch')
    # is the login ok?
    if len(name) > 20:
        return flask.render_template('login.html', state='bad-username')
    if len(email) > 100:
        return flask.render_template('login.html', state='bad-email')
    # search for existing user
    existing = models.User.query.filter_by(name=name).first()
    if existing is not None:
        # oops
        return flask.render_template('login.html', state='username-used')

    # create user
    user = models.User()
    user.name = name
    user.email = email
    # hash password
    user.pw_hash = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt(15))

    # save user
    db.session.add(user)
    db.session.commit()

    flask.session['auth_user'] = user.id

    return flask.redirect(flask.request.form['url'], 303)


@app.route('/u/<name>')
def show_profile(name):
    user = models.User.query.filter_by(name=name).first()
    if user is None:
        flask.abort(404)

    # load list of posts
    marked_posts = dict()
    posts = user.posts.all()
    # Sort posts in descending order by timestamp
    posts.sort(key=lambda post: post.timestamp, reverse=True)
    upper_bound = len(posts)
    if upper_bound > 10:
        upper_bound = 10
    if posts is not None:
        posts = posts[0:upper_bound]
        for i in range(0, upper_bound):
            if posts[i].post is None:
                marked_post = ""
            else:
                marked_post = Markup(markdown.markdown(posts[i].post, output_format='html5'))
            marked_posts[posts[i].id] = marked_post
    # Determine if user is following this profile
    follow_text = ''  # Pass empty string if user not logged in
    data_state = ''
    if 'auth_user' in flask.session:
        follow_text = 'Follow'
        data_state = 'not-following'
        client = models.User.query.get(flask.session['auth_user'])
        for followee in client.followees:
            if followee.name == name:
                follow_text = "Unfollow"
                data_state = 'following'
    return flask.render_template('profile.html', user=user, posts=posts, marked_posts=marked_posts,
                                 followText=follow_text, dataState=data_state)


@app.route('/logout')
def handle_logout():
    # user wants to say goodbye, just forget about them
    del flask.session['auth_user']
    # redirect to specfied source URL, or / if none is present
    return flask.redirect(flask.request.args.get('url', '/'))


# function handles 404 URL
@app.errorhandler(404)
def page_not_found(err):
    return flask.render_template('404.html', path=flask.request.path), 404
