from django.db import models

# Create your models here.

#Create two models, Author and Book.
class Author(models.Model):
    name = models.CharField(max_length=255, default="Unknown")

class Book(models.Model):
    title = models.CharField(max_length=255, default="Unknown")
    publication_year = models.IntegerField(default=0000)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)