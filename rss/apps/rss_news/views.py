from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def index(request):
    number = random.randrange(0, 100)
    context = {
        'value': 'Hello Python',
        'random': str(number)
    }
    return render(request, 'indexRandom.html', context)


def indexAnother(request):
    number = random.randrange(0, 100)
    context = {
        'value': 'Hello Python',
        'random': str(number)
    }
    return render(request, 'index.html', context)
    # return render(request, 'MyBootstrap.html', context)
