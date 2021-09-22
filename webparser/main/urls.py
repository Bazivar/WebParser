from django.urls import path
from . import  views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('dkc/', views.dkc, name = 'dkc'),
    path('bolid/', views.bolid, name = 'bolid'),
    path('dahua/', views.dahua, name = 'dahua'),
    path('dlink/', views.dlink, name = 'dlink'),
    path('hikvision/', views.hikvision, name = 'hikvision'),
    path('iek/', views.iek, name = 'iek'),
    path('itk/', views.itk, name = 'itk'),
    path('mikrotik/', views.mikrotik, name = 'mikrotik'),
    path('optimus/', views.optimus, name = 'optimus'),
    path('phoenix/', views.phoenix, name = 'phoenix'),
    path('rittal/', views.rittal, name = 'rittal'),
    path('se/', views.se, name = 'se'),
    path('ubiquiti/', views.ubiquiti, name = 'ubiquiti'),
    path('unv/', views.unv, name = 'unv'),
    path('wago/', views.wago, name = 'wago'),


    path('se_mass/', views.se_mass, name = 'se_mass'),

]