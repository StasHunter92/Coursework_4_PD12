import pytest

from unittest.mock import MagicMock

from app.dao.director_dao import DirectorDAO
from app.dao.favourite_dao import FavouriteMovieDAO
from app.dao.genre_dao import GenreDAO
from app.dao.movie_dao import MovieDAO
from app.dao.user_dao import UserDAO
from app.tests.service_test.test_data.director_data import ALL_DIRECTORS, ONE_DIRECTOR
from app.tests.service_test.test_data.favourite_data import FAVOURITE_MOVIE
from app.tests.service_test.test_data.genre_data import ALL_GENRES, ONE_GENRE
from app.tests.service_test.test_data.movie_data import ALL_MOVIES, ONE_MOVIE
from app.tests.service_test.test_data.user_data import ONE_USER, NEW_USER


# ----------------------------------------------------------------------------------------------------------------------
# Mocked fixture for movie dao
@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)
    movie_dao.get_all = MagicMock(return_value=ALL_MOVIES)
    movie_dao.get_one = MagicMock(return_value=ONE_MOVIE)
    return movie_dao


# ----------------------------------------------------------------------------------------------------------------------
# Mocked fixture for director dao
@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)
    director_dao.get_all = MagicMock(return_value=ALL_DIRECTORS)
    director_dao.get_one = MagicMock(return_value=ONE_DIRECTOR)
    return director_dao


# ----------------------------------------------------------------------------------------------------------------------
# Mocked fixture for genre dao
@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)
    genre_dao.get_all = MagicMock(return_value=ALL_GENRES)
    genre_dao.get_one = MagicMock(return_value=ONE_GENRE)
    return genre_dao


# ----------------------------------------------------------------------------------------------------------------------
# Mocked fixture for user dao
@pytest.fixture()
def user_dao():
    user_dao = UserDAO(None)
    user_dao.get_user_by_email = MagicMock(return_value=ONE_USER)
    user_dao.create = MagicMock(return_value=NEW_USER)
    user_dao.update = MagicMock()
    return user_dao


# ----------------------------------------------------------------------------------------------------------------------
# Mocked fixture for favourite dao
@pytest.fixture()
def favourite_dao():
    favourite_dao = FavouriteMovieDAO(None)
    favourite_dao.get_movie = MagicMock(return_value=FAVOURITE_MOVIE)
    favourite_dao.add_movie = MagicMock()
    favourite_dao.delete_movie = MagicMock()
    return favourite_dao
