from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm      
from django.urls import path, reverse_lazy
from django.views.generic import CreateView
from .models import Library, Book, UserProfile
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.views import View
from .admin_view import Admin
from django.contrib.auth.decorators import user_passes_test, permission_required

#The first task is to list all the books stored in the database
#Call model from the models.py module and import modules for class based view subclassing

def list_books(request):
    """This function based view will retrieve all books and 
    render it via a template displaying the list"""
    
    books = Book.objects.all()                  #Fetches all book instances from the db
    context = {'book_list': books}              #Creates a dict to hold the list with key book_list
    return render(request, 'relationship_app/list_books.html', context)


"""class based view that displays details for,
 a specific library and lists all the books in that library"""
class LibraryDetailView(DetailView):
    #A class to display the details of a specific Library
    model = Library
    template_name = 'relationship_app/library_detail.html'


"""Implementing user authentication views in django"""
#Class based view that Handles User registration
class register(CreateView):
    model = User
    form_class = UserCreationForm()       #Creates a view class for user registration
    success_url = reverse_lazy('login')     #Page to redirect to after the registration is successful
    template_name = 'relationship_app/register.html'

"""Create a custom LogoutView which inherits from views in django.view
Being that the Built in LogoutView doesn't accept get request"""
class LogoutView(View):
    template_name = ""              #FUnction variable to store the template location
    def get(self, request):
        logout(request)         #logouts user 
        return render(request, self.template_name)      #displays the logout the logout page after user has been logged out
    
from django.contrib.auth.decorators import user_passes_test

def role_check(user):
    try:
        logged_in_user = UserProfile.objects.get(user=user)     #Gets the logged in user
        user_role = logged_in_user.role                 #Gets user instance role

        match user_role:
            case "Admin" | "Librarians" | "Member":     
                return True                                  #Checks if the user has the role                           
            case _:
                return False               

    except UserProfile.DoesNotExist:
        return False

@user_passes_test(role_check)
def Admin(request):
    return(request, "relationship_app/admin_view.html")

@user_passes_test(role_check)
def Librarians(request):
    return(request, "relationship_app/librarian_view.html")

@user_passes_test(role_check)
def Member(request):
    return(request, 'relationship_app/member_view.html')


"""Task 4: implement permission checks to handle crud operations"""
def get_book_list():
    return Book.objects.all()

#Permission for a user to create book
@permission_required('relationship_app.can_add_book')
def add_book(request):
    book = Book.objects.create()
    book.save()
    context = {"book_list": get_book_list()}
    return render(request, "relationship_app/list_book.html", context)

#Permission to delete book
@permission_required('relationship_app.can_delete_book')
def delete(request):
    book = Book.objects.get(id=None)       #Fetches the book instance to be deleted
    book.delete()       #Deletes the book
    context = {"book_list": get_book_list()}
    return render(request, "relationship_app/list_book.html", context)

#Permission to edit/change book
@permission_required("relationship_app.can_change_book")
def edit(request);
    book = Book.objects.get(id=None)
    book.title = None
    book.author = None
    book.save()
    context = {"book_list": get_book_list()}
    return render(request, "relationship_app/list_book.html", context)
    