from marshmallow import Schema, fields

from app.database.setup_db import db


# ----------------------------------------------------------------------------------------------------------------------
# Create model for database
class Movie(db.Model):
    """Movie model"""
    __tablename__ = "movie"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    trailer = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"), nullable=False)
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"), nullable=False)

    genre = db.relationship("Genre")
    director = db.relationship("Director")


# ----------------------------------------------------------------------------------------------------------------------
# Create schema for model
class MovieSchema(Schema):
    """Schema for Movie"""
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()
