import imp
from django.urls import path, re_path, include
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list')
]