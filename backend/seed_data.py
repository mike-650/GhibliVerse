import sqlite3

# Function to establish a connection to the SQLite database
def get_db_connection():
    connection = sqlite3.connect("ghibli.db")
    return connection

# Seed data for the "films" table
films_data = [
    (1, 'Spirited Away', 'Hayao Miyazaki', "Chihiro's family is moving to a new house, but when they stop on the way to explore an abandoned village, her parents undergo a mysterious transformation and Chihiro is whisked into a world of fantastic spirits ruled over by the sorceress Yubaba."),
    (2, "Howl's Moving Castle", 'Hayao Miyazaki', "Howl's Moving Castle is a fantasy novel about the infamous wizard Howl, and a cursed hatmaker named Sophie. Sophie Hatter is a pretty average girl whose been left to maintain her family's hat shop. However, she gets cursed one day by the Witch of the Waste and is turned into an old woman."),
]

# Seed data for the "characters" table
characters_data = [
    (1, 'Chihiro', '10', "A gangly, ten-year-old human girl, heroine of the movie. At first Chihiro is sullen, whiny, and afraid, with an annoying voice and sulky face. After her name is changed to Sen, she becomes brave and self-sufficient enough to free herself and her parents from the spirit world.", 1),  # Character from Spirited Away
    (2, 'Howl', '27', "Howl is a young, handsome man with bright blue eyes and hair that reaches below his chin. At the beginning of the film, his hair is blonde, but because of an incident while Sophie is cleaning Howl's bathroom, he briefly comes to have orange hair, before it finally turns black.",2),  # Character from My Neighbor Totoro
    # Add more characters as needed
]

# Insert seed data into the tables
def insert_seed_data():
    connection = get_db_connection()
    cursor = connection.cursor()

    # Insert seed data into the "films" table
    cursor.executemany("INSERT INTO films (id, title, release_year) VALUES (?, ?, ?)", films_data)

    # Insert seed data into the "characters" table
    cursor.executemany("INSERT INTO characters (id, name, role, film_id) VALUES (?, ?, ?, ?)", characters_data)

    connection.commit()
    connection.close()

if __name__ == "__main__":
    insert_seed_data()
