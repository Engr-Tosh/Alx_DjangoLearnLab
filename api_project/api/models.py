from django.db import models

"""Creating a basic model for my api"""
class Book(models.Model):
    title = models.CharField
    author = models.CharField
