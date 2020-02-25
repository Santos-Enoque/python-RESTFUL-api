import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True,
                        help="This filed cannot be empty")
    parser.add_argument('password', type=str, required=True,
                        help="This filed cannot be empty")

    def post(self):
        # the following line represents how we will get the arguments
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "User already exists"}, 400
      
        user = UserModel(**data)
        user.save_to_db()
        return {"message": "user created"}

