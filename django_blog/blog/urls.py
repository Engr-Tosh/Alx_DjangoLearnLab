from django.urls import path, include
from .views import SignUpView, LogoutView
from django.contrib.auth.views import LoginView
from . import views


urlpatterns = [
    path("register/", SignUpView.as_view(), name="register"),
    path("login/", LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="blog/logout.html"), name="logout-user"),
    path("profile/", views.profile_view, name="profile")
]