from rest_framework import permissions, pagination, viewsets, generics
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
    pagination_class = PostCommentPagination
    filter_backends = [SearchFilter]
    search_fields = ["title", "author__username"]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
    pagination_class = [PostCommentPagination]
    filter_backends = [SearchFilter]
    search_fields = ["author"]


"""Implementing the feed functionality"""
class PostFeedView(generics.ListAPIView):
    """Feeds of posts from the users the current logged-in user is following"""
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = PostCommentPagination

    def get_queryset(self):
        following_users = self.request.user.following.all()  # Fetches all the users being followed
        return Post.objects.filter(author__in=following_users).order_by("-created_at")   # Shows the most reent posts of those users 

        