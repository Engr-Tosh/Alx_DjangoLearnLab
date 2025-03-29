"""Custom permission to ensure only the author of a post or a comment can delete or edit it"""
import logging
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

logger = logging.getLogger(__name__)

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Allows only the author to update or delete 
    their post/comment
    Allows every other person to read only
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if obj.author != request.user:
            logger.warning(f"Unauthorized edit/delete attempt by {request.user} on {obj}")
            raise PermissionDenied("You do not have permission to modify this content.")
        
        return obj.author == request.user
    
    

