from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logoutUser', views.logoutUser, name='logoutUser'),
    path('signup', views.signup, name='signup'),
    path('teacher_logged_in', views.teacher_logged_in, name='teacher_dashboard'),
    path('student_logged_in', views.student_logged_in, name='student_dashboard'),
    path('admin_logged_in', views.admin_logged_in, name='admin_dashboard'),
]
