from django.urls import path
from . import  views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('se/', views.se, name = 'se'),
    path('dkc/', views.dkc, name = 'dkc'),
]