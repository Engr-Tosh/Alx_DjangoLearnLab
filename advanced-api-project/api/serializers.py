#serializers go here

from rest_framework import serializers
from .models import Book, Author

#Book model serializer
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "author", "publication_year"]

        #Custom validation to ensure publication_year is not in the future
        def validate(self, data):
            if data['publication_year'] > 2025:
                raise serializers.ValidationError("That's a future date")
            
#Author model serializer
class AuthorSerializer(serializers.ModelSerializer):
    book = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Author
        fields = ["name", "book"]