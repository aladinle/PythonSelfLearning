from django.urls import path
from views import lyric_search # type: ignore

urlpatterns = [
    path('search/', lyric_search, name='lyric_search'),
]