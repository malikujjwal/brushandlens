from django.shortcuts import render
from django.template import loader

def index(request):
    return render(request, 'root/index.html')

def about(request):
    context = {'active': 'About'}
    return render(request, 'root/about.html', context)

def preview(request):
    return render(request, 'root/preview.html')

def feelinglucky(request):
    urls = ["../static/root/images/bg-masthead.jpg", "../static/root/images/bg-masthead.jpg", "../static/root/images/bg-masthead.jpg"]
    imgLabels = ["Image 1", "Image 2", "Image 3"]
    imgDescription = ["Some representative placeholder content for the first slide.", 
                      "Some representative placeholder content for the second slide.", 
                      "Some representative placeholder content for the third slide."]

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
    return render(request, 'root/preview.html', context)