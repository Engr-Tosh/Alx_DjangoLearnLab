import relationship_app.models


#query all books by a specific author, that is to get all books by a particular author.

#list all books in the library
books = Library.objects.get(name=library_name)
books.all()