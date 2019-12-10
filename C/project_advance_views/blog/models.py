from django.db import models

# Create your models here.

class Blog(models.Model):
    Gambar            = models.CharField(max_length = 200)
    Title             = models.CharField(max_length = 200)
    Content           = models.TextField(max_length = 200)

class Mentor(models.Model):
    Gambar          = models.CharField(max_length = 200)
    Nama            = models.CharField(max_length = 200)
    Experience      = models.CharField(max_length = 200)
    Quote           = models.TextField(max_length = 200)

class Mentee(models.Model):
    Gambar          = models.CharField(max_length = 200)
    Name            = models.CharField(max_length = 200)
    Quote           = models.TextField(max_length = 200)
