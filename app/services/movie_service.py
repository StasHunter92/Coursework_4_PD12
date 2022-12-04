from app.dao.models.movie_model import Movie
from app.dao.movie_dao import MovieDAO


# ----------------------------------------------------------------------------------------------------------------------
# Create service class
class MovieService:
    def __init__(self, dao: MovieDAO):
        """
        Initialize service with DAO \n
        :param dao: MovieDAO
        """
        self.dao = dao

    def get_all(self, page: str | None = None, status: str | None = None) -> list:
        """
        Get all movies \n
        :param page: Page number
        :param status: Sort result by year (desc) if status is "new"
        :return: List with movies
        """
        return self.dao.get_all(page, status)

    def get_one(self, movie_id: int) -> Movie:
        """
        Get a single movie \n
        :param movie_id: ID of the movie
        :return: Movie object
        """
        return self.dao.get_one(movie_id)
