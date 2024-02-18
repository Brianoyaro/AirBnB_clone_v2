#!/usr/bin/python3
"""module displaying cities and state"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """deletes current sqlalchemy Session."""
    storage.close()


@app.route('/states', strict_slashes=False)
def state():
    """Lists all states."""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """Displays a State by id."""
    key = "State.{}".format(id)
    if key in storage.all():
        state = storage.all()[key]
    else:
        state = None
    return render_template('9-states.html', state=state)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
