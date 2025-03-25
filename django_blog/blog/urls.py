from django.urls import path, include
from .views import (
    SignUpView, 
    LogoutView,
    ProfileView,
    ListPostView, 
    DetailPostView, 
    CreatePostView, 
    UpdatePostView, 
    DeletePostView,
    HomeView,
    CommentCreateView,
    CommentUpdateView, 
    CommentDeleteView
)
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # path("home/", HomeView.as_view(template_name="blog/base.html"), name="home"),
    path("", HomeView.as_view(), name="home"),
    path("register/", SignUpView.as_view(), name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="blog/logout.html"), name="logout"),
    path("profile/", ProfileView.as_view(template_name="blog/profile.html"), name="profile"),
    path("posts/", ListPostView.as_view(), name="posts"),
    path("posts/<int:pk>/", DetailPostView.as_view(), name="post_detail"),
    path("post/new/", CreatePostView.as_view(), name="post_create"),
    path("post/<int:pk>/update/", UpdatePostView.as_view(), name="post_update"),
    path("post/<int:pk>/delete/", DeletePostView.as_view(), name="post_delete"),
    path("posts/<int:pk>/comments/new/", CommentCreateView.as_view(template_name="blog/add_comment.html"), name="comment_create"),
    path("comments/<int:pk>/edit/", CommentUpdateView.as_view(), name="comment_update"),
    path("comments/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment_delete"),
    
]