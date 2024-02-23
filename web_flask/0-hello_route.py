#!/usr/bin/python3

"""the `0-hello_route` module
starts a flask web application listening on `0.0.0.0:5000`
"""

<<<<<<< HEAD
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """returns `Hello HBNB!` message"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
=======
"""
starts a Flask web application
"""

=======
>>>>>>> 00da37a2c99807fe12c53439eec2d906eebefd27
from flask import Flask
app = Flask(__name__)


<<<<<<< HEAD
@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

=======
@app.route('/')
def hello_flask():
    """Return string when route queried
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 00da37a2c99807fe12c53439eec2d906eebefd27
