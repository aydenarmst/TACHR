# Software Requirements Specification

TAchr
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
- [Software Requirements Specification](#software-requirements-specification)
  - [## Your Project Title](#-your-project-title)
  - [Table of Contents](#table-of-contents)
  - [Document Revision History](#document-revision-history)
- [1. Introduction](#1-introduction)
  - [1.1 Document Purpose](#11-document-purpose)
  - [1.2 Product Scope](#12-product-scope)
  - [1.3 Document Overview](#13-document-overview)
- [2. Requirements Specification](#2-requirements-specification)
  - [2.1 Customer, Users, and Stakeholders](#21-customer-users-and-stakeholders)
  - [2.2 Use Cases](#22-use-cases)
  - [2.3 Non-Functional Requirements](#23-non-functional-requirements)
- [3. User Interface](#3-user-interface)
- [4. Product Backlog](#4-product-backlog)
- [5. References](#5-references)
- [Appendix: Grading Rubric](#appendix-grading-rubric)

<a name="revision-history"> </a>

## Document Revision History

| Name | Date | Changes | Version |
| ------ | ------ | --------- | --------- |
|Revision 1 |2022-12-05 |Initial draft | 1.0        |
|      |      |         |         |
|      |      |         |         |

----
# 1. Introduction

This document will outline our specifications and design goals for our TAchr website project. Its formatting lays out a clear vision for TAchr's creation and functionality.

## 1.1 Document

The purpose of this document is to allow the desginers and clients to have a cohesive vision of what TAchr should become. Writing down requirements allows the design team to reference this document whenever they are unsure about the use cases or implementation of certain aspects of TAchr. It also leaves a paper trail for the design team so they can be sure that they are remembering and implementing correctly according to the client's specifications. 

## 1.2 Product Scope

In this document, we describe the Student/Faculty Member interface TAchr. TAchr is a website designed to streamline the process by which Faculty recruit Teacher's Assitants (TA's) for their classes. Both TA's and Faculty Members will be able to create accounts for TAchrs, and TA's will be able to apply to available positions created by a Faculty Member. The TA's account will have releveant academic information on it, that a Teacher will be able to check upon receiving an application. A Faculty Member can then assign as many TA's as they request to their class based on the applications they recieve.  

## 1.3 Document Overview

The first section of this document lays out why this document exists and the product we hope to describe in the later sections. The second section of this document contains the description of the project in meticulous detail. In section 2, this document describes the requirements that TAchr sets out to fufil, a description of how all clients will interact with the product, a description of use cases, and the non-functional of the project requirements. The third section of this document will have sketches for our idea of what the product U.I. will look like. The fourth section has a link to the project's github, and the fifth section contains our references.  

----
# 2. Requirements Specification

This section specifies the software product's requirements. Specify all of the software requirements to a level of detail sufficient to enable designers to design a software system to satisfy those requirements, and to enable testers to test that the software system satisfies those requirements.

## 2.1 Customer, Users, and Stakeholders

A brief description of the customer, stakeholders, and users of your software.
Users:
- Student/TA: User who is looking for a TA position. Will be able to apply to TA positions created by faculty members.
- Faculty User: User who is looking for TAs to fill a position. Will be able to create positions for students to fill.


----
## 2.2 Use Cases

This section will include the specification for your project in the form of use cases. The section should start with a short description of the actors involved (e.g., regular user, administrator, etc.) and then follow with a list of the use cases.

For each use case you should have the following:

* Name,
* Actors,
* Triggers (what initiates the use case),
* Preconditions (in what system state is this use case applicable),
* Actions (what actions will the code take to implement the use case),
* Alternative paths
* Postconditions (what is the system state after the use case is done),
* Acceptance tests (list one or more acceptance tests with concrete values for the parameters, and concrete assertions that you will make to verify the postconditions).

Each use case should also have a field called "Iteration" where you specify in which iteration you plan to implement this feature.

You may use the following table template for your use cases. Copy-paste this table for each use case you will include in your document.


| Use case # 1      |   |
| ------------------|--|
| Name              | Create an account  |
| Users             | All Users   |
| Rationale         | When a student wants to make an account. The create student account function will prompt the student user for username, password, name, last name, WSU ID, email, phone, and other additional information they would like to provide. If the student has already created an account with the same username or email then prompt them to sign in.   |
| Triggers          | User selects the "Create Account" option.  |
| Preconditions     | The user is currently enrolled in the school.  |
| Actions           | 1. The student indicates that the software is to perform a “Create account” in the database. </br> 2. The software responds by requesting the student's info </br> 3. The student inputs contact information, and additional information. </br> 4. The software creates the users account with the data provided.    |
| Alternative paths | 1. In Step 1, the user indictaes that they are a student creating an account. In this case, a user chooses they may want to create a faculty user account, which loads a form based on information for a faculty user which includes only username, password, name, last name, WSU ID, email, and phone. The postconditon state is identical, except the faculty user account is created using different information. </br> 2. The user may decide to abort the "Create Account" operation at any time during steps 1, 2, 3. In this case, the software returns to the precondition state.   |
| Postconditions    | The user's account is created with all the inputted information.    |
| Acceptance tests  | Make sure the user has created the correctly titled account (Student or Faculty) and all information inputted is displayed.    |
| Iteration         | #1  |

| Use case # 2      |   |
| ------------------|--|
| Name              | User Login   |
| Users             | All Users   |
| Rationale         | In order to access the site, the Login function allows the user to access their account by entering their username and password. If the user enters the wrong password for an account, than the system indicates that they must enter correct information.   |
| Triggers          | The user selects the "Login" function.   |
| Preconditions     | The user already has an account in the system. The user is not already logged In.    |
| Actions           | 1. The user indicates that the software is to preform a Login</br> 2. The Software responds by requesting username and password of the user. </br> 3. The User inputs the username and password. </br>4. The software returns to main page with the user logged into the system. </br>|
| Alternative paths | 1. In step 3, the user enters in their username and password. In this case, if the user enters the wrong password for a given username, the function will display an error for an incorrect password, the postconditon state will then revert back to step 1. </br> 2. In the 3, the user enters their username and password. If the username is not in the system the function will display a flash message that no account under that username exists. The postconditon state will again revert back to step 1.</br> 3. The user may decide to abort the login operation at any times during steps 1,2, or 3. In this case, the software returns to the precondtion state.  |
| Postconditions    | If user enters in correct login infomation, they will be logged into the system.   |
| Acceptance tests  | Make sure user is logged into account with username and password provided.  |
| Iteration         | #1  |


| Use case # 3      |   |
| ------------------ |--|
| Name              | User Logout   |
| Users             | All users   |
| Rationale         | While a user has logged into an account in the system. The user may find they would like to logout of current account, the Logout function allows user to signout of current account.  |
| Triggers          | The user selects the "Logout" option  |
| Preconditions     | A user is already signed into an account.  |
| Actions           | 1. The user indicates that the software is to preform a logout in the system.</br> 2. The software responds by logging the current user out of the system  |
| Alternative paths | 1. The user may decide to abort the logout function in step 1 before the request to the system is submitted. In this case the software returns to the precondition state   |
| Postconditions    | A current user is logged out of an account   |
| Acceptance tests  | Past user was logged out of their account  |
| Iteration         | 1  |

| Use case # 4      |   |
| ------------------|--|
| Name              | View open TA positions and all TA position info  |
| Users             | Students   |
| Rationale         | After open TA positions are made, users will find positions that are available. The ViewTAPositions function displays all open TA position and identifies the TA positions that match the current student’s qualifications and list them separately under the “Recommended TA Positions”. Info displayed for each TA position involves various sections such as course title, semester, Instructor and contact information, and qualifications.
| Triggers          | User selects the "View TA position page"  |
| Preconditions     | A student is logged in |
| Actions           | 1. The software sees if the user is on the TA position display page and requests access to the TA info database to display the positions. </br> 2. The software also accesses the user's information like grades & GPA and uses that information to display reccomended TA position.|
| Alternative paths | 1. In step 1, the user applys for a TA position and once they do, the user is taken back to the TA position view page. </br> 2. If the user decides to abort the function in steps 1 or 2 before the request is submitted, returning to the precondition state.  |
| Postconditions    | All Available positions are available to be viewed |
| Acceptance tests  | Make sure that all Positions that are made and are open are available for the student to view.  |
| Iteration         | #2  |

| Use case # 5      |   |
| ------------------|--|
| Name              | Apply for TA positions.   |
| Users             | All Students  |
| Rationale         | While on TAchr a student browsing the website would see a TAship posted by a faculty member that they would want to apply for. The student would then be able to click on the listing and apply for the class. The student would then enter the grade they got in the class, when they took the course, and when they are applying for the TAship. After submitting relevant information, the student would click the apply button and they would be sent back to the main page.  |
| Triggers          | A student clicks on the "apply" option on a faculty posted classroom |
| Preconditions     | A student is logged in  |
| Actions           | 1. A student selects a class listing posted by a faculty member </br>2. A student enters what their GPA was in said class, when they took the class, and when they are applying for the TAship </br>3. A student submits the application</br>5. The website adds the application to the student's pending applications |
| Alternative paths | 1. In step 2 or step 3, the student might choose that they no longer want to submit this application. The student can delete all record of their applciation simply by returning to the precondition state. |
| Postconditions    | A student has applied to a class. A student's pending applications have been updated, and a classes pending application has been updated. If the student chose to delete their application, the postcondition state is identical to the precondition state  |
| Acceptance tests  | The student has a pending application and the TAship the student applied for has the relevant student entered in its potential TA list |
| Iteration         | #2  |

| Use case # 6      |   |
| ------------------ |--|
| Name              | View the TA positions they already applied to and check the statuses of their applications. |
| Users             | Students  |
| Rationale         | A student might want to view the applications that they have sent out to see if any of them have been accepted or rejeceted. The view pending application feature allows students to view all the TAships they have applied for and see if they have been accepted, or if their application is still pending.    |
| Triggers          | A student selects the view applications option  |
| Preconditions     | A student is logged in  |
| Actions           | 1. A student selects applications tab. </br>2. The student is redirected to a page displaying all their pending applications </br>3. Applications are displayed as either Assigned or Pending   |
| Alternative paths | 1. On step 1, if the student has no applications, text will be displayed saying as "No applications submitted"  |
| Postconditions    | The student's current page has been changed to the applications page  |
| Acceptance tests  | The URL of the website changes to application page  |
| Iteration         | #3 |


| Use case # 7 |   |
| ------------------|--|
| Name              | Withdraw from Application  |
| Users             | Students  |
| Rationale         | At some point after creating an application for a TA position, a student may decide they need to withdraw their application so they are no longer considered for the position. The withdraw function will remove their name from consideration for the given position. Sometimes the user might want to be removed from all their currently applied positions, and should have an option to do this.  |
| Triggers          | The user selects the "Withdraw from Application" option |
| Preconditions     | The user is logged in as a student, has a pending application, and is looking at a current application. |
| Actions           | 1. The user indicates they would like to withdraw their application from a position </br> 2. The site responds by removing the application|
| Alternative paths | 1. In step 1, the user may indicate that they would like to be removed from all currently pending position applications. If this option is selected, all applications will be removed |
| Postconditions    | The selected application(s) will be removed.   |
| Acceptance tests  | Make sure that the application is properly withdrawn, and can not be viewed by either the user, or a faculty member.  |
| Iteration         | #3  |

| Use case # 8      |   |
| ------------------|---|
| Name              | Create TA Position |
| Users             | Faculty User |
| Rationale         | When logged in, many students will want to see if there are new TA positions available on the front page to apply for. The createTAposition function will allow the faculty to create the course for the TAship, enter the number of TAs needed for the course, Enter the qualifications for the course (min GPA, min grade earned for the course, prior TA experience, etc.), and choose the semester for the TAship.
| Triggers          | User Selects create TA position button  |
| Preconditions     | A page is loaded and to be filled out |
| Actions           | 1. User indicates that the website is to take the user to the TA position creation page.</br>2. The software responds by requesting the TA creation page to be displayed. </br>3. The User inputs the text for all of the required fields to create the open position and then creates the position by clicking on a link to create it. </br>4. The software responds by creating the open position on the TA open position page. |
| Alternative paths | 1. In step 4, the user creates the position to be displayed on the TA position display page for open positions. In this case, the user chooses if they want to create another case, which displays a link that takes them back to the create TA position page.   |
| Postconditions    | The position will be displayed on the main viewing page.  |
| Acceptance tests  | Make sure that the position is displayed properly on the page, and that all necessary information is present.  |
| Iteration         | #3  |


| Use case # 9      |   |
| ------------------|--|
| Name              | View Position/Accept Student as TA  |
| Users             | Faculty User |
| Rationale         | When a faculty user is ready, they will want to view all the students who have applied to one of their positions, including their qualifications. They may then select a student from the list of those who applied, and will add them as a TA to the course. Once the required number of TAs for the course have been selected, no more TAs can be added.  |
| Triggers          | The user selects the "View Position" option.  |
| Preconditions     | The user is logged in as a faculty user, has created a postion, and is viewing said position. |
| Actions           | 1. The user indicates they would like to view a position they made. </br> 2. The website responds by showing all the students who have applied to the position, as well as information about their qualifications such as GPA, grade earned in class, and previous courses they TAd for.  |
| Alternative paths | 1. After step 2, and if the position still needs more TAs, the user may indicate that they would like to accept a student as a TA. If the student is not already accepted as a TA, they will be added as a TA to this positon.  |
| Postconditions    | The students are displayed, and the student is added as a TA if the option is indicated.  |
| Acceptance tests  | All the students with applications to the position are displayed, alongside the qualifications they provided. The option to add a student should only be available if the position still requires TAs, and the student is not already accepted as a TA.  |
| Iteration         | #2: Displaying the students who applied </br> #3: all other functionality.   |

**Include a swim-lane diagram that illustrates the message flow and activities for following scenario:**
![](https://i.imgur.com/sYAPp9m.jpg)

----
## 2.3 Non-Functional Requirements

List the non-functional requirements in this section.

You may use the following template for non-functional requirements.

1. Security:  
     * System requires users to create an account to access all of the data on the website for a given student or faculty member. 
     * The system shall not disclose any personal student infomation to other students.
     * The system shall not disclose any personal Faculty user information to the other faculty members.
2. Performance: 
    * The websites response time should be under 3 seconds.

3. Usability:
    * The website's interface has to be user-friendly and not complex to use. 

4. Platform:
    * The system should be compatible with all major browsers: Chrome, Firefox, IE/Edge, Safari, etc. 
    * Designed for use on desktop devices
5. Process: 
    * Our deliverable documents shall conform to the agile process

6. Reliability: 
    * Users are able to access their account all of the time excluding errors & maintinence periods. 

7. Scalability: 
    * System can handle up to all of the given schools faculty and students.
 
8. Throughput:
    * Up to all of the schools faculty and students can access the system at any given time. 

9. Robustness: 
    * System shall not allow invalid user responses in forms. 

10. Availability: 
    * All users can create accounts, aswell as access all other features of the website throughout the week at any time during the day. In a case of unplanned system downtime, all features will be avaliable again after 1 business day. 

11. Recovery from failure: 
    * If a major error in the system has occured on the website, we must take measures to become fully operational within 1 business day of the error.  

12. Maintainability:
    * If the users database has become unavailable, the system will be under maintenance for 12 or fewer hours. 

13. Reusability: 
    * Build the system in a modular manner, with common components such as login and logout in different user types which have logic that can be used in multiple user account types.


----
# 3. User Interface

Login page for all users
![](https://i.imgur.com/MPUFDmi.jpg)

Student view of positions they can apply for
![](https://i.imgur.com/13Ien6K.jpg)

Student application page for a position
![](https://i.imgur.com/Yd9dFLp.jpg)

Faculty view of created applications
![](https://i.imgur.com/vFE8Qqk.jpg)

Faculty view of applications for one of their positions
![](https://i.imgur.com/g4J82qz.jpg)

Teacher view for adding position
![](https://i.imgur.com/9mGT497.jpg)


----
# 4. Product Backlog

https://github.com/WSU-CptS322-Fall2022/termproject-chasingwaterfalls/issues

----
# 5. References

Cite your references here.

For the papers you cite give the authors, the title of the article, the journal name, journal volume number, date of publication and inclusive page numbers. Giving only the URL for the journal is not appropriate.

For the websites, give the title, author (if applicable) and the website URL.

----
----
# Appendix: Grading Rubric
(Please remove this part in your final submission)

These is the grading rubric that we will use to evaluate your document. 

| Max Points  | **Content** |
| ----------- | ------- |
| 10          | Do the requirements clearly state the customers’ needs? |
| 5           | Do the requirements avoid specifying a design (note: customer-specified design elements are allowed; non-functional requirements may specify some major design requirements)? |
| | |  
|    | **Completeness** |
| 25 | Are use cases written in sufficient detail to allow for design and planning? |
| 4 | Do use cases have acceptance tests? | 
| 20 | Is your use case model complete? Are all major use cases included in the document? |
| 8 | Has the team provided an appropriate swim-lane diagram for the scenario where faculty reviews a student’s application? |
| 10 |  Are the User Interface Requirements given with some detail? Are there some sketches, mockups?  |
| | |  
|   | **Clarity** |
| 4 | Is the document carefully written, without typos and grammatical errors? |
| 2 | Is each part of the document in agreement with all other parts? |
| 2 | Are all items clear and not ambiguous? (Minor document readability issues should be handled off-line, not in the review, e.g. spelling, grammar, and organization). |
|   |   |
|    | **GitHub Issues** |
| 10 | Has the team setup their GitHub Issues page? Have they  generated the list of user stories, use-cases, created milestones, assigned use-cases (issues) to milestones?   Example GitHub repo (check the issues): https://github.com/WSU-CptS322-Fall2022/TermProjectSampleRepo/issues  |

