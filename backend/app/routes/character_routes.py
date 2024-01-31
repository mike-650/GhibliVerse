from flask import Blueprint, jsonify
from app.models.models import Character

character_routes = Blueprint('character_routes', __name__)

@character_routes.route('/', methods=['GET'])
def get_characters():
    characters = Character.query.all()
    return jsonify({'characters': [{'id': character.id, 'name': character.name, 'description': character.description} for character in characters]})

# Add more character routes as needed
