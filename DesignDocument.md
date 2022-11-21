# Design Document

## TAChr
--------
Prepared by:

* `Gabriel Righi`,`Washington State University`
* `Zayn Abou-Harb`,`Washington State University`
* `Stefanos Pamboukas`,`Washington State University`
* `Ayden Armstrong`,`Washington State University`
---

**Course** : CptS 322 - Software Engineering Principles I

**Instructor**: Sakire Arslan Ay
---

## Table of Contents
- [Design Document](#design-document)
  - [TAchr](#-TACHR)
  - [Table of Contents](#table-of-contents)
    - [Document Revision History](#document-revision-history)
- [1. Introduction](#1-introduction)
- [2.	Architectural and Component-level Design](#2architectural-and-component-level-design)
  - [2.1 System Structure](#21-system-structure)
  - [2.2 Subsystem Design](#22-subsystem-design)
    - [2.2.1 Model](#221-model)
    - [2.2.2 Controller](#222-controller)
    - [2.2.3 View and User Interface Design](#223-view-and-user-interface-design)
- [3. Progress Report](#3-progress-report)
- [4. Testing Plan](#4-testing-plan)
- [5. References](#5-references)
- [Appendix: Grading Rubric](#appendix-grading-rubric)

<a name="revision-history"> </a>

### Document Revision History

| Name | Date | Changes | Version |
| ------ | ------ | --------- | --------- |
|Revision 1 |2022-18-10 |Initial draft | 1.0        |
|Revision 2 |2022-14-11 |Iteration 2   |1.1      |
|      |      |         |         |


# 1. Introduction

This document is meant to outline the project structure for our group project TAchr. This design document is meant to keep all the developers and the client on the same page when it comes to how we plan to implement the design of our website. The goal of our project is to create a hub for teachers and students to come together to find TAships for interested students. Teachers will be able to post TA positions that students will be able to apply for. This matching will ease the process of aquiring TA's for both Teachers and Students. 

This first section of this document contains an introduction which discusses the scope and purpose of this project and document. The second section of this document contains most of the revelant information. It outlines the MVC pattern that we will implement in our project. The third section contains progress reports about the project. The fourth section outlines how plan for testing the project, and will not be included in iteration 1. The fifth section outlines any references we have. 



[Section II](#2-architectural-and-component-level-design) includes Architectural and Component-level Design

[Section III](#22-subsystem-design) includes Our Progres report

# 2.	Architectural and Component-level Design
## 2.1 System Structure

![](https://i.imgur.com/XB1j1JO.png)


The View subsystem controls the UI depending on which kind of user is logged in. It will display TAShips for logged in students, and will display TAShip applications for logged in teachers.

The Controller manages the interaction between the Model and the View. It will take information from the view, and give it to the model to add to the database.

The Model controls the storage and definition of data on the backend. It will return data when queried, and store necessary data when asked. 

The reason why we adopted the MCV is it helps define clear boundaries between what each part of the project is supposed to do. We can create templates for our view aspect, and send them data from our model via the controller. It helps us break down the front and backend of the code into separate components to make things easier to manage each side. It also seperates the data from the view, which allows us to modify the later without having to redefine our model.



## 2.2 Subsystem Design 

### 2.2.1 Model

The model is the component that describes how our datastructure and backend is implemented. The point of separating the model from the view and controller is so the view and controller can call data from the model without having to know how the model implements its data storage. 


| User      | Attribute Type |
| ----------- | ----------- |
| id      | Integer, Primary Key       |
| firstName   | String        |
| lastName   | String        |
| wsuID   | String        |
| phoneNumber   | String        |
| email   | String        |
| password_hash   | String        |
| userType | String |

The User class is the parent class for all types of accounts in our database. A User can either be extended to be a student, or a teacher, but someone with an account is never directly a User themselves. This class stores essential information about the Client, and the specific data can be seen in the table above. 

|studentMajors (TABLE) | ForeignKey|
| ----------- | ----------- |
| student_id | student.id|
| major_id | major.id|

The studentMajors table creates a many to many relationship between student

| Major       | Attribute Type |
| ----------- | ----------- |
| id          | Integer     |
| title       | String      |
| students    | Many to One Relation to Student | 

The major class defines a preset series of majors that a student can claim to be studying. There is a many to many relationship between majors and students. A major can relate to many students, and each student can have multiple majors. This covers the case of a student having multiple majors ( though we have not implemented this case yet). The major only has a title, studentlist, and id.



| Teacher Course    | Attribute Type |
| ----------- | ----------- |
| id          | Integer|
| title |String|

The teacher course class defines a preset series of classes that a teacher can create a TAship for. The class only has a title and id



| TAShip       | Attribute Type |
| ----------- | ----------- |
| id          | Integer     |
| creator_id  | One to many relationship to Teacher Class (ForeignKey=teacher.id)     |
| title       | String|
|semester | String|
| TACount | Integer (default = 1)|
| cumGPA | Float|
| minGrade | String|
| experienceRequired| Boolean|

The TAShip class stores data for a TAShip created by a teacher. The TAShip has a one to many relationship with the Teacher class. A teacher can have multiple TAShips, but a TAShip only has one teacher. The TAShip class stores the above data listed in the table. 

| Student (Extends User)      | Attribute Type |
| ----------- | ----------- |
| id| Integer (Foreign Key = user.id)|
| major      | Many to Many Relationship with Major       |
| GPA   | Float       |
| graduationDate   | DateTime        |
| takencourses| A many to one relationship with the TakenCourse class|
| applications| A many to one relationship with the Application class|


The Student class is an extension of the User class. The student class defines a new ID, with a foreign key of the User table, and stores specific information to a student. One student can map to many majors.


The Teacher class is an extension of the User class. The teacher defines a new id, and a Many to one relationship with the TAShip class.

| Teacher       | Attribute Type |
| ----------- | ----------- |
| id|Integer (Foreign Key = user.id)|
| TAShips | Many to one relationship to TAship class |

The taken course class relates a course to a student taken at a specific time. It stores when the student took a class, and the grade they got in it

| TakenCourse       | Attribute Type |
| ----------- | ----------- |
| id|Integer (Primary Key)|
| teachercourse_id | one to Many relationship to the TeacherCourse class |
| grade | String|
| student_id| one to Many relationship to the Student Class|
| course | backreference variable to access related TeacherCourse|

The application class stores a student's application to a TAship. It stores when they applied, and the current status of their application. It relates the application to a specific student

| Application       | Attribute Type |
| ----------- | ----------- |
| id|Integer (Primary Key)|
| appTime | DateTime|
| status | String|
| student_id| one to Many relationship to the Student Class|
| taship_id | one to Many relationship to the TAship Class|



<br>


![](https://i.imgur.com/vUSpqVw.png)


### 2.2.2 Controller

Briefly explain the role of the controller. If your controller is decomposed into smaller subsystems (similar to the Smile App design we discussed in class), list each of those subsystems as subsections. 

The controller controls the flow of the program. When the user attempts to request data, and the controller requests its from the model, and then returns it to the user in the view. The controller also has gets forms from the model that it displays to the user via the view. It controls all the calls for routing, and manages all calls to the database. 

There are 3 Subsystems I will define are the Auth Controller, Form Controller, and Route Controller

Auth Controller
The auth controller controls all login sensitive information and controls the actual login feature. Through the auth controller classes and methods, one can create accounts for teachers and students, and login as a teacher or a student. The auth controller contains all the forms necessary for submitting login information. It also contains all the routes necessary for submitting information. Auth controller queries the database for form validation.

Route Controller
The route controller stores all the routes for non-login requests. It queries and adds info to the database, and gets input from the form controller. The route controller will send all necessary forms to the view, and will add data from the forms to the database



|   | Methods           | URL Path   | Description  |
|:--|:------------------|:-----------|:-------------|
|1. index() | GET, POST                 |/index            | This route should redirect the user to the login route if they are not logged in. If the user is logged in as a TA, it should display all the open TAships that the User could apply for. If the user is logged in as a teacher, it should show all the applications they have recieved for their TA positions. If a TA clicks apply on a TAship, it should send a get request to the index route, for the apply to TAship route. If the teacher accepts a TA for a position, it should send a post request to the index route, and update the database.             |
|2. registerTeacher()| GET, POST                  |/registerTeacher            | This route should allow teachers to create an account. Once they have created an account they should be redirected to the login route, and be logged in   |
|3. registerStudent()| GET, POST                  | /registerStudent           | This route should allow students to create an account. Once they have created an account they should be redirected to the login route, and be logged in             |
|4. login()| GET, POST                  | /login           | This route should login the user (if they enter proper information), and redirect them to the index route.              |
|5. logout()| GET                   |  /logout          | This route should logout the user,and redirect them to login page.             |
|6. display_profile()|GET, POST|/display_profile<id>|This page allows a user to display their profile. If the user is a student, then the profile displayed will be that of a student profile with the necessary information filled in. It will also give the student the option to add classes to their profile and edit their profile information. If the user logged in is a teacher, then it will fill in the teacher's information. It will show the teacher's created TAships and the allow the teacher to edit their profile information|
|7. edit_profile()|GET, POST|/edit_profile|This page allows either a teacher or student user to edit their profile information. When the user submits the form, they will be redirected to the profile page, and the necessary information will be updated in the database|
|8. createTAShip()|GET, POST|/createApplication|This page will display a form that allows teachers to create a TAship. If a non logged in teacher tries to access this page they will be redirect to index. Upon clicking submit, a post request will be sent to the server and the user will be redirected to the index page. The TAship will be added to the database. |
|9. deleteClass()|POST|/delete_class|This route will delete a class selected by the student on their profile page. If the current user is not logged in as a student, it will reroute to the main profile page.|
|10. apply()|POST|/apply<id>|This page will display a form that allows students to apply for a TAship. If a non logged in teacher tries to access this page they will be redirect to index. Upon clicking submit, a post request will be sent to the server and the user will be redirected to the index page. The student's application will be added to the database for that TAship. |
|11. viewApplicants()|POST|/viewApplicants<id>|This page will display a page that allows teachers view applicants for a TAship. If a non logged in teacher tries to access this page they will be redirect to index. Upon clicking accept, a post request will be sent to the server and the user will be redirected to the index page. The student who applied for the TAship will be accepted and will be put into the database. |
|12. assign_student()| GET, POST| /assign_student<sid><cid><mode>|This route will allow a teacher to assign or reject a student to a specific TAship. The database will be updated with the relevant student id appened to the TAship class if necessary. It will then redirect the user to the view applicants page, and decrement the ta count. |
|13. withdraw_app| POST|/withdraw_app<id>| This route will remove a student's application from the potential TAships, and allow them to reapply if they so wish. It will redirect them to the index page after so they can view all their applications|
    







### 2.2.3 View and User Interface Design 


We’ll be using the HTML and WTForms to build the framework of the interface of the application.
The page templates that we used were from the smile application, which we’ll use and modify to show the interface. Error templates and the login template will be implemented, as well as the base for the interface and index templates. The create template that was originally used to create a new post will be used to create a new TA position for students to apply for. The register template will be separated into two, one being for students and the other being for teachers.

The below image shows a screenshot of the login page. The login page allows a user to sign in as either a student or a teacher. It also contains hyperlinks to allow someone to register as a teacher or student 
![](https://i.imgur.com/P9nbjCq.png)


The register for student page will allow a student to register for a student account. 
![](https://i.imgur.com/Us5brKq.png)


The register for teacher page will allow a teacher to register for a teacher account.
![](https://i.imgur.com/xPnRCCB.png)




The student view will consist of recommended positions that the student should apply for based on their GPA and major and show the name of the position and requirements. The status of the open position will also show whether the student has applied for it or not. The page will also give the user the option to logout and show pending applications. Use Case #3, 4, and 6 will utilize the interface. This page will eventually grow to contain a list of reccomended courses for a student. As of now this has not been implemented, but there will be an option for that in interation 3. It will also display if a student has been reject or accepted for a TAship. 

![](https://i.imgur.com/BY4KWAC.png)



The Student profile view allows a student to edit their profile information, and also to add classes they have taken
    ![](https://i.imgur.com/fXC8H1x.png)

The edit sutdent page allows a student to edit their profile information
    ![](https://i.imgur.com/W9XA0FZ.png)


Faculty view will show current positions posted for students to apply to, and faculty can view those applications for the positions. Options to logout and create positions are also available. Use case #8, 9,  and 3 will be utilized.

![](https://i.imgur.com/C0jNql9.png)


The application viewer for faculty will show all students who applies for the position and gives them the option to accept students into the position. Option to logout will be available. Use case #3 and 9 will be utilized. From this page in the future, a teacher will have an option to reject or accept students for a specific TAship. 

![](https://i.imgur.com/DZU7Vzj.png)


The position adder will allow faculty to fill out information to create a new open position for students to fill out. Logout and main page links will be available. Use cases #3, and 8 will be utilized.

![](https://i.imgur.com/IZaYzDF.png)
    
Teachers can also edit their profile like a student, and can view the TAShips they have created
    ![](https://i.imgur.com/adeOAqe.png)







# 3. Progress Report

For the first iteration, we completed all of our tasks laid out in the document specification. We implemented necessary forms for registering, logging in, and creating TAShips. We created relevant routes for the aforementioned forms, and add the given data to the database. We created templates for all of our forms, and our main index page, which displays relevant data. We also implemented login for multiple users, and added necssary relationships between models. 
    
For the second iteration, we completed the second pile of tasks laid out in the document specification. We created pages for viewing and applying for open TAships as well as displaying the nessesary information for the TAships, as well as creating a page for faculty to see who applied for TAships for their courses. Additional route controllers and a UML class diagram has also been added to the document. 
    
# 4. Testing Plan
    
To minimize the amount of work we actually have to do, we will rely on automatic testing where possible, and will defer to humans when automatic testing is not realistic. The main aspects of our program that we need to test are as follows:
    
    Can a user create a student account
    Can a user create a teacher account
    Can a student edit their profile information
    Can a student add a class to their profile
    Can a student apply to a TAship
    Can a student un-apply to a TAship
    Can a teacher create a TAship
    Can a teacher accept a student for a TAship
    Can a teacher reject a student for a TAship
    
Now that we have established the general material that we are testing I will break the above tests into the categories of Unit Testing, Functional Testing, and UI Testing. For the first two we plan on using unittest as it looks like it will fit our needs the best.
    
| Unit Testing      | Description|
| :---        |    :---|
| Student model      | Create a new user that is a student, and assert that all the data values match the preprogrammed data values|
| Teacher Model | Create a new user that is a teacher, and assert that all the data values in the class match the preprogrammed data values|
| Major model | Create a new major, and append it to a student object. Assert that the major has the correct data values, and can be accessed via the student class|
|TakenCourse model| Create a course that has been taken by a student. Assert that its data values are accurate. Attach the takencourse to a student and a teachercourse and assert that the takencourse can be accessed via both the takencourse and the student objects|
| TeacherCourse model| Create a teachercourse and assert that all its data values match what is expected.|
|TAship model| Create a taship and assert that all its values are expected. Connect the TAship to a teacher, and assert that the correct teacher can be accessed via the model. Add multiple students to TAship, and assert that they have been added on both TAship and student's ends.Also assert that the correct class has been associated with TAShip|
|Application Model| Create an application and assert that all its data values match what is expected. Connect the application to a student and to a TAship. Assert that the application can be accessed via the student and via the TAship.|

The below list will be tested both functionally by humans, and automatically by unit testing
    
| Functional Testing/Unit Testing      | Description| 
| :---        |    :---|    
| RegisterStudent Route| Assert that after calling register student with filled in form, that the data matches what we would expect. Also assert that the student has been added to the database|
| RegisterTeacher Route| Assert that after calling registerteacher with filled in form, that the data matches what we would expect. Assert that the teacher has been added to the database|
|Login Route| Assert that after calling user login with a valid account, that the user is logged in. Assert that after calling login with an invalid account, that the user is not logged in|
|Logout Route| Assert that after calling logout, the user is no longer logged in|
|Index route| Assert that after calling index, if the user is a student, they are returned a list of TAlistings. Assert that if the user is a teacher, they are returned a list of their TAships. Also assert that a non-logged in user cannot access this page and is redirected to login|
|createTAship route| Assert that after calling this route with approrpriate TAship information, that a new TAship has been entered into the database|
|deleteClass route| Assert that after calling this route, the logged in user no longer has the listed class in their taken classes list. 
|editProfile| Assert that after this form has been submitted, the logged in user's information has been updated to reflect the forms contents|
|Apply Route| Assert that after a student has applied for a TAship, that the TAship in the database now contains an application object with the correct student appended|
|View applicants| Assert that when this is called, a teacher account is returned a list of applicants for a given TAship id.|
        
For the UI testing, we will rely on manual testing of the same routes and functionalities that we outlined above. These tests will focus on making sure that the visuals are what we expected and that the user input fields accept the data as expected.
    

# 5. References



Arslan Ay, Sakire - Smile App - https://github.com/WSU-CptS322-Fall2022/SmileApp-Tasks


----
# Appendix: Grading Rubric
(Please remove this part in your final submission)

These is the grading rubric that we will use to evaluate your document. 


|**MaxPoints**| **Design** |
|:---------:|:-------------------------------------------------------------------------|
|           | Are all parts of the document in agreement with the product requirements? |
| 10        | Is the architecture of the system described well, with the major components and their interfaces?  Is the rationale for the proposed decomposition in terms of cohesion and coupling explained well? |
| 15        | Is the document making good use of semi-formal notation (i.e., UML diagrams)? Does the document provide a clear and complete UML component diagram illustrating the architecture of the system? |
| 15        | Is the model (i.e., “database model”) explained well with sufficient detail? | 
| 10        | Is the controller explained in sufficient detail?  |
| 22        | Are all major interfaces (i.e., the routes) listed? Are the routes explained in sufficient detail? |
| 10        | Is the view and the user interfaces explained well? Did the team provide the screenshots of the interfaces they built so far.   |
| 5         | Is there sufficient detail in the design to start Iteration 2?   |
| 5         | Progress report  |
|           |   |
|           | **Clarity** |
| 3         | Is the solution at a fairly consistent and appropriate level of detail? Is the solution clear enough to be turned over to an independent group for implementation and still be understood? |
| 5         | Is the document carefully written, without typos and grammatical errors?  |
|           |  |
|           | **Total** |
|           |  |