from django.db import models

# Create your models here.

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def get_or_create_user(username, password):
    user, created = User.objects.get_or_create(username=username)
    if created:
        user.set_password(password)
        user.save()
    return created


class CourseDetail(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    course_id = models.CharField(max_length=30)
    credit = models.FloatField()
    category = models.CharField(max_length=40)
    college = models.CharField(max_length=40)
    prerequisite = models.TextField()
    description = models.TextField()
    outline = models.TextField()


class CourseLesson(models.Model):

    def __str__(self):
        return self.code

    code = models.CharField(max_length=20)
    teacher = models.CharField(max_length=30)
    choose_id = models.CharField(max_length=60)
    num = models.CharField(max_length=20)
    term = models.CharField(max_length=20)
    classroom = models.CharField(max_length=70)
    hold_all = models.IntegerField()
    hold_me = models.IntegerField()
    object = models.CharField(max_length=60)
    mode = models.CharField(max_length=50)
    book = models.CharField(max_length=110)
    arrange = models.CharField(max_length=40)



    startday = models.IntegerField()               #3
    startcourse = models.IntegerField()            #1
    firstcourse = models.CharField(max_length=20)  #3,1,2  means fri, the first and second
    secondcourse = models.CharField(max_length=20)

    season = models.CharField(max_length=10,default='')
    #name = models.CharField(max_length=50)
    #credit = models.FloatField()
