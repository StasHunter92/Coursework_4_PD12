from app.database.setup_db import db

from app.dao.director_dao import DirectorDAO
from app.dao.genre_dao import GenreDAO
from app.dao.movie_dao import MovieDAO
from app.dao.user_dao import UserDAO
from app.dao.favourite_dao import FavouriteMovieDAO

from app.services.director_service import DirectorService
from app.services.genre_service import GenreService
from app.services.movie_service import MovieService
from app.services.user_service import UserService
from app.services.auth_service import AuthService
from app.services.favourite_service import FavouriteMovieService

# ----------------------------------------------------------------------------------------------------------------------
# Create DAO instance
director_dao = DirectorDAO(db.session)
genre_dao = GenreDAO(db.session)
movie_dao = MovieDAO(db.session)
user_dao = UserDAO(db.session)
favourite_dao = FavouriteMovieDAO(db.session)
# ----------------------------------------------------------------------------------------------------------------------
# Create Service instance
director_service = DirectorService(director_dao)
genre_service = GenreService(genre_dao)
movie_service = MovieService(movie_dao)
user_service = UserService(user_dao)
auth_service = AuthService(user_service)
favourite_service = FavouriteMovieService(favourite_dao)
