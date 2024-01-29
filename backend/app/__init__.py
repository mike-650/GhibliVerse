from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../ghibli.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Import routes after initializing app and db to avoid circular imports
# from backend.app.routes import routes

@app.cli.command()
def seed():
    from scripts.seed import seed_data
    seed_data()
