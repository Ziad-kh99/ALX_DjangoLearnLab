from django.urls import path
from .views import BookList, BookDetail, BookCreate, BookUpdate, BookDelete

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('books/create', BookCreate.as_view(), name='book-create'),
    path('books/update/', BookDetail.as_view(), name='book-update'),
    path('books/delete/', BookDelete.as_view(), name='book-delete'),
]

