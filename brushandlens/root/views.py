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

def artistworks(request):
    context = {
                'active': 'Artist',
                'artists': {
                    'uid': '1',
                    'name': 'Artist1',
                    'desc' : 'My work goes into dank memes art!',
                    'art': 'design',
                    'image_data': [{'image_path':'bg-masthead.jpg',
                                    'image_name':'BG',
                                    'image_link': '2'}]  
               }}
    
    print(request.GET.get('id'))
    return render(request, 'root/artistworks.html', context)

def get_artists(request):
    return JsonResponse( {
        'goats' :[{
            'uid': '1',
            'name': 'Artist1',
            'theme': 'design',
            'image': 'bg-masthead.jpg'   
        }
        ,
        {
            'uid': '2',
            'name': 'Artist2',
            'theme': 'market',
            'image': 'bg-masthead.jpg'   
        },
        {
            'uid': '3',
            'name': 'Artist3',
            'theme': 'develop',
            'image': 'bg-masthead.jpg'   
        },
        {
            'uid': '4',
            'name': 'Artist4',
            'theme': 'market',
            'image': 'bg-masthead.jpg' 
        },
        {
            'uid': '5',
            'name': 'Artist5',
            'theme': 'br',
            'image': 'bg-masthead.jpg'  
        },
        {
            'uid': '6',
            'name': 'Artist6',
            'theme': 'br',
            'image': 'bg-masthead.jpg'
        }]})