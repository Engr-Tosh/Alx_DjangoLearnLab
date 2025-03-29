from rest_framework import permissions, pagination, viewsets
from .models import Post, Comment
from .permissions import IsAuthorOrReadOnly
from .serializers import (
    PostSerializer,
    CommentSerializer,
)
from rest_framework.filters import SearchFilter
# Applying pagination
class PostCommentPagination(pagination.PageNumberPagination):
    page_size = 10
   

"""Views for CRUD operations"""
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
    pagination_class = [PostCommentPagination]
    filter_backends = [SearchFilter]
    search_fields = ["title", "author__username"]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
    pagination_class = [PostCommentPagination]
    filter_backends = [SearchFilter]
    search_fields = ["author"]
