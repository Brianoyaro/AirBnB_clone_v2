#!/usr/bin/python3
""" script that starts a Flask web application:"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """route logic handling connection to the home page"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """handles /hbnb routes"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """handles routes to c"""
    text = text.replace("_", " ")
    return "C " + text


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python(text="is cool"):
    """handles routes to python"""
    replaced_text = text.replace("_", " ")
    return "Python " + replaced_text


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """handles routes to /number/some_value_here """
    return "{} is a anumber".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """renders atemplate if n is an integer"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
