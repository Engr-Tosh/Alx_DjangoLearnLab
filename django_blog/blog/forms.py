from django import forms
from .models import Post, Comment

#Define the model to inherit now from the form model
class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

# Comment model form
class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    # Data validation
    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) < 10:
            raise forms.ValidationError("Comment is too short (Minimum: 10 characters)t")
        if len(content) > 500:
            raise forms.ValidationError("Comment is too long (Maximum: 500 characters)")
        return content