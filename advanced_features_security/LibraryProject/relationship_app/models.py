from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    name = models.CharField

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='authors')

    class Meta():
        permissions = [("can_add_book", "can_change_book", "can_delete_book")]      #Permissions for CRUD operations
    
    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField
    library = models.ManyToManyField(Book, related_name='books')

    def __str__(self):
        return self.name
    
class Librarian(models.Model):
    name = models.CharField
    library = models.OneToOneField(Library, on_delete=models.CASCADE)


"""Implementing role based access in django"""
"""1.Extend the user Model with with a UserProfile"""
class UserProfile(models.Model):
    #Each user role is to be given a choice.
    ROLE_CHOICES = {
        ('Admin', 'Admin'),
        ('Member', 'Member'),
        ('Librarian', 'Librarian')
    }

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(choices=ROLE_CHOICES, default='member')

    def __str__(self):
        return self.user 
    
"""Using django signals for automatic creation"""
from django.db.models.signals import post_save
from django.dispatch import receiver

"""Signal creation"""
@receiver(post_save, sender=UserProfile)        #signals that the trigger would be from this sender
def user_profile_created(sender, instance, created, **kwargs)
    if created:
        UserProfile.objects.create(instance=sender)
        return f"UserProfile automatically created for {instance}"


"""Creating/Immplementing custom user models"""
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    date_of_birth = models.DateField
    profile_photo = models.ImageField

    #custom functions to implement
    def create_user(self, date_of_birth, profile_photo, **extra_fields)
        user = self.model(date_of_birth=date_of_birth, profile_photo=profile_photo, **extra_fields)
        return user
    
    def create_superuser(self, date_of_birth, profile_photo, **extra_fields):
        """Creates and returns a superuser with admin privileges"""

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(date_of_birth, profile_photo, **extra_fields)

