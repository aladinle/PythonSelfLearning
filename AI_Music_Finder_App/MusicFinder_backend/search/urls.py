from django.urls import path
from .views import lyric_search

urlpatterns = [
    path('search/', lyric_search, name='lyric_search'),
]