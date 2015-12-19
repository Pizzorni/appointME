from django.conf.urls import url
from . import views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
   url(r'^$', views.index, name='index'),
   #url(r'^login', views.login, name='login'),
   #url(r'^register', views.register, name='register'),
   #url(r'^advisorCalendar', views.advisorCalendar, name='advisorCalendar'),
   #url(r'^studentCalendar', views.studentCalendar, name='studentCalendar'),
   url(r'^calendar', views.advisorCalendar, name='advisorCalendar'),
   url(r'^calendar', views.advisorCalendar, name='studentCalendar'),
   url(r'^studentSearch', views.studentSearch, name='studentSearch'),
   url(r'^studentBooking', views.studentBooking, name='studentBooking'),
   url(r'^advisorPosting', views.advisorPosting, name='advisorPosting'),
   
   url(r'^register', views.register, name='register'),
   url(r'^regAdvisor', views.regAdvisor, name='regAdvisor'),
   url(r'^register_success', views.registered, name='registered'),
   url(r'^login', views.login, name='login'),
   url(r'^auth', views.auth_view, name='auth_view'),
   url(r'^logout', views.logout, name='logout'),
   url(r'^loggedIn', views.loggedIn, name='loggedIn'),
   url(r'^loggedInAdvisor', views.loggedInAdvisor, name='loggedInAdvisor'),
   url(r'^invalid', views.invalid, name='invalid'),
   url(r'^findAppointment', views.findAppointment, name='findAppointment'),

]
