from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'Kapp/home.html')


def about(request):
    return render(request, 'Kapp/about.html')


def gallery(request):
    return render(request, 'Kapp/gallery.html')


def contact(request):
    return render(request, 'Kapp/contact.html')

