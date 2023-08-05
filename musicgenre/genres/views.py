from django.shortcuts import render
from .models import Genre, Musician

def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'genre_list.html', {'genres': genres})

def musician_list(request, genre_id):
    musicians = Musician.objects.filter(genre_id=genre_id)
    return render(request, 'musician_list.html', {'musicians': musicians})

def musician_detail(request, musician_id):
    musician = Musician.objects.get(id=musician_id)
    return render(request, 'musician_detail.html', {'musician': musician})
