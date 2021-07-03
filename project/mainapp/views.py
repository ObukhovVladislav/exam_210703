from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from mainapp.models import Adjective
import random


@login_required
def index(request):
    adjective = ['Хороший', 'Плохой', 'Красивый', 'Добрый', 'Большой', 'Маленький']
    # adjective = Adjective.objects.all()
    random_adjective = random.choice(adjective)
    context = {
        'adjective': random_adjective,
        'title': 'Главная'
    }
    return render(request, 'mainapp/index.html', context)


def about(request):
    context = {
        'title': 'О нас'
    }
    return render(request, 'mainapp/about.html', context)
