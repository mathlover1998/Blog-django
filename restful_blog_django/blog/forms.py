from django import forms
from .models import BlogPost
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget


class CreateBlogPostForm(forms.ModelForm):

    title = forms.CharField(label='Blog Post Label', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    subtitle = forms.CharField(
        label='Subtitle', widget=forms.TextInput(attrs={'class': 'form-control'}))
    author = forms.CharField(label='Your name', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    img_url = forms.CharField(label='Blog Image URL', max_length=400,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    body = forms.CharField(label='Blog content', widget=CKEditorWidget(
        attrs={'class': 'form-control'}))

    class Meta:
        model = BlogPost
        fields = ['title', 'subtitle', 'author', 'img_url', 'body']


class RegisterForm(forms.ModelForm):
    email = forms.CharField(label='Email', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    fullname = forms.CharField(label='Your full name', widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['email'].widget.attrs['class'] = 'email'
    class Meta:
        model = User
        fields = ['email', 'password', 'fullname']
