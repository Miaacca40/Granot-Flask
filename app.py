from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    conn = sqlite3.connect('granot.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM inventory')
    items = cursor.fetchall()
    conn.close()
    return render_template('market.html', items=items)

@app.route('/estimate')
def estimate():
    return render_template('estimate.html')

@app.route('/create_table')
def create_table():
    # Database connection
    conn = sqlite3.connect('granot.db')
    cursor = conn.cursor()

    # SQL query to create a table
    sql = '''
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(60) NOT NULL,
            volume INTEGER NOT NULL,
            weight INTEGER NOT NULL,
            bulky VARCHAR(10),
            need_pack VARCHAR(10),
            category VARCHAR(70)
        )
    '''

    try:
        # Execute the query
        cursor.execute(sql)
        conn.commit()
        return 'Table created successfully'
    except Exception as e:
        return f'Error creating table: {str(e)}'
    finally:
        # Close the database connection
        conn.close()
    
if __name__ == '__main__':
    app.run()
