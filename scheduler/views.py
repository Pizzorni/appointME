from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from .models import MyUserCreationForm

#Login - 
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.core.context_processors import csrf
from forms import RegistrationForm

# Create your views here.

def index(request):
    #template = loader.get_template('index.html')
    #return HttpResponse(template.render())
	#return render(request,'index.html')
	if request.user.is_authenticated():
		return render(request, 'loggedIn.html')
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
	return render_to_response('loggedIn.html', {'full_name': request.user.email})
	
def invalid(request):
	return render_to_response('invalid.html')
	
def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')
	
def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return render_to_response('registered.html')
	else:
		form = RegistrationForm()
	return render(request, 'register.html', { 'form':form,})

def registered(request):
	return HttpResponseRedirect('registered.html')

def advisorCalendar(request):
    #List of date and time bookings for advisors
    #Post button to redirect to Posting URL
    #View current bookings
        #Each booking will have an expand feature to view detailed information regarding booking
        #Appointment Cancel Button
            #Delete Posting
    template = loader.get_template('calendar.html')
    return HttpResponse(template.render())
    #return HttpResponse("This is the advisor's calendar")

def studentCalendar(request):
# Search button to redirect to Student search URL
# List of date and time bookings for students
    # Each booking will have an expand feature to view detailed information regarding booking
    # Appointment Cancel Button
        # Repost the posting
    template = loader.get_template('calendar.html')
    return HttpResponse(template.render())
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
