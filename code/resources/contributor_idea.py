from flask_restful import Resource, reqparse
from models.contributor_idea import ContributorIdeaModel

class ContributorIdea(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('user_id', required=True, type=int, help="Builder id required")
    parser.add_argument('idea_id', required=True, type=int, help="Idea id required")

    def post(self):
        data = ContributorIdea.parser.parse_args()


        contributoridea = ContributorIdeaModel(**data)
        contributoridea.save_to_db()

        return {"message": "Contributor created successfully"}

class ContributorList(Resource):
    def get(self):
        return {"contributors": list(map(lambda contributor: contributor.json(), ContributorIdeaModel.query.all()))}
