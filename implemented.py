from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO
from service.director import DirectorService
from service.genre import GenreService
from service.movie import MovieService
from setup_db import db
from дз_jwt.dao.user import UserDAO
from дз_jwt.service.auth import AuthService
from дз_jwt.service.user import UserService

director_dao = DirectorDAO(db.session)
genre_dao = GenreDAO(db.session)
movie_dao = MovieDAO(db.session)
user_dao = UserDAO(db.session)

director_service = DirectorService(director_dao)
genre_service = GenreService(genre_dao)
movie_service = MovieService(movie_dao)
user_service = UserService(user_dao)
auth_service = AuthService(user_service)
