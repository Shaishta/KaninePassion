from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='Home'),
    path('about', views.about, name='About'),
    path('gallery', views.gallery, name='Gallery'),
    path('contact', views.contact, name='Contact'),

]