from django.shortcuts import render

# Having created my book model
#To implement generic view endpoints for performing CRUD operations on the model

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer 

#ListView endpoint for retrieving all books

class ListBookAPiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


#DetailView endpoint for retrieving a single book by id
class DetailBookAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'

#CreateView for adding a new book
class CreateBookAPIView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


#UpdateView for modifying existing view
class UpdateBookAPIView(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'

#DeleteView for removing an existing book
class DeleteBookAPIView(generics.RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'