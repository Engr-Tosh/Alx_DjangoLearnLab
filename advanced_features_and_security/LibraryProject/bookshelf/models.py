from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField(default=2024)

    def __str__(self):
        return f"{self.title} by {self.author}"
    
"""Creating cutom User models"""
class CustomUser(AbstractUser):
    date_of_birth = models.DateField
    profile_photo = models.ImageField


"""Creating the custom user manager to handle user(object) creation
and querying of my custom user model"""
class CustomUserManager(BaseUserManager):
    def create_user(self, email, username=None, password=None, date_of_birth, profile_photo, **extra_fields):
        user = self.model(email, username, password, date_of_birth, profile_photo, **extra_fields)
        user.save(using=self.db)
        return user 
    
    def create_superuser(self, email, username=None, password=None, date_of_birth, profile_photo, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, username, password, date_of_birth, profile_photo, **extra_fields)