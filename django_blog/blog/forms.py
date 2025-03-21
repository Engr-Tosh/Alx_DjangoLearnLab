from django import forms
from .models import Post

#Define the model to inherit now from the form model
class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']