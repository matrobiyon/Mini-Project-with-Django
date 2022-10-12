from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("etaji<int:etaj>/", get_etaj, name="etaj" ),
    path("etaji<int:etaj>/hujrai<int:hujra>", malumot, name="malumot")
]