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