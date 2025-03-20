from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

"""Setting up User Authentication Views"""

class SignUpView(CreateView):
    """Implementing user registration view"""
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('login')     #Redirects to the login page after successfully creating user
    template_name = 'blog/register.html'        #template to use for registration


#Implementing the logout view via CBV which is called from Django built in views
class LogoutView(View):
    template_name=""

    """Logout view would display this view when the user logs out"""
    def get(self, request):     #Remember a view takes an http request and returns a response
        logout(request)         #Logs Out a User
        return render(request, self.template_name)      #Returns this page after a user is logged out.
    
#Implementing user profile view

class ProfileView(LoginRequiredMixin, View):
    template_name =  "blog/profile.html"

    
    def get(self, request):
        user= request.user      #To get the the particular view for the current user
        context = {"user": user}
        return render(request, self.template_name, context)
    
    
    def post(self, request):
        user = request.user
        updated_email = request.POST.get("email")       #gets email from form input i.e the user input

        if updated_email:
            user.email = updated_email      #if a new mail is provided, update.
            user.save()
        return redirect(reverse_lazy("profile"))      #redirects to the profile page after update
    
    

# """"Home Page View"""
# class HomeView(TemplateView): 
#     model = User
#     template_name = ""

