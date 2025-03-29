from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import Post, Comment
from .permissions import IsAuthorOrReadOnly
from .serializers import (
    PostSerializer,
    CommentSerializer,
)

"""Views for CRUD operations"""
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]