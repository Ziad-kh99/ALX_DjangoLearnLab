from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class BookList(ListView):
    model = Book
class BookDetail(DetailView):
    model = Book
class BookCreate(CreateView):
    model = Book
class BookUpdate(UpdateView):
    model = Book
class BookDelete(DeleteView):
    model = Book

