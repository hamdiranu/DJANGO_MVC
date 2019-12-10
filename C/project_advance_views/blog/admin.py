from django.contrib import admin
from .models import Blog, Mentor, Mentee

# Register your models here.
admin.site.register(Blog)
admin.site.register(Mentor)
admin.site.register(Mentee)