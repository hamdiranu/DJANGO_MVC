from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Mentor, Mentee

# Create your views here.

def home(request):
    return render(request, 'home.html',{})

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html',{'blogs':blogs})

def mentee(request):
    mentees = Mentee.objects.all()
    return render(request, 'mentee.html',{'mentees':mentees})

def mentor(request):
    mentors = Mentor.objects.all()
    return render(request, 'mentor.html',{'mentors':mentors})

def author(request):
    return render(request, 'author.html',{})

def form(request):
    return render(request, 'form.html',{})

def formupdate(request):
    judul   = request.POST['judul_post']
    konten  = request.POST['content_post']
    link    = request.POST['link_gambar']
    new = Blog(Title = judul, Content = konten, Gambar = link)
    new.save()
    # blogs = Blog.objects.all()
    return redirect('/blog')
    
def detail(request, blog_id):
    blogs = get_object_or_404(Blog,pk = blog_id)
    return render(request, 'baca_selengkapnya.html',{'blogs': blogs})