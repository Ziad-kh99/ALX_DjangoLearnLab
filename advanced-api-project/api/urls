from django.urls import path
from .views import BookList, BookDetail, BookCreate, BookUpdate, BookDelete

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('books/', BookCreate.as_view(), name='book-create'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-update'),
    path('books/<int:pk>/', BookDelete.as_view(), name='book-delete'),
]

