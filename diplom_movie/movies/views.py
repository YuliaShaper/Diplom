from django.shortcuts import render, redirect
from django.views.generic.base import View

from .models import Movie
from .forms import ReviewFrom


class MoviesView(View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, "movies/movies.html", {"movie_list": movies})


class MovieDetailView(View):
    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        return render(request, "movies/movie_detail.html", {"movie": movie})


class AddReview(View):
    def post(self, request, pk):
        form = ReviewFrom(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())
