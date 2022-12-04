from os import path


# ----------------------------------------------------------------------------------------------------------------------
# Create configuration
class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{path.abspath(path.join('app', 'database', 'movies.db'))}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTX_JSON = {"ensure_ascii": False, "indent": 4}
    ITEMS_PER_PAGE = 12
