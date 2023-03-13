from django.shortcuts import render, HttpResponse
from django.template import loader
from django.http import JsonResponse

def index(request):
    return render(request, 'root/index.html')

def about(request):
    context = {'active': 'About'}
    return render(request, 'root/about.html', context)

def gallery(request):
    context = {'active': 'Gallery'}
    return render(request, 'root/gallery.html', context)

def get_artists(request):
    return JsonResponse( {
        'goats' :[{
            'uid': '1',
            'name': 'N',
            'age': 12,
            'adopted': 1,
            'image': 'bg-masthead.jpg'   
        }
        ,
        {
            'uid': '1',
            'name': 'N',
            'age': 12,
            'adopted': 1,
            'image': 'bg-masthead.jpg'   
        },
        {
            'uid': '1',
            'name': 'N',
            'age': 12,
            'adopted': 1,
            'image': 'bg-masthead.jpg'   
        },
        {
            'uid': '1',
            'name': 'N',
            'age': 12,
            'adopted': 1,
            'image': 'bg-masthead.jpg'   
        },
        {
            'uid': '1',
            'name': 'N',
            'age': 12,
            'adopted': 1,
            'image': 'bg-masthead.jpg'   
        },
        {
            'uid': '1',
            'name': 'N',
            'age': 12,
            'adopted': 1,
            'image': 'bg-masthead.jpg'   
        }]})