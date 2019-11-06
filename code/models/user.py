from db import db
from werkzeug.security import generate_password_hash, check_password_hash

class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String)
    bio = db.Column(db.String(500))
    avatar = db.Column(db.String)

    ideas = db.relationship('IdeaModel', lazy='dynamic')
    contributorideas = db.relationship('ContributorIdeaModel', lazy='dynamic')
    externallinks = db.relationship('ExternalLinkModel', lazy='dynamic')
    theme_id = db.Column(db.Integer, db.ForeignKey('themes.id'))
    theme = db.relationship('ThemeModel')

    def __init__(self, username, password, first_name, last_name, email, bio, theme_id):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.bio = bio,
        self.theme_id = theme_id

    def json(self):
        return {
            'id': self.id,
            'username': self.username,
            'first name': self.first_name,
            'last name': self.last_name,
            'email': self.email,
            'bio': self.bio,
            'theme_id': self.theme_id,
            'founded_ideas': [idea.json() for idea in self.ideas.all()],
            'contributed_to': [contributoridea.json() for contributoridea in self.contributorideas.all()],
            'external_links': [external_link.json() for external_link in self.externallinks.all()]
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    
    
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

