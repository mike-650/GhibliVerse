from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    """
    In a production environment, you might want to configure CORS more restrictively for security reasons.
    You may limit which origins are allowed to access your API, specify allowed methods, headers, etc.
    This is done to prevent potential security vulnerabilities that could arise from allowing any origin to make requests.
    """
    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/ghibli.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Import and register blueprints
    from .routes import character_routes, film_routes
    app.register_blueprint(character_routes, url_prefix='/api/characters')
    app.register_blueprint(film_routes, url_prefix='/api/films')

    return app
