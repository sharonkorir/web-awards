
from django.http import JsonResponse
from django.shortcuts import render,redirect
from awards.models import RATE_CHOICES, Project, Profile, Rate
from django.contrib.auth.models import User
from .forms import ProjectForm, RateForm

# Create your views here.
def index(request):
  projects = Project.objects.all()
  context = {
    'projects':projects
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
    return render(request, 'authenticate/user_profile.html', {'users':users, 'profiles':profiles})

def project_details(request, title):
    project = Project.objects.filter(title = title)
    return render(request, 'projects/project_detail.html', {'project':project})

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

def rate_project(request, id):
    project = Project.objects.get(id=id)
    user = request.user

    if request.method == 'POST':
        form = RateForm(data = request.POST)
        print(form)
        if form.is_valid():
            design = request.POST.get('design')
            content = request.POST.get('content')
            usability = request.POST.get('usability')
            rate = Rate(design=design, content=content, usability=usability, project=project, user=user)
            rate.user = user
            rate.project = project
            rate.save()
            data = {'success': 'Your rate has been submitted'}
            
            #return redirect('project_details', id)
            return JsonResponse(data)
            
    else:
        form = RateForm()
        print('request is not POST')

    context = {
      'form':form,
      'project':project
    }
    return render(request, 'project_detail.html', context)