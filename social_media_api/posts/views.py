from django.shortcuts import render
from rest_framework import viewsets
from .models import Post, Comment
from .serializers import (
    PostSerializer,
    CommentSerializer,
)

"""Views for CRUD operations"""
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related("author")
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.select_related("post", "author")
    serializer_class = CommentSerializer