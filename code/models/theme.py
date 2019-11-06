from db import db

class ThemeModel(db.Model):

    __tablename__ = "themes"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String)

    users = db.relationship('UserModel', lazy='dynamic')

    def __init__(self, type):
        self.type = type


    def json(self):
        return {
            'id': self.id,
            'type': self.type,
            'users': [user.json() for user in self.users.all()]
        }

    @classmethod
    def find_by_type(cls, type):
        return cls.query.filter_by(type=type).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
