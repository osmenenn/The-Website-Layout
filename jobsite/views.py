from django.shortcuts import render, redirect
from django.http import HttpRespone 
from django import Post

from jobsite.forms import PostForm 

# Create your views here.
def index(request):
    if request.method == "HOME":
        form = PostForm(request.index)
        if form.is_valid():
            post = form.save(commit =False)
            post.author = request.user 
        
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
   
    if request.method == "HOME":
        form = PostForm(request.index)
        if form.is_valid():
            post = form.save(commit =False)
            post.author = request.user 
    return render(request, 'jobsite/profile.html', {})

