from django.shortcuts import render
from django.template import loader
from django.http import JsonResponse
from .models import Artist
from .models import Images

def index(request):
    context = {'active': 'Home'}
    return render(request, 'root/index.html')

def about(request):
    context = {'active': 'About'}
    return render(request, 'root/about.html', context)

def feelinglucky(request):
    images = Images.objects.all()
    image_data = []
    for image in images:
        image_data.append({
            'image_label': image.title,
            'image_src': image.image_path,
            'image_desc':image.artist.description,
            'image_pr': image.price
        })
    
    context = {'active': 'Lucky',
                'slider_info':[
                {
                'image_src': "../static/root/images/bg-masthead.jpg",
                'image_label': "Image 1",
                'image_desc': "Some representative placeholder content for the first slide.",
                'image_pr': '35'
                },
                {
                'image_src': "../static/root/images/bg-masthead.jpg",
                'image_label': "Image 2",
                'image_desc': "Some representative placeholder content for the second slide.",
                'image_pr': '25'
                },
                {
                'image_src': "../static/root/images/bg-masthead.jpg",
                'image_label': "Image 3",
                'image_desc': "Some representative placeholder content for the third slide.",
                'image_pr': '45'
                }
                ]
              }

    context = {'active': 'Lucky',
               'slider_info': list(image_data)}
    return render(request, 'root/preview.html', context)

def preview(request):
    image_list = []
    if(request.GET.get('id')):
        artist = Artist.objects.get(id=(int(request.GET.get('id'))))
    elif(request.GET.get('img_id')):
        first_image = Images.objects.filter(pk = int(request.GET.get('img_id')))
        artist = first_image[0].artist
        image_dict = {
            'image_label': first_image[0].title,
            'image_src': first_image[0].image_path,
            'image_desc': first_image[0].artist.description,
            'image_pr': first_image[0].price
        }
        
        image_list.append(image_dict)
    #artist = Artist.objects.get(id=(int(request.GET.get('id'))))
    # Retrieve all images associated with the artist
    images = Images.objects.filter(artist=artist)

    # Create a list of image dictionaries to pass to JsonResponse
    for image in images:
        
        if (request.GET.get('img_id')):
            if (image.pk == int(request.GET.get('img_id'))):
                continue
            
        image_dict = {
            'image_label': image.title,
            'image_src': image.image_path,
            'image_desc':image.artist.description,
            'image_pr': image.price
        }
        image_list.append(image_dict)
        
    context = {'active': 'NA',
               'slider_info': list(image_list)}
    
    return render(request, 'root/preview.html', context)

def gallery(request):
    context = {'active': 'Gallery'}
    return render(request, 'root/gallery.html', context)

def artistworks(request):
    art = Artist.objects.all()
    imgs = Images.objects.filter(artist = art[int(request.GET.get('id')) - 1] )
    context = {
                'active': 'Artist',
                'artists': art[int(request.GET.get('id')) - 1],
                'images': imgs
               }
    return render(request, 'root/artistworks.html', context)

def get_artists(request):
    artists = Artist.objects.all()
    artist_data = []
    for artist in artists:
        first_image = Images.objects.filter(artist=artist).first()
        data = {
            'id': artist.id,
            'name': artist.name,
            'description': artist.description,
            'type': artist.type,
            'image_path': first_image.image_path if first_image else None,
            'price': first_image.price if first_image else None,
            'date_posted': first_image.date_posted if first_image else None
        }
        artist_data.append(data)
    
    return JsonResponse({'goats': list(artist_data)})
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
