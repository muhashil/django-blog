from django.shortcuts import render
from articles.models import Article, Category

def home(request):
    featured_articles = Article.objects.featured()
    latest_articles = Article.objects.all()


    context = {
        'featured_articles': featured_articles,
        'latest_articles': latest_articles
    }
    return render(request, 'articles/home.html', context)

def article_by_category(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    articles_by_category = Article.objects.with_category(category_slug)

    context = {
        'articles_by_category': articles_by_category,
        'category': category
    }
    return render(request, 'articles/category.html', context)

def article_detail(request, category_slug, slug):
    article = Article.objects.get(slug=slug)

    context = {
        'article': article
    }
    return render(request, 'articles/article-detail.html', context)