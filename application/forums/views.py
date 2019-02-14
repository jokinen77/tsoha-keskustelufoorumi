from flask import session, flash, redirect, render_template, request, url_for
from application import app, db
from application.auth.models import Usertype, User, Usergroup
from application.forums.models import Forum, Message
from flask_login import login_required, current_user
from application.utils import validate as val


@app.route("/forums")
@login_required
def forums_index():
    user = current_user

    # For filtering
    keyword = request.args.get('key', '').lower()

    forums = []

    # For showing forums from user's usergroups
    for group in user.usergroups:
        for forum in group.forums:
            if keyword in forum.name.lower():
                forums.append(forum)

    # For showing forums, which have no usergroup, to all the users
    for forum in Forum.query.filter_by(usergroup_id=None).order_by(Forum.date_created).all():
        if keyword in forum.name.lower():
            forums.append(forum)

    # Sorting forums list by date created
    forums.sort(key=lambda forum: forum.date_created, reverse=True)

    return render_template("forums/forums.html", forums=forums, usergroups=user.usergroups)

@app.route("/forums/new", methods=["POST"])
@login_required
def forum_create():
    name=request.form.get("name")
    usergroup_id=request.form.get("usergroup_id")
    if not usergroup_id:
        usergroup_id = None

    if val.validateStringLength(name, label='Forum', min = 3):
        forum=Forum(name, usergroup_id)
        db.session().add(forum)
        db.session().commit()
        flash('New forum added: ' + forum.name)

    return redirect(url_for("forums_index"))

@app.route("/forums/<forum_id>")
@login_required
def forums_show(forum_id=None):
    user_id = session.get('user_id', -1)
    user = User.query.get(user_id)

    forum = Forum.query.get(int(forum_id))
    messages = Message.query.filter_by(forum_id=forum_id).order_by(Message.date).all()

    return render_template("forums/messages.html", forum=forum, messages=messages)

@app.route("/forums/<forum_id>", methods=["POST"])
@login_required
def forum_send_message(forum_id=None):
    content=request.form.get("content")
    user_id = session.get('user_id', -1)

    if val.validateStringLength(content, label='Message', min = 1) and forum_id != None:
        message=Message(content, user_id, forum_id)
        db.session().add(message)
        db.session().commit()
        flash('Message sended')

    return redirect(url_for("forums_show", forum_id=forum_id))
