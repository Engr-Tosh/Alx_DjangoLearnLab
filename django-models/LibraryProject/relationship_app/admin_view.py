from django.shortcuts import render, redirect
from django.views import View
from .models import UserProfile
from django.contrib.auth.decorators import login_required, user_passes_test

def role_check(user):           #function to check user role to be passed to the user_passes_test decorator
    try:
        logged_in_user = UserProfile.objects.get(user=user)
        user_role = logged_in_user.role
        if user_role == 'admin':
            return True
        else:
            return False
    except UserProfile.DoesNotExist:
        return False

@user_passes_test(role_check, )
class AdminView(View):
    template_name = ""    
    def get(self, request):
        return render(request, self.template_name)