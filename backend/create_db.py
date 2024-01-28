import sqlite3

# Step 1: Connect to the database (creates a new file if it doesn't exist)
connection = sqlite3.connect("ghibli.db")

# Step 2: Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Step 3: Execute SQL commands using the cursor to create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS films (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    director TEXT,
                    description TEXT,
                    release_date 
                )''')

# Add more tables if needed

# Step 4: Commit changes and close the connection
connection.commit()
connection.close()
