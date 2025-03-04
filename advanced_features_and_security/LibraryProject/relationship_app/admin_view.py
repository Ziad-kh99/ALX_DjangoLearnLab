from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

def is_admin(user):
    return user.is_authenticated and user.role == 'admin'

@user_passes_test(is_admin, login_url='/login')
def admin(request):
    return HttpResponse('I am sure that you are librarian.') 

