from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import path, reverse_lazy
from django.views.generic import CreateView
from .models import Library, Book
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.
#The first task is to list all the books stored in the database
#Call model from the models.py module and import modules for class based view subclassing

def list_books(request):
    """This function will retrieve all books and render it via a template displaying the list"""
    books = Book.objects.all()  #Fetches all book instances from the db
    context = {'book_list': books}  #Creates a dict to hold the list with key book_list
    return render(request, 'relationship_app/list_books.html', context)

#Now to implement a class based view
#class based view that displays details for a specific library and lists all the books in that library
class LibraryDetailView(DetailView):
    """A class to display the details of a specific Library"""
    model = Library
    template_name = 'relationship_app/library_detail.html'


"""Implementing user authentication views in django"""
#Class based view that Handles User registration
class register(CreateView):
    model = User
    form_class = UserCreationForm       #Creates a view class for user registration
    success_url = reverse_lazy('login')     #Page to redigrect to after the registration is successful
    template_name = 'registration/register.html'

def custom_logout(request):
    logout(request)
    return redirect('login')
    