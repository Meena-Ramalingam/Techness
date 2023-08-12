import sqlite3

# Create a connection to the database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE users (
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    userType TEXT NOT NULL
);
''')


conn.commit()
conn.close()
