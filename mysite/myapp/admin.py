from django.contrib import admin
from .models import Admin, Student, Teacher, Course, Enrol, Instruct, Assignment, Result, UserProfile
# Register your models here.

admin.site.register(Admin)
admin.site.register(UserProfile)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Enrol)
admin.site.register(Instruct)
admin.site.register(Assignment)
admin.site.register(Result)
