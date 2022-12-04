from flask import request, abort
from flask_restx import Namespace, Resource

from app.utils.implemented import user_service, auth_service

# ----------------------------------------------------------------------------------------------------------------------
# Create namespace
auth_ns = Namespace("auth")


# ----------------------------------------------------------------------------------------------------------------------
# Create routes
@auth_ns.route("/register/")
class RegistrationView(Resource):
    @auth_ns.doc(description="User registration", responses={201: "Created", 400: "Bad Request"})
    @auth_ns.response(201, "Created", headers={"location": "/user/user_id"})
    def post(self):
        """
        User registration \n
        :return: Status code 201 with location or 400 if email or password is empty or user already exists
        """
        email: str = request.json.get("email")
        password: str = request.json.get("password")

        if None in [email, password]:
            abort(400, "Email or password is empty")

        data = {
            "email": email,
            "password": password
        }

        user = user_service.create_user(data)
        return "", 201, {"location": f"/user/{user.id}"}


@auth_ns.route("/login/")
class LoginView(Resource):
    @auth_ns.doc(description="User login", responses={201: "Created", 400: "Bad Request", 404: "Not Found"})
    def post(self):
        """
        User login \n
        :return: Authorization tokens or (404, 400) status code if error occurs
        """
        email = request.json.get("email")
        password = request.json.get("password")

        if None in [email, password]:
            abort(400, "Email or password is empty")

        return auth_service.get_access_tokens(email, password), 201

    @auth_ns.doc(description="Refresh tokens", responses={201: "Created", 400: "Bad Request", 404: "Not Found"})
    def put(self):
        """
        Refresh authorization tokens \n
        :return: New authorization tokens or (404, 400) status code if error occurs
        """
        refresh_token = request.json.get("refresh_token")

        if not refresh_token:
            abort(400, "Refresh token is empty")

        return auth_service.approve_refresh_token(refresh_token), 201
