#!/usr/bin/python3

"""the `0-hello_route` module
starts a flask web application listening on `0.0.0.0:5000`
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_flask():
    """Return string when route queried
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
