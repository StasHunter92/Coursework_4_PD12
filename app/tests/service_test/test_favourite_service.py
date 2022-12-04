import pytest

from app.services.favourite_service import FavouriteMovieService


# ----------------------------------------------------------------------------------------------------------------------
# Test class for genre service
class TestFavouriteMovieService:
    @pytest.fixture(autouse=True)
    def favourite_service(self, favourite_dao):
        """
        Create a test genre service \n
        """
        self.favourite_service = FavouriteMovieService(favourite_dao)

    def test_get_movie(self):
        movie = self.favourite_service.get_movie({'user_id': 1, 'movie_id': 1})
        assert movie is not None, "Failed to get movie from database"
        assert movie.user_id == 1, "Wrong user_id"
        assert movie.movie_id == 1, "Wrong movie_id"

    def test_add_movie(self):
        assert self.favourite_service.add_movie({'user_id': 1, 'movie_id': 1}) is None, "Something returned"

    def test_delete_movie(self):
        assert self.favourite_service.delete_movie({'user_id': 1, 'movie_id': 1}) is None, "Something returned"
