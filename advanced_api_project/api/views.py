from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer


class ListView (generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DetialView (generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CreateView (generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class UpdateView (generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


