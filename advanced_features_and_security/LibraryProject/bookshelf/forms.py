from .models import Book
from django import forms

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description']

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'pages_no']
