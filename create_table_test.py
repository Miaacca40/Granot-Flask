import sqlite3

# Connect to the database (creates a new database if it doesn't exist)
conn = sqlite3.connect('granot.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create the table with the desired fields
sql = '''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    '''

cursor.execute(sql)
# Commit the changes and close the connection
conn.commit()
conn.close()
