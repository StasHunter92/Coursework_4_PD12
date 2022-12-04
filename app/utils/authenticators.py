import jwt

from flask import request, abort
from jwt import InvalidSignatureError

from app.utils.secret import JWT_SECRET_KEY, JWT_ALGORITHM


# ----------------------------------------------------------------------------------------------------------------------
# Create wrapper for authentication
def auth_required(func):
    """
    Check authorization token for authentication \n
    :param func: Function for checking
    """
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401, "Authorization error")

        data = request.headers["Authorization"]
        token = data.split("Bearer ")[-1]

        try:
            jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        except InvalidSignatureError:
            abort(401, "Authentication error")
        return func(*args, **kwargs)

    return wrapper
