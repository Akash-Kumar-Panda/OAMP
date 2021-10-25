from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.db import IntegrityError
from .models import Admin, Student, Teacher, Course, Enrol, Instruct, Assignment, Result, UserProfile
from django.contrib.auth import login as log_in, authenticate, logout as log_out
from django.contrib.auth.models import User, Group
from django.contrib import messages

# Create your views here.


def index(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            messages.info(request, 'Yu are already signed in')
            u = UserProfile.objects.get(user=request.user)
            return redirect(u.Tag + '_dashboard')
        return render(request, 'myapp/index.html')
    else:
        user_id = request.POST.get('user_id')
        passwd = request.POST.get('password')
        radio = request.POST.get('User')
        # print(user_id, radio, passwd)

        user = authenticate(request, username=user_id, password=passwd)
        if user is not None:
            usr = User.objects.get(username=user_id)
            tag = UserProfile.objects.get(user=usr).Tag
            print('tag=', tag)
            print('radio=', radio)
            if(tag == radio):
                log_in(request, user)
                # return render(request, 'myapp/'+radio+'_logged_in.html')
                return redirect(tag+'_dashboard')
            else:
                msg = 'Incorrect radio button choice'
                return render(request, 'myapp/index.html', {'error': msg})
        else:
            msg = 'CREDENTIALS DO NOT MATCH. Try Again'
            return render(request, 'myapp/index.html', {'error': msg})


def signup(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('index')

        return render(request, 'myapp/signup.html')
    else:
        user_id = request.POST.get('user_id')
        passwd = request.POST.get('password')
        radio = request.POST.get('User')
        repasswd = request.POST.get('repassword')
        email = request.POST.get('email')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        contact = request.POST.get('contact')
        about = request.POST.get('about')

        # print(radio)
        if passwd != repasswd:
            return HttpResponse('Passwords do not match')
        else:
            try:
                if(radio == 'Admin'):
                    new = User.objects.create_user(
                        username=user_id, password=passwd)
                    new.save()
                    newUserProfile = UserProfile(user=new, Tag='admin')
                    newUserProfile.save()
                    new_admin = Admin(user_id=newUserProfile,
                                      fname=fname,
                                      lname=lname,
                                      email=email,
                                      contact=contact)
                    new_admin.save()

                    # new_group = Group.objects.get(name='Admins')
                    # new.groups.add(new_group)
                    #

                    return render(request, 'myapp/index.html', {'error': 'Successfully Signed up. Now log in to your account'})
                elif(radio == 'Teacher'):
                    new = User.objects.create_user(
                        user_id, password=passwd)
                    new.save()
                    newUserProfile = UserProfile(user=new, Tag='teacher')
                    newUserProfile.save()
                    new_teacher = Teacher(user_id=newUserProfile,
                                          fname=fname,
                                          lname=lname,
                                          email=email,
                                          contact=contact,
                                          about=about)
                    new_teacher.save()
                    return render(request, 'myapp/index.html', {'error': 'Successfully Signed up. Now log in to your account'})
                elif(radio == 'Student'):
                    new = User.objects.create_user(
                        user_id, password=passwd)
                    new.save()
                    newUserProfile = UserProfile(user=new, Tag='student')
                    newUserProfile.save()
                    new_student = Student(user_id=newUserProfile,
                                          fname=fname,
                                          lname=lname,
                                          email=email,
                                          contact=contact,
                                          about=about)
                    new_student.save()
                    return render(request, 'myapp/index.html', {'error': 'Successfully Signed up. Now log in to your account'})
                else:
                    return render(request, 'myapp/signup.html', {'error': 'Please fill the form properly'})

            except IntegrityError:
                return HttpResponse('Integrity Error ')


def teacher_logged_in(request):
    return render(request, 'myapp/teacher_logged_in.html')


def student_logged_in(request):
    return render(request, 'myapp/student_logged_in.html')


def admin_logged_in(request):
    return render(request, 'myapp/admin_logged_in.html')


def logoutUser(request):
    log_out(request)
    messages.info(request, 'User was logged out!')
    return redirect('index')
