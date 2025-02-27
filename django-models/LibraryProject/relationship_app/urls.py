from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books
from .views import LibraryDetailView, SignUpView
# views.register


urlpatterns = [
    path('listbooks/', list_books), 
    path('librarydetails/', LibraryDetailView.as_view(template_name='relationship_app/library_detail.html')),
    path('register/', SignUpView.as_view(template_name='relationship_app/register.html'), name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]