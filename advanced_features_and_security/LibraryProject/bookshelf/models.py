from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200, default="Unknown")
    author = models.CharField(max_length=100, default="Unknown")
    publication_year = models.IntegerField(default=2024)

    def __str__(self):
        return f"{self.title} by {self.author}"
    

    """Implementing a custom user model in django"""
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(default=date.today, null=True)
    profile_photo = models.ImageField(default="default.jpg", null=True)