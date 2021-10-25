

# OAMP



Online Assignment Management Portal



 ONLINE ASSIGNMENT MANAGEMENT PORTAL(OAMP)



1. Introduction

The purpose of this document is to describe the behavior of the Online Portal. Requirements Specification defines and describes the operations, interfaces, performance, and quality assurance requirements of the Online Portal. The document also describes the non-functional requirements such as the user interfaces. It also describes the design constraints that are to be considered when the system is to be designed, and other factors necessary to provide a complete and comprehensive description of the requirements for the software. The existing system is a manual system or a semi-automated system. Manual system involves paper work in the form of maintaining various Assignment files submitted by students. Maintaining critical information in the files and manuals is full of risk and a tedious process. It’s a limited system and less user friendly. Searching for particular assignments is critical and time consuming. The Online Portal is one that aims to give the Students, Teachers and Administrator an experience equal to or better than the sort they would find in a traditional System. The advantages of using this software will be vivid as we go further in the document.



1.1.Document Purpose

The main objective of this document is to illustrate the requirements of the project Online Portal. The purpose of developing this system is to provide a virtual platform for Students and Teachers to interact between each other through different modules, regarding the issuance and submission of different assignments, maintaining a database of the results recorded, keeping the students up-to-date with deadlines and results, etc. 



1.2.Product Scope

The product is designed for Educational Institutions. It will be a helpful product in a very effective way as it will provide a virtual platform. This system allows the students to maintain their Assignments.



The Online Portal is supposed to have the following features:

The Online Portal is up and running all day.

The system provides a log-in facility to the students and teachers.

The system provides the Students with the option to check their account,and/or change their options like password, check assignment deadlines whenever needed all throughout the day but the submission is dependent on the information provided by the teachers.

The system allows the Administrator to do CRUD operations on Student and Teacher accounts.



1.3.Overview

In the existing system, people have to go to Teachers to submit assignments which consume a lot of time while in this system students can submit assignments online from the comfort of their home which will save their valuable time.

Few functionalities of the software and different rights given to Administrator, Teachers and Students are given below:



Administrator:

1. The system allows the Administrator to create/delete/edit the new entries of student and teachers and maintain the Results catalog.

2. Can view different Assignments in courses and results recorded.

3. The Administrator is provided with interfaces to add/delete students and teachers when they join or leave the institutes.

4. Administrators can also edit the information about them.

5. Administrators approve accounts of Students and Teachers if they self-register themselves on the portal.



  Students:

1. EDUCATIONAL LEVEL: At least user of the system should be comfortable with English language

2. The students can view the different assignments.

3. The students should be notified with the updated information about the assignment.

4. Provisions for the students to submit the assignment, if all the other required parameters hold good.

5. The students are given a provision to check his account information and change the account information any time in the given valid period.

6. The students are provided with the yet-to-submit assignments list.

7. Students can self-register themselves but they will be called a legit registration once approved by the Administrator.



Teachers:

1. The Teacher can edit/add/change the information about different assignments and courses they belong to.

2. The Teacher should also update the information about the real time changing needs of the assignment.

3. Teachers can self-register themselves but they will be called a legit registration once approved by the Administrator.



  **Assignment should be textual(for now).

  **Answer script should also be textual(for now).



1.4.Environmental Characteristics

1.4.1. Operating Environment (Software)

This system will be operated on any computer with the following minimum system

specifications: -

 Operating System: Windows, Linux or MacOS

 Authentication model: TBD, RBAC

 Frontend Framework/Technology: Django View

 Backend/API framework: Django REST framework

 Dependency Libraries: Pillow

 Will it be microservice based Architecture? No

 Database: sqLite3

 Language: Python

 Multimedia content management: Account Profile photo





2. Functional Requirements

 1.Signup

Description: Student/Teacher details are entered into this module, the details are then verified by the Administrator. If the details are found to be valid then their account is approved by the Admin. This Registration ID is a unique ID which is given to each user as per which their daily transactions are recorded against it.

Input: User information

F-name

L-name

Email

Access Level (teacher or student)

    If Teacher:

        i.   Contact

        ii.  Teacher_id

        iii. Tell us about yourself

            If Student:

        i.   Contact

        ii.  Batch you are in

        iii. Roll Number

        iv. Tell us about yourself

Output: Account setup

 2.Login

Description: The Teacher_id/Roll_Number and password are required to do the login process.

Input: Teacher_ID/Roll_Number, Login Request

i. Email

ii. Password

Also there will be a separate login page for admin for security reasons.

Output: Logged In as the students/Teacher/Administrator

 3.Admin Homepage

Description: The information that is shown when an Admin logs into his/her account.

Input: Request for browsing the Student/Teacher/assignment/course details and can also do the CRUD operation.

Output: HTTPResponse(Shows the required detail..)

Primary panel

Course details

Student details

Teacher details

Result

Assign courses to teachers and students

    Secondary panel

        Approval requests



 4. Teacher Homepage

Description: It shows Course list and when clicked on Courses, the section expands to show the Assignment list where he/she can do CRUD operations on the Assignments

Input: request 

Output: HTTPResponse

Courses

Result

Teacher list(Read only)

Student List(Read only)

 5. Results

Description: Viewable by everyone but editable by Teacher or Admin

Input: request by an authorised account

Output: HTTPResponse

 6. Student Homepage

Description: It shows the information of different courses that the students is enrolled into and when clicked on a particular course, respective assignments are shown. If not submitted the assignment, the assignment section will be in red color but upon completion, the section will be in green colour. Newest first will be the display order in this part.

Input: Request for showing the assignment Items information

Output: HTTPResponse

Courses

Assignments

Result

 7.Profile page

Description: Displays the profile of a registered account.

Input: Request for view/add/delete/change of the required information in database and the requested id against which you want to see the information.

Output: HTTPResponse

Displays the necessary page if requested by an authorised account.

3. Non-Functional Requirements:

1. Performance Requirements

The system should be available at all times, meaning the user can access it using a web browser. Backups of the database should be retrieved from the server and saved by the administrator. 

2. Software Quality Attributes

System can be maintained easily.

The availability of the software is easy and for everyone.

The results of the function are pure and accurate.

The operation may be flexible and reports can be presented in many ways.

The performance of the software is better which will increase the reliability of the software.

3. Security:

The system must automatically log out all users after a period of inactivity.The system should 2not leave any cookies on the user’s computer containing the user’s password.



4. Availability:

This software will be free and available.

5. Maintainability

This software is easy to maintain with a constant maintaining cost for a longer period of time.

6. DataBase

A default database sqLite3 is used for its development which provides a tremendous amount of functionalities.



3.1 Other non-Functional Requirements:

3.1.1 User Interface :

Various interfaces for the product could be-

Login Page

Signup Form

There will be a view displaying information about the Assignment..

If the students select the results button then another view for Results recorded will be opened.

3.1.2 Software Interface

Any window-based operating system with DOS support are primary requirements for software development.

The systems must be connected to the internet.

3.1.3 Hardware Interfaces

The System must run over the internet, all the hardware shall require internet access. e.g. Modem, WAN – LAN, Ethernet Cross-Cable.



4. Entity Relationship Diagram



E-R Diagram for Online Portal

**Because of constraints of only 60 shapes per diagram on the free account in creately, fewer attributes have been mentioned for Student and Teacher entity, also there are some missing connecting lines for entity and attributes for Results, Assignment and Admin Entities. Admin CRUDS on Student and Teacher account and can view/edit all the other information.

5. Model:

Student:(Viewable by everyone)

Student_id

Approval Requests

F_name

L_name

Email

Contact

About (nullable)

Verified (nullable and boolean)

Hashed Password



    2. Teacher:(Viewable by Teachers and Admins)

teacher_id

F_name

L_name

Email

Contact

About (nullable)

Verified (nullable and boolean)

Hashed Password



    3. Admin:(Only admins)

Admin_id

F-name

L-name

Email

Contact



    4. Courses

Course_id

Course name

    5. Enrols

Student_Id

Course_Id

    6. Instructs

Course_Id

Teacher_Id

    7. Assignment

Assignment_Id

Assignment_Name

Course_Id

Deadline

    8. Results

Submission_Id

Student_Id

Assignment_Id

Course_Id

Evaluation






​
