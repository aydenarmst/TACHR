from app import create_app, db
from app.Model.models import Teacher, Student, TeacherCourse, Major
from datetime import date

app = create_app()

@app.before_first_request
def initDB(*args, **kwargs):
    db.create_all()
    # if Tag.query.count() == 0:
    #     tags = ['funny','inspiring', 'true-story', 'heartwarming', 'friendship']
    #     for t in tags:
    #         db.session.add(Tag(name=t))
    #     db.session.commit()
    if TeacherCourse.query.first() is None:
        with open("app/data/classes.txt","r") as classesFile:
            for line in classesFile.readlines():
                db.session.add(TeacherCourse(title=line.rstrip())) 
            db.session.commit()

    if Major.query.first() is None: # If There are No Majors, load them all
        with open("app/data/majors.txt","r") as majorsFile:
            for line in majorsFile.readlines():
                db.session.add(Major(title=line.rstrip())) 
            db.session.add(Major(title="NONE"))
            db.session.commit()

    if Student.query.first() is None:
        # student = Student(firstName="foo", lastName="foo", wsuID="123456789", phoneNumber="1234567890", email="foo@wsu.edu", major=Major.query.first(), minor=Major.query.first(), cumGPA=4.0, graduationDate=date.today())
        for i in range(10):
            student = Student(firstName=f"foo{i}", lastName="foo", wsuID=f"00000000{i}", phoneNumber=f"000000000{i}", email=f"foo{i}@wsu.edu", major=[Major.query.first()], cumGPA=4.0, graduationDate=date.today())
            student.set_password("foo")
            teacher = Teacher(firstName=f"bar{i}", lastName="bar", wsuID=f"0000000{i}0", phoneNumber=f"00000000{i}0", email=f"bar{i}@wsu.edu")
            teacher.set_password("bar")
            db.session.add(student)
            db.session.add(teacher)
        db.session.commit()

    
if __name__ == "__main__":
    app.run(debug=True)