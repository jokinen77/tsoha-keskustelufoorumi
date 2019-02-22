from flask import flash, redirect, render_template, request, url_for
from application import app, db, login_required
from application.auth.models import Usertype, User, Usergroup
from flask_login import current_user
from application.utils import validate as val


@app.route("/")
@login_required(value=30)
def index():
    return render_template("index.html")
