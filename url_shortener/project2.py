import flask
import uuid
import base64
import json
import os

app = flask.Flask(__name__)

bookmark_file = 'bookmark.json'

urls = {}

if os.path.exists(bookmark_file):
    with open(bookmark_file, 'r', encoding="utf8") as the_urls:
        urls = json.load(the_urls)
        print(urls)


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/shorten', methods=['POST'])
def shorten():
    url = flask.request.form['url']
    # Redirect to website if key is in dictionary
    for url_key in urls:
        if urls[url_key] == url:
            return flask.redirect(flask.url_for('shortened_url', key=url_key))
    # If key is not in dictionary, add to dictionary and go to preview page
    key = base64.urlsafe_b64encode(uuid.uuid4().bytes)[:12].decode('ascii')
    urls[key] = url
    with open(bookmark_file, 'w') as outfile: # Output dictionary to output file
        json.dump(urls, outfile)
    return flask.redirect(flask.url_for('shortened_url', key=key) + '?preview=1', code=302)


@app.route('/<key>')
def shortened_url(key):
    if key not in urls:
        flask.abort(404)
    if 'preview' in flask.request.args:
        preview = flask.request.args['preview']
    else:
        preview = '0'
    if preview is '1':
        return flask.render_template('preview.html', key=key, url=urls[key])
    else:
        return flask.redirect(urls[key], code=301)


# function handles 404 URL
@app.errorhandler(404)
def page_not_found(err):
    return flask.render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
