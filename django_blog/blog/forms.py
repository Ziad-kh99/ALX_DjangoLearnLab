from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post, Comment


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']



class PostCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)      # pop request from kwargs.
        super().__init__(*args, **kwargs)
    class Meta:
        model = Post
        fields = ['title', 'content']
    
    def save(self, commit=True):
        post = super().save(commit=False)   # Create the object, but don't save yet.
        post.author = self.request.user     # Assign the logged-in user.
        if commit:
            post.save()                     # Now, save the object.
        return post 

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ['content']