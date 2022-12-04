from flask import request, abort
from flask_restx import Resource, Namespace

from app.dao.models.movie_model import MovieSchema, Movie
from app.utils.authenticators import auth_required
from app.utils.implemented import movie_service

# ----------------------------------------------------------------------------------------------------------------------
# Create namespace and schemas instance
movie_ns = Namespace("movies")
movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()


# ----------------------------------------------------------------------------------------------------------------------
# Create routes
@movie_ns.route("/")
class MoviesView(Resource):
    @movie_ns.doc(description="Get all movies", params={"page": "Page number"},
                  responses={200: "OK", 401: "Unauthorized"})
    @auth_required
    def get(self):
        """
        Get all movies \n
        :return: JSON response with status code 200 or 401 if unauthorized
        """
        page: str = request.args.get("page")
        status: str = request.args.get("status")

        all_movies: list = movie_service.get_all(page, status)
        return movies_schema.dump(all_movies), 200


@movie_ns.route("/<int:movie_id>/")
@movie_ns.doc(description="Get a single movie", params={"movie_id": "Movie ID"},
              responses={200: "OK", 401: "Unauthorized", 404: "Not Found"})
class MovieView(Resource):
    @auth_required
    def get(self, movie_id: int):
        """
        Get a single movie \n
        :param movie_id: ID of the movie
        :return: JSON response with status code 200 or 401 if unauthorized or 404 if movie is not found
        """
        movie: Movie = movie_service.get_one(movie_id)

        if not movie:
            abort(404, "Invalid movie id")

        return movie_schema.dump(movie), 200
