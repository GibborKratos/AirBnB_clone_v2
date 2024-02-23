#!/usr/bin/python3
<<<<<<< HEAD
<<<<<<< HEAD
"""the `7-states_list` module
=======
"""
>>>>>>> 212529db4b955a72d996660137790c2497399ff5
starts a Flask web application
"""

from flask import Flask, render_template
<<<<<<< HEAD
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states_list")
def states_list():
    """fetchs the list of states from the database and displays it"""
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    return render_template("7-states_list.html", states=states)
=======
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a HTML page with the states listed in alphabetical order"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)
>>>>>>> 212529db4b955a72d996660137790c2497399ff5


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

<<<<<<< HEAD

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
=======
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
>>>>>>> 212529db4b955a72d996660137790c2497399ff5
=======
"""Start web application with two routings
"""

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states_list')
def states_list():
    """Render template with states
    """
    path = '7-states_list.html'
    states = storage.all(State)
    # sort State object alphabetically by name
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template(path, sorted_states=sorted_states)


@app.teardown_appcontext
def app_teardown(arg=None):
    """Clean-up session
    """
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 00da37a2c99807fe12c53439eec2d906eebefd27
