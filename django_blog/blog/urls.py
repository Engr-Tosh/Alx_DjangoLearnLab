from django.urls import path, include
from .views import SignUpView, LogoutView, ProfileView
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # path("home/", HomeView.as_view(template_name="blog/base.html"), name="home"),
    path("register/", SignUpView.as_view(), name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="blog/logout.html"), name="logout"),
    path("profile/", ProfileView.as_view(template_name="blog/profile.html"), name="profile"),
    
]