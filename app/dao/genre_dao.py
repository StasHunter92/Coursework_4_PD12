from flask import current_app

from app.dao.models.genre_model import Genre


# ----------------------------------------------------------------------------------------------------------------------
# Create DAO model
class GenreDAO:
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
        Get all genres \n
        :param page: Page number
        :return: List with genres
        """
        result = self.session.query(Genre)

        if page:
            return result.paginate(page=int(page), per_page=self.items_per_page()).items

        return result.all()

    def get_one(self, genre_id: int) -> Genre:
        """
        Get a single genre \n
        :param genre_id: ID of the genre
        :return: Genre object
        """
        return self.session.query(Genre).get(genre_id)
