from django.shortcuts import render

# Having created my book model
#To implement generic view endpoints for performing CRUD operations on the model

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer 
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

#ListView endpoint for retrieving all books

class ListBookAPiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
 

#DetailView endpoint for retrieving a single book by id
class DetailBookAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticatedOrReadOnly]

#CreateView for adding a new book
class CreateBookAPIView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = IsAuthenticated


#UpdateView for modifying existing view
class UpdateBookAPIView(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'
    permission_classes = IsAuthenticated

#DeleteView for removing an existing book
class DeleteBookAPIView(generics.RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]