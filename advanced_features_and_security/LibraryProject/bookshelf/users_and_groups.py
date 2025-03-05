from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Book

group, created = Group.objects.get_or_create(name='Editors')

content_type = ContentType.objects.get_for_model(Book)

can_create_book = Permission.objects.get(
    codename = 'can_create',
    content_type=content_type
)

can_edit_book = Permission.objects.get(
    codename='can_edit', 
    content_type=content_type
)

group.permissions.add(can_create_book, can_edit_book)
group.save()
