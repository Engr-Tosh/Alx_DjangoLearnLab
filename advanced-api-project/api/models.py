from django.db import models

# Create your models here.

#Create two models, Author and Book.
#Author model rpr book authors which defualt to unknown, if not provided 
class Author(models.Model):
    name = models.CharField(max_length=255, default="Unknown")

#Book model rpr books in the system
#Each book is associated with an author
#The one to many relationship via the foreign key establishes that many books can be associated with a single author
class Book(models.Model):
    title = models.CharField(max_length=255, default="Unknown")
    publication_year = models.IntegerField(default=0000)

    #Establishes foreignkey relationshipwit the author model
    #on_delete ensures that if an author is deleted, their associated books are also removed
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")