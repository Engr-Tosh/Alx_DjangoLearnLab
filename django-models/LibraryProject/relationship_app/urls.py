from django.urls import path
from . import views 
from .views import list_books 

urlpatterns = [
    path('book_list', views.list_books, name ='Available books'),
    path('library_details', views.LibraryDetailView.as_view(), name= 'details')
]