from django.urls import path

from . import views

urlpatterns = [
  path('',views.index, name='index'),
  path('about/', views.about, name='about'),
  path('contact/',views.contact, name='contact'),
  path('news/',views.news, name='news'),
  path('admin/',views.admin, name='admin'),
  path('/modificar/<str:ciudad>/', views.modificar, name='modificar'),
]