from flask import Flask, render_template, redirect, url_for, request
from flask_login import (
    LoginManager,
    UserMixin,
    current_user,
    login_user,
)


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


app.run()
