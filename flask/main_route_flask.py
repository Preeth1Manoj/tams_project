from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.utils import secure_filename
from flask_migrate import Migrate



app = Flask(__name__)
app.secret_key = 'your_secret_key'

# SQLAlchemy Database URI
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'mssql+pyodbc://DESKTOP-79EIPER\\SQLEXPRESS/User_registration?driver=ODBC+Driver+17+for+SQL+Server'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy object
db = SQLAlchemy(app)
migrate = Migrate(app, db)

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
    profile = db.Column(db.String(150), nullable=True)  
@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/userdashboard')
def userdashboard():
    if 'user_id' not in session:
        flash("Please log in to access the dashboard.", "danger")
        return redirect(url_for('login'))

    user_id = session['user_id']
    user = UserRegistration.query.get(user_id)
    return render_template('Userdreamdashboard.html', user=user)

@app.route('/editprofile', methods=['GET', 'POST'])
def edit_profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user = UserRegistration.query.get(session['user_id'])

    if request.method == 'POST':
        user.first_name = request.form['first_name']
        user.last_name = request.form['last_name']
        user.email = request.form['email']
        user.phone = request.form['phone']
        user.age = request.form['age']
        user.passout_year = request.form['passout_year']
        user.address = request.form['address']

        # Handle profile picture upload
        if 'profile_picture' in request.files:
            file = request.files['profile_picture']
            if file and file.filename != '':  # Check if a file is uploaded
                # Check if the uploaded file is an image
                if allowed_file(file.filename):  # Implement allowed_file function
                    filename = secure_filename(file.filename)
                    file_path = os.path.join('static/profilepic', filename)
                    file.save(file_path)
                    user.profile = filename  # Save filename in the database
                else:
                    flash("Uploaded file is not an image.", "danger")

        db.session.commit()
        flash("Profile updated successfully!", "success")
        return redirect(url_for('userdashboard'))

    return render_template('Editprofileuserdashboard.html', user=user)

def allowed_file(filename):
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}  # Specify allowed image formats
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

@app.route('/changepassword', methods=['GET', 'POST'])
def change_password():
    user = UserRegistration.query.get(session.get('user_id'))
    if user is None:
        flash('User not found. Please log in again.')
        return redirect(url_for('login'))

    if request.method == 'POST':
        current_password = request.form['current_password']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']
        
        errors = []  # Create a list to hold error messages

        if user.password != current_password:
            errors.append('Current password is incorrect.')

        if new_password != confirm_password:
            errors.append('New passwords do not match.')

        if errors:  # If there are any errors, render the template with the errors
            for error in errors:
                flash(error, "danger")
            return render_template('changepassworduserdashboard.html', user=user)

        user.password = new_password  # Store the new password as plain text
        db.session.commit()
        flash('Password updated successfully!', "success")
        return redirect(url_for('userdashboard'))

    return render_template('changepassworduserdashboard.html', user=user)

@app.route('/viewenquiries')
def viewenquiries():
    return render_template('viewenquiryuserdashboard.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['txtfirstname']
        last_name = request.form['txtlastname']
        email = request.form['txtemail']
        phone = request.form['txtphnum']
        password = request.form['txtpwd']
        age = request.form['txtage']
        passout_year = request.form['txtpassoutyear']
        qualification = request.form['txtqualification']
        address = request.form['txtaddress']

        existing_user = UserRegistration.query.filter_by(email=email).first()

        if existing_user:
            flash("Email already registered, login here", "danger")
            return redirect(url_for('login'))

        new_user = UserRegistration(
            first_name=first_name, last_name=last_name, email=email, phone=phone,
            password=password, age=age, passout_year=passout_year, 
            qualification=qualification, address=address
        )

        try:
            db.session.add(new_user)
            db.session.commit()
            flash("Registration successful!", "success")
            return redirect(url_for('login'))
        except Exception as e:
            print("Error occurred: ", e)
            db.session.rollback()
            flash("An error occurred. Please try again.", "danger")

    return render_template('registration.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = UserRegistration.query.filter_by(email=email, password=password).first()

        if user:
            flash("Login successful!", "success")
            session['user_id'] = user.id
            return redirect(url_for('userdashboard'))
        else:
            flash("Invalid email or password. Please try again.", "danger")

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("You have been logged out.", "success")
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
