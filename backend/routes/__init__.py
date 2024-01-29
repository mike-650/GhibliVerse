# Import blueprints from other modules
from .film      import film_bp
from .character import character_bp



def register_blueprints(app):
  app.register_blueprint(film_bp, url_prefix='/films')
  app.register_blueprint(character_bp, url_prefix='/characters')
