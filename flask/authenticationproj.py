from flask import Flask, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy #import sqlalchemy class from flask_alchemy pkq
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, IntegerField, SubmitField,PasswordField
from wtforms.validators import DataRequired,Length,EqualTo
from flask import sessions,flash
from flask_migrate import Migrate
from flask_login import UserMixin


app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config.from_object('config.Config')
mydb_obj = SQLAlchemy(app)

# This is for creating the user registration form 
class RegisterForm(FlaskForm):
    username = StringField('Username:',validators=[DataRequired(),Length(min=4,max=150)])
    password = PasswordField('Password:',validators=[DataRequired(),Length(min=6)])
    confirm_password = PasswordField('Confirm Password:',validators=[DataRequired(),EqualTo('password')])
    profile = FileField('Profile Image',validators=[FileAllowed(['jpg','png'],'upload images only')])
    submit = SubmitField('Register')


#Created the role of user// admin has to be added manually by changing default value from user to admin
class User(mydb_obj.Model,UserMixin):
    id = mydb_obj.Column(mydb_obj.Integer, primary_key=True)
    username = mydb_obj.Column(mydb_obj.String(150),unique=True,nullable=False)
    password = mydb_obj.Column(mydb_obj.String(150),nullable=False)
    role = mydb_obj.Column(mydb_obj.String(50),nullable=False,default='user')
    profile =  mydb_obj.Column(mydb_obj.String(150),nullable=True)


@app.route('/')
def index():
    # Redirect to /userdashboard when accessing the root path
    return '<h1>login page ivide varum </h1>'

@app.route('/userdashboard')
def userdashboard():
    return render_template('Userdreamdashboard.html')

@app.route('/editprofile')
def editprofile():
    return render_template('Editprofileuserdashboard.html')



@app.route('/changepassword')
def changepassword():
    return render_template('changepassworduserdashboard.html')


@app.route('/viewenquiries')
def viewenquiries():
    return render_template('viewenquiryuserdashboard.html')









with app.test_request_context():
    print(app.url_map)

# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)
