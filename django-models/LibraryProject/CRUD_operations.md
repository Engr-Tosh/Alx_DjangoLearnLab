#Creating a record in the database
from bookshelf.models import Book 
>>> bk1 = Book(title="1984", author="George Orwell", publication_
year=1949)
>>> bk1.save()  
<QuerySet [<Book: 1984 by George Orwell>]> #Book object created 


#Retreiving data from the database: 
>>> all_books = Book.objects.all()   
>>> print(all_books)
<QuerySet [<Book: 1984 by George Orwell>]>  #Retrieved all books

#Updating a record in the database
>>> update_book = Book.objects.get(id=1) 
>>> update_book.title = "Nineteen Eighty-Four"
>>> update_book.save()
<QuerySet [<Book: Nineteen Eighty-Four by George Orwell>]> #Updated title

#Deleting records from the database
>>> remove_book = Book.objects.get(id=1)       
>>> remove_book.delete()
(1, {'bookshelf.Book': 1})
>>> print(all_books)   
<QuerySet []>