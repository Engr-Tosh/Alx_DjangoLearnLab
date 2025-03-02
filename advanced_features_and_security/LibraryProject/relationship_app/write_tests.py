"""I want to creaat a function that to pass to te user_passes_test decorator
"""
#This function should accept a user object as parameter
from .models import UserProfile
from django.contrib.auth.decorators import login_required


def role_check(user):
    try:
        logged_in_user = UserProfile.objects.get(user=user)
        user_role = logged_in_user.role
        if user_role == 'admin':
            return True
        else:
            return False
    except UserProfile.DoesNotExist:
        return False
        
    
