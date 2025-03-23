from django.urls import path
from django.contrib.auth import views as auth_views
from blog import views as user_views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentListView, CommentCreateView, CommentUpdateView, CommentDeleteView



urlpatterns = [
    path('', user_views.home, name='home'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),

    path('post/', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('post/<int:pk>/comments/list', CommentListView.as_view(), name='comment-list'),
    path('post/<int:pk>/comments/add', CommentCreateView.as_view(), name='comment-create'),
    path('post/<int:pk>/comments/<int:comment_pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('post/<int:pk>/comments/<int:comment_pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]