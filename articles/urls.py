from django.urls import path, include
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.home, name='home'),
    path('articles/<slug:category_slug>/', views.article_by_category, name='category'),
    path('articles/<slug:category_slug>/<slug>/', views.article_detail, name='detail'),
]
