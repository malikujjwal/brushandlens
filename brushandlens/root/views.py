from django.shortcuts import render, HttpResponse
from django.template import loader

def index(request):
    return render(request, 'root/index.html')

def about(request):
    context = {'active': 'About'}
    return render(request, 'root/about.html', context)