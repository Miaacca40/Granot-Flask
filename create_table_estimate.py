import sqlite3

# Connect to the database (creates a new database if it doesn't exist)
conn = sqlite3.connect('granot.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create the table with the desired fields
cursor.execute('''
    CREATE TABLE IF NOT EXISTS job (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT,
        customer_address1 TEXT,
        customer_address2 TEXT,
        customer_location TEXT,
        customer_sublocation TEXT,
        customer_floor TEXT,
        customer_apt TEXT,
        customer_city TEXT,
        customer_state TEXT,
        customer_zipcode TEXT,
        customer_phone_h TEXT,
        customer_phone_o TEXT,
        customer_email TEXT,
        customer_proxy TEXT,
        recipient_name TEXT,
        recipient_address1 TEXT,
        recipient_address2 TEXT,
        recipient_location TEXT,
        recipient_sublocation TEXT,
        recipient_floor TEXT,
        recipient_apt TEXT,
        recipient_city TEXT,
        recipient_state TEXT,
        recipient_zipcode TEXT,
        recipient_phone_h TEXT,
        recipient_phone_o TEXT,
        recipient_fax TEXT,
        recipient_proxy TEXT,
        expected_move_date TEXT
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
