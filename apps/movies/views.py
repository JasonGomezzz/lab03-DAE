from django.shortcuts import render
from .models import Movie

# Verifica que el nombre sea exactamente movie_list
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, "movies/movie_list.html", {"movies": movies})