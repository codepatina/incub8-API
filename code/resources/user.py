from flask_restful import Resource, reqparse
from models.user import UserModel
from flask_jwt import jwt_required, current_identity

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', 
    type=str, 
    required=True, 
    help="Username cannot be empty"
    )
    parser.add_argument('password', type=str,
    required=True,
    help="Password cannot be empty"
    )
    parser.add_argument('name', 
    type=str, required=True, 
    help="First Name is required"
    )
    
    parser.add_argument('email', type=str, required=True, help="Email cannot be blank")
    parser.add_argument('bio', type=str, required=True, help="Please fill out bio")

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(**data)
        user.set_password(data['password'])  # same as data['username'], data['password']
        user.save_to_db()

        return {"message": "User created successfully"}, 201

class User(Resource):
    def get(self, username):
        user = UserModel.find_by_username(username)
        if user:
            return user.json(), 201
            
        return {"message": "User not found"}, 404

class UserList(Resource):
     def get(self):
        return {'users': list(map(lambda user: user.json(), UserModel.query.all()))}
