from django.shortcuts import render

# Create your views here.


def index(request, template='index.html'):
    context = { }
    return render(request, template, context)


def about(request, template='about.html'):
    context = {}
    return render(request, template, context)


def contact(request, template='contact.html'):
    context = {}
    return render(request, template, context)


def team(request, template='team.html'):
    context = {}
    return render(request, template, context)
 