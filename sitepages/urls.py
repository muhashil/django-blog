from django.urls import path, include
from . import views

app_name = 'sitepages'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]