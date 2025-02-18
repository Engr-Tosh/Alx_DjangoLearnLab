#Deleting records from the database
Book.objects.delete(id=1)       
(1, {'bookshelf.Book': 1})
print(all_books)   
<QuerySet []>