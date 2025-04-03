from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
class Notification(models.Model):
    """
    This model represents notifications for actions performed by users,
    such as liking a post, commenting on a post, following/unfollowing a user, etc.
    """
    NOTIFICATION_ACTION_CHOICES = [
        ("LIKE", "like"),
        ("UNLIKE", "unlike")
        ("COMMENT", "comment"),
        ("FOLLOW", "follow"),
        ("UNFOLLOW", "unfollow"),
    ]
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notifications")
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="actions")
    verb = models.CharField(max_length=100, choices=NOTIFICATION_ACTION_CHOICES)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    target = GenericForeignKey("content_type", "object_id")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification {self.verb} by {self.actor} for {self.recipient} on {self.timestamp}"