from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

NUM_LOGICAL_SHARDS = 16
NUM_PHYSICAL_SHARDS = 2

LOGICAL_TO_PHYSICAL = (
  'db1', 'db2', 'db1', 'db2', 'db1', 'db2', 'db1', 'db2',
  'db1', 'db2', 'db1', 'db2', 'db1', 'db2', 'db1', 'db2',
)
# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gpa = models.DecimalField(max_digits = 3, decimal_places = 2, default = 2.0)
    majorOne = models.CharField(max_length = 8, default = "None")
    majorTwo = models.CharField(max_length = 8, default = "None")
    minor = models.CharField(max_length = 8, default = "None")
    year_in_school = models.CharField(max_length=20, default = "Freshman")
    
class Advisor(models.Model):
    user = models.CharField(max_length = 50,default = "Jane Smith")
    officeLocation =  models.CharField(max_length = 50, default = "251 mercer street")
    specialty = models.CharField(max_length = 20, default = "None")


class Appointment(models.Model):
    student = models.ForeignKey(Student, null=True)
    advisor = models.ForeignKey(Advisor, null=True)
    #date = models.DateTimeField()
    #time = models.DateTimeField()
    timeslot = models.DateTimeField()
    description = models.CharField(max_length = 300, default = "Enter description")






