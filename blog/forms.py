from django.forms import ModelForm
from blog.models import Blog
from django import forms


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'content')


class BlogModeratorForm(ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'content')