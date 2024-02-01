from app import db

class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    director = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    imagePath = db.Column(db.String(255), nullable=False)

    # Define the one-to-many relationship
    characters = db.relationship('Character', backref='film', lazy=True)

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)

    # Define the foreign key relationship
    film_id = db.Column(db.Integer, db.ForeignKey('film.id'), nullable=False)
