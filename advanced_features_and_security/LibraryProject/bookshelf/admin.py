from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'data_of_birth', 'profile_photo')

admin.site.register(CustomUser, CustomUserAdmin)
