from django.urls import path, re_path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('team/', views.team, name='team'),
    path('about/', views.about, name='about'),
]