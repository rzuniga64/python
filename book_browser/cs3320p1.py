import flask
import json

app = flask.Flask(__name__)

authors = {}
books = {}
edition_count = 0
numOfauthors = 0

with open('data/authors.json', 'r', encoding="utf8") as a:
    author = json.load(a)
    for auth in author:
        authors[auth['id']] = auth

with open('data/books.json', 'r', encoding="utf8") as b:
    book = json.load(b)
    for booky in book:
        books[booky['id']] = booky
        for editions in booky['editions']:
            edition_count += 1
            if 'publish_date' not in editions:
                editions['publish_date'] = 'Undated'


# function handles index URL
@app.route('/')
def index():
    return flask.render_template('index.html', books=books.values(), authors=authors, numOfbooks=len(books),
                                 numOfauthors=len(author), edition_count=edition_count)


@app.route('/authors/')
def list_of_authors():
    for author in authors.values():
        if author['name'] is None:
            author['name'] = 'Anonymous'
        if 'name' not in author:
            author['name'] = 'Unknown'
    return flask.render_template('authors.html', authors=authors.values())


# function handles URL for list of books
@app.route('/books/')
def list_of_books():
    return flask.render_template('books.html', books=books.values())


# function handles URL for a book
@app.route('/books/<bid>/')
def book_page(bid):
    # check if bid is good
    if bid not in books:
        flask.abort(404)
    # check for cover
    cover_id = None
    for edition in books[bid]['editions']:
        if 'cover' in edition:
            cover_id = edition['cover']
            break
    # check for publish_date in editions
    return flask.render_template('book.html', book=books[bid], authors=authors, cover_id=cover_id)


# function handles URL for a book
@app.route('/authors/<aid>/')
def author_page(aid):
    # check if aid is good
    if aid not in authors:
        flask.abort(404)
    for author in authors.values():
        if 'death_date' not in author:
            author['death_date'] = 'N/A'
        if 'birth_date' not in author:
            author['birth_date'] = 'N/A'
        if 'bio' not in author:
            author['bio'] = 'No bio is available'
    return flask.render_template('author.html', books=books.values(), author=authors[aid], authors=authors)

# function handles URL for the book editions
@app.route('/books/<bid>/editions/<eid>')
def book_edition(bid, eid):
    if bid not in books:
        flask.abort(404)
    for ed in books[bid]['editions']:
        if ed['id'] == eid:
            edition = ed
    return flask.render_template('editions.html', book=books[bid], authors=authors, edition=edition)


# function handles 404 URL
@app.errorhandler(404)
def page_not_found(err):
    return flask.render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
