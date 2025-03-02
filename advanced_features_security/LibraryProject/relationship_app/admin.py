from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

#Registering my models with the default UserAdmin
admin.site.register(CustomUser, UserAdmin)