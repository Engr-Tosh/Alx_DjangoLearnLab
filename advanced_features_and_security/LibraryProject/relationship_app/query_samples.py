import relationship_app.models


#query all books by a specific author, that is to get all books by a particular author.
Author.objects.get(name=author_name)
objects.filter(author=author)

#list all books in the library
books = Library.objects.get(name=library_name)
books.all()

#Retrieve the librarian for a library
Librarian.objects.get(library="")