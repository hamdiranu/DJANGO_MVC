from django.contrib import admin
from .models import Direksi, Mentee, Mentor, MataPelajaran, Challenge, LiveCode

# Register your models here.
admin.site.register(Direksi)
admin.site.register(Mentee)
admin.site.register(Mentor)
admin.site.register(MataPelajaran)
admin.site.register(Challenge)
admin.site.register(LiveCode)