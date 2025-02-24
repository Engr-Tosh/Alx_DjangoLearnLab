from django.shortcuts import render

# Create your views here.
#The first task is to list all the books stored in the database
#Call model from the models.py module
from .models import Book

def book_list(request):
    """This function will retrieve all books and render it via a template displaying the list"""

    books = Book.objects.all()  #Fetches all book instances from the db
    context = {'book_list': books}  #Creates a dict to hold the list with key book_list
    return render(request, 'relationship_app/list_books.html', context)