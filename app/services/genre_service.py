from app.dao.genre_dao import GenreDAO
from app.dao.models.genre_model import Genre


# ----------------------------------------------------------------------------------------------------------------------
# Create service class
class GenreService:
    def __init__(self, dao: GenreDAO):
        """
        Initialize service with DAO \n
        :param dao: GenreDAO
        """
        self.dao = dao

    def get_all(self, page: str | None = None) -> list:
        """
        Get all genres \n
        :param page: Page number
        :return: List with genres
        """
        return self.dao.get_all(page)

    def get_one(self, genre_id: int) -> Genre:
        """
        Get a single genre \n
        :param genre_id: ID of the genre
        :return: Genre object
        """
        return self.dao.get_one(genre_id)
