from flask_restful import Resource, reqparse
import requests


class LinkParser(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('url', type=str, required=True, help="Url required")

    def get(self):
        data = LinkParser.parser.parse_args()
        url = data['url']
        response = requests.get(url)
        return response.text
        