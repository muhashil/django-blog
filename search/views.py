from django.shortcuts import render
from articles.models import Article
from django.core.paginator import Paginator
from django.db.models import Q


def search(request):
    if 'q' in request.GET:
        query = request.GET.get('q')
        article_list = Article.objects.all().filter(
            Q(judul__contains=query)
        )

        # Paginator
        paginator = Paginator(article_list, 8)

        page = request.GET.get('page')
        articles = paginator.get_page(page)

        return render(request, 'search/search.html', {'articles': articles})
