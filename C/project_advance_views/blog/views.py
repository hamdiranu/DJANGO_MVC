from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html',{})

def blog(request):
    return render(request, 'blog.html',{})

def mentee(request):
    return render(request, 'mentee.html',{})

def mentor(request):
    return render(request, 'mentor.html',{})

def author(request):
    return render(request, 'author.html',{})