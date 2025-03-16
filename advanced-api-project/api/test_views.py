from rest_framework.test import APIRequestFactory
from rest_framework import status
from django.test import TestCase
from .models import Book
from .views import BookListView


class BookAPITestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.book = Book.objects.create(title='Book1', publication_year=1958)

    def test_list_books(self):
        view = BookListView.as_view()({'get': 'retrive'})
        request = self.factory.get(f'/books/{self.book.id}/')
        response = view(request, pk=self.book.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], '1958')

# self.client.login
        