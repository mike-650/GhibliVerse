from flask import Flask
from models import db, Film, Character

# Create Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ghibli.db'

# Initialize Flask-SQLAlchemy
db.init_app(app)

# Check if the script is being run as the main module
if __name__ == "__main__":
    # Step 3: Create the tables in the database using Flask-SQLAlchemy
    with app.app_context():
        db.create_all()

    # Step 4: Create a Flask-SQLAlchemy session
    with app.app_context():
        session = db.session

        # Step 5: Insert data into the tables
        film1 = Film(title="Spirited Away", director="Hayao Miyazaki", description="...")
        film2 = Film(title="Howl's Moving Castle", director="Hayao Miyazaki", description="...")

        character1 = Character(name="Chihiro", age=10, description="...", film=film1)
        character2 = Character(name="Howl", age=27, description="...", film=film2)

        session.add_all([film1, film2, character1, character2])
        session.commit()

        # Step 6: Query the database using Flask-SQLAlchemy
        films = Film.query.all()
        characters = Character.query.all()

        # Print the results
        for film in films:
            print(f"Film: {film.title}, Director: {film.director}")

        for character in characters:
            print(f"Character: {character.name}, Film: {character.film.title}")
