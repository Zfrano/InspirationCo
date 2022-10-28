from django.urls import path, include
from .views import index, stores

urlpatterns = [
    path('', index, name='home'),
    path('stores/', stores, name='stores'),
]
