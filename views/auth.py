from flask import request
from flask_restx import Resource, Namespace

from дз_jwt.dao.model.movie import MovieSchema
from дз_jwt.implemented import movie_service, auth_service, user_service

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):

    def post(self):
        req_json = request.json
        username = req_json.get('username', None)
        password = req_json.get('password', None)
        if None in [username, password]:
            return '', 400

        tokens = auth_service.generate_tokens(username, password)

        return tokens
        # movie = movie_service.create(req_json)
        # return "", 201, {"location": f"/movies/{movie.id}"}

    def put(self):
        req_json = request.json
        token = req_json.get('refresh_token')
        tokens = auth_service.approve_refresh_token(token)
        return '', 201


