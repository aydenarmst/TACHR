from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from app import db, login
from flask_login import UserMixin
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(64))
    lastName = db.Column(db.String(64))
    wsuID = db.Column(db.String(9))
    phoneNumber = db.Column(db.String(12))
    email = db.Column(db.String, unique = True)
    password_hash = db.Column(db.String(128))
    userType = db.Column(db.String(1))

    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': userType
    }

    def __repr__(self):
        return f"User - {self.id} - {self.username}"

    def set_password(self, password):
            self.password_hash = generate_password_hash(password)

    def get_password(self, password):
        return check_password_hash(self.password_hash, password)

    def check_password(self,password):
        return check_password_hash(self.password_hash, password)

    def get_user_posts(self):
        return self.posts

studentMajors = db.Table('studentMajors',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
    db.Column('major_id', db.Integer, db.ForeignKey('major.id')))


appToStudent = db.Table('appToStudent',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
    db.Column('application', db.Integer, db.ForeignKey('application.id')))


class Major(db.Model):
    __tablename__ = 'major'
    id = db.Column(db.Integer, primary_key=True)
    title =  db.Column(db.String(128))
    students = db.relationship(
        'Student', secondary=studentMajors,
        primaryjoin=(studentMajors.c.major_id == id), backref=db.backref('studentMajors', lazy='dynamic'), lazy='dynamic')


class TakenCourse(db.Model):
    __tablename__ = 'takencourse'
    id = db.Column(db.Integer,primary_key=True)
    teachercourse_id = db.Column(db.Integer,db.ForeignKey('teachercourse.id'))
    grade = db.Column(db.String(2))
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    semester = db.Column(db.String(150))
    course =db.relationship('TeacherCourse', foreign_keys='TakenCourse.teachercourse_id')


class TeacherCourse(db.Model):
    __tablename__ = 'teachercourse'
    id = db.Column(db.Integer, primary_key=True)
    title =  db.Column(db.String(128))
    studentCourses = db.relationship('TakenCourse', backref='studentCourse', lazy='dynamic')
    tashipCourses = db.relationship('TAShip', backref='tashipCourse', lazy='dynamic')


    

class TAShip(db.Model):
    __tablename__ = "taship"
    id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.Integer,db.ForeignKey('teacher.id'))
    teachercourse_id = db.Column(db.Integer,db.ForeignKey('teachercourse.id'))
    title =  db.Column(db.String(128))
    semester = db.Column(db.String(32))
    TACount = db.Column(db.Integer, default = 1)
    acceptedTACount = db.Column(db.Integer, default = 0)
    cumGPA = db.Column(db.Float)
    minGrade = db.Column(db.String(2))
    experienceRequired = db.Column(db.Boolean)
    # app_id = db.Column(db.Integer, db.ForeignKey("application.id"))
    applications = db.relationship('Application', backref='taship', lazy='dynamic')
    


class Student(User):
    __tablename__ = 'student'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    # major = db.Column(db.String(128))
    major = db.relationship(
        'Major', secondary=studentMajors,
        primaryjoin=(studentMajors.c.student_id == id), backref=db.backref('studentMajors', lazy='dynamic'), lazy='dynamic')
    cumGPA = db.Column(db.Float)
    graduationDate = db.Column(db.DateTime)
    takencourses = db.relationship('TakenCourse', backref='takenStudent', lazy='dynamic')
    applications = db.relationship('Application', backref='applicationStudent', lazy='dynamic')

    __mapper_args__ = {
        'polymorphic_identity': 'student'
    }

class Teacher(User):
    __tablename__ = 'teacher'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    TAships = db.relationship('TAShip', backref='creator', lazy='dynamic')

    __mapper_args__ = {
        'polymorphic_identity': 'teacher'
    }

class Application(db.Model):
    __tablename__ = 'application'
    id = db.Column(db.Integer, primary_key=True)
    appTime = db.Column(db.DateTime)
    status = db.Column(db.String(150))
    student_id = db.Column(db.Integer,db.ForeignKey('student.id'))
    taship_id = db.Column(db.Integer,db.ForeignKey('taship.id'))
