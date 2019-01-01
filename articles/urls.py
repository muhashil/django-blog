from django.urls import path, include
from .views import home

app_name = 'articles'

urlpatterns = [
    path('', home, name='home')
]
