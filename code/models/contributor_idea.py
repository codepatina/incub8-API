from db import db

class ContributorIdeaModel(db.Model):
    __tablename__ = 'contributorideas'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('UserModel')
    idea_id = db.Column(db.Integer, db.ForeignKey('ideas.id'))
    idea = db.relationship('IdeaModel')

    def __init__(self, user_id, idea_id):
        self.user_id = user_id
        self.idea_id = idea_id

    def json(self): 
        return {
            'id': self.id,
            'user_id': self.user_id,
            'idea': self.idea_id
        }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
