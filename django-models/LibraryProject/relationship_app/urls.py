from django.urls import path
import views


urlpatterns = [
    path('listbooks/', views.list_books), 
    path('librarydetails/', views.LibraryDetailView),
]