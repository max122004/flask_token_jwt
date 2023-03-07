from flask import request
from flask_restx import Resource, Namespace

from дз_jwt.dao.model.user import UserSchema
from дз_jwt.helpers import admin_required
from дз_jwt.implemented import user_service, auth_service

user_ns = Namespace('user')


@user_ns.route('/')
class UserView(Resource):
    def get(self):
        users = user_service.get_all()
        result = UserSchema(many=True).dump(users)
        return result, 200

    def post(self):
        req_json = request.json
        user_service.create_user(req_json)
        return '', 201


@user_ns.route('/<int:mid>')
class UserView(Resource):
    @admin_required
    def delete(self, mid):
        user_service.delete(mid)

        return '', 204


