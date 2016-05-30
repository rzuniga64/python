import flask
from flask import Flask

#   A Minimal Flask Application
#   Create an instance of this class. The first argument is the name of the application’s module or package.
#   If you are using a single module use __name__ because depending on if it’s started as application or imported as
#   module the name will be different ('__main__' versus the actual import name). This is needed so that Flask knows
#   where to look for templates, static files, and so on.

app = Flask(__name__)

#   The route() decorator is used to bind a function to a URL
#   Use the route() decorator to tell Flask what URL should trigger our function.
@app.route( '/')
def hello_world():
    return flask.render_template("index.html")  # Flask will look for templates in the templates folder

#   Finally we use the run() function to run the local server with our application. The if __name__ == '__main__':
#   makes sure the server only runs if the script is executed directly from the Python interpreter and not used as an
#   imported module.

#   If you enable debug support the server will reload itself on code changes, and it will also provide you with a
#   helpful debugger if things go wrong.
if __name__ == '__main__':
    app.run()
