from flask import jsonify, request
from app import app, db
from app.models import Film

@app.route('/films', methods=['GET'])
def get_films():
    films = Film.query.all()
    film_list = [{'id': film.id, 'title': film.title, 'director': film.director, 'description': film.description} for film in films]
    return jsonify({'films': film_list})

@app.route('/films', methods=['POST'])
def add_film():
    data = request.get_json()
    title = data.get('title')
    director = data.get('director')
    description = data.get('description')

    new_film = Film(title=title, director=director, description=description)
    db.session.add(new_film)
    db.session.commit()

    return jsonify({'message': 'Film added successfully'})
