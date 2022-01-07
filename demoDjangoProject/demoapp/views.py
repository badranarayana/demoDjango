from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # business logic
    # retrieve data from db
    # render html temlate with data
    return HttpResponse("This is my demo app view result")
    
