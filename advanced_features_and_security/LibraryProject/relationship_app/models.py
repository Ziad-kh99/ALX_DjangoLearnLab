from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length = 100)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)

    class Meta():
        permissions = [
            ('can_add_book', 'can add book'),
            ('can_change_book', 'can change book'),
            ('can_delete_book', 'can delete book')
        ]

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length = 100)
    books = models.ManyToManyField(Book)
    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length = 100)
    library = models.OneToOneField(Library, on_delete = models.PROTECT)
    def __str__(self):
        return self.name


class UserProfile(models.Model):
    ROLES = [
        ('admin', 'Admin'),
        ('author', 'Author'),
        ('librarian', 'Librarian'),
        ('member', 'Member')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(
            max_length=100,
            choices= ROLES,
            default='customer'
        )
