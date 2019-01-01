from django.shortcuts import render
from .models import Article

def home(request):
    return render(request, 'articles/home.html', {})