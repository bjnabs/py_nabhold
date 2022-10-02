from django.urls import path, re_path, include
from . import views


app_name = 'movies'

urlpatterns = [
    path('', views.MovieListView.as_view(), name='movie_list'),
]