#App's "api" Urls go here

from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
#register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

#include the path to the book list api view 
urlpatterns = [
    #Route for Booklist view
    path("books/", BookList.as_view(), name="book-list"),

    #router for the BookViewSet(all CRUD operations)
    path('', include(router.urls)),

    #Path/route for obtaining auth tokens
    path("user-authtoken/", views.obtain_auth_token),
]