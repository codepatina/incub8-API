from flask_restful import Resource, reqparse
from models.external_link import ExternalLinkModel

class ExternalLinkManager(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('url', type=str, required=True, help="Url required")
    parser.add_argument('icon', type=str, required=True, help="Icon required")
    parser.add_argument('user_id', type=int, required=True, help="External link must belong to user, please insert User id")


    def post(self):
        data = ExternalLinkManager.parser.parse_args()

        if ExternalLinkModel.find_by_url(data['url']):
            return {"message": "A link with this URL already exists"}

        link = ExternalLinkModel(**data)
        link.save_to_db()
        return {"message": "Link created for User"}
