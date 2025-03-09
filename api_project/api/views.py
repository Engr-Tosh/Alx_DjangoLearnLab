from django.shortcuts import render

"""Creating the view for my first API Endpoint"""
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

#Now to define the view
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

"""Adding a viewset that would extend the existing BookList view"""
class BookViewSet(BookList, viewsets.ModelViewSet):
    #adding authentication and permisssion classes
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    