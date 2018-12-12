from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('article/', views.article_list),
    path('article/<slug:slug>', views.article_detail),
]
