import base64
import hashlib
import hmac

from flask import abort

from app.dao.models.user_model import User
from app.dao.user_dao import UserDAO
from app.utils.secret import HASH_SALT, HASH_ITERATIONS


# ----------------------------------------------------------------------------------------------------------------------
# Create service class
class UserService:
    def __init__(self, dao: UserDAO):
        """
        Initialize service with DAO \n
        :param dao: UserDAO
        """
        self.dao = dao

    @staticmethod
    def hash_password(password: str) -> bytes:
        """
        Encode user password using hashlib algorithm \n
        :param password: User password
        :return: Encoded password
        """
        return base64.b64encode(hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), HASH_SALT, HASH_ITERATIONS))

    @staticmethod
    def compare_password(password_hash: str, password: str) -> bool:
        """
        Compare two passwords \n
        :param password_hash: User password from database
        :param password: User password from request
        :return: True if passwords are equal, False otherwise
        """
        return hmac.compare_digest(
            base64.b64decode(password_hash),
            hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), HASH_SALT, HASH_ITERATIONS)
        )

    def get_user(self, email: str) -> User:
        """
        Get user by user email \n
        :param email: User email
        :return: User object
        """
        return self.dao.get_user_by_email(email)

    def create_user(self, data: dict) -> User:
        """
        Create a new user \n
        :param data: Dictionary with user information
        :return: User object
        """
        if self.get_user(data["email"]):
            abort(400, "User already exists")

        data["password"] = self.hash_password(data["password"])
        return self.dao.create(data)

    def update_user(self, email: str, data: dict) -> None:
        """
        Update user information (without password and email) \n
        :param email: User email
        :param data: Dictionary with user information
        :return: None
        """
        if "password" not in data and "email" not in data:
            self.dao.update(email, data)
        else:
            abort(400, "Email or password are not allowed")

    def update_password(self, email: str, data: dict) -> None:
        """
        Update user password \n
        :param email: User email
        :param data: Dictionary with old and new passwords
        :return: None
        """
        user: User = self.dao.get_user_by_email(email)
        old_password: str = data.get("old_password")
        new_password: str = data.get("new_password")

        if None in [old_password, new_password] or not self.compare_password(user.password, old_password):
            abort(400, "Incorrect password information")

        if old_password == new_password:
            abort(400, "Passwords should not match")

        data = {"password": self.hash_password(new_password)}

        self.dao.update(email, data)
