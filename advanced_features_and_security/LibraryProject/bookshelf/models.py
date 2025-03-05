from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()

from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, date_of_birth, profile_photo):
        user = self.model(username=username, date_of_birth=date_of_birth, profile_photo=profile_photo)
        user = set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, password, date_of_birth, profile_photo):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fileds.setdefault('is_active', True)

        return self.create_user(username, password, date_of_birth, profile_photo)


class Author(models.Model):
    name = models.CharField(150)


class Book(models.Model):
    title = models.CharField(max_length=250)
    pages_no = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
   
    class Meta():
        permissions = [
            ('can_view', 'Can view a book'),
            ('can_create', 'Can create a book'),
            ('can_edit', 'Can edit a book'),
            ('can_delete', 'Can delete a book')
        ]
