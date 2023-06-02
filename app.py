from flask import Flask, render_template ,request
import sqlite3
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))


@app.route('/')
@app.route('/home')
def home_page():
    db.create_all()
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

@app.route('/dataentry')
def dataentry():
    return render_template('dataentry.html')

@app.route("/add_record", methods=["POST"])
def add_record():
    name = request.form["name"]
    email = request.form["email"]

    # Create a new user
    new_user = User(name=name, email=email)

    # Save the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect("/")






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
