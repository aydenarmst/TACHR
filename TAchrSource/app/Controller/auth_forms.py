from wsgiref.validate import validator
import re
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, DecimalField, DateTimeField,DateField, BooleanField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import  ValidationError, DataRequired, EqualTo, Length,Email
from app.Model.models import Major, Student, Teacher
from wtforms.widgets import PasswordInput

def getMajors():
    return  Major.query.order_by(Major.title).filter(Major.title != "NONE").all()

def isEmailUnique(form ,field):
    if (Student.query.filter_by(email = field.data).first()) or (Teacher.query.filter_by(email = field.data).first()):
        raise ValidationError("This email is already in use.")

def isWSUIDUnique(form ,field):
    if (Student.query.filter_by(wsuID = field.data).first()) or (Teacher.query.filter_by(wsuID = field.data).first()):
        raise ValidationError("This ID is already in use.")

def isValidSID(form, field):
    if not(len(field.data) == 9 and field.data.isdigit()):
        raise ValidationError("Invalid Value, must be 9 digits")

def isValidPhoneNumber(form, field):
    if not(len(field.data) == 10 and field.data.isdigit()):
        raise ValidationError("Invalid Number, must be 10 digits")

def isWSUEmail(form, field):
    email = field.data.split("@")
    if len(email) < 2 or email[len(email)-1] != "wsu.edu":
        raise ValidationError("Invalid Email, must be wsu.edu")

def getMinors():
    return Major.query.filter_by(title = "NONE").first() + getMajors()

def getMajorTitle(majorObject):
  return majorObject.title

# def checkForValid
class LoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired()])
    password = StringField('Password', validators = [DataRequired()], widget=PasswordInput(hide_value=False))
    remember_me = BooleanField('Remember Me')
    submit = SubmitField("Log In")


class RegistrationForm(FlaskForm):
    firstName = StringField('First Name', validators=[DataRequired()])
    lastName = StringField('Last Name', validators=[DataRequired()])
    wsuID = StringField('WSU ID', validators = [DataRequired(), isWSUIDUnique,isValidSID])
    email = StringField('Email', validators = [DataRequired(), Email(), isEmailUnique, isWSUEmail])#, Unique(User.email)
    phoneNumber = StringField('Phone Number', validators = [DataRequired(), isValidPhoneNumber])
    password = PasswordField('Password', validators=[DataRequired(),EqualTo('password_confirm', message='Passwords must match') ])
    password_confirm = PasswordField('Repeat Password', validators=[DataRequired()])
    submit = SubmitField("Register")


class StudentRegistrationForm(RegistrationForm):
    major =  QuerySelectField( 'Major', query_factory=getMajors , get_label=getMajorTitle, allow_blank=False)
    # minor  =  QuerySelectField( 'Minor', query_factory=getMinors , get_label=getMajorTitle, allow_blank=False)
    cumGPA = DecimalField('Cumulative GPA', places = 2, validators = [DataRequired()])
    graduationDate = DateField('Graduation Date [M-D-Y]', format='%m-%d-%Y', validators = [DataRequired()])



