#serializers go here

from rest_framework import serializers
from .models import Book

#Book model serializer
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "author", "publication_year"]