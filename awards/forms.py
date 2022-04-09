from django import forms
from django.forms import ModelForm
from .models import Project, Rate, RATE_CHOICES
from django import forms


class ProjectForm(ModelForm):

    class Meta:
        model = Project
        fields = ('title', 'description', 'link', 'image')

class RateForm(ModelForm):
    design = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(), required=True)
    content = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(), required=True)
    usability = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(), required=True)

    class Meta:
        model = Rate
        fields = ('design', 'content', 'usability')