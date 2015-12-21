from django import forms
from django.forms import ModelForm
from models import Student, Appointment, Advisor
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


Days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')

class AppointmentForm(forms.Form):
	#days = forms.ChoiceField(choices=Days)
	date = forms.DateField(label="date", input_formats = ['%m/%d/%Y'])
	times = (
		('9:00', '9:00 AM'),
		('9:30', '9:30 AM'),
		('10:00', '10:00 AM'),
		('10:30', '10:30 AM'),
		('11:00', '11:00 AM'),
		('11:30', '11:30 AM'),
		('12:00', '12:00 PM'),
		('12:30', '12:30 PM'),
		('13:00', '1:00 PM'),
		('13:30', '1:30 PM'),
		('14:00', '2:00 PM'),
		('14:30', '2:30 PM'),
		('15:00', '3:00 PM'),
		('15:30', '3:30 PM'),
		('16:00', '4:00 PM'),
		('16:30', '4:30 PM'),
	)
	time = forms.ChoiceField(label="time", choices =  times)
	class Meta:
		fields = ('date', 'time',)
		

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	gpa = forms.DecimalField(max_digits = 3, decimal_places = 2, max_value = 4, min_value = 0)
	fullname = forms.CharField(max_length = 30)
	majorOne = forms.CharField(max_length = 8)
	majorTwo = forms.CharField(max_length = 8)
	minor = forms.CharField(max_length = 8)
	year_in_school = forms.CharField(max_length=20)
	
	class Meta:
		model = User
		fields = ('username', 'fullname', 'email', 'gpa', 'majorOne', 'majorTwo', 'minor', 'year_in_school', 'password1', 'password2')
		
	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.fullname = self.cleaned_data['fullname']
		user.email = self.cleaned_data['email']
		user.gpa = self.cleaned_data['gpa']
		user.majorOne = self.cleaned_data['majorOne']
		user.majorTwo = self.cleaned_data['majorTwo']
		user.minor = self.cleaned_data['minor']
		user.year_in_school = self.cleaned_data['year_in_school']
		
		if commit:
			user.save()
			
		return user

class RegisterForm1(UserCreationForm):
	email = forms.EmailField(required=True)
	
	class Meta:
		model = User
		fields = ('username','email', 'password1', 'password2')
	
	def save(self, commit=True):
		user = super(RegisterForm1, self).save(commit=False)
		user.email = self.cleaned_data['email']
		
		if commit:
			user.save()
			
		return user

class RegisterForm2(forms.ModelForm):
	class Meta:
		model = Student
		fields = ('gpa', 'majorOne', 'majorTwo', 'minor', 'year_in_school')

class RegisterForm3(forms.ModelForm):
	class Meta:
		model = Advisor
		fields = ('officeLocation', 'specialty')
		
