from django.contrib import admin
from .models import Book, CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('title', 'author')
    search_fields = ('title', 'author')

"""CustomAdmin class creation"""
class CustomUserAdmin(UserAdmin):
    """Configurations for additional fields"""
    list_display = ('email', 'username', 'password', 'date_of_birth', 'profile_photo')
    list_filter = ('email', 'username')
    search_fields = ('email', 'username')

admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)