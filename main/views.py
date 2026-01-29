from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home',
        'content': 'Главная страница магазина - HOME',
        'list': ['First', 'second'],
        'dict': {'First':1},
        'is_authenticated': False

    }
    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse('About page')
