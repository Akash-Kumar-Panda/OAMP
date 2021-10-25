from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    choice = (
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )
    Tag = models.CharField(max_length=10, choices=choice)

    def __str__(self):
        return self.Tag


class Admin(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    # password = models.CharField(max_length=100)user
    fname = models.CharField(max_length=15, default='fname')
    lname = models.CharField(max_length=15, default='lname')
    email = models.EmailField(max_length=254, default='xyz@gmail.com')
    contact = models.CharField(max_length=13, default='1234567890')

    def __str__(self):
        return self.user_id


class Student(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    # password = models.CharField(max_length=100)
    choice = (
        ('yes', 'YES'),
        ('no', 'NO'),
    )
    fname = models.CharField(max_length=15, default='fname')
    lname = models.CharField(max_length=15, default='lname')
    email = models.EmailField(max_length=254, default='xyz@gmail.com')
    contact = models.CharField(max_length=13, default='1234567890')
    approved = models.CharField(
        max_length=3, choices=choice, default='no')  # Yes or No
    about = models.CharField(max_length=254, default='abcd')
    category = 'Student'

    def __str__(self):
        return self.fname


class Teacher(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    # password = models.CharField(max_length=100)
    choice = (
        ('yes', 'YES'),
        ('no', 'NO'),
    )
    fname = models.CharField(max_length=15, default='fname')
    lname = models.CharField(max_length=15, default='lname')
    email = models.EmailField(max_length=254, default='xyz@gmail.com')
    contact = models.CharField(max_length=13, default='1234567890')
    approved = models.CharField(
        max_length=3, choices=choice, default='no')  # Yes or No
    about = models.CharField(max_length=254, default='abcd')
    category = 'Teacher'

    def __str__(self):
        return self.fname


class Course(models.Model):
    course_id = models.CharField(max_length=10)
    name = models.CharField(max_length=50)

    def __str__(self):
        return (self.course_id + " - " + self.name)


class Enrol(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return (str(self.student_id) + " - " + str(self.course_id))


class Instruct(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return (str(self.course_id) + " - " + str(self.teacher_id))


class Assignment(models.Model):
    # id = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    deadline = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return (self.name + " - " + self.course_id + " - " + self.teacher_id)


class Result(models.Model):
    choice = (
        ('late', 'Late Submission'),
        ('onTime', 'Okay'),
    )
    name = models.CharField(max_length=10)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    assignment_id = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    text = models.TextField(max_length=5000, blank=True, null=True)
    subTime = models.CharField(
        max_length=20, choices=choice, blank=True, null=True)
    evaluation = models.IntegerField(blank=True)

    def __str__(self):
        return (self.name + " - " + self.student_id + " - " + self.assignment_id + " - " + self.course_id + " - " + self.evaluation)
