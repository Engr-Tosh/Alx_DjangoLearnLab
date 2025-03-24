from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Tables/Models for my blog application

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")         #The related name ensures orm
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(blank=True, upload_to="")

    def __str__(self):
        return self.user.username
    

class Post(models.Model):
    title = models.CharField(max_length=200, default="")
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_author")


"""Adding comment functionality to bog post"""
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comment")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_author")
    content = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()