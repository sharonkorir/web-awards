
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from awards.models import Project, Profile, Rate
from django.contrib.auth.models import User
from .forms import ProjectForm, RateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import requests

# Create your views here.
def index(request):
  projects = Project.objects.all()
  random = Project.get_random()
  rates = Rate.get_rate_count(random.pk)
  if rates > 0:
        averages = Rate.find_sum(random.pk)
        design = averages[0]
        content = averages[1]
        usability = averages[2]
        average = averages[3] 
        context = {
          'projects':projects,
          'design': design,
          'content': content,
          'usability': usability,
          'average': average,
          'random': random
        }
  else:
      context = {
        'projects':projects,
        'random':random
      }
  return render(request,'index.html', context)

def search_results(request):
    '''
    Function to search for projects
    
    Args: search term
    '''

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_project(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

#test if user profiles are created on registration
def user_profile(request, username):
    profiles = Profile.objects.filter(user__username = username)
    users = User.objects.all()
    projects = Project.objects.filter(profile__user__username=username)
    return render(request, 'authenticate/user_profile.html', {'users':users, 'profiles':profiles, 'projects':projects})

def project_details(request, pk):
    project = Project.objects.filter(pk = pk)
    rates = Rate.get_rate_count(pk)
    if rates > 0:
        
        averages = Rate.find_sum(pk)
        design = averages[0]
        content = averages[1]
        usability = averages[2]
        average = averages[3] 
        context = {
          'project':project,
          'design': design,
          'content': content,
          'usability': usability,
          'average': average,
        }
    else:
        context = {
          'project':project,

        }

    return render(request, 'projects/project_detail.html', context)

@login_required()
def create_project(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProjectForm()

    return render(request, 'projects/create_project.html', {'form':form})

@login_required()
def rate_project(request, pk):
    project = Project.objects.get(id=pk)
    user = request.user
    print('testing', project, user)

    if request.method == 'POST':
        form = RateForm(request.POST)
        print('test form',form)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = user
            rate.project = project
            rate.save()
            print('test form save' ,rate)
            
            return HttpResponseRedirect(reverse('project_details', args=pk))
            
    else:
        form = RateForm()
        print('request is not POST')

    context = {
      'form':form,
      'project':project
    }
    print(user, project)
    return render(request, 'projects/rate_project.html', context)

def update_profile(request, username):
    '''
    returns user profile if user is authenticated
    '''
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if p_form.is_valid():
            p_form.save()
            #fetch projects
            projects = Project.objects.filter(profile__user=request.user)
            #succesful update message
            messages.success(request, f'Your account has been updated')
            # return redirect('profile')
            return render(request,'authenticate/user_profile.html', {'projects':projects})
            # return HttpResponseRedirect(reverse('user_profile', args=username))
            
    else:
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)

    context = {
      'p_form': p_form,
      'projects': Project.objects.filter(profile__user = request.user)
    }

    return render(request, 'authenticate/update_profile.html', context)
