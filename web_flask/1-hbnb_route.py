#!/usr/bin/python3
""" script that starts a Flask web application:"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """route logic handling connection to the home page"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """handles /hbnb routes"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
