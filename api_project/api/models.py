from django.db import models

"""Creating a basic model for my api"""
class Book(models.Model):
    title = models.CharField(max_length=255, default="Unknown")
    author = models.CharField(max_length=255, default="Unknown")
