from django.urls import path
from . import views
from django.conf import settings



urlpatterns =[
    path('', views.home, name='index'),
    path('gallery/', views.gallery, name='gallery'),
    path('search/', views.search, name='search')

] 
