from flask import Blueprint, jsonify
from create_db import Character

character_bp = Blueprint('character', __name__)

@character_bp.route('/')
def get_characters():
    try:
        # Query all films from the Film model
        characters = Character.query.all()

        # Convert the result to a list of dictionaries
        characters_list = [
            {'id': character.id, 'name': character.name, 'age': character.age, 'desription': character.description}
            for character in characters
        ]

        # Return the result as JSON
        return jsonify({'characters': characters_list})

    except Exception as e:
        # Handle any exceptions that might occur during the query
        return jsonify({'error': str(e)}), 500
