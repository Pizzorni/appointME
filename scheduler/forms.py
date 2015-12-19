from django import forms
from django.forms import ModelForm
from models import Student
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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
