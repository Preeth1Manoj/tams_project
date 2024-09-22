from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = 'your_secret_key'

# SQLAlchemy Database URI
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'mssql+pyodbc://DESKTOP-79EIPER\\SQLEXPRESS/User_registration?driver=ODBC+Driver+17+for+SQL+Server'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy object
db = SQLAlchemy(app)

# Define the database model for the registration entries
class UserRegistration(db.Model):
    __tablename__ = 'users_registration_new_entry'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    passout_year = db.Column(db.Integer, nullable=False)
    qualification = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String, nullable=False)


@app.route('/')
def index():
    # Redirect to /userdashboard when accessing the root path
    return redirect(url_for('userdashboard'))

@app.route('/userdashboard')
def userdashboard():
    return render_template('Userdreamdashboard.html')

# Route to render the registration form
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Fetch form data
        first_name = request.form['txtfirstname']
        last_name = request.form['txtlastname']
        email = request.form['txtemail']
        phone = request.form['txtphnum']
        password = request.form['txtpwd']
        age = request.form['txtage']
        passout_year = request.form['txtpassoutyear']
        qualification = request.form['txtqualification']
        address = request.form['txtaddress']

        # Create a new user object
        new_user = UserRegistration(
            first_name=first_name, last_name=last_name, email=email, phone=phone, 
            password=password, age=age, passout_year=passout_year, 
            qualification=qualification, address=address
        )

        try:
            # Add new user to the database
            db.session.add(new_user)
            db.session.commit()
            flash("Registration successful!", "success")
        except Exception as e:
            print("Error occurred: ", e)
            db.session.rollback()
            flash("An error occurred. Please try again.", "danger")

        return redirect(url_for('register'))

    return render_template('registration.html')

# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)
