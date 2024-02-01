from flask import Blueprint, request
from app.models.models import Film
from app import db

film_routes = Blueprint('film_routes', __name__)

@film_routes.route('/', methods=['GET'])
def get_films():
    films = Film.query.all()
    return {'films': [{'id': film.id, 'title': film.title, 'director': film.director, 'description': film.description, 'imageURL': film.imageURL} for film in films]}

@film_routes.route('/films', methods=['POST'])
def add_film():
    data = request.get_json()
    title = data.get('title')
    director = data.get('director')
    description = data.get('description')

    new_film = Film(title=title, director=director, description=description)
    db.session.add(new_film)
    db.session.commit()

    return {'message': 'Film added successfully'}

# Add more film routes as needed
