import sqlite3

# Function to establish a connection to the SQLite database
def get_db_connection():
    connection = sqlite3.connect("ghibli.db")
    return connection

# Seed data for the "films" table
films_data = [
    ('Spirited Away', '2001'),
    ('My Neighbor Totoro', '1988'),
    ()
]

# Seed data for the "characters" table
characters_data = [
    (1, 'Chihiro', 'Protagonist', 1),  # Character from Spirited Away
    (2, 'Totoro', 'Forest Spirit', 2),  # Character from My Neighbor Totoro
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
