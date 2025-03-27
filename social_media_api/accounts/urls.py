from django.shortcuts import render
from django.urls import path
from .views import (
    UserRegisterView,
    UserLoginView,
    UserProfileView
)
from rest_framework.authtoken import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('profile/', UserProfileView.as_view(), name="profile")

]