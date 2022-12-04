from app.dao.director_dao import DirectorDAO
from app.dao.models.director_model import Director


# ----------------------------------------------------------------------------------------------------------------------
# Create service class
class DirectorService:
    def __init__(self, dao: DirectorDAO):
        """
        Initialize service with DAO \n
        :param dao: DirectorDAO
        """
        self.dao = dao

    def get_all(self, page: str | None = None) -> list:
        """
        Get all directors \n
        :param page: Page number
        :return: List with directors
        """
        return self.dao.get_all(page)

    def get_one(self, director_id: int) -> Director:
        """
        Get a single director \n
        :param director_id: ID of the director
        :return: Director object
        """
        return self.dao.get_one(director_id)
