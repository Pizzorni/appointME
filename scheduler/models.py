from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gpa = models.DecimalField(max_digits = 3, decimal_places = 2)

    COMPSCI = 'CS'
    MATH = 'MATH'
    ECONOMICS = 'ECON'
    ENGLISH = 'ENGL'
    MAJOR_CHOICES = (
        (MATH, 'Mathematics'),
        (COMPSCI, 'Computer Science'),
        (ECONOMICS, 'Economics'),
        (ENGLISH, 'English'),
    )

    major = models.CharField(max_length = 4,
                            choices = MAJOR_CHOICES,
                            default = ENGLISH)
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    year_in_school = models.CharField(max_length=2,
                                    choices = YEAR_IN_SCHOOL_CHOICES,
                                    default = FRESHMAN)
    


#class Advisor(models.Model):

#class Posting(models.Model):
