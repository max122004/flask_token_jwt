from дз_jwt.dao.movie import MovieDAO


class MovieService:
    def __init__(self, movie_dao):
        self.movie_dao = movie_dao

    def get_one(self, bid):
        return self.movie_dao.get_one(bid)

    def get_all(self, filters):
        if filters.get("director_id") is not None:
            movies = self.movie_dao.get_by_director_id(filters.get("director_id"))
        elif filters.get("genre_id") is not None:
            movies = self.movie_dao.get_by_genre_id(filters.get("genre_id"))
        elif filters.get("year") is not None:
            movies = self.movie_dao.get_by_year(filters.get("year"))
        else:
            movies = self.movie_dao.get_all()
        return movies

    def create(self, movie_d):
        return self.movie_dao.create(movie_d)

    def update(self, movie_d):
        self.movie_dao.update(movie_d)
        return self.movie_dao

    def delete(self, rid):
        self.movie_dao.delete(rid)
