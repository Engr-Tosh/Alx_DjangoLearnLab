from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import (
    View,
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView,  
    DeleteView,
    TemplateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .forms import PostCreateForm

"""Setting up blog home page"""
class HomeView(TemplateView):
    template_name = "blog/home.html"


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

        if request.method == "POST":
            updated_email = request.POST.get("email")       #gets email from form input i.e the user input

            if updated_email:
                user.email = updated_email      #if a new mail is provided, update.
                user.save()
        return redirect("profile")     #redirects to the profile page after update
    
    


"""
Creating blog Post Management features
"""

#Implement CRUD operations
#I have created the form and also created the template to render 
class ListPostView(ListView):
    """View to display all blog posts"""
    model = Post
    template_name = "blog/listview.html"
    context_object_name = "posts"

class DetailPostView(DetailView):
    """View to show individual blog post"""
    model = Post
    template_name = "blog/detailview.html"
    context_object_name = "post"

class CreatePostView(LoginRequiredMixin, CreateView):   #Ensures only authenticated users can create a post
    """View to allow blog posts creation"""
    model = Post
    template_name = "blog/createview.html"
    form_class = PostCreateForm
    success_url = reverse_lazy("posts")

    #Ensuring logged in user is the post author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  
    """View to show individual blog posts"""
    model = Post
    template_name = "blog/updateview.html"
    fields = ["title", "content"]
    context_object_name = "post"
    success_url = reverse_lazy("posts")

    """A test function to ensure it is the required user that can perform this view function"""
    def test_func(self):
        post = self.get_object()       #Fetches the post
        return self.request.user == post.author     #Checks if the post author is the logged in user


class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """View to show individual blog posts"""
    model = Post
    template_name = "blog/deleteview.html"
    success_url = reverse_lazy("posts")

    """A test function to ensure only authenticated user who is the author can 
    delete post."""
    def test_func(self):
        post = self.get_object()       #Fetches the post
        return self.request.user == post.author     #Checks if the post author is the logged in user
   