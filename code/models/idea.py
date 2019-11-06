from db import db
from models.user import UserModel
from flask import jsonify

class IdeaModel(db.Model):

    __tablename__ = 'ideas'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    tagline = db.Column(db.String)
    description = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('UserModel')
    contributorideas = db.relationship('ContributorIdeaModel', lazy='dynamic')


    def __init__(self, title, tagline, description, user_id):
        self.title =  title
        self.tagline = tagline
        self.description = description
        self.user_id = user_id

    def json(self):
        return {
            'id': self.id,
            'tagline': self.tagline,
            'description': self.description,
            'user_id': self.user_id,
            'contributors': [contributoridea.json() for contributoridea in self.contributorideas.all()]

        }

    @classmethod
    def find_by_title(cls, title):
        return cls.query.filter_by(title=title).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
