from django import forms
from .models import BlogPost
from django.forms import PasswordInput

class CreateBlogPostForm(forms.ModelForm):

    title = forms.CharField(label='Blog Post Label')
    subtitle = forms.CharField(label='Subtitle')
    name = forms.CharField(label='Your name')
    img_url = forms.CharField(label='Blog Image URL',max_length=400)
    content = forms.CharField(label = 'Blog content',widget=forms.Textarea)
    class Meta:
        model = BlogPost
        fields = ['title','subtitle','name','img_url','content']