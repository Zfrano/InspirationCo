from django.db import connection

from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'main/index.html')


def stores(request):
    # store_info = DistrictManager.objects.select_related('store_manager').all().select_related(
    #     'store_manager__store').all()
    store_info = StoreManager.objects.select_related('district_manager').all().select_related('store')
    return render(request, 'main/stores.html', {'store_info': store_info})
