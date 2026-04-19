from django.shortcuts import render
from rest_framework import viewsets
from .models import Movie
from .serializers import MovieSerializer

# 1. VISTA PARA API (Django Rest Framework)
class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite ver, crear, editar y eliminar películas (CRUD).
    """
    queryset = Movie.objects.all().order_by('-created_at')
    serializer_class = MovieSerializer


# 2. VISTA PARA HTML (Tradicional)
def movie_list(request):
    """
    Vista para renderizar la lista de películas en un template HTML.
    """
    movies = Movie.objects.all()
    return render(request, "movies/movie_list.html", {"movies": movies})