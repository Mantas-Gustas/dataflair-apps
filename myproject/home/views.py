from django.shortcuts import render
from .templates import *
import datetime
# DataFlair #Views #TemplateInheritance
# Create your views here.


def home(request):
    return render(request, 'index.html')


def other(request):
    context = {
        'k1': 'Welcome to the Second page',
    }
    return render(request, 'others.html', context)


def about(request):
    time = datetime.datetime.now()
    return render(request, 'about.html', {'time': time})
