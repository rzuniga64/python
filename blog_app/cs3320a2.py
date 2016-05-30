import flask
import markdown
from markupsafe import Markup
import models

from init import app, db

blogs = dict()

@app.route('/')
def index():
    # try to get blogs by ID
    all_blogs = models.Blog.query.all()
    if all_blogs is not None:
        for a_blog in all_blogs:
            content = Markup(markdown.markdown(a_blog.entry, output_format='html5'))
            blogs[a_blog.title] = content
        return flask.render_template("index.html", blogs=blogs)  # Flask will look for templates in the templates folder

@app.route('/login')
def login_form():
    # GET request to /login - send the login form
    return flask.render_template('login.html')


@app.route('/login', methods=['POST'])
def handle_login():
    # POST request to /login = check user
    login = flask.request.form['user']
    password = flask.request.form['password']
    # do authentication
    if login == "admin" and password == app.config['ADMIN_PASSWORD']:
        # mark as authenticated and redirect to main page
        flask.session['auth_user'] = "admin"
        return flask.render_template('index.html', blogs=blogs, state='good')
    if login != "admin" or password != app.config['ADMIN_PASSWORD']:
        # not authenticated so return a state = 'bad'
        return flask.render_template('login.html', state='bad')


@app.route('/logout')
def handle_logout():
    # user is logging out so delete them from session
    del flask.session['auth_user']
    # redirect to  main page
    return flask.redirect(flask.url_for('index', blogs=blogs))


@app.route('/postblog')
def post_blog():
    # redirect to  main page
    return flask.render_template('blog_entry.html')


@app.route('/add', methods=['POST'])
def add_blog():
    if 'auth_user' not in flask.session:
        app.logger.warn('unauthorized user tried to add blog')
        flask.abort(401)

    title = flask.request.form['title']
    entry = flask.request.form['blog']
    # create a new blog
    blog = models.Blog()
    # set its properties
    blog.title = title
    blog.entry = entry
    # add it to the database
    db.session.add(blog)
    # commit the database session
    db.session.commit()
    return flask.redirect(flask.url_for('blog', bid=blog.id), code=303)


@app.route('/blog/<int:bid>')
def blog(bid):
    # try to get blog by ID
    theblog = models.Blog.query.get(bid)
    if theblog is None:
        # no blog, we're done
        flask.abort(404)
    else:
        content = Markup(markdown.markdown(theblog.entry, output_format='html5'))
        return flask.render_template('blog.html', blog=theblog, content=content)

if __name__ == '__main__':
    app.run(debug=True)
