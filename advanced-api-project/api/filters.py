import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    publication_year = django_filters.NumberFilter(lookup_expr='icontains')
    
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']