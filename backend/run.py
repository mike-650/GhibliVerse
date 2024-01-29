from app import app, db
from app.routes import character_routes, film_routes
from scripts.seed import seed_data

# Register blueprints
app.register_blueprint(film_routes)
app.register_blueprint(character_routes)

with app.app_context():
    db.create_all()
    seed_data()

if __name__ == '__main__':
    app.run(debug=True)
