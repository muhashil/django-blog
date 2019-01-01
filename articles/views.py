from django.shortcuts import render
from .models import Article

def home(request):
    featured_articles = Article.objects.featured()
    latest_articles = Article.objects.all()


    context = {
        'featured_articles': featured_articles,
        'latest_articles': latest_articles
    }
    return render(request, 'articles/home.html', context)