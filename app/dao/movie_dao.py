from flask import current_app
from sqlalchemy import desc

from app.dao.models.movie_model import Movie


# ----------------------------------------------------------------------------------------------------------------------
# Create DAO model
class MovieDAO:
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

    def get_all(self, page: str | None = None, status: str | None = None) -> list:
        """
        Get all movies \n
        :param page: page number
        :param status: Sort result by year (desc) if status is "new"
        :return: List with movies
        """
        result = self.session.query(Movie)

        if status == "new":
            result = result.order_by(desc(Movie.year))

        if page:
            return result.paginate(page=int(page), per_page=self.items_per_page()).items

        return result.all()

    def get_one(self, movie_id: int) -> Movie:
        """
        Get a single movie \n
        :param movie_id: ID of the movie
        :return: Movie object
        """
        return self.session.query(Movie).get(movie_id)
