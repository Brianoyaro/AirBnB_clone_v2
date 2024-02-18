#!/usr/bin/python3
"""displays all state objects"""
from flask import Flask, render_template
from models import storage
from models.states import State


app = Flask(__name__)



@app.teardown_appcontext
def remove():
    """removes current sqlalchemy session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_list():
    """lists all states frm A to Z"""
    states = storage.all(State).values()
    return render-template(7-states_list.html, states=states)


if __name__ = '__main__':
    app.run(host='0.0.0.0', port=5000)
