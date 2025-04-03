from rest_framework import generics, permissions, pagination
from .models import Notification
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import status
from posts.models import Post, Like

User = get_user_model()

class pagenumbers(pagination.PageNumberPagination):
    page_size = 10

"""Implementing Notification System"""

# Helper function to create notification
def create(self, actor, recipient, verb, target):     # create the notification
    """
    Helper function to create a notification.
    """
    content_type = ContentType.objects.get_for_model(target)  # Get content type of target model
    
    notification = Notification.objects.create(
        recipient = recipient,
        verb = verb,
        actor = actor,
        target = target,
        content_type = content_type,
        object_id = target.id
    )
        
    return notification

class NotificationAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = pagenumbers
    
    # Handles actions that trigger notifications
    def post(self, request, *args, **kwargs):
        """
        Handle actions that trigger notifications (e.g., following, liking, commenting).
        """
        verb = request.data.get("verb")
        target_user_id = request.data.get("target_user_id")
        actor = request.user

        if not verb or not target_user_id:
            return Response({"error": "Missing Required Fields"}, status=status.HTTP_400_BAD_REQUEST)

        target_user = generics.get_object_or_404(User, id=target_user_id)
                
        if verb == "follow":
            if actor == target_user:
                return Response({"error": "You cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)

            notification = self.create_notification(
                actor = actor,
                recipient = target_user,
                verb = "follow",
                target = target_user
            )
            return Response({"Message": "Notification sent", "Notification": str(notification)}, status=status.HTTP_201_CREATED)
        
        
        # Unliking
        if verb == "unlike":
            pk = request.data.get("post_pk")
            post = generics.get_object_or_404(Post, pk=pk)

            like_instance = Like.objects.filter(user=request.user, post=post).first()

            if like_instance:
                like_instance.delete()
            else:
                return Response({"error": "You have not liked this post yet"}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"error": "Invalid action"}, status=status.HTTP_400_BAD_REQUEST)
    
    # When a User unlikes a post or unfollows another user.
    