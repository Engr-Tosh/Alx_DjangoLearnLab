#Deleting records from the database
from bookshelf.models import Book
book = Book.objects.get(id=1)
book.delete      
(1, {'bookshelf.Book': 1})
print(all_books)   
<QuerySet []>