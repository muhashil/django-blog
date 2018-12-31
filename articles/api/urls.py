from articles.api.views import ArticleViewSet, CategoryViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'article', ArticleViewSet, basename='article')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'user', UserViewSet, basename='user')
urlpatterns = router.urls
