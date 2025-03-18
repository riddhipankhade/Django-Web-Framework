from django.urls import path
from . import views

#. represents same working directoroy as the file

urlpatterns = [
    path('', views.home, name="home"),  
    
]