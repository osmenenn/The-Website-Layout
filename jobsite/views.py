from django.shortcuts import render
from django.http import HttpRespone 
from django import Post 

# Create your views here.
def index(request):
    return render(request, 'jobsite/index.html', {})

def AboutUs(request):
    return render(request, 'jobsite/AboutUs.html', {})

def conncet(request):
    return render(request, 'jobsite/connect.html', {})

def explore(request):
    return render(request, 'jobsite/connect.html', {})

def HowItWorks(request):
    return render(request, 'jobsite/HowItWorks.html', {})

def profile(request):
    return render(request, 'jobsite/profile.html', {})

