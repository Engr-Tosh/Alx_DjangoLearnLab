from django.shortcuts import render

# Having created my book model
#To implement generic view endpoints for performing CRUD operations on the model
#Import necessary modules

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer 
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework as filter 
from rest_framework import filters 

#ListView endpoint for retrieving all books
class ListBookAPIView(generics.ListAPIView):
    """API endpoint to retrieve a list a books.
    
    Attribute:
        Queryset (queryset): All instances of the Book model.
        serializer_class (serializer): Serializer class for Book model
        permission_classes (list): Permission classes required to access the view.
        
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filter.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author']   
    ordering_fields = ['title', 'publication_year']

#DetailView endpoint for retrieving a single book by id
class DetailBookAPIView(generics.RetrieveAPIView):
    """API endpoint to retrieve details of a single book by the id.
    
    Attribute:
        Queryset (queryset): All instances of the Book model.
        serializer_class (serializer): Serializer class for Book model
        permission_classes (list): Permission classes required to access the view.
        look_up_field (str): Field that's used to retrieve a single book by its primary key
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticatedOrReadOnly]

#CreateView for adding a new book
class CreateBookAPIView(generics.CreateAPIView):
    """
    API endpoint to create a new book.

    Attributes:
        queryset (QuerySet): All instances of Book model.
        serializer_class (Serializer): Serializer class for Book model.
        permission_classes (list): Permission classes required for view.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


#UpdateView for modifying existing view
class UpdateBookAPIView(generics.RetrieveUpdateAPIView):
    """
    API endpoint to update details of an existing book.

    Attributes:
        queryset (QuerySet): All instances of Book model.
        serializer_class (Serializer): Serializer class for Book model.
        lookup_field (str): Field used to retrieve a single book by its primary key.
        permission_classes (list): Permission classes required for view.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]

#DeleteView for removing an existing book
class DeleteBookAPIView(generics.RetrieveDestroyAPIView):
    """
    API endpoint to delete an existing book.

    Attributes:
        queryset (QuerySet): All instances of Book model.
        serializer_class (Serializer): Serializer class for Book model.
        lookup_field (str): Field used to retrieve a single book by its primary key.
        permission_classes (list): Permission classes required for view.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]