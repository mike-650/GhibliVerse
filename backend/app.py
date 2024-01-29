from flask import Flask
from routes import register_blueprints
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ghibli.db'
db.init_app(app)  # Initialize Flask-SQLAlchemy

register_blueprints(app)

# Remove the SQLite connection function, as we're using Flask-SQLAlchemy

if __name__ == '__main__':
    app.run(debug=True)
