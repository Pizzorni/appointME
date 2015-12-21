from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from models import Student, Appointment, Advisor
from datetime import datetime
from time import strptime, mktime

#Login - 
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.template.context_processors import csrf
from forms import RegistrationForm
from forms import RegisterForm1, RegisterForm2, RegisterForm3, AppointmentForm
from models import Student, Advisor

# Create your views here.

def index(request):
    #template = loader.get_template('index.html')
    #return HttpResponse(template.render())
	#return render(request,'index.html')
	if request.user.is_authenticated():
		if Student.objects.filter(user=request.user).exists():
			return HttpResponseRedirect('loggedIn')
		else:
			return HttpResponseRedirect('loggedInAdvisor')
	else:
		return render(request,'login.html')

	
def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)
	
def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	
	if user is not None:
		auth.login(request, user)
		request.session['member_id'] = username
		return HttpResponseRedirect('loggedIn')
	else:
		return HttpResponseRedirect('invalid')
		
def loggedIn(request):
	if request.user.is_authenticated():
		if Student.objects.filter(user=request.user).exists():
			student = Student.objects.get(user=request.user)
			#Do something with appointments
			appointment=Appointment.objects
			return render_to_response('loggedIn.html', {'full_name':request.user.username,'email': request.user.email, 'gpa':student.gpa, 'majorOne':student.majorOne, 'majorTwo':student.majorTwo, 'minor':student.minor, 'year_in_school':student.year_in_school,})
		else:
			advisor = Advisor.objects.get(user=request.user)
			context = {
				'full_name': request.user.username,
				'email': request.user.email,
				'location': advisor.officeLocation,
				'spec': advisor.specialty,
			}
			return render_to_response('loggedInAdvisor.html', context)
	else:
		return render_to_response('login.html')
		
def loggedInAdvisor(request):
	advisor = Advisor.objects.get(user=request.user)
	context = {
		'full_name': request.user.username,
		'email': request.user.email,
		'location': advisor.officeLocation,
		'spec': advisor.specialty,
	}
	return render_to_response('loggedInAdvisor.html', context)
		
def invalid(request):
	return render_to_response('invalid.html')
	
def logout(request):
	if request.user.is_authenticated():
		auth.logout(request)
		return render_to_response('logout.html')
	else:
		return render_to_response('login.html')
	
def register(request):
	if request.method == 'POST':
		form = RegisterForm1(request.POST, prefix='new_user')
		form2 = RegisterForm2(request.POST, prefix='userprofile')
		if form.is_valid():
			new_user = form.save()
			userprofile = form2.save(commit=False)
			userprofile.user = new_user
			userprofile.save()
			return render_to_response('registered.html')
	else:
		form = RegisterForm1(prefix='new_user')
		form2 = RegisterForm2(prefix='userprofile')
	return render(request, 'register.html', { 'userform':form, 'userprofileform':form2})

def regAdvisor(request):
	if request.method == 'POST':
		form = RegisterForm1(request.POST, prefix='new_user')
		form2 = RegisterForm3(request.POST, prefix='userprofile')
		if form.is_valid() * form2.is_valid():
			new_user = form.save()
			userprofile = form2.save(commit=False)
			userprofile.user = new_user
			userprofile.save()
			return render_to_response('registered.html')
	else:
		form = RegisterForm1(prefix='new_user')
		form2 = RegisterForm3(prefix='userprofile')
	return render(request, 'regAdvisor.html', {'userform': form, 'userprofileform': form2})


def registered(request):
	return HttpResponseRedirect('registered.html')

def findAppointment(request):
	if request.method == 'GET':
		form = AppointmentForm(request.GET, prefix='new_appointment')
		if form.is_valid():
			#appointment.day = form['day']
			date = form.cleaned_data['date']
			time = form.cleaned_data['time']
			f_time = strptime(time, "%H:%S")
			temp = datetime.fromtimestamp(mktime(f_time)).time()
			timeslot = datetime.combine(date, temp)
			if Appointment.objects.filter(timeslot = timeslot).exists():
				#try again because this appointment is already booked
				return render(request, 'canNotBook.html', {'date': date, 'time': time})
			else: 
				#good job you've requested an open slot

				#at the moment we have one advisor and it is the default one
				advisor=Advisor.objects.create(specialty="Computer Science")
				appointment = Appointment.objects.create(timeslot = timeslot,student=Student.objects.get(user=request.user),advisor=advisor)
				appointment.save()
				return render(request, 'createdAppointment.html', {'date': date, 'time': time})
	else:
		form = AppointmentForm(prefix='new_appointment')
	return render(request, 'findAppointment.html', {'AppointmentForm':form})

def canNotBook(request):
	return render(request, 'canNotBook.html')

def createdAppointment(request):
	return render(request, 'createdAppointment.html')

def advisorCalendar(request):
    #List of date and time bookings for advisors
    #Post button to redirect to Posting URL
    #View current bookings
        #Each booking will have an expand feature to view detailed information regarding booking
        #Appointment Cancel Button
            #Delete Posting
    #template = loader.get_template('calendar.html')
    #return HttpResponse(template.render())
	return render(request, 'calendar.html')
    #return HttpResponse("This is the advisor's calendar")

def studentCalendar(request):
# Search button to redirect to Student search URL
# List of date and time bookings for students
    # Each booking will have an expand feature to view detailed information regarding booking
    # Appointment Cancel Button
        # Repost the posting
    #template = loader.get_template('calendar.html')
    #return HttpResponse(template.render())
	return render(request, 'calendar.html')
    #return HttpResponse("This is the student's calendar")

def studentSearch(request):
    #A search bar with side filters (example advisor name, department, location, Date/Time)
    #Return button to go redirect to Student Calendar URL

    return HttpResponse("This is the student search page. Stretch goal?")

def studentBooking(request):
    # Time/Date/Location/Department of advisor posting
    # Confirm button to book
    # Cancel button to redirect to search URL
    # Option to include short memo (Text field)
    # Removes posting
    template = loader.get_template('studentBooking.html')
    return HttpResponse(template.render())
    #return HttpResponse("This is the student booking ")

def advisorPosting(request):
    # Time/Date/Location/Department
    # Confirm button to post
    # Cancel button to redirect to Advisor Calendar URL
    # A way to add multiple appointments at a time
    template = loader.get_template('advisorPosting.html')
    return HttpResponse(template.render())
    #return HttpResponse("This is the advisor posting page")
