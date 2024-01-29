# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Film(db.Model):
    __tablename__ = "films"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    director = db.Column(db.String)
    description = db.Column(db.String)

    characters = db.relationship("Character", back_populates="film")

class Character(db.Model):
    __tablename__ = "characters"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    description = db.Column(db.String)
    film_id = db.Column(db.Integer, db.ForeignKey("films.id"))

    film = db.relationship("Film", back_populates="characters")
