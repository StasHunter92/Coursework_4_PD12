from app.dao.favourite_dao import FavouriteMovieDAO
from app.dao.models.favourite_model import FavouriteMovie


# ----------------------------------------------------------------------------------------------------------------------
# Create service class
class FavouriteMovieService:
    def __init__(self, dao: FavouriteMovieDAO):
        """
        Initialize service with DAO \n
        :param dao: FavouriteMovieDAO
        """
        self.dao = dao

    def get_movie(self, data: dict) -> FavouriteMovie:
        """
        Get one favourite movie from database by user id and movie id \n
        :param data: Dictionary with user id and movie id
        :return: FavouriteMovie object
        """
        return self.dao.get_movie(data)

    def add_movie(self, data: dict) -> None:
        """
        Add movie to favourites \n
        :param data: Dictionary with user id and movie id
        :return: None
        """

        self.dao.add_movie(data)

    def delete_movie(self, data: dict) -> None:
        """
        Delete movie from favourites \n
        :param data: Dictionary with user id and movie id
        :return: None
        """
        self.dao.delete_movie(data)
