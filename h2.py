from flask import Flask, render_template
from flask_bootstrap import flask_bootstrap
from flask_wtf import FlaskForm
from wtforms import StrigField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/signup')
def signup():
	return render_template('signup.html')

@app.route('/signup')
def dashboard():
	return render_template('dashboard.html')

if __name__ == '__mian__':
	app.run(debug=True)