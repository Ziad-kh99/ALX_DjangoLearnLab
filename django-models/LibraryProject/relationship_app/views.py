from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Book
from .models import Library
from django.contrib.auth import login
from django.contrib.auth.decorators import permission_required


def list_books(request):
    books = Book.objects.all()

    return render(request, 'relationship_app/list_books.html', books)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    library_name = 'Lib 1'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = Library.objects.filter(name = self.library_name)


class SignUpView(CreateView):
    form_class = UserCreationForm()
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

class register:
    pass

