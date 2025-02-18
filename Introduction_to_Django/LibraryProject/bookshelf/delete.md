#Deleting records from the database
>>> remove_book = Book.objects.get(id=1)       
>>> remove_book.delete()
(1, {'bookshelf.Book': 1})
>>> print(all_books)   
<QuerySet []>