from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .filters import BookFilter
from rest_framework import filters

class BookList(ListView):
    model = Book
    
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilter
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author', 'publication_year']
    ordering_fields = ['title', 'author', 'publication_year']


    
class BookDetail(DetailView):
    model = Book
class BookCreate(CreateView):
    model = Book
    permission-classes = [IsAuthenticated]
class BookUpdate(UpdateView):
    model = Book
class BookDelete(DeleteView):
    model = Book

