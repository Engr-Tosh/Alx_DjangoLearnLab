from django.urls import path, include
from .views import SignUpView
from django.contrib.auth.views import LoginView


urlpatterns = [
    path("register/", SignUpView.as_view(), name="register"),
    path("login/", LoginView.as_view(template_name="blog/login.html"), name="login"), 
]