from flask import session, flash, redirect, render_template, request, url_for
from application import app, db
from application.auth.models import Usertype, User
from flask_login import login_required


@app.route("/")
@login_required
def index():
    user_id = session.get('user_id', -1)
    user = User.query.get(user_id)
    return render_template("index.html")

@app.route("/usertype/new", methods=["POST"])
@login_required
def usertype_create():
    name=request.form.get("name")
    value=float(request.form.get("value"))

    valid=True

    if len(name) < 3:
        flash("Usertype's name lenght must be 3 at least!")
        valid=False

    if value > 100 and value < 0:
        flash("Usertype's value must be in range [0,100]!")
        valid=False

    if not valid:
        return redirect(url_for("usermanager"))

    usertype=Usertype(name, value)

    db.session().add(usertype)
    db.session().commit()

    print('New usertype added:', usertype.name)

    return redirect(url_for("usertypes_index"))

@app.route("/usertype", methods=["GET"])
@login_required
def usertypes_index():
    user_id=session.get('user_id', -1)
    return render_template("auth/usertype.html", usertypes=Usertype.query.all())

@app.route("/usermanager", methods=["GET"])
@login_required
def usermanager():
    user_id=session.get('user_id', -1)
    user=User.query.get(user_id)
    usertypes=filter(lambda x: x.value <= user.usertype.value, Usertype.query.all())
    return render_template("auth/usermanager.html", usertypes=usertypes)

@app.route("/user/new", methods=["POST"])
@login_required
def user_create():
    user_id=session.get('user_id', -1)
    user=User.query.get(user_id)

    if user.usertype.value < 50:
        flash("Permission denied!")
        redirect(url_for("usermanager"))

    name=request.form.get("name")
    username=request.form.get("username")
    usertype=request.form.get("usertype_id")
    email=request.form.get("email")
    password=request.form.get("password")
    password1=request.form.get("password1")

    valid=True

    if password != password1:
        flash("Passwords don't match!")
        valid=False

    if len(username) < 3:
        flash("Username lenght must be 3 at least!")
        valid=False

    if not valid:
        return redirect(url_for("usermanager"))

    user=User(name, username, password, email, usertype)

    db.session().add(user)
    db.session().commit()

    print('New user added:', user.name, 'type:', user.usertype.name)

    return redirect(url_for("user_index"))

@app.route("/user", methods=["GET"])
@login_required
def user_index():
    user_id=session.get('user_id', -1)
    return render_template("auth/user.html", users=User.query.all())
