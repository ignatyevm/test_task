from django.urls import path

from .views import get_csv, get_json

urlpatterns = [
    path('get_csv', get_csv),
    path('get_json', get_json),
]