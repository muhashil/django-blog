from articles.models import Article, Category
from .serializers import ArticleSerializer, CategorySerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from accounts.models import Author



class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'