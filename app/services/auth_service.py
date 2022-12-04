import calendar
import datetime
import jwt

from flask import abort
from jwt import DecodeError

from app.services.user_service import UserService
from app.utils.secret import JWT_SECRET_KEY, JWT_ALGORITHM


# ----------------------------------------------------------------------------------------------------------------------
# Create authentication service
class AuthService:
    def __init__(self, user_service: UserService):
        """
        Initialize service with UserService \n
        :param user_service: UserService
        """
        self.user_service = user_service

    @staticmethod
    def get_email(token: str) -> str:
        """
        Get the email from the token \n
        :param token: User token
        :return: User email
        """
        data = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return data.get("email")

    def get_access_tokens(self, email: str, password: str | None, is_refresh: bool = False) -> dict | Exception:
        """
        Get a dictionary with the access token and refresh token or Exception \n
        :param email: User email
        :param password: User password
        :param is_refresh: Bool check refresh token is used
        :return: Dictionary with tokens or exception
        """
        user = self.user_service.get_user(email)

        # Check user existence
        if user is None:
            abort(404, "User not found")

        # Check refresh token status and password validity
        if not is_refresh:
            if not self.user_service.compare_password(user.password, password):
                abort(400, "Invalid password")

        data = {
            "email": user.email
        }

        # Generate access token with 1 hour expires
        hour_1 = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        data["expires"] = calendar.timegm(hour_1.timetuple())
        access_token = jwt.encode(data, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)

        # Generate refresh token with 90 days expires
        day_90 = datetime.datetime.utcnow() + datetime.timedelta(days=90)
        data["expires"] = calendar.timegm(day_90.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)

        return {"access_token": access_token, "refresh_token": refresh_token}

    def approve_refresh_token(self, refresh_token: str) -> dict | Exception:
        """
        Get a dictionary with new access token and refresh token or Exception \n
        :param refresh_token: User refresh token
        :return: Dictionary with tokens or exception
        """
        try:
            email = self.get_email(refresh_token)
            return self.get_access_tokens(email, None, is_refresh=True)
        except DecodeError:
            abort(400, "Invalid refresh token")
