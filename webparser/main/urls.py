from django.urls import path
from . import  views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('apc/', views.apc, name = 'apc'),
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
    path('Planet/', views.planet, name = 'planet'),
    path('rittal/', views.rittal, name = 'rittal'),
    path('se/', views.se, name = 'se'),
    path('ubiquiti/', views.ubiquiti, name = 'ubiquiti'),
    path('unv/', views.unv, name = 'unv'),
    path('wago/', views.wago, name = 'wago'),


    path('se_mass/', views.se_mass, name = 'se_mass'),
    path('dkc_mass/', views.dkc_mass, name = 'dkc_mass'),
    path('iek_mass/', views.iek_mass, name = 'iek_mass'),
    path('itk_mass/', views.itk_mass, name = 'itk_mass'),
    path('phoenix_mass/', views.phoenix_mass, name = 'phoenix_mass'),
    path('rittal_mass/', views.rittal_mass, name = 'rittal_mass'),
    path('wago_mass/', views.wago_mass, name = 'wago_mass'),

]