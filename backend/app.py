from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Function to establish a connection to the SQLite database
def get_db_connection():
    connection = sqlite3.connect("ghibli.db")
    connection.row_factory = sqlite3.Row
    return connection

# Endpoint to retrieve film data
@app.route('/films', methods=['GET'])
def get_films():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM films")
        films = cursor.fetchall()
        connection.close()

        film_list = []
        for film in films:
            film_dict = dict(film)
            print(film_dict)
            film_list.append(film_dict)

        return jsonify({'films': film_list})
    except Exception as e:
        return jsonify({'error': str(e)})

# Endpoint to add a new film
@app.route('/films', methods=['POST'])
def add_film():
    try:
        data = request.get_json()
        title = data['title']
        director = data['director']
        description = data['description']

        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO films (title, director, description) VALUES (?, ?, ?)", (title, director, description))
        connection.commit()
        connection.close()

        return jsonify({'message': 'Film added successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
