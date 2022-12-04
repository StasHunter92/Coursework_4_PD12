from flask import request, abort
from flask_restx import Resource, Namespace

from app.dao.models.director_model import DirectorSchema, Director
from app.utils.authenticators import auth_required
from app.utils.implemented import director_service

# ----------------------------------------------------------------------------------------------------------------------
# Create namespace and schemas instance
director_ns = Namespace("directors")
directors_schema = DirectorSchema(many=True)
director_schema = DirectorSchema()


# ----------------------------------------------------------------------------------------------------------------------
# Create routes
@director_ns.route("/")
class DirectorsView(Resource):
    @director_ns.doc(description="Get all directors", params={"page": "Page number"},
                     responses={200: "OK", 401: "Unauthorized"})
    @auth_required
    def get(self):
        """
        Get all directors \n
        :return: JSON response with status code 200 or 401 if unauthorized
        """
        page: str = (request.args.get("page"))

        all_directors: list = director_service.get_all(page)
        return directors_schema.dump(all_directors), 200


@director_ns.route("/<int:director_id>/")
@director_ns.doc(description="Get a single director", params={"director_id": "Director ID"},
                 responses={200: "OK", 401: "Unauthorized", 404: "Not Found"})
class DirectorView(Resource):

    @auth_required
    def get(self, director_id: int):
        """
        Get a single director \n
        :param director_id: ID of the director
        :return: JSON response with status code 200 or 401 if unauthorized or 404 if director is not found
        """
        director: Director = director_service.get_one(director_id)

        if not director:
            abort(404, "Invalid director id")

        return director_schema.dump(director), 200
