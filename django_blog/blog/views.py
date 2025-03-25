from django.shortcuts import render, redirect, get_object_or_404
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
from .models import Post, Comment
from .forms import PostCreateForm, CreateCommentForm
from django.contrib.auth.decorators import login_required

# Blog Home page view
class HomeView(TemplateView):
    template_name = "blog/home.html"


"""Setting up User Authentication Views"""
# User registration View
class SignUpView(CreateView):
    """Handles user registration"""
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('login')     #Redirects to the login page after successfully creating user
    template_name = 'blog/register.html'        

# User logout view
class LogoutView(View):
    """Logs out a user and renders a specified template"""
    template_name=""

    """Logout view would display this view when the user logs out"""
    def get(self, request):     
        logout(request)         # Logs Out a User
        return render(request, self.template_name)
    
#Implementing user profile view

class ProfileView(LoginRequiredMixin, View):
    template_name =  "blog/profile.html"

    
    def get(self, request):
        user= request.user      #To get the the particular view for the current logged in user
        context = {"user": user}
        return render(request, self.template_name, context)
    
    
    def post(self, request):
        """Handles updating user email from the profile page"""
        user = request.user

        if request.method == "POST":
            updated_email = request.POST.get("email")       # gets email from form input i.e the user input

            if updated_email:
                user.email = updated_email      # if a new mail is provided, update.
                user.save()
        return redirect("profile")     #redirects to the profile page after update
    
    


"""
Creating blog Post Management features
"""
# Blog Post Management Views
class ListPostView(ListView):
    """View to display all blog posts"""
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"

class DetailPostView(DetailView):
    """View to show individual blog post"""
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

class CreatePostView(LoginRequiredMixin, CreateView):   #Ensures only authenticated users can create a post
    """View to allow authenticated users to create blog posts"""
    model = Post
    template_name = "blog/post_form.html"
    form_class = PostCreateForm
    success_url = reverse_lazy("posts")

    #Ensuring logged in user is the post author
    def form_valid(self, form):
        """Assigns the logged-in user as the post author before saving"""
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  
    """Allows post authors to update their posts"""
    model = Post
    template_name = "blog/post_form.html"
    fields = ["title", "content"]
    context_object_name = "post"
    success_url = reverse_lazy("posts")

    """A test function to ensure it is the required user that can perform this view function"""
    def test_func(self):
        """Ensures only the post author can update the post"""
        post = self.get_object()       # Fetches the post
        return self.request.user == post.author     # Checks if the post author is the logged in user


class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Allows post authors to delete their posts"""
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("posts")

    """A test function to ensure only authenticated user who is the author can 
    delete post."""
    def test_func(self):
        """Ensures only the post author can update the post"""
        post = self.get_object()       # Fetches the post
        return self.request.user == post.author     # Checks if the post author is the logged in user


"""Adding comment functionality"""
# Comment management views
# A view to create a comments under a blog post
class CommentCreateView(LoginRequiredMixin, CreateView):
    """Allows authenticated users to add comments to a post"""
    model = Comment
    form_class = CreateCommentForm
    
    """form validation to ensure comment is associated with a post"""
    def form_valid(self, form):
        """Associates the comment with the correct post and author before saving"""
        post = get_object_or_404(Post, pk=self.kwargs['pk'])   # Get the post from the URL
        form.instance.post = post      # Associate comment with post
        form.instance.author = self.request.user  # Assign the logged in user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        """Ensures the post is available in the template context"""
        context = super().get_context_data(**kwargs)
        context["post"] = get_object_or_404(Post, pk=self.kwargs["pk"])  # Ensure post is available in template
        return context
    
    # def test_func(self):
    #     comment = self.get_object()
    #     return self.request.user == comment.author
    
    def get_success_url(self):
        """Redirects back to the post detail page after a comment is added"""
        return reverse_lazy("post_detail", kwargs={"pk": self.kwargs['pk']})  # Redirect to the post detail page

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Allows comment authors to update their comments"""
    model = Comment
    form_class = CreateCommentForm      # Reuse the existing form with validation
    template_name = "blog/comment_update.html"
   
    def get_success_url(self):
        """Redirects to the post detail page after comment update"""
        return reverse_lazy("post_detail", kwargs={"pk": self.kwargs["post_pk"]})

    def test_func(self):
        """Ensures only the comment author can edit the comment"""
        comment = self.get_object()
        return self.request.user == comment.author
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = get_object_or_404(Post, pk=self.kwargs["post_pk"])    # Ensures the post is available in the template
        return context
    
    def form_valid(self, form):
        """Associates the comment with the correct post and saves it"""
        post = get_object_or_404(Post, pk=self.kwargs['post_pk'])   # Get the post from the URL
        form.instance.post = post      # Associate comment with post
        form.instance.author = self.request.user  # Assign the logged in user
        form.save()
        return redirect('post_detail', pk=self.kwargs['post_pk']) # Ensure form is validated and saved

    def get_object(self, queryset=None):
        """Retrieves the correct comment instance"""
        return get_object_or_404(Comment, pk=self.kwargs["comment_pk"])


# Delete comment view
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Allows comment authors to delete their comments"""
    model = Comment
    template_name = "blog/comment_confirm_delete.html"

    def get_success_url(self):
        """Redirects to the post detail page after deleting the comment"""
        return reverse_lazy("post_detail", kwargs={"pk": self.kwargs["post_pk"]})

    def test_func(self):
        """Ensures only the comment author can delete the comment"""
        comment = self.get_object()
        return self.request.user == comment.author

    def get_object(self, queryset=None):
        """Retrieves the correct comment instance"""
        return get_object_or_404(Comment, pk=self.kwargs["comment_pk"])
