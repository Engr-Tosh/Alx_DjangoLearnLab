from django.contrib import admin
from .models import Book, CustomUser

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('title', 'author')
    search_fields = ('title', 'author')

"""Integrating custom user model into admin by adding 
custom Model admin class that includes config 
for the additional field os the model"""
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('date_of_birth', 'profile_photo')


admin.site.register(Book, BookAdmin)

#Register the the custom user admin
admin.site.register(CustomUser, CustomUserAdmin)