from flask import Flask
from flask.wrappers import Request

app = Flask(__name__)


@app.route("/welcome")
def welcome_page():
    return "<h1>Welcome</h1>"


@app.route("/welcome/<term>")
def welcome_back_or_home(term):

    return f"<h1>Welcome {term}</h1>"
