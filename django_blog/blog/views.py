from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
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


#Implementing the logout view via CBV which is called from Django built in views
class LogoutView(View):
    template_name=""

    """Logout view would display this view when the user logs out"""
    def get(self, request):     #Remember a view takes an http request and returns a response
        logout(request)         #Logs Out a User
        return render(request, self.template_name)      #Returns this page after a user is logged out.
    
        
#Implementing the user profile view
def profile_view(request):
    """Gets the user profile and display the profile details"""
    user = request.user
    context = {"user": user}
    return render(request, "blog/profile.html", context)


"""Step 4: Implement Profile Management
Profile Management Features:
Develop a view that allows authenticated users to view and edit their profile details. This view should handle POST requests to update user information.
Ensure the user can change their email and optionally extend the user model to include more fields like a profile picture or bio."""

#View that allows authenticated users to edit profile details
