from flask import Blueprint, jsonify, request
from app.models import Film
from app import db

film_routes = Blueprint('film_routes', __name__)

@film_routes.route('/films', methods=['GET'])
def get_films():
    films = Film.query.all()
    return jsonify({'films': [{'id': film.id, 'title': film.title, 'director': film.director, 'description': film.description} for film in films]})

@film_routes.route('/films', methods=['POST'])
def add_film():
    data = request.get_json()
    title = data.get('title')
    director = data.get('director')
    description = data.get('description')

    new_film = Film(title=title, director=director, description=description)
    db.session.add(new_film)
    db.session.commit()

    return jsonify({'message': 'Film added successfully'})

# Add more film routes as needed
