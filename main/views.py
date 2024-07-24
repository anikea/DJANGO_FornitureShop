from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    context = {
        'title': 'Home',
        'content': 'Головна сторінка магазину - HOME',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_authenticated': False,
    }   

    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse('About us page')