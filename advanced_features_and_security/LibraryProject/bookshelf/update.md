#Updating a record in the database
>>> update_book = Book.objects.get(id=1) 
>>> update_book.title = "Nineteen Eighty-Four"
>>> update_book.save()
<QuerySet [<Book: Nineteen Eighty-Four by George Orwell>]> #Updated title