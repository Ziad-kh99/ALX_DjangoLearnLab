from django.contrib.auth.decorators import user_passes_test

def is_member(user):
    return user.is_authenticated and user.role == 'member'

@user_passes_test(is_member, login_url='/login')
def member(request):
    pass 
