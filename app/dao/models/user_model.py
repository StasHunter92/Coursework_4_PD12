from marshmallow import Schema, fields

from app.database.setup_db import db


# ----------------------------------------------------------------------------------------------------------------------
# Create model for database
class User(db.Model):
    """User model"""
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    favourite_genre = db.Column(db.Integer, db.ForeignKey("genre.id"))

    genre = db.relationship("Genre")


# ----------------------------------------------------------------------------------------------------------------------
# Create schema for model
class UserSchema(Schema):
    """Schema for User"""
    id = fields.Int()
    email = fields.Str()
    password = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    favourite_genre = fields.Int()
