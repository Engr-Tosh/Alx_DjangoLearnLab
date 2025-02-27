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
        ('admin', 'Admin'),
        ('member', 'Member'),
        ('librarian', 'Librarian')
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
        UserProfile.objects.create(instance)
        return f"UserProfile automatically created for {instance}"
