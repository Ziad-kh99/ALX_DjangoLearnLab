from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, ProfileUpdateform, UserUpdateForm, PostCreateForm, PostUpdateForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from django.views.generic.edit import CreateView, UpdateView
from .models import Post, Comment
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404


def home(request):
    return render(request, 'blog/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login.')
            return redirect('home')
    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }

    return render(request, 'blog/register.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateform(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated.')
            return redirect('profile')
        
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateform(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'blog/profile.html', context)

class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'    # Optional: Rename the context variable. (default = object)

class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy('post-list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request        # pass 'request' to form as an attribute.
        return kwargs

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'blog/post_update.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post-list')
    context_object_name = 'post'

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

class CommentListView(ListView):
    model = Comment
    template_name = 'blog/comment_list.html'
    context_object_name = 'comments'

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return Comment.objects.filter(post=post)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk=self.kwargs['pk'])
        return context

class CommentCreateView(LoginRequiredMixin,CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.post = post
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['pk']})
    
class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_update.html'

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user
    
    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.pk})

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'blog/comment_delete.html'

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user
    
    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.pk})







