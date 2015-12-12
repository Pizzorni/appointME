from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

# Create your views here.

# Anonymous views
#################s
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
   #return HttpResponse("Hello, World. You win.")

def login(request):

    #Username and Password text flied
    #Sign in button (Redirects to Student/Advisor calendar url)
    #$Register button (redirects to Register page url)
    template = loader.get_template('login.html')
    return HttpResponse(template.render())
    #return HttpResponse("You need to login.")

def register(request):
    #username, password, confirm password
    #submit button
    template = loader.get_template('register.html')
    return HttpResponse(template.render())

# Authenticated views
#####################
@login_required
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

@login_required
def studentCalendar(request):
# Search button to redirect to Student search URL
# List of date and time bookings for students
    # Each booking will have an expand feature to view detailed information regarding booking
    # Appointment Cancel Button
        # Repost the posting
    template = loader.get_template('calendar.html')
    return HttpResponse(template.render())
    #return HttpResponse("This is the student's calendar")

@login_required
def studentSearch(request):
    #A search bar with side filters (example advisor name, department, location, Date/Time)
    #Return button to go redirect to Student Calendar URL

    return HttpResponse("This is the student search page. Stretch goal?")

@login_required
def studentBooking(request):
    # Time/Date/Location/Department of advisor posting
    # Confirm button to book
    # Cancel button to redirect to search URL
    # Option to include short memo (Text field)
    # Removes posting
    template = loader.get_template('studentBooking.html')
    return HttpResponse(template.render())
    #return HttpResponse("This is the student booking ")
    
@login_required
def advisorPosting(request):
    # Time/Date/Location/Department
    # Confirm button to post
    # Cancel button to redirect to Advisor Calendar URL
    # A way to add multiple appointments at a time
    template = loader.get_template('advisorPosting.html')
    return HttpResponse(template.render())
    #return HttpResponse("This is the advisor posting page")