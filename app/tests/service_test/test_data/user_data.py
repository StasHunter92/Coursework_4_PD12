from app.dao.models.user_model import User
# ----------------------------------------------------------------------------------------------------------------------
# Constants for user MagicMock

ONE_USER = User(
    id=1,
    email="test@example.com",
    password="oSvTQ3vIVvPszyYe1jCxs91Pklfsi8p64yUAkIc40oI=",
    name="User",
    surname="User",
    favourite_genre=8
)

NEW_USER = User(
    id=2,
    email="test2@example.com",
    password="oSvTQ3vIVvPszyYe1jCxs91Pklfsi8p64yUAkIc40oI=",
    name="User",
    surname="User",
    favourite_genre=8
)
