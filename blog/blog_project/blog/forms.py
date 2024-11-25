from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User
from .models import Profile

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_image']
