from marshmallow import Schema, fields

from app.database.setup_db import db


# ----------------------------------------------------------------------------------------------------------------------
# Create model for database
class Genre(db.Model):
    """Genre model"""
    __tablename__ = "genre"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)


# ----------------------------------------------------------------------------------------------------------------------
# Create schema for model
class GenreSchema(Schema):
    """Schema for Genre"""
    id = fields.Int(dump_only=True)
    name = fields.Str()
