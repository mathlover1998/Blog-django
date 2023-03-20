from django import forms
from .models import BlogPost
from django.forms import PasswordInput

class CreateBlogPostForm(forms.ModelForm):

    title = forms.CharField(label='Blog Post Label',widget=forms.TextInput(attrs={'class':'form-control'}))
    subtitle = forms.CharField(label='Subtitle',widget=forms.TextInput(attrs={'class':'form-control'}))
    name = forms.CharField(label='Your name',widget=forms.TextInput(attrs={'class':'form-control'}))
    img_url = forms.CharField(label='Blog Image URL',max_length=400,widget=forms.TextInput(attrs={'class':'form-control'}))
    content = forms.CharField(label = 'Blog content',widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = BlogPost
        fields = ['title','subtitle','name','img_url','content']