from flask import current_app

from app.dao.models.director_model import Director


# ----------------------------------------------------------------------------------------------------------------------
# Create DAO model
class DirectorDAO:
    def __init__(self, session):
        """
        Initialize DAO with session \n
        :param session: Database session
        """
        self.session = session

    @staticmethod
    def items_per_page() -> int:
        """
        Get the number of items per page for paginate \n
        :return: Integer number from app config
        """
        return current_app.config.get("ITEMS_PER_PAGE")

    def get_all(self, page: str | None = None) -> list:
        """
        Get all directors \n
        :param page: Page number
        :return: List with directors
        """
        result = self.session.query(Director)

        if page:
            return result.paginate(page=int(page), per_page=self.items_per_page()).items

        return result.all()

    def get_one(self, director_id: int) -> Director:
        """
        Get a single director \n
        :param director_id: ID of the director
        :return: Director object
        """
        return self.session.query(Director).get(director_id)
