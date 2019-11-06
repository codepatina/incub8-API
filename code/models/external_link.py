from db import db

class ExternalLinkModel(db.Model):
    __tablename__ = "externallinks"

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String)
    icon = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('UserModel')

    def __init__(self, url, icon, user_id):
        self.url = url,
        self.icon = icon,
        self.user_id = user_id

    def json(self):
        return {
            "id": self.id,
            "url": self.url,
            "icon": self.icon,
            "user_id": self.user_id
        }

    @classmethod
    def find_by_url(cls, url):
        return cls.query.filter_by(url=url).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
