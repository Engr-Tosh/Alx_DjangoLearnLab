#Creating a record in the database
from bookshelf.models import Book 
>>> bk1 = Book(title="1984", author="George Orwell", publication_
year=1949)
>>> bk1.save()  
<QuerySet [<Book: 1984 by George Orwell>]> #Book object created 