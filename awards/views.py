from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render,redirect
from awards.models import Project, Profile, Rate
from django.contrib.auth.models import User
from .forms import ProjectForm, RateForm
from django.db.models import Sum

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
    rates = Rate.objects.filter(project__title = title)
    averages = Rate.find_sum(title)
    design = averages[0]
    content = averages[1]
    usability = averages[2]
    average = averages[3]


    return render(request, 'projects/project_detail.html', {'project':project, 'rates':rates, 'content':content, 'design':design, 'usability':usability, 'average':average})

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

def rate_project(request, title):
    project = Project.objects.get(title=title)
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
            
            return HttpResponseRedirect(reverse('project_details', args=title))
            
    else:
        form = RateForm()
        print('request is not POST')

    context = {
      'form':form,
      'project':project
    }
    print(user, project)
    return render(request, 'projects/rate_project.html', context)
