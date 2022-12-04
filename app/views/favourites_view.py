from flask import request, abort
from flask_restx import Namespace, Resource

from app.dao.models.favourite_model import FavouriteMovieSchema
from app.utils.authenticators import auth_required
from app.utils.implemented import user_service, auth_service, favourite_service, movie_service

# ----------------------------------------------------------------------------------------------------------------------
# Create namespace and schema instance
favourite_ns = Namespace("favourites")
favourite_schema = FavouriteMovieSchema()


# ----------------------------------------------------------------------------------------------------------------------
# Create routes
@favourite_ns.doc(params={"movie_id": "Movie ID"})
@favourite_ns.route("/movies/<int:movie_id>")
class FavouriteView(Resource):
    @favourite_ns.doc(description="Add a movie",
                      responses={201: "Created", 400: "Bad Request", 401: "Unauthorized", 404: "Not Found"})
    @auth_required
    def post(self, movie_id: int):
        """
        Add movie to favourites \n
        :return: JSON response with status code 201 or 400 if movie already exists
         or 401 if unauthorized or 404 if user or movie is not found
        """
        authentication: str = request.headers.get("Authorization")
        token: str = authentication.split("Bearer ")[-1]
        email: str = auth_service.get_email(token)

        user = user_service.get_user(email)

        if user is None:
            abort(404, "User nof found")

        movie = movie_service.get_one(movie_id)

        if movie is None:
            abort(404, "Movie not found")

        data = {"user_id": user.id, "movie_id": movie.id}
        favourite_movie = favourite_service.get_movie(data)

        if favourite_movie:
            abort(404, "Movie already in favorites")

        favourite_service.add_movie(data)
        return "", 201

    @favourite_ns.doc(description="Delete a movie",
                      responses={204: "No Content", 401: "Unauthorized", 404: "Not Found"})
    @auth_required
    def delete(self, movie_id):
        """
        Delete movie from favourites \n
        :return: No response 204 or 401 if unauthorized or 404 if user or movie is not found
        """
        authentication: str = request.headers.get("Authorization")
        token: str = authentication.split("Bearer ")[-1]
        email: str = auth_service.get_email(token)

        user = user_service.get_user(email)

        if user is None:
            abort(404, "User nof found")

        movie = movie_service.get_one(movie_id)

        if movie is None:
            abort(404, "Movie not found")

        if not favourite_service.get_movie({"user_id": user.id, "movie_id": movie.id}):
            abort(404, "Movie already deleted")

        favourite_service.delete_movie({"user_id": user.id, "movie_id": movie.id})
        return "", 204
