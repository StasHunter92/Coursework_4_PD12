from app.dao.models.favourite_model import FavouriteMovie


# ----------------------------------------------------------------------------------------------------------------------
# Create DAO model
class FavouriteMovieDAO:
    def __init__(self, session):
        """
        Initialize DAO with session \n
        :param session: Database session
        """
        self.session = session

    def get_movie(self, data: dict) -> FavouriteMovie:
        """
        Get one favourite movie from database by user id and movie id \n
        :param data: Dictionary with user id and movie id
        :return: FavouriteMovie object
        """
        user_id: int = data["user_id"]
        movie_id: int = data["movie_id"]
        favourite_movie = self.session.query(FavouriteMovie).filter(FavouriteMovie.user_id == user_id,
                                                                    FavouriteMovie.movie_id == movie_id).first()
        return favourite_movie

    def add_movie(self, data: dict) -> None:
        """
        Add movie to favourites \n
        :param data: Dictionary with user id and movie id
        :return: None
        """
        new_favourite_movie = FavouriteMovie(**data)
        self.session.add(new_favourite_movie)
        self.session.commit()

    def delete_movie(self, data: dict) -> None:
        """
        Delete movie from favourites \n
        :param data: Dictionary with user id and movie id
        :return: None
        """
        favourite_movie = self.get_movie(data)
        self.session.delete(favourite_movie)
        self.session.commit()
