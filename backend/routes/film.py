from flask import Blueprint, jsonify
from create_db import Film

film_bp = Blueprint('film', __name__)

@film_bp.route('/')
def get_films():
    try:
        # Query all films from the Film model using Flask-SQLAlchemy
        films = Film.query.all()
        print(films)

        # Convert the result to a list of dictionaries
        films_list = [
            {'id': film.id, 'title': film.title, 'director': film.director, 'description': film.description}
            for film in films
        ]

        # Return the result as JSON
        return jsonify({'films': films_list})

    except Exception as e:
        # Handle any exceptions that might occur during the query
        return jsonify({'error': str(e)}), 500
