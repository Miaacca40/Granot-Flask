import sqlite3

# Connect to the database (creates a new database if it doesn't exist)
conn = sqlite3.connect('granot.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create the table with the desired fields
# Create a connection to the database
conn = sqlite3.connect('granot.db')
cursor = conn.cursor()

# Create the jobs table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS jobs
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 sname TEXT,
                 sadd1 TEXT,
                 sadd2 TEXT,
                 slevel TEXT,
                 ssublevel TEXT,
                 sfloor TEXT,
                 sapt TEXT,
                 scity TEXT,
                 sstate TEXT,
                 szip TEXT,
                 stelh TEXT,
                 stelo TEXT,
                 email TEXT,
                 sproxy TEXT,
                 rname TEXT,
                 radd1 TEXT,
                 radd2 TEXT,
                 rlevel TEXT,
                 rsublevel TEXT,
                 rfloor TEXT,
                 rapt TEXT,
                 rcity TEXT,
                 rstate TEXT,
                 rzip TEXT,
                 rtelh TEXT,
                 rtelo TEXT,
                 sfax TEXT,
                 rproxy TEXT)''')
# Commit the changes and close the connection
conn.commit()
conn.close()
