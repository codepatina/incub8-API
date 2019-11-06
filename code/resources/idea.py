from flask_restful import Resource, reqparse
from models.idea import IdeaModel

class IdeaCreator(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, required=True, help="Enter title")
    parser.add_argument('tagline', type=str, required=True, help="Tagline required")
    parser.add_argument('description', type=str, required=True, help="Description required")
    parser.add_argument('user_id', type=int, required=True, help="Founder Id cannot be blank")

    def post(self):
        data = IdeaCreator.parser.parse_args()

        if IdeaModel.find_by_title(data['title']):
            return {"message": "A title with that name already exists"}

        idea = IdeaModel(**data)
        idea.save_to_db()

        return {"message": "Idea created successfully"}

    
class Idea(Resource):

    def get(self, title):
        idea = IdeaModel.find_by_title(title)

        if idea:
            return idea.json(), 201

        return {"message": "Idea not found"}, 404
