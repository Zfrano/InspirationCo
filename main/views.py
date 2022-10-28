from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'main/index.html')


def stores(request):
    all_stores = Store.objects.all()
    return render(request, 'main/stores.html', {'all_stores': all_stores})
