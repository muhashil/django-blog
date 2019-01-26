from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from articles.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('articles.api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', home, name='home'),
    path('articles/', include('articles.urls')),
    path('search/', include('search.urls')),
    path('', include('sitepages.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
