from flask_restful import Resource, request, reqparse
import requests


class LinkParser(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('url', type=str, location='args')

    def get(self):
        args = LinkParser.parser.parse_args()
        url = args['url']
        print(url)
        response = requests.get(url)
        return response.text
        