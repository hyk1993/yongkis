from django import forms
from .models import Blog, Comment



class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']