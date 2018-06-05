from flask import Flask, render_template, request, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import TextField,RadioField, IntegerField, TextAreaField, SubmitField, SelectField, StringField, PasswordField, BooleanField
from wtforms import validators, ValidationError 
from wtforms.validators import Email, InputRequired, Length


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisupposedtobesecret!'
Bootstrap(app)


class LoginForm(FlaskForm):
  username = StringField("username", validators=[InputRequired(), Length(min=4, max=15)])
  password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
  remember = BooleanField('remember me')
  submit = SubmitField("Sign in")


class RegisterForm(FlaskForm):
  username = TextField("Name of User",[validators.Required("Please enter your name.")])
  password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
  submit = SubmitField("submit")


@app.route("/<path:filename>", methods = ["GET", "POST"])
def display(filename):
  try:
    return render_template(filename)
  except TemplateNotFound:
    return app.send_static_file(filename)



@app.route('/')
def index():
  return render_template("01.html")



@app.route('/login')
def login():
  form = LoginForm()

  return render_template('login.html', form=form)
  

@app.route('/signup' , methods = ['GET', 'POST'])
def signup():
	form = RegisterForm()
	if request.method == 'POST':
		if form.validate() == False:
			flash('All fields are required.')
			return render_template('signup2.html', form = form)
		else:
			return render_template('success.html')
	else:
		return render_template('signup2.html', form = form)


if (__name__) == '__main__':
	app.run(debug = True)