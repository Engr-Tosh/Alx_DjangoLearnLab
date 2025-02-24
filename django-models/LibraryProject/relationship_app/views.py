from django.shortcuts import render

# Create your views here.
#The first task is to list all the books stored in the database
#Call model from the models.py module and import modules for class based view subclassing

from .models import Library, Book
from django.views.generic import DetailView

def book_list(request):
    """This function will retrieve all books and render it via a template displaying the list"""

    books = Book.objects.all()  #Fetches all book instances from the db
    context = {'book_list': books}  #Creates a dict to hold the list with key book_list
    return render(request, 'relationship_app/list_books.html', context)

#Now to implement a class based view
#class based view that displays details for a specific library and lists all the books in that library

class LibraryDetailView(DetailView):
    """A class to display the details of a specific book"""
    model = Library
    template_name = 'relationship_app/library_detail.html'
   
    