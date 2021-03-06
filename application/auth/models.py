from application import db
import application.forums.models
from sqlalchemy.ext.declarative import declarative_base

usergroup_account_table = db.Table('usergroup_account', db.metadata,
    db.Column('account_id', db.Integer, db.ForeignKey('account.id', ondelete="CASCADE")),
    db.Column('usergroup_id', db.Integer, db.ForeignKey('usergroup.id', ondelete="CASCADE"))
)

class User(db.Model):

    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255))
    password = db.Column(db.String(255), nullable=False)

    usertype_id = db.Column(db.Integer, db.ForeignKey('usertype.id'), nullable=False)
    usertype = db.relationship("Usertype", back_populates="user", load_on_pending=True)

    usergroups = db.relationship("Usergroup", secondary=usergroup_account_table, back_populates="users")
    messages = db.relationship("Message", back_populates="user")

    def __init__(self, name, username, password, email, usertype_id):
        self.name = name
        self.username = username
        self.password = password
        self.email = email
        self.usertype_id = usertype_id

    def is_in_usergroup(self, usergroup):
        if self.usertype.value >= 100:
            return True
        if usergroup == None:
            return True
        for group in self.usergroups:
            if group.name == usergroup.name:
                return True
        return False

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def sended_message_count(self):
        stmt = db.text("SELECT COUNT(message.id) FROM account"
                    " LEFT JOIN message ON message.user_id = account.id"
                    " WHERE (account.id = :id)"
                    " GROUP BY account.id").params(id=self.id)
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

class Usergroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String(500))

    forums = db.relationship("Forum", back_populates="usergroup")
    users = db.relationship("User", secondary=usergroup_account_table, back_populates="usergroups")

    def __init__(self, name, description=None):
        self.name = name
        self.description = description


class Usertype(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    value = db.Column(db.Float)

    user = db.relationship("User", back_populates="usertype")

    def __init__(self, name, value=0.0):
        self.name = name
        self.value = value
