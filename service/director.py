from дз_jwt.dao.director import DirectorDAO


class DirectorService:
    def __init__(self, director_dao):
        self.director_dao = director_dao

    def get_one(self, bid):
        return self.director_dao.get_one(bid)

    def get_all(self):
        return self.director_dao.get_all()

    def create(self, director_d):
        return self.director_dao.create(director_d)

    def update(self, director_d):
        self.director_dao.update(director_d)
        return self.director_dao

    def delete(self, rid):
        self.director_dao.delete(rid)