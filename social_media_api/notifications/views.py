from rest_framework import generics, permissions, pagination
from .models import Notification
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

class pagenumbers(pagination.PageNumberPagination):
    page_size = 10

"""Implementing Notification System"""

class NotificationAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = pagenumbers
    
    """
    Fetch the notification for authenticated user
    """        
    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user)
    
# Helper function to create notification
def create(actor, recipient, verb, target):     # create the notification
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