#!/usr/bin/python3
"""Displays State and Cities in /states/<id>."""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """Disposes of the current Session."""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Displays a States, Cities and Amenities."""
    return render_template(
        "10-hbnb_filters.html",
        states=storage.all(State).values(),
        amenities=storage.all(Amenity).values()
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
