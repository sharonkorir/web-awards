from django.urls import path
from . import views

urlpatterns=[
  path('', views.index, name='index'),
  path('search/', views.search_results, name='search_results'),
  path('create_project/', views.create_project, name ='create_project'),
  path('profile/<str:username>/', views.user_profile, name='user_profile'),
  path('project/<str:pk>/', views.project_details, name='project_details'),
  path('rate_project/<str:pk>', views.rate_project, name = 'rate_project'),
  path('profile/<str:username>/update', views.update_profile, name='update_profile'),
]