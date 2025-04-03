from rest_framework import permissions, pagination, viewsets, generics, status
from rest_framework.response import Response
from .models import Post, Comment, Like
from .permissions import IsAuthorOrReadOnly
from .serializers import (
    PostSerializer,
    CommentSerializer,
)
from rest_framework.filters import SearchFilter
from notifications.models import Notification 

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
    pagination_class = PostCommentPagination
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

# View to handle a user liking a post
class LikePostAPIView(generics.GenericAPIView):
    """Handles when a user likes a post"""
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        """
        Like a post
        """

        pk = request.data.get("post_pk")

        if not pk:
            return Response({"error": "Post ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        post = generics.get_object_or_404(Post, pk=pk)

        like_instance, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            Notification.objects.create(
                actor= request.user,
                recipient= post.user,
                verb= "like",
                target = post
            )
            return Response({"Message": "Liked a post",}, status=status.HTTP_201_CREATED)

        return Response({"message": "You have already liked this post"}, status=status.HTTP_400_BAD_REQUEST)

# When a user unlikes a post
class UnlikePostAPIView(generics.GenericAPIView):
    """
    Unlikes a post
    """
    def post(self, request, *args, **kwargs):
        pk = request.data.get("post_pk")

        if not pk:
            return Response({"error": "Post ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        post = generics.get_object_or_404(Post, pk=pk)     

        like_instance = Like.objects.filter(user=request.user, post=post).first()

        if like_instance:
            like_instance.delete()
            return Response({"Message": "Post unliked succesfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "You have not liked this post"}, status=status.HTTP_400_BAD_REQUEST)