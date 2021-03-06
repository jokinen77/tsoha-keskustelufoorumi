from flask import session, flash, redirect, render_template, request, url_for
from application import app, db, login_required
from application.auth.models import Usertype, User, Usergroup
from application.forums.models import Forum, Message
from flask_login import current_user
from application.utils import validate as val


@app.route("/forums")
@login_required(value=30)
def forums_index():
    # For filtering
    keyword = request.args.get('key', '').lower()
    only_forums_user_have_posted_to = request.args.get('only_forums_user_have_posted_to', '').lower()

    forums = []

    # For showing forums from user's usergroups
    for group in current_user.usergroups:
        for forum in group.forums:
            if keyword in forum.name.lower():
                forums.append(forum)

    # For showing forums, which have no usergroup, to all the users
    for forum in Forum.query.filter_by(usergroup_id=None).order_by(Forum.date_created).all():
        if keyword in forum.name.lower():
            forums.append(forum)


    # Filter forums which user have posted to
    if only_forums_user_have_posted_to:
        forum_names = list(map(lambda message: message.forum.name, current_user.messages))
        forums = list(filter(lambda forum: forum.name in forum_names, forums))


    # Sorting forums list by date created
    forums.sort(key=lambda forum: forum.date_created, reverse=True)

    return render_template("forums/forums.html", forums=forums, usergroups=current_user.usergroups)

@app.route("/forums/new", methods=["POST"])
@login_required(value=30)
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
@login_required(value=30)
def forums_show(forum_id=None):
    forum = Forum.query.get(int(forum_id))

    if not current_user.is_in_usergroup(forum.usergroup):
        flash('No permission to this forum!')
        return redirect(url_for("forums_index"))

    messages = Message.query.filter_by(forum_id=forum_id).order_by(Message.date).all()

    return render_template("forums/messages.html", forum=forum, messages=messages)

@app.route("/forums/<forum_id>", methods=["POST"])
@login_required(value=30)
def forum_send_message(forum_id=None):
    content=request.form.get("content")
    user_id = session.get('user_id', -1)
    forum = Forum.query.get(int(forum_id))

    if not current_user.is_in_usergroup(forum.usergroup):
        flash('No permission to this forum!')
        return redirect(url_for("forums_index"))

    if val.validateStringLength(content, label='Message', min = 1, max = 1000) and forum_id != None:
        message=Message(content, current_user.id, forum_id)
        db.session().add(message)
        db.session().commit()
        flash('Message sended')

    return redirect(url_for("forums_show", forum_id=forum_id))

@app.route("/forums/<forum_id>/delete/message", methods=["POST"])
@login_required(value=100)
def forum_delete_message(forum_id=None):
    message_id=request.form.get("message_id")

    try:
        message = Message.query.get(int(message_id))
        db.session().delete(message)
        db.session().commit()
        flash("Message deleted with id:" + message_id)
    except:
        flash("Message didn't found!")

    return redirect(url_for("forums_show", forum_id=forum_id))
