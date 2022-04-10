
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from awards.models import Project
from .forms import RegisterUserForm
from django.urls import reverse

# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('index')
        else:
            # Redirect to an error page.
            messages.success(request, "Incorrect password or email. Please try again")
            return redirect('login')

    else:
        return render(request, 'authenticate/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "You'be been logged out")
    return redirect('index')

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password, email = email)
            login(request,user)
            messages.success(request, 'Your account has been created successfully')
            return redirect('index')
    else:
        form = RegisterUserForm()
    
    return render(request, 'authenticate/register_user.html', {'form':form})

