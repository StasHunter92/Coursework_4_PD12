import pytest

from app.services.movie_service import MovieService


# ----------------------------------------------------------------------------------------------------------------------
# Test class for movie service
class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        """
        Create a test movie service \n
        :param movie_dao: Mocked movie dao
        """
        self.movie_service = MovieService(movie_dao)

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert movies is not None, "Failed to get movies from database"
        assert len(movies) > 0, "Empty list of movies"

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None, "Failed to get movie from database"
        assert movie.id == 1, "Wrong movie id"
        assert movie.title == "Movie_1", "Wrong movie title"
