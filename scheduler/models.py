from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gpa = models.DecimalField(max_digits = 3, decimal_places = 2, default = 2.0)
    majorOne = models.CharField(max_length = 8, default = "None")
    majorTwo = models.CharField(max_length = 8, default = "None")
    minor = models.CharField(max_length = 8, default = "None")
    year_in_school = models.CharField(max_length=20, default = "Freshman")
    
class Advisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    officeLocation =  models.CharField(max_length = 50, default = "251 mercer street")
    specialty = models.CharField(max_length = 20, default = "None")


class Appointment(models.Model):
    student = models.ForeignKey(Student)
    advisor = models.ForeignKey(Advisor)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        help_texts = {
            'username' : '',
        }












