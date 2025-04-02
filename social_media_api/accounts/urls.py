from django.shortcuts import render
from django.urls import path
from .views import (
    UserRegisterView,
    UserLoginView,
    UserProfileView,
    FollowersAPIView
)


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('profile/', UserProfileView.as_view(), name="profile"),
    path('follow/<int:user_id>/', FollowersAPIView, name='follow'),
    path('unfollow/<int:user_id>/', FollowersAPIView.as_view(), name="unfollow")

]