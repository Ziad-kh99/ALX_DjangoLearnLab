from django.urls import path
from .views import list_books
from .views import LibraryDetailView


urlpatterns = [
    path('listbooks/', list_books), 
    path('librarydetails/', LibraryDetailView),
]