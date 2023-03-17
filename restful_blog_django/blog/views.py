from django.shortcuts import render,redirect
from .models import BlogPost
from .forms import CreateBlogPostForm
from datetime import datetime as dt
# Create your views here.

def index(request):
    posts = BlogPost.objects.all()

    return render(request,'index.html',{'all_posts':posts})

def show_post(request,id):
    post = BlogPost.objects.get(id=id)
    return render(request,'post.html',{'post':post})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def add_post(request):
    form = CreateBlogPostForm()
    if form.is_valid():
        new_blog = BlogPost(title = form.title,date = dt.now().strftime('%B %-d, %Y'),body=form.content,
                            author = 'TEST AUTHOR', img_url = form.img_url,subtitle= form.subtitle )
        new_blog.save()
        return redirect('index')
    return render(request,'make-post.html',{'form':form})