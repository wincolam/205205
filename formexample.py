from flask import *
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import Form, TextField,RadioField, IntegerField, TextAreaField, SubmitField, SelectField, StringField, PasswordField, BooleanField
from wtforms import validators, ValidationError 
from wtforms.validators import Email, InputRequired, Length
from pymysql import escape_string as thwart
from jinja2 import TemplateNotFound
import pymysql
import pymysql.cursors
import wtforms
import gc


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisupposedtobesecret!'
Bootstrap(app)

def connection():
    return pymysql.connect( host="localhost", user="user", password="123456", database="205CDE")

def select(sql):
    print (sql)
    conn = connection()
    with conn.cursor() as cur:
        cur.execute(sql)
        return cur.fetchall()


    

# cursor = db.cursor()
# cursor.execute("DROP TABLE IF EXISTS loginform")
# sqlloginform = """CREATE TABLE loginform (email varchar(80) primary key, username varchar(15), password varchar(80))"""
# cursor.execute(sqlloginform)
# db.close()


@app.route("/", defaults={"filename": "index.html"})
@app.route("/<path:filename>", methods = ["GET", "POST"])
def display(filename):
    try:
        return render_template(filename)
    except TemplateNotFound:
        return app.send_static_file(filename)

class add(Form):
    name=TextField("Name of User",[validators.Required("Please enter your name.")])
    price=TextField("Name of User",[validators.Required("Please enter your name.")])
    interval=TextField("Name of User",[validators.Required("Please enter your name.")])
    age=TextField("Name of User",[validators.Required("Please enter your name.")])
    projecttype=TextField("Name of User",[validators.Required("Please enter your name.")])
    developer=TextField("Name of User",[validators.Required("Please enter your name.")])
    contactname=TextField("Name of User",[validators.Required("Please enter your name.")])
    contactnumber=TextField("Name of User",[validators.Required("Please enter your name.")])

class RegisterForm(Form):
    username = TextField("Name of User",[validators.Required("Please enter your name.")])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    email = TextField("Email",[validators.Required("Please enter your email address.")])
    submit = SubmitField("submit")



@app.route('/login', methods=["POST", "GET"])
def login(errmsg=""):
    if request.method == "POST":
        sql = "SELECT * FROM user WHERE username='%s' AND password='%s'" % (request.form['username'], request.form['password'])
        result = select(sql)
        if len(result) == 1:
            session['username'] = request.form['username']
            return redirect("/")
        return redirect(url_for('login'), errmsg="incorrect username / password")
        
    return render_template('login.html')
    
    

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

@app.route('/add')
def add():
    return render_template('add.html', form=form)
  
if __name__ == '__main__':
    app.run(debug = True)
