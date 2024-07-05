from django.urls import path
from .views import *
urlpatterns = [
    path('header/',header,name='header'),
    path('footer/',footer,name='footer'),
    path('home/',home,name='home'),
    path('services/',services,name='services'),
    path('contact/',contact,name='contact')
    
]