from дз_jwt.dao.genre import GenreDAO


class GenreService:
    def __init__(self, genre_dao):
        self.genre_dao = genre_dao

    def get_one(self, bid):
        return self.genre_dao.get_one(bid)

    def get_all(self):
        return self.genre_dao.get_all()

    def create(self, genre_d):
        return self.genre_dao.create(genre_d)

    def update(self, genre_d):
        self.genre_dao.update(genre_d)
        return self.genre_dao

    def delete(self, rid):
        self.genre_dao.delete(rid)
