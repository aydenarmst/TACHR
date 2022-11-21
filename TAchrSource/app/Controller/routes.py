from __future__ import print_function
import sys
from flask import render_template, Blueprint,flash, redirect, url_for, request
from config import Config
from flask_login import login_user, current_user, logout_user, login_required
from app import db
from app.Model.models import TAShip, TakenCourse, Application, Student
from app.Controller.forms import CreateTAShipForm, SortForm, EditForm, EditStudentForm, CourseAddForm
from datetime import datetime


def grade_to_number(grade):
    if(grade == 'A'):
        return 10
    elif (grade == 'B+'):
        return 9
    elif (grade == 'B'):
        return 8
    elif (grade == 'B-'):
        return 7
    elif (grade == 'C+'):
        return 6
    elif (grade == 'C'):
        return 5
    elif (grade == 'C-'):
        return 4
    elif (grade == 'D+'):
        return 3
    elif(grade == 'D'):
        return 2
    elif (grade== 'D-'):
        return 1
    elif (grade == 'F'):
        return 0
    return 0

bp_routes = Blueprint('routes', __name__)
bp_routes.template_folder = Config.TEMPLATE_FOLDER #'..\\View\\templates'



@bp_routes.route('/', methods=['GET','POST'])
@bp_routes.route('/index', methods=['GET','POST'])
#@login_required
def index():
    #return redirect(url_for('auth.login'))
    sForm = SortForm()
    # posts = Post.query.order_by(Post.timestamp.desc())
    if current_user.is_authenticated:
        all_taships = TAShip.query.order_by(TAShip.title.desc()).all()
        if current_user.userType == 'teacher':
            all_taships = TAShip.query.filter(TAShip.creator_id == current_user.id).order_by(TAShip.title.desc()).all()
            return render_template('teacherIndex.html', title="TAcherTeacher", TAShips=all_taships, form = sForm)
        else:
            if sForm.sortByQualify.data:
                all_taships = TAShip.query.filter(TAShip.cumGPA <= current_user.cumGPA).order_by(TAShip.title.desc()).all()
            return render_template('studentIndex.html', title="TAcherStudent", TAShips=all_taships, form = sForm)
    return redirect(url_for('auth.login'))

@bp_routes.route('/createTAShip', methods=['GET', 'POST'])
@login_required
def createTAShip():
    if current_user.userType == "teacher":
        TAForm = CreateTAShipForm()
        if TAForm.validate_on_submit():
            newTAShip = TAShip(
                title =  TAForm.courseTitle.data.title,
                teachercourse_id = TAForm.courseTitle.data.id,
                semester = TAForm.semester.data,
                TACount = TAForm.TACount.data,
                cumGPA = TAForm.cumGPA.data,
                minGrade = TAForm.minGrade.data,
                experienceRequired = TAForm.experienceRequired.data,
                creator_id = current_user.id
            )
            db.session.add(newTAShip)
            db.session.commit()
            flash("Successfully Created TA Position")
            return redirect(url_for('routes.index'))
        return render_template('createTAShip.html', title='Create TA Position', form = TAForm)
    else:
        return redirect(url_for('routes.index'))

@bp_routes.route('/delete_class/<id>', methods=['POST'])
@login_required
def delete_class(id):
    if current_user.userType == "student":
        print(id)
        TakenCourse.query.filter_by(id = id).delete()
        db.session.commit()
    return redirect(url_for('routes.display_profile', id=id))
    
@bp_routes.route('/display_profile/<id>', methods=['GET', 'POST'])
@login_required
def display_profile(id):
    courseAddForm = CourseAddForm() if current_user.userType == "student" else None
    if courseAddForm is not None and courseAddForm.validate_on_submit():
        presentCourse = TakenCourse.query.filter_by(teachercourse_id = courseAddForm.courseTitle.data.id).filter_by(student_id = current_user.id).first()
        if presentCourse is None:
            print(courseAddForm.courseTitle.data.id)
            current_user.takencourses.append(TakenCourse(teachercourse_id = courseAddForm.courseTitle.data.id, grade = courseAddForm.grade.data, semester = courseAddForm.semester.data))
        else:
            presentCourse.grade = courseAddForm.grade.data
            presentCourse.semester = courseAddForm.semester.data
        db.session.commit()
    if current_user.userType == "teacher":
        currentTAShip = TAShip.query.filter(TAShip.creator_id == current_user.id).first()
        if currentTAShip is not None:
            for applicant in currentTAShip.applications:
                    applicant = Student.query.filter_by(id = id).first()
                    if applicant is not None:
                        return render_template('display_profile.html', title='Display Profile', profile = applicant)
            
    return render_template('display_profile.html', title='Display Profile', profile = current_user, courseAddForm = courseAddForm)

@bp_routes.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    is_student = current_user.userType == "student"
    eform = EditStudentForm() if is_student else EditForm()
    if request.method == 'POST':
        #handle form submission
        if eform.validate_on_submit():
            current_user.email = eform.email.data
            current_user.firstName = eform.firstName.data
            current_user.lastName = eform.lastName.data
            current_user.wsuID = eform.wsuID.data
            current_user.phoneNumber = eform.phoneNumber.data
            current_user.set_password(eform.password.data)
            if is_student:
                print("test")
                current_user.major=[eform.major.data]
                current_user.cumGPA=eform.cumGPA.data
                current_user.cumGPA=eform.cumGPA.data
                current_user.graduationDate=eform.graduationDate.data
            db.session.add(current_user)
            db.session.commit()
            flash("Your changes have been saved")
            return redirect(url_for('routes.display_profile', id = current_user.id))
    else:
        #populate the user from DB
        eform.email.data = current_user.email
        eform.firstName.data = current_user.firstName
        eform.lastName.data = current_user.lastName
        eform.wsuID.data = current_user.wsuID
        eform.phoneNumber.data = current_user.phoneNumber
        if is_student:
                eform.major.data = current_user.major
                eform.cumGPA.data = current_user.cumGPA
                eform.graduationDate.data = current_user.graduationDate
    return render_template('edit_profile.html', title='Edit Profile', form = eform, student_mode = is_student)
        
@bp_routes.route('/apply/<id>', methods=['POST'])
@login_required
def apply(id):
    if current_user.userType == "student":
        currentTAShip = TAShip.query.filter_by(id = id).first()
        currentTakenCourse = current_user.takencourses.filter_by(teachercourse_id = currentTAShip.teachercourse_id).first()
        if currentTakenCourse:
            if grade_to_number(currentTakenCourse.grade) >= grade_to_number(currentTAShip.minGrade):
                if current_user.cumGPA >= currentTAShip.cumGPA:
                    application = Application.query.filter_by(taship_id = id).filter_by(student_id = current_user.id).first()
                    if application is None:
                        application = Application(appTime = datetime.now(), status = "Pending", student_id = current_user.id, taship_id = id)
                        db.session.add(application)
                        db.session.commit()
                        flash("Successfully applied!")
                    else:
                        flash("You have already applied")
                else:
                    flash("Your GPA is not high enough")
            else:
                flash("Your grade is not high enough")
        else:
            print(currentTAShip.teachercourse_id)
            print(current_user.takencourses.all)
            flash("You have not taken this class")
    return redirect(url_for('routes.index'))

@bp_routes.route('/viewApplicants/<id>', methods=['GET','POST'])
@login_required
def viewApplicants(id):
    if current_user.userType == "teacher":
        currentTAShip = TAShip.query.filter(TAShip.id == id).first()
        if currentTAShip is not None and currentTAShip.creator_id == current_user.id:
            applicantList = currentTAShip.applications.filter(Application.status != "Rejected")
            if currentTAShip.acceptedTACount == currentTAShip.TACount:
                applicantList = applicantList.filter_by(status = "Accepted")
            return render_template('viewApplicants.html', title='View Applicants', taship = currentTAShip, applicants = applicantList)
    return redirect(url_for('routes.index'))

@bp_routes.route('/accept/<sid><tid><option><vid>', methods=['GET','POST'])
@login_required
def accept(sid, tid,option,vid):
    if current_user.userType == "teacher":
        currentTAShip = TAShip.query.filter_by(id = tid).first()
        if currentTAShip is not None:
            currentApplication = currentTAShip.applications.filter_by(student_id = sid).first()
            if currentApplication is not None and currentApplication.status == "Pending":
                if option == '0': # Accept
                    currentApplication.status = "Accepted"
                    currentTAShip.acceptedTACount += 1
                else: # Reject
                    currentApplication.status = "Rejected"
            db.session.commit()
    return redirect(url_for('routes.viewApplicants', id = vid))

@bp_routes.route('/rescind/<id>', methods=['POST'])
@login_required
def rescind(id):
    if current_user.userType == "student":
        currentApplication = TAShip.query.filter_by(id = id).first().applications.filter_by(student_id = current_user.id)
        print(currentApplication)
        if currentApplication is not None and currentApplication.first().status == "Pending":
            currentApplication.delete()
            db.session.commit()
    return redirect(url_for('routes.index'))

# @bp_routes.route('/add_course', methods=['GET', 'POST'])
# @login_required
# def add_course():
#     is_student = current_user.userType == "student"
#     if is_student:
#         return redirect(url_for('routes.display_profile'))
#     else:
#         return redirect(url_for('routes.display_profile()'))
    

    