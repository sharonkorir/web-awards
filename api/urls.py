from django.urls import path
from . import views

urlpatterns =[
    path('profiles', views.getProfiles),
    path('projects', views.getProjects),
    path('rate/', views.addRate),
]