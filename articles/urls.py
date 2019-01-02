from django.urls import path, include
from . import views

app_name = 'articles'

urlpatterns = [
    path('<slug:category_slug>/', views.article_by_category, name='category'),
    path('<slug:category_slug>/<slug>/', views.article_detail, name='detail'),
]
