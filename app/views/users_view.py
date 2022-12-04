from flask import request, abort
from flask_restx import Namespace, Resource

from app.dao.models.user_model import UserSchema
from app.utils.authenticators import auth_required
from app.utils.implemented import user_service, auth_service

# ----------------------------------------------------------------------------------------------------------------------
# Create namespace and schemas instance
user_ns = Namespace("user")
user_schema = UserSchema()


# ----------------------------------------------------------------------------------------------------------------------
# Create routes
@user_ns.route("/")
class UserView(Resource):
    @user_ns.doc(description="User profile", responses={200: "OK", 401: "Unauthorized", 404: "Not Found"})
    @auth_required
    def get(self):
        """
        Get a single user \n
        :return: JSON response with status code 200 or 401 if unauthorized or 404 if user is not found
        """
        authentication: str = request.headers.get("Authorization")
        token: str = authentication.split("Bearer ")[-1]
        email: str = auth_service.get_email(token)

        user = user_service.get_user(email)

        if user is None:
            abort(404, "User nof found")

        return user_schema.dump(user), 200

    @user_ns.doc(description="User information update", responses={204: "No Content", 401: "Unauthorized"})
    @auth_required
    def patch(self):
        """
        Update user information (without password and email) \n
        :return: No response, 204 or 401 if unauthorized
        """
        authentication: str = request.headers.get("Authorization")
        token: str = authentication.split("Bearer ")[-1]
        email: str = auth_service.get_email(token)

        update_data = user_schema.dump(request.json)
        user_service.update_user(email, update_data)
        return "", 204


@user_ns.route("/password/")
class PasswordView(Resource):
    @user_ns.doc(description="User password update", responses={204: "No Content", 401: "Unauthorized"})
    @auth_required
    def put(self):
        """
        Update user password \n
        :return: No response, 204 or 401 if unauthorized
        """
        authentication = request.headers.get("Authorization")
        token = authentication.split("Bearer ")[-1]
        email = auth_service.get_email(token)

        data = request.json
        user_service.update_password(email, data)
        return "", 204
