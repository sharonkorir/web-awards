from django.urls import path
from . import views

urlpatterns=[
  path('', views.index, name='index'),
  path('search/', views.search_results, name='search_results'),
  path('users/<str:username>', views.user_profile, name='user_profile'),
  path('create_project/', views.create_project, name ='create_project')
]