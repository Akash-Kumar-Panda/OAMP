# Generated by Django 3.2.6 on 2021-08-30 10:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tag', models.CharField(choices=[('admin', 'Admin'), ('student', 'Student'), ('teacher', 'Teacher')], max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(default='fname', max_length=15)),
                ('lname', models.CharField(default='lname', max_length=15)),
                ('email', models.EmailField(default='xyz@gmail.com', max_length=254)),
                ('contact', models.CharField(default='1234567890', max_length=13)),
                ('approved', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='no', max_length=3)),
                ('about', models.CharField(default='abcd', max_length=254)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(default='fname', max_length=15)),
                ('lname', models.CharField(default='lname', max_length=15)),
                ('email', models.EmailField(default='xyz@gmail.com', max_length=254)),
                ('contact', models.CharField(default='1234567890', max_length=13)),
                ('approved', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='no', max_length=3)),
                ('about', models.CharField(default='abcd', max_length=254)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('evaluation', models.IntegerField()),
                ('assignment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.assignment')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.course')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.student')),
            ],
        ),
        migrations.CreateModel(
            name='Instruct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.course')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Enrol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.course')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.student')),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.course'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='teacher_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.teacher'),
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(default='fname', max_length=15)),
                ('lname', models.CharField(default='lname', max_length=15)),
                ('email', models.EmailField(default='xyz@gmail.com', max_length=254)),
                ('contact', models.CharField(default='1234567890', max_length=13)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.userprofile')),
            ],
        ),
    ]