from flask import session, flash, render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from application import app, db
from application.auth.models import Usertype, User
from application.auth.forms import LoginForm#, UpdateEmailForm, UpdatePasswordForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/login_form.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/login_form.html", form = form,
                                error = "No such username or password")
    session['user_id'] = user.id

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

# @app.route("/user/update/email", methods = ["GET", "POST"])
# @login_required
# def user_update_email():
#     if request.method == "GET":
#         return render_template("auth/update_email_form.html", form = UpdateEmailForm())
#
#     form = UpdateEmailForm(request.form)
#     if not form.validate():
#         return render_template("auth/update_email_form.html", form = form)
#
#     user_id = session.get('user_id', -1)
#     user = User.query.get(user_id)
#
#     user.email = form.email.data
#     db.session().add(user)
#     db.session().commit()
#     flash("Email updated!")
#
#     return render_template("auth/update_email_form.html", form = UpdateEmailForm())
#
# @app.route("/user/update/password", methods = ["GET", "POST"])
# @login_required
# def user_update_password():
#     if request.method == "GET":
#         return render_template("auth/update_password_form.html", form = UpdatePasswordForm())
#
#     form = UpdatePasswordForm(request.form)
#     if not form.validate():
#         return render_template("auth/update_password_form.html", form = form)
#
#     user_id = session.get('user_id', -1)
#     user = User.query.get(user_id)
#
#     password_old = form.password_old.data
#
#     if user.password == password_old:
#         user.password = form.password_new.data
#         db.session().add(user)
#         db.session().commit()
#         flash("Password updated!")
#     else:
#         flash("Password could't be updated! Old password is incorrect!")
#
#     return render_template("auth/update_password_form.html", form = UpdatePasswordForm())
