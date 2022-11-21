from __future__ import print_function
import email
import sys
from flask import Blueprint
from flask import render_template, flash, redirect, url_for
from flask_sqlalchemy import sqlalchemy
from flask_login import login_user, current_user, logout_user, login_required
from config import Config

from app.Controller.auth_forms import LoginForm, StudentRegistrationForm,RegistrationForm
from app.Model.models import User, Student, Teacher

from app import db

bp_auth = Blueprint('auth', __name__)
bp_auth.template_folder = Config.TEMPLATE_FOLDER

@bp_auth.route('/registerStudent', methods=['GET', 'POST'])
def registerStudent():
    if current_user.is_authenticated:
        return redirect(url_for('routes.index'))
    studentForm = StudentRegistrationForm()
    if studentForm.validate_on_submit():
        student = Student(firstName=studentForm.firstName.data, lastName=studentForm.lastName.data, wsuID=studentForm.wsuID.data, phoneNumber=studentForm.phoneNumber.data, email=studentForm.email.data, major=[studentForm.major.data], cumGPA=studentForm.cumGPA.data, graduationDate=studentForm.graduationDate.data)
        student.set_password(studentForm.password.data)
        db.session.add(student)
        db.session.commit()
        flash('Congratulations, you are now a registered student user!')
        return redirect(url_for('auth.login'))
    return render_template('studentRegister.html',title = 'Student Register', form = studentForm)

@bp_auth.route('/registerTeacher', methods=['GET', 'POST'])
def registerTeacher():
    if current_user.is_authenticated:
        return redirect(url_for('routes.index'))
    teacherForm = RegistrationForm()
    if teacherForm.validate_on_submit():
        teacher = Teacher(firstName=teacherForm.firstName.data, lastName=teacherForm.lastName.data, wsuID=teacherForm.wsuID.data, phoneNumber=teacherForm.phoneNumber.data, email=teacherForm.email.data)
        teacher.set_password(teacherForm.password.data)
        db.session.add(teacher)
        db.session.commit()
        flash('Congratulations, you are now a registered teacher user!', )
        return redirect(url_for('routes.index'))
    return render_template('teacherRegister.html',title = 'Teacher Register', form = teacherForm)

@bp_auth.route('/login', methods =['GET','POST'])
def login():
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        user = User.query.filter_by(email = loginForm.email.data).first()
        #Login Failure Check
        if (user is None) or not user.get_password(loginForm.password.data):
            flash('Invalid email or password. Please try again!')
            return redirect(url_for('auth.login'))
        login_user(user, remember = loginForm.remember_me.data)
        return redirect(url_for('routes.index'))
    return render_template('login.html',title = 'Login', form = loginForm)

@bp_auth.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.index'))