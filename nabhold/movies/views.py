from django.shortcuts import render
from django.views import generic

# Create your views here.


class MovieListView(generic.ListView):
    pass


class MovieDetailView(generic.DetailView):
    pass


class MovieUpdateView(generic.UpdateView):
    pass


class MovieDeleteView(generic.DeleteView):
    pass


class MovieCreateView(generic.CreateView):
    pass