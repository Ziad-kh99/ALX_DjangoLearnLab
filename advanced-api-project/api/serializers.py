from rest_framework import serializers
from .models import Book, Author
import datetime
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    def validate(self, data):
        current_year = datetime.date.today().year
        if data['publication_year'] > current_year:
            raise serializers.ValidationError('Publication year should be at most this year.')
        return data
    

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name']

     