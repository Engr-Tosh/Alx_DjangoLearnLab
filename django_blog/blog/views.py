from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views import View
"""Setting up User Authentication Views"""

class SignUpView(CreateView):
    """Implementing user registration view"""
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('login')     #Redirects to the login page after successfully creating user
    template_name = 'blog/register.html'        #template to use for registration


#Implementing the login viewvia CBV which is called from Django built in views
