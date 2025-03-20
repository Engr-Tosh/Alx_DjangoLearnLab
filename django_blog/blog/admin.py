from django.contrib import admin
from .models import UserProfile, Post

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Post)

"""
It's not strictly necessary for every model to appear in the admin panel.
 if you want a quick way to view your data during development, registering the model in the admin can be very useful
"""