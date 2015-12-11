from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello World, can you hear me? I'm in New York dreaming about who I used to be")
