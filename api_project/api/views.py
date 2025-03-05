from django.shortcuts import render

"""Creating the view for my first API Endpoint"""
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

#Now to define the view
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

"""Adding a viewset that would extend the existing BookList view"""
class BookViewSet(BookList, viewsets.ModelViewSet):
    pass