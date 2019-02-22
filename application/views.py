from flask import session, flash, redirect, render_template, request, url_for
from application import app, db, login_required
from application.auth.models import Usertype, User, Usergroup
from flask_login import current_user
from application.utils import validate as val


@app.route("/")
@login_required(value=30)
def index():
    return render_template("index.html")

@app.route("/usertype", methods=["GET"])
@login_required(value=30)
def usertype_index():
    return render_template("auth/usertype.html", usertypes=Usertype.query.all())

@app.route("/usertype/new", methods=["POST"])
@login_required()
def usertype_create():
    name=request.form.get("name")
    value=float(request.form.get("value"))

    if val.validateStringLength(name, label='Usertype', min = 3) and val.validateNumberBetween(value, 0, 100):
        usertype=Usertype(name, value)
        db.session().add(usertype)
        db.session().commit()
        flash('New usertype added: ' + usertype.name)

    return redirect(url_for("usermanager"))

@app.route("/usergroup", methods=["GET"])
@login_required(value=30)
def usergroup_index():
    return render_template("auth/usergroup.html", usergroups=Usergroup.query.all())

@app.route("/usergroup/new", methods=["POST"])
@login_required(value=50)
def usergroup_create():
    name=request.form.get("name")
    description=request.form.get("description")

    if val.validateStringLength(name, label='Usergroup', min = 3) and val.validateStringLength(description, label='Description', min = 0, max = 500):
        usergroup=Usergroup(name, description)
        db.session().add(usergroup)
        db.session().commit()
        flash('New usergroup added: ' + usergroup.name)

    return redirect(url_for("usermanager"))

@app.route("/usermanager", methods=["GET"])
@login_required(value=30)
def usermanager():
    user = current_user
    usertypes = filter(lambda x: x.value <= user.usertype.value, Usertype.query.all())
    usergroups = user.usergroups
    if user.usertype.value >= 100:
        usergroups = Usergroup.query.all()
    users = User.query.all()
    return render_template("auth/usermanager.html", users=users, usertypes=usertypes, usergroups=usergroups)

@app.route("/user", methods=["GET"])
@login_required(value=30)
def user_index():
    return render_template("auth/user.html", users=User.query.all())

@app.route("/user/new", methods=["POST"])
@login_required(value=50)
def user_create():
    user=current_user

    name=request.form.get("name")
    username=request.form.get("username")
    usertype_id=request.form.get("usertype_id")
    email=request.form.get("email")
    password=request.form.get("password")
    password_re=request.form.get("password_re")

    if val.validateNewUser(name, username, password, password_re, email, usertype_id):
        user=User(name, username, password, email, usertype_id)
        db.session().add(user)
        db.session().commit()
        flash('New user added: ' + user.name)

    return redirect(url_for("usermanager"))

@app.route("/user/register", methods=["POST", "GET"])
def user_register():
    if request.method == "GET":
        return render_template("auth/user_register.html")

    name=request.form.get("name")
    username=request.form.get("username")
    usertype_id=Usertype.query.filter(Usertype.name == 'Normal').one().id
    email=request.form.get("email")
    password=request.form.get("password")
    password_re=request.form.get("password_re")

    if val.validateNewUser(name, username, password, password_re, email, usertype_id):
        user=User(name, username, password, email, usertype_id)
        db.session().add(user)
        db.session().commit()
        flash('New user added: ' + user.name)

    return redirect(url_for("index"))

@app.route("/user/delete", methods=["POST"])
@login_required(value=100)
def user_delete():
    user_id=request.form.get("user_id")
    # user = User.query.get(user_id)
    #
    # for message in user.messages:
    #     message.user_id = None
    #     db.session().add(message)
    # db.session().commit()
    User.query.filter(User.id == user_id).delete()
    db.session.commit()
    flash("User is deleted by id: " + user_id)
    return redirect(url_for("user_index"))

@app.route("/user/update/password", methods=["POST"])
@login_required(value=30)
def user_update_password():
    user = current_user

    password_new=request.form.get("password_new")
    password_new_re=request.form.get("password_new_re")
    password_old=request.form.get("password_old")

    if val.validateUpdatePassword(password_new, password_new_re, password_old, user.password):
        user.password = password_new
        db.session().add(user)
        db.session().commit()
        flash("Password updated!")

    return redirect(url_for("usermanager"))

@app.route("/user/update/information", methods=["POST"])
@login_required(value=30)
def user_update_information():
    user = current_user

    email = request.form.get("email")
    name = request.form.get("name")
    username = request.form.get("username")
    if val.validateEmail(email) and val.validateStringLength(name, label="Name") and val.validateStringLength(username, label="Username"):
        user.email = email
        user.name = name
        user.username = username
        db.session().add(user)
        db.session().commit()
        flash("Information updated!")

    return redirect(url_for("usermanager"))

@app.route("/user/add/usergroup", methods=["POST"])
@login_required(value=50)
def user_add_usergroup():
    user = current_user

    user1_id=request.form.get("user_id")
    user1=User.query.get(user1_id)
    usergroup_id=request.form.get("usergroup_id")
    usergroup=Usergroup.query.get(usergroup_id)

    if user.usertype.value >= 100 or usergroup in user.usergroups:
        user1.usergroups.append(usergroup)
        usergroup.users.append(user1)
        db.session().add(user1)
        #db.session().add(usergroup)
        db.session().commit()
        flash("User " + user1.name + " added to usergroup " + usergroup.name)
    else:
        flash("No permission to the usergroup!")

    return redirect(url_for("usermanager"))
