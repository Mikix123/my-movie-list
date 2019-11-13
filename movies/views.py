from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import ModelForm
from django import forms
from django.utils.translation import gettext_lazy as _

from movies.models import Movie


# Create your views here.


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'duration', 'year', 'posterUrl', 'ageRating', 'topic', 'country', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        }
        labels = {
            'title': _('Tytuł'),
            'duration': _('Długość'),
            'year': _('Rok'),
            'posterUrl': _(
                'Id obrazu z <a href="https://www.themoviedb.org/" style="color: cadetblue;">The movie DB</a>'),
            'ageRating': _('Kategoria wiekowa'),
            'topic': _('Tematyka'),
            'country': _('Kraj'),
            'description': _('Opis')
        }


def movie_list(request):
    movies_list = Movie.objects.order_by('-createAt').all()

    page = request.GET.get('page', 1)
    paginator = Paginator(movies_list, 10)

    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)

    return render(request, 'movies/movie_list.html', {'movies': movies})


def movie_view(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/movie_view.html', {'movie': movie})


def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    form = MovieForm(request.POST or None, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('movie_list')
    return render(request, 'movies/movie_form.html', {'form': form})


def movie_create(request):
    form = MovieForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('movie_list')
    return render(request, 'movies/movie_form.html', {'form': form})
