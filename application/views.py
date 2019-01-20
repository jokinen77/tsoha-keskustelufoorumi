from flask import redirect, render_template, request, url_for
from application import app, db
from application.auth.models import Usertype, User

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/usertype/new", methods=["GET"])
def usertype_form():
    return render_template("auth/new_usertype.html")

@app.route("/usertype/new", methods=["POST"])
def usertype_create():
    name = request.form.get("name")
    value = request.form.get("value")
    usertype = Usertype(name, value)

    db.session().add(usertype)
    db.session().commit()

    print('New usertype added:', usertype.name)

    return redirect(url_for("usertypes_index"))

@app.route("/usertype", methods=["GET"])
def usertypes_index():
    return render_template("auth/usertype.html", usertypes = Usertype.query.all())

@app.route("/user/new", methods=["GET"])
def user_form():
    return render_template("auth/new_user.html", usertypes = Usertype.query.all())

@app.route("/user/new", methods=["POST"])
def user_create():
    name = request.form.get("name")
    username = request.form.get("username")
    usertype = request.form.get("usertype_id")
    email = request.form.get("email")
    password = request.form.get("password")
    password1 = request.form.get("password1")

    user = User(name, username, password, email, usertype)

    db.session().add(user)
    db.session().commit()

    print('New user added:', user.name, 'type:', user.usertype.name)

    return redirect(url_for("user_index"))

@app.route("/user", methods=["GET"])
def user_index():
    return render_template("auth/user.html", users = User.query.all())
