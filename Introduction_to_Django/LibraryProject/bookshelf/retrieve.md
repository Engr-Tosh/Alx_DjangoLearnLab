#Retreiving data from the database: 
>>> all_books = Book.objects.all()   
>>> print(all_books)
<QuerySet [<Book: 1984 by George Orwell>]>  #Retrieved all books