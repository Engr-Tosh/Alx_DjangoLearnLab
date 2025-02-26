from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm      
from django.urls import path, reverse_lazy
from django.views.generic import CreateView
from .models import Library, Book
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.contrib.auth import login, logout

#The first task is to list all the books stored in the database
#Call model from the models.py module and import modules for class based view subclassing

def list_books(request):
    """This function will retrieve all books and 
    render it via a template displaying the list"""
    
    books = Book.objects.all()                  #Fetches all book instances from the db
    context = {'book_list': books}              #Creates a dict to hold the list with key book_list
    return render(request, 'relationship_app/list_books.html', context)

#Now to implement a class based view
"""class based view that displays details for,
 a specific library and lists all the books in that library"""

class LibraryDetailView(DetailView):
    """A class to display the details of a specific Library"""
    model = Library
    template_name = 'relationship_app/library_detail.html'


"""Implementing user authentication views in django"""
#Class based view that Handles User registration
class register(CreateView):
    model = User
    form_class = UserCreationForm       #Creates a view class for user registration
    success_url = reverse_lazy('login')     #Page to redirect to after the registration is successful
    template_name = 'templates/register.html'

class LoginView(CreateView):
    def login(request):
        return render(request, "templates/login.html")

class LogoutView(CreateView):
    def logout(request):
        """Render the logout confirmation page"""
        return render(request, 'templates/logout.html')
