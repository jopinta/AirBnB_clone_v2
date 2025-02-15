#!/usr/bin/python3
'''starting flasf web application'''

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''adding routes'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hi_hbnb():
    '''an other one'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text():
    '''display with value'''
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>')
def python(text="is cool"):
    '''same with py'''
    return 'Python {}'.format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    '''same with integer'''
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def template(n):
    """display if n is an int"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', srict_slashes=False)
def par_inpar(n):
    '''even or odd to display if is int'''
    if (n % 2 == 0):
        return (render_template('6-number_odd_or_even.html', n=n, even=True))
    else:
        return (render_template('6-number_odd_or_even.html', n=n, even=False))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
