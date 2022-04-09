from django import forms
from django.forms import ModelForm
from .models import Project
from django import forms

class ProjectForm(ModelForm):

    class Meta:
        model = Project
        fields = ('title', 'description', 'link', 'image')
