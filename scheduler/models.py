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
    NONE = 'NONE'
    MAJOR_CHOICES = (
        (MATH, 'Mathematics'),
        (COMPSCI, 'Computer Science'),
        (ECONOMICS, 'Economics'),
        (ENGLISH, 'English'),
        (NONE, 'None'),
    )


    majorOne = models.CharField(max_length = 4, choices = MAJOR_CHOICES, default = ENGLISH)
    majorTwo = models.CharField(max_length = 4, choices = MAJOR_CHOICES, default = NONE)
    minor = models.CharField(max_length = 4, choices = MAJOR_CHOICES, default = NONE)

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
    year_in_school = models.CharField(max_length=2, choices = YEAR_IN_SCHOOL_CHOICES, default = FRESHMAN)

    def getName(self):
        return self.user.get_full_name()
    def getGPA(self):
        return self.gpa
    def getYear(self):
        return self.year_in_school
    def getMajorOne(self):
        return self.majorOne
    def getMajorTwo(self):
        return self.majorTwo
    def getMajors(self):
        majors = []
        majors.append(self.majorOne)
        majors.append(self.majorTwo)
        return majors
    def getMinor(self):
        return self.minor
    def printName(self):
        return "Name:", self.user.get_full_name()
    def printGPA(self):
        return "GPA:", self.gpa
    def printMajors(self):
        return "First Major:" , self.majorOne, "Second Major:", self.majorTwo
    def printMinors(self):
        return "Minor:", self.minor
    def printYear(self):
        return "Academic Year:", self.year_in_school
    def printStudentInfo(self):
        name = printName()
        gpa = printGPA()
        majors = printMajors()
        minor = printMinors()
        year = printYear()
        return name + "\n" + gpa + "\n" + majors + "\n" + minors + "\n" + year 


class Advisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    officeLocation =  models.CharField(max_length = 20)


#class Posting(models.Model):












