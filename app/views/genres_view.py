from flask import request, abort
from flask_restx import Resource, Namespace

from app.dao.models.genre_model import GenreSchema, Genre
from app.utils.authenticators import auth_required
from app.utils.implemented import genre_service

# ----------------------------------------------------------------------------------------------------------------------
# Create namespace and schema instance
genre_ns = Namespace("genres")
genres_schema = GenreSchema(many=True)
genre_schema = GenreSchema()


# ----------------------------------------------------------------------------------------------------------------------
# Create routes
@genre_ns.route("/")
class GenresView(Resource):
    @genre_ns.doc(description="Get all genres", params={"page": "Page number"},
                  responses={200: "OK", 401: "Unauthorized"})
    @auth_required
    def get(self):
        """
        Get all genres \n
        :return: JSON response with status code 200 or 401 if unauthorized
        """
        page: str = request.args.get("page")

        all_genres: list = genre_service.get_all(page)
        return genres_schema.dump(all_genres), 200


@genre_ns.route("/<int:genre_id>/")
@genre_ns.doc(description="Get a single genre", params={"genre_id": "Genre ID"},
              responses={200: "OK", 401: "Unauthorized", 404: "Not Found"})
class GenreView(Resource):
    @auth_required
    def get(self, genre_id: int):
        """
        Get a single genre \n
        :param genre_id: ID of the genre
        :return: JSON response with status code 200 or 401 if unauthorized or 404 if genre is not found
        """
        genre: Genre = genre_service.get_one(genre_id)

        if not genre:
            abort(404, "Invalid genre id")

        return genre_schema.dump(genre), 200
