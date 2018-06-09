from flask import Flask, render_template, request, flash, url_for, session, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import Form, TextField,RadioField, IntegerField, TextAreaField, SubmitField, SelectField, StringField, PasswordField, BooleanField
from wtforms import validators, ValidationError 
from wtforms.validators import Email, InputRequired, Length
from pymysql import escape_string as thwart
import pymysql
import pymysql.cursors
import wtforms
import gc


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisupposedtobesecret!'
Bootstrap(app)

db = pymysql.connect( host="localhost", user="root", password="123456", database="205CDE")
cursor = db.cursor()
sqlloginform = """CREATE TABLE loginform (email varchar(80) primary key, username varchar(15), password varchar(80))"""
cursor.execute("DROP TABLE IF EXISTS loginform")
cursor.execute(sqlloginform)
db.close()




class LoginForm(Form):
  propertyname = StringField("username", validators=[InputRequired(), Length(min=4, max=15)])
  password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
  remember = BooleanField('remember me')
  email = TextField("Email",[validators.Required("Please enter your email address.")])
  submit = SubmitField("Sign in")


class RegisterForm(Form):
  username = TextField("Name of User",[validators.Required("Please enter your name.")])
  password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
  email = TextField("Email",[validators.Required("Please enter your email address.")])
  submit = SubmitField("submit")




@app.route('/')
def index():
  return render_template("mianpage.html")

@app.route('/add')
def add():
  return render_template("add.html")


@app.route('/header')
def random():
  return render_template("header.html")


@app.route('/login')
def login():
  form = LoginForm()

  return render_template('login.html', form=form)
  
  

@app.route('/signup' , methods = ['GET', 'POST'])
def signup():
  
  
    form = RegisterForm(request.form)
     
    if request.method == "POST":      
      username=request.form['username']
      password=request.form['password']
      email=request.form['email']
      db = pymysql.connect( host="localhost", user="root", password="123456", database="205CDE")
      cursor = db.cursor()
      
      sql = "INSERT INTO loginform (username, password, email) VALUES ('%s', '%s', '%s')" % (username, password, email)
      print(sql)
      cursor.execute(sql)
      db.commit()
      flash("Thanks for sign up")

      cursor.close()
      db.close()
      gc.collect()

      session['logged_in'] = True
      session['username'] = username

      return redirect(url_for('add'))


    return render_template('signup2.html', form = form)    


if (__name__) == '__main__':
	app.run(debug = True)