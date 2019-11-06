from flask_restful import Resource, reqparse
from models.theme import ThemeModel

class ThemeManager(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('type', type=str, required=True, help="Theme type required")

    def post(self):
        data = ThemeManager.parser.parse_args()

        if ThemeModel.find_by_type(data['type']):
            return {"message": "This theme already exists"}

        theme = ThemeModel(**data)
        theme.save_to_db()
        return {"message": "New Theme saved"}