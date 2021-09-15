from django.urls import path
from . import  views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('se/', views.se, name = 'se'),
    path('dkc/', views.dkc, name = 'dkc'),
    path('iek/', views.iek, name = 'iek'),
    path('itk/', views.itk, name = 'itk'),
    path('bolid/', views.bolid, name = 'bolid'),
    path('dahua/', views.dahua, name = 'dahua'),
    path('optimus/', views.optimus, name = 'optimus'),
    path('phoenix/', views.phoenix, name = 'phoenix'),
    path('rittal/', views.rittal, name = 'rittal'),
    path('wago/', views.wago, name = 'wago'),
    path('dlink/', views.dlink, name = 'dlink'),
]