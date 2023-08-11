import sqlite3

# Create a connection to the database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    user_type TEXT NOT NULL
);''')

conn.commit()
conn.close()
