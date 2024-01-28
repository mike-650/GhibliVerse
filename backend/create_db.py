from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# Step 1: Define the SQLAlchemy engine and connect to the database
engine = create_engine("sqlite:///ghibli.db", echo=True)  # Set echo=True for logging SQL statements
Base = declarative_base()

# Step 2: Define the SQLAlchemy models (equivalent to tables in SQLite)
class Film(Base):
    __tablename__ = "films"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    director = Column(String)
    description = Column(String)

    characters = relationship("Character", back_populates="film")


class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    description = Column(String)
    film_id = Column(Integer, ForeignKey("films.id"))

    film = relationship("Film", back_populates="characters")

# Step 3: Create the tables in the database
Base.metadata.create_all(engine)

# Step 4: Create a SQLAlchemy session
Session = sessionmaker(bind=engine)
session = Session()

# Step 5: Insert data into the tables
film1 = Film(title="Spirited Away", director="Hayao Miyazaki", description="A magical adventure")
film2 = Film(title="Howl's Moving Castle", director="Hayao Miyazaki", description="A heartwarming tale")

character1 = Character(name="Chihiro", age=10, description="Protagonist of Spirited Away", film=film1)
character2 = Character(name="Howl", age=27, description="Protagonist of Howl's Moving Castle", film=film2)

session.add_all([film1, film2, character1, character2])
session.commit()

# Step 6: Query the database using SQLAlchemy
films = session.query(Film).all()
characters = session.query(Character).all()

# Print the results
for film in films:
    print(f"Film: {film.title}, Director: {film.director}")

for character in characters:
    print(f"Character: {character.name}, Film: {character.film.title}")

# Step 7: Close the session
session.close()
