from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gpa = models.DecimalField(max_digits = 3, decimal_places = 2, default = 2.0)
    majorOne = models.CharField(max_length = 8, default = "None")
    majorTwo = models.CharField(max_length = 8, default = "None")
    minor = models.CharField(max_length = 8, default = "None")
    year_in_school = models.CharField(max_length=20, default = "Freshman")

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
    officeLocation =  models.CharField(max_length = 50, default = "251 mercer street")
    specialty = models.CharField(max_length = 20, default = "None")


class Appointment(models.Model):
    student = models.ForeignKey(Student, null=True)
    advisor = models.ForeignKey(Advisor, null=True)
    date = models.DateTimeField()
    time = models.DateTimeField()
    description = models.CharField(max_length = 300, default = "Enter description")
    










