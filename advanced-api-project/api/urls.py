"""The routes to view endpoints goes here"""

from django.urls import path, include
from .views import (
    ListBookAPIView,
    DetailBookAPIView,
    CreateBookAPIView,
    UpdateBookAPIView,
    DeleteBookAPIView
)

urlpatterns = [
    path("books/", ListBookAPIView.as_view(), name="book-list"),
    path("books/details/<int:pk>/", DetailBookAPIView.as_view(), name="book-details"),
    path("books/create/", CreateBookAPIView.as_view(), name="book-create"),
    path("books/update/<int:pk>/", UpdateBookAPIView.as_view(), name="books-update"),
    path("books/delete/<int:pk>/", DeleteBookAPIView.as_view(), name="book-delete"),
]