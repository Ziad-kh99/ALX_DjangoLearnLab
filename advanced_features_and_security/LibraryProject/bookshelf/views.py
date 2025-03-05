from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required

@permission_required('bookshelf.can_view')
def book_list(request):
    return HttpResponse('List all books')

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    return HttpResponse('You can create book')

