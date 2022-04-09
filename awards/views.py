from django.shortcuts import render
from awards.models import Project, Profile
from django.contrib.auth.models import User

# Create your views here.
def index(request):
  return render(request,'index.html')

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

def user_profile(request):
    profiles = Profile.objects.all()
    users = User.objects.all()
    return render(request, 'authenticate/user_profile.html', {'users':users, 'profiles':profiles})