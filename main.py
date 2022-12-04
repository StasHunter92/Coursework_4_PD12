from flask import Flask
from flask_restx import Api
# from flask_cors import CORS

from app.database.setup_db import db

from app.views.auth_view import auth_ns
from app.views.directors_view import director_ns
from app.views.favourites_view import favourite_ns
from app.views.genres_view import genre_ns
from app.views.movies_view import movie_ns
from app.views.users_view import user_ns

from config import Config

api = Api()
# cors = CORS()


# ----------------------------------------------------------------------------------------------------------------------
# Create application
def create_app(config_object: Config) -> Flask:
    """
    Create a new app with the given config \n
    :param config_object: Config instance
    :return: Flask instance
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)

    # cors.init_app(app)
    db.init_app(app)
    api.init_app(app)
    return app


def register_extensions(app: Flask) -> None:
    """
    Configures the application \n
    :param app: Flask instance
    :return: None
    """
    db.init_app(app)
    # api = Api(doc="/docs")
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)
    api.add_namespace(favourite_ns)
    create_database(app, db)


def create_database(app: Flask, db) -> None:
    """
    Create a new database \n
    :param app: Flask instance
    :param db: SQLAlchemy instance
    :return: None
    """
    with app.app_context():
        db.create_all()


app = create_app(Config())
app.debug = True


# ----------------------------------------------------------------------------------------------------------------------
# Error handlers
@app.errorhandler(404)
def error_404(error):
    """Page 404 error"""
    return f"OOPS! Error {error}, page not found", 404


@app.errorhandler(500)
def error_500(error):
    """Internal server error"""
    return f"OOPS! Error {error}, server have a problem", 500


# ----------------------------------------------------------------------------------------------------------------------
# Run application
if __name__ == "__main__":
    app.run()
