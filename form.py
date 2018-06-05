from flask_wtf import Form
from wtforms import TextField,RadioField, IntegerField, TextAreaField, SubmitField, SelectField
from wtforms import validators, ValidationError 
from flask import Flask


class ContactForm(Form):
   name = TextField("Name of User",[validators.Required("Please enter your name.")])
   Gender = RadioField('Gender' , choices = [('M','Male'),('F','Femail')])
   Address = TextAreaField("Address")
   email = TextField("Email",[validators.Required("Please enter your email address.")])
   Age = IntegerField("Age")
   language = SelectField('Languags' , choices = [('cpp', 'C++'), ('py', 'Python')])
   submit = SubmitField("Send")




