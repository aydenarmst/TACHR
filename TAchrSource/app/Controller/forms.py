from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, DecimalField, BooleanField, PasswordField, DateField
from wtforms.validators import  ValidationError, DataRequired, Length, EqualTo, Email
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.widgets import CheckboxInput
from flask_login import current_user
import datetime

from app.Model.models import TeacherCourse, Major, Student, Teacher, User

def get_courses():
    return TeacherCourse.query.all()

def get_course_title(course):
    return course.title

def getMajors():
    return  Major.query.order_by(Major.title).filter(Major.title != "NONE").all()

def getMajorTitle(majorObject):
  return majorObject.title

def get_semesters():
    year = datetime.date.today().year
    return [f"Fall {year}", f"Spring {year}",f"Fall {year+1}",f"Spring {year+1}"]

def previousSemesters():
    year = datetime.date.today().year
    yearsBack = 4
    semesters = []
    for i in range(yearsBack):
        semesters.append(f"Fall {year - i}")
        semesters.append(f"Spring {year - i}")
    return semesters

def isValidPhoneNumber(form, field):
    if not(len(field.data) == 10 and field.data.isdigit()):
        raise ValidationError("Invalid Number, must be 10 digits")

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    happiness_level = SelectField('Happiness Level',choices = [(3, 'I can\'t stop smiling'), (2, 'Really happy'), (1,'Happy')])
    submit = SubmitField('Post')

class SortForm(FlaskForm):
    sortByQualify = BooleanField('Only display listings that match my qualifications')
    submit = SubmitField('Refresh')

class CreateTAShipForm(FlaskForm):
    courseTitle =  QuerySelectField( 'Course', query_factory=get_courses , get_label=get_course_title, allow_blank=False)
    semester = SelectField("Semester", choices=get_semesters())
    TACount = IntegerField('TA Count', validators=[DataRequired()])
    cumGPA = DecimalField('Min GPA', places = 2, validators = [DataRequired()])
    minGrade = SelectField("Min Grade in Class", choices=['A','A-','B+','B','B-','C+','C','C-','D+','D','D-','F'])
    experienceRequired = BooleanField("Prior TA Experience Required?")
    submit = SubmitField('Create TA Position')

class EditForm(FlaskForm):
    firstName = StringField('First Name', validators=[DataRequired()])
    lastName = StringField('Last Name', validators=[DataRequired()])
    wsuID = StringField('WSU ID', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired(), Email()])
    phoneNumber = StringField('Phone Number', validators = [DataRequired(), isValidPhoneNumber])
    password = PasswordField('Password', validators=[DataRequired(),EqualTo('password_confirm', message='Passwords must match') ])
    password_confirm = PasswordField('Repeat Password', validators=[DataRequired()])
    submit = SubmitField("Submit")

    def validate_email(self, email):
        domain = email.data.split("@")
        if len(domain) < 2 or domain[len(domain)-1] != "wsu.edu":
            raise ValidationError("Invalid Email, must be wsu.edu")

        users = User.query.filter_by(email = email.data).all()
        for user in users:
            if (user.id != current_user.id):
                raise ValidationError('This email is already in use! Please use a diffrent email.')

    def validate_wsuID(self, wsuID):
        if not(len(wsuID.data) == 9 and wsuID.data.isdigit()):
            raise ValidationError("Invalid Value, must be 9 digits")

        users = User.query.filter_by(wsuID = wsuID.data).all()
        for user in users:
            if (user.id != current_user.id):
                raise ValidationError('This wsu ID is already in use! Please use a diffrent wsu ID.')

class EditStudentForm(EditForm):
    major =  QuerySelectField( 'Major', query_factory=getMajors , get_label=getMajorTitle, allow_blank=False)
    # minor  =  QuerySelectField( 'Minor', query_factory=getMinors , get_label=getMajorTitle, allow_blank=False)
    cumGPA = DecimalField('Cumulative GPA', places = 2, validators = [DataRequired()])
    graduationDate = DateField('Graduation Date [M-D-Y]', format='%m-%d-%Y', validators = [DataRequired()])

class CourseAddForm(FlaskForm):
    courseTitle =  QuerySelectField( 'Course', query_factory=get_courses , get_label=get_course_title, allow_blank=False)
    grade = SelectField("Min Grade in Class", choices=['A','A-','B+','B','B-','C+','C','C-','D+','D','D-','F'])
    semester = SelectField("Semester", choices=previousSemesters())
    submit = SubmitField("Add Class")


