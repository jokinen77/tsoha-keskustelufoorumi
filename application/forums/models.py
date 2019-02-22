from application import db
import application.auth.models

class Forum(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    name = db.Column(db.String(255), nullable=False)

    usergroup_id = db.Column(db.Integer, db.ForeignKey('usergroup.id'))
    usergroup = db.relationship("Usergroup", back_populates="forums", load_on_pending=True)
    messages = db.relationship("Message", back_populates="forum")

    def __init__(self, name, usergroup_id):
        self.name = name
        self.usergroup_id = usergroup_id

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=db.func.current_timestamp())
    content = db.Column(db.String(1000))

    user_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=True)
    user = db.relationship("User", back_populates="messages", load_on_pending=True)

    forum_id = db.Column(db.Integer, db.ForeignKey('forum.id'), nullable=False)
    forum = db.relationship("Forum", back_populates="messages", load_on_pending=True)

    def __init__(self, content, user_id, forum_id):
        self.content = content
        self.user_id = user_id
        self.forum_id = forum_id
