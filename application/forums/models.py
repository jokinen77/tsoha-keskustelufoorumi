from application import db

class Forum(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    name = db.Column(db.String(255), nullable=False)

    usergroup_id = db.Column(db.Integer, db.ForeignKey('usergroup.id'),
                           nullable=False)

    def __init__(self, name, usergroup_id):
        self.name = name
        self.usergroup_id = usergroup_id
