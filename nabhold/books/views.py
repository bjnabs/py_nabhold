import datetime
from .models import Book, Author, BookInstance, Genre
from . forms import RenewBookForm, RenewBookModelForm
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic
from django.shortcuts import render, get_object_or_404


class BookListView(generic.ListView):
    pass