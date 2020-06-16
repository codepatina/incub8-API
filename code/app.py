from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWT
from flask_cors import CORS
from db import db
from ma import ma


import os

from security import authenticate, identity
from resources.user import UserRegister, User, UserList
from resources.idea import IdeaCreator, Idea, IdeaList
from resources.contributor_idea import ContributorIdea, ContributorList
from resources.external_link import ExternalLinkManager
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://localhost/incub8dev')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
app.secret_key = 'Nael Saif Khan'
api = Api(app)

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity, )
api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<string:username>')
api.add_resource(UserList, '/users')
api.add_resource(IdeaCreator, '/idea')
api.add_resource(IdeaList, '/ideas')
api.add_resource(ContributorIdea, '/contributor')
api.add_resource(ContributorList, '/contributors')
api.add_resource(ExternalLinkManager, '/link')
@jwt.auth_response_handler
def customized_response_handler(access_token, identity):
    return jsonify({
        'access_token': access_token.decode('utf-8'),
        'user_id': identity.id,
        'username': identity.username


    })
@jwt.jwt_error_handler
def customized_error_handler(error):
    return jsonify({
        'message': error.description,
        'code': error.status_code
    }), error.status_code


if __name__ == '__main__':
    ma.init_app(app)
    
    app.run(port=5001)