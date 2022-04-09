from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'input-field col s12'}))
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'input-field col s12'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'input-field col s12'}))

    class Meta:
        model = User
        fields = ( 'first_name','last_name', 'email','username', 'password1', 'password2')
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'input-field col s12'
        self.fields['password1'].widget.attrs['class'] = 'input-field col s12'
        self.fields['password2'].widget.attrs['class'] = 'input-field col s12'

