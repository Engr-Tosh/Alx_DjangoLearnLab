#App's "api" Urls go here

from django.urls import path
from .views import BookList

#include the path to the book list api view 
urlpatterns = [
    path("books/", BookList.as_view(), name="book-list"),
]