# Serializers go here
from django.db import models
from rest_framework import serializers
from .models import Book, Author

# Book model serializer
# The BookSerializer is responsible for converting the Book model instances
# into JSON format and vice versa. It includes all relevant fields of the model.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "author", "publication_year"]

        #Custom validation to ensure publication_year is not in the future
        def validate(self, data):
            if data['publication_year'] > 2025:
                raise serializers.ValidationError("That's a future date")
            return data
            

# Author model serializer
# The AuthorSerializer serializes the Author model.
# It includes a nested representation of books written by the author.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Author
        fields = ["name", "books"]