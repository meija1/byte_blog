from .models import Comment
from django import forms
from . import models


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class BlogForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'content']
