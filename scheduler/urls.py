from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^index', views.index, name='index'),
   url(r'^login', views.login, name='login'),
   #url(r'^advisorCalendar', views.advisorCalendar, name='advisorCalendar'),
   #url(r'^studentCalendar', views.studentCalendar, name='studentCalendar'),
   url(r'^calendar', views.advisorCalendar, name='advisorCalendar'),
   url(r'^calendar', views.advisorCalendar, name='studentCalendar'),
   url(r'^studentSearch', views.studentSearch, name='studentSearch'),
   url(r'^studentBooking', views.studentBooking, name='studentBooking'),
   url(r'^advisorPosting', views.advisorPosting, name='advisorPosting'),
]