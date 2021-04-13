#from flask_wtf import FlaskForm
from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField
from wtforms import validators, ValidationError

class ContactForm(Form):
   name = TextField("Name Of Student",[validators.Required("Please enter your name.")])  #文本框
   Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])                #单选框
   Address = TextAreaField("Address")                                                    #地址框
   
   email = TextField("Email",[validators.Required("Please enter your email address."),   #邮件框
      validators.Email("Please enter your email address.")])
   #整型文本框
   Age = IntegerField("age")
   #选择框
   language = SelectField('Languages', choices = [('cpp', 'C++'), 
      ('py', 'Python')])
   #提交按钮
   submit = SubmitField("Send")
