from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from datetime import date
from django.conf import settings    #The AUTH USER MODEL setting will be imported here

class Book(models.Model):
    title = models.CharField(max_length=200, default="Unknown")
    author = models.CharField(max_length=100, default="Unknown")
    publication_year = models.IntegerField(default=2024)

    #To ensure the association between model and user
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
    

    """Implementing a custom user model in django"""
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(default=date.today, null=True)
    profile_photo = models.ImageField(default="default.jpg", null=True)

    objects = CustomUserManager

    """Implementing custom user manager for the custom user model"""
class CustomUserManager(BaseUserManager):
    #Custom usermanager methods 

    def create_user(self, email, username=None, password=None, **extra_fields):
        """Create and return a normal user with username and password"""
        if not email:
            raise ValueError("Email field is required")
        
        email = self.normalize_email(email)     #converts the email string into lowercase
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password) #This hashes the password
        user.save(using=self._db)   #save to this paricular database incase of the use multiple databases
        return user
    
    """Creating and returning a superuser"""
    def create_superuser(self, email, username=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, username, password, **extra_fields)
    
#assigning the usermanager to the custom user
CustomUser.objects = CustomUserManager()