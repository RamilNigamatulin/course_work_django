from django.forms import ModelForm
from blog.models import Blog
from django import forms


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'content', 'created_date')


class BlogModeratorForm(ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'content', 'preview', 'created_date')