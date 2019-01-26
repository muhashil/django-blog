from django.shortcuts import render
from articles.models import Article, Category
from django.core.paginator import Paginator


def home(request):
    featured_articles = Article.objects.featured()
    latest_articles = Article.objects.all()

    # Paginatior
    paginator = Paginator(latest_articles, 8)

    page = request.GET.get('page')
    articles = paginator.get_page(page)

    context = {
        'featured_articles': featured_articles,
        'latest_articles': articles
    }
    return render(request, 'articles/home.html', context)


def article_by_category(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    articles_by_category = Article.objects.filter(kategori=category).all()

    # Paginatior
    paginator = Paginator(articles_by_category, 8)

    page = request.GET.get('page')
    articles = paginator.get_page(page)

    context = {
        'articles_by_category': articles,
        'category': category
    }
    return render(request, 'articles/category.html', context)


def article_detail(request, category_slug, slug):
    article = Article.objects.get(slug=slug)

    context = {
        'article': article
    }
    return render(request, 'articles/article-detail.html', context)
