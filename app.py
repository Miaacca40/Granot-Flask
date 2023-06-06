from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, IntegerField
from wtforms.validators import InputRequired
import sqlite3


app = Flask(__name__)

app.config['SECRET_KEY'] = "Ibtisam"





# Create a form
class InventoryForm(FlaskForm):
    name = SelectField('Name', choices=[])
    quantity = IntegerField('Quantity', validators=[InputRequired()])
    submit = SubmitField('Add')

    # Initialize the form with the data from the database
    def __init__(self):
        super().__init__()
        db = sqlite3.connect('granot.db')
        c=db.cursor()
        self.name.choices = [(item[0], item[0]) for item in c.execute('SELECT name FROM inventory')]




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
    
@app.route('/add_inv', methods=['GET', 'POST'])
def add_inv():

    # Fetch the list from the database
    conn = sqlite3.connect("granot.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM inventory")
    inventory = cursor.fetchall()
    conn.close()

    return render_template('add_inv.html', inventory=inventory)

@app.route('/add_inv2', methods=['GET', 'POST'])
def add_inv2():
    entries = []

    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        
        # Create a dictionary for the new entry
        entry = {'name': name, 'quantity': quantity}
        
        # Add the new entry to the list
        entries.append(entry)

    # Fetch the list from the database
    conn = sqlite3.connect("granot.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM inventory")
    inventory = cursor.fetchall()

    if 'save' in request.form:
        # Save the list to the database table
        for entry in entries:
            name = entry['name']
            quantity = entry['quantity']
            cursor.execute("INSERT INTO your_table_name (name, quantity) VALUES (?, ?)", (name, quantity))

        conn.commit()

        # Redirect to a success page or display a success message
        return render_template('success.html')

    conn.close()

    return render_template('add_inv_2.html', inventory=inventory, entries=entries)

@app.route('/add_inv3', methods=['GET', 'POST'])
def add_inv3():
    form = InventoryForm()
    if form.validate_on_submit():
        # Get the data from the form
        name = form.name.data
        quantity = form.quantity.data

        # Add the item to the database
        db = sqlite3.connect('granot.db')
        c = db.cursor()
        c.execute('INSERT INTO temp (name, size) VALUES (?, ?)', (name, quantity))
        db.commit()

        # Redirect to the index page
        return redirect('/')

    return render_template('add_inv3.html', form=form)


@app.route('/save_job', methods=['POST'])
def save_job():
    # Retrieve form data
    
    sname = request.form['SNAME']
    sadd1 = request.form['SADD1']
    sadd2 = request.form['SADD2']
    slevel = request.form['SLEVEL']
    ssublevel = request.form['SSUBLEVEL']
    sfloor = request.form['SFLOOR']
    sapt = request.form['SAPT']
    scity = request.form['SCITY']
    sstate = request.form['SSTATE']
    szip = request.form['SZIP']
    stelh = request.form['STELH']
    stelo = request.form['STELO']
    email = request.form['EMAIL']
    sproxy = request.form['SPROXY']
    rname = request.form['RNAME']
    radd1 = request.form['RADD1']
    radd2 = request.form['RADD2']
    rlevel = request.form['RLEVEL']
    rsublevel = request.form['RSUBLEVEL']
    rfloor = request.form['RFLOOR']
    rapt = request.form['RAPT']
    rcity = request.form['RCITY']
    rstate = request.form['RSTATE']
    rzip = request.form['RZIP']
    rtelh = request.form['RTELH']
    rtelo = request.form['RTELO']
    sfax = request.form['SFAX']
    rproxy = request.form['RPROXY']
    
    conn = sqlite3.connect('granot.db')
    cursor = conn.cursor()

    # Insert the form data into the jobs table
    cursor.execute('''INSERT INTO jobs (sname, sadd1, sadd2, slevel, ssublevel, sfloor, sapt,
                   scity, sstate, szip, stelh, stelo, email, sproxy, rname, radd1, radd2,
                   rlevel, rsublevel, rfloor, rapt, rcity, rstate, rzip, rtelh, rtelo,
                   sfax, rproxy)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)''',
               (sname, sadd1, sadd2, slevel, ssublevel, sfloor, sapt, scity, sstate, szip,
                stelh, stelo, email, sproxy, rname, radd1, radd2, rlevel, rsublevel, rfloor,
                rapt, rcity, rstate, rzip, rtelh, rtelo, sfax, rproxy))

    conn.commit()
    conn.close()
    
    return "THIS IS DONE"+sname

    


@app.route('/dataentry')
def dataentry():
    return render_template('dataentry.html')

@app.route("/add_record", methods=["POST"])
def add_record():
    name = request.form["name"]
    email = request.form["email"]
    conn = sqlite3.connect("granot.db")
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
    conn.commit()
    conn.close()
    return "Data Entered Successfully"






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
