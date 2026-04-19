from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.movies.views import MovieViewSet 

router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movies')

urlpatterns = [
    path('admin/', admin.site.urls),
    # ESTA LÍNEA ES LA QUE TE FALTA O ESTÁ MAL ESCRITA:
    path('api/', include(router.urls)), 
    path('', include('apps.movies.urls')), 
]