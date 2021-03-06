from django import forms
from django.forms import ModelForm
from .models import Profile, Project, Rate, RATE_CHOICES

class ProjectForm(ModelForm):
    link = forms.URLField()

    class Meta:
        model = Project
        fields = ('title', 'description', 'link', 'image')

class RateForm(forms.ModelForm):
    design = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'browser-default'}),
        choices=RATE_CHOICES, 
        required=True,
    )
    content = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'browser-default'}),
        choices=RATE_CHOICES, 
        required=True,
    )
    usability = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'browser-default'}),
        choices=RATE_CHOICES, 
        required=True,
    )
    class Meta:
        model = Rate
        fields = ('design', 'content', 'usability')

class ProfileUpdateForm(forms.ModelForm):
    '''
    Form that inherits from the django ModelForm and allows user to update their profile
    '''

    class Meta:
        model = Profile
        fields = ['profile_photo', 'bio', 'linkedIn_url', 'twitter_url', 'website_url']