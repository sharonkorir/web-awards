from django.contrib import admin
from .models import Profile, Project, Rate

# Register your models here.
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Rate)