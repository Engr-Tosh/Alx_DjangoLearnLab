from django.urls import path
from .views import list_books 

urlpatterns = [
    path('book_list', views.book_list, name ='Available books'),
    path('library_details', views.LibraryDetailView.as_view(), name= 'details')
]