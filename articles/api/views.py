from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from articles.models import Article
from .serializers import ArticleSerializer


def article_list(request):
    # Get list of all articles
    if request.method == 'GET':
        try:
            articles = Article.objects.all()
        except Article.DoesNotExist:
            return HttpResponse(status=404)

        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)


def article_detail(request, slug):
    # Get article detail by slug
    try:
        article = Article.objects.get(slug=slug)
    except Article.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data)
