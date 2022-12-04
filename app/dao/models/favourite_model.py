from marshmallow import Schema, fields

from app.database.setup_db import db


# ----------------------------------------------------------------------------------------------------------------------
# Create model for database
class FavouriteMovie(db.Model):
    """Secondary table for user favourite movies"""
    __tablename__ = "favourite_movie"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))

    user = db.relationship("User")
    movie = db.relationship("Movie")


# ----------------------------------------------------------------------------------------------------------------------
# Create schema for model
class FavouriteMovieSchema(Schema):
    """Schema for user favourite movies"""
    id = fields.Int(dump_only=True)
    user_id = fields.Int()
    movie_id = fields.Int()
