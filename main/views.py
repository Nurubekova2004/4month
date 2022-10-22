from django.shortcuts import render, get_object_or_404
import datetime

from main import models


def about_us(request):
    return render(request, 'about_us.html')


def date_now(request):
    date = datetime.datetime.now()
    return render(request, 'date_now.html', {'date':date})

def films(request):
    film = models.Film.objects.all()
    return render(request, 'all_films.html', {'film':film} )

def films_detail(request, id):
    detail = get_object_or_404(models.Film, id=id)
    return render(request, 'films_detail.html', {'detail':detail})
