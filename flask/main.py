"""A simple flask app"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Simple hello world route function"""
    return "<p>Hello, Godric!</p>"
