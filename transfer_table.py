import mysql.connector
import sqlite3

# MySQL connection
mysql_conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345',
    database='Granot'
)
mysql_cursor = mysql_conn.cursor()

# Retrieve table data
table_name = 'inventory'
mysql_cursor.execute(f'SELECT name, volume, weight, bulky, need_pack, category FROM {table_name}')
table_data = mysql_cursor.fetchall()

# SQLite connection
sqlite_conn = sqlite3.connect('granot.db')
sqlite_cursor = sqlite_conn.cursor()

# Create the table in SQLite
sqlite_cursor.execute('DROP TABLE IF EXISTS inventory')
sqlite_cursor.execute('''
    CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(60) NOT NULL,
        volume INTEGER NOT NULL,
        weight INTEGER NOT NULL,
        bulky VARCHAR(10),
        need_pack VARCHAR(10),
        category VARCHAR(70)
    )
''')

# Insert data into SQLite table
sqlite_cursor.executemany('''
    INSERT INTO inventory (name, volume, weight, bulky, need_pack, category)
    VALUES (?, ?, ?, ?, ?, ?)
''', table_data)

# Commit the changes and close connections
sqlite_conn.commit()
sqlite_conn.close()
mysql_conn.close()
