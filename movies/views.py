from django.shortcuts import render
from .models import Movie
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    template = loader.get_template('index.html')
    context = {
        'movies': movies,
    }
    return HttpResponse(template.render(context, request))

def movie(request, movie_id):
    movie = Movie.objects.get(id = movie_id)
    template = loader.get_template('display_movie.html')
    context = {
        'movie': movie
    }
    return HttpResponse(template.render(context, request))