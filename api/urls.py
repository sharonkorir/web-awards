from django.urls import path
from . import views

urlpatterns =[
    path('profiles/<str:pk>', views.get_profiles),
    path('projects/', views.get_projects),
    path('urls/', views.get_urls),
    path('rate/', views.add_rate),
    path('rate/get/', views.get_rates)
]