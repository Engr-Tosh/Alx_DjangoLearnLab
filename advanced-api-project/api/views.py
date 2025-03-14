from django.shortcuts import render

# Having created my book model
#To implement generic view endpoints for performing CRUD operations on the model

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer 

#ListView endpoint for retrieving all books

class BookListAPiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer