from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

def is_librarian(user):
    return user.is_authenticated and user.role == 'librarian'

@user_passes_test(is_librarian, login_url='/login')
def librarian(request):
    return HttpResponse('I am sure that you are librarian.')
