from django.shortcuts import render,redirect,get_object_or_404
from .models import BlogPost
from .forms import CreateBlogPostForm,RegisterForm
from datetime import datetime as dt
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib.auth.hashers import make_password
from django.conf import settings


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
    if request.method == 'POST':
        form = CreateBlogPostForm(request.POST)
        if form.is_valid():
            new_blog = BlogPost(
                title=form.cleaned_data['title'],
                date=str(dt.now().strftime('%B %d, %Y')),
                body=form.cleaned_data['body'],
                author=form.cleaned_data['author'],
                img_url=form.cleaned_data['img_url'],
                subtitle=form.cleaned_data['subtitle'],
            )
            new_blog.save()
            return redirect('show_post',id = new_blog.id)
    else:
        form = CreateBlogPostForm()
    return render(request, 'make-post.html', {'form': form,"is_edit":False})

def edit_post(request,id):
    
    selected_post = get_object_or_404(BlogPost, pk=id)
    
    if request.method =='POST':
        form = CreateBlogPostForm(request.POST)
        if form.is_valid():
            
            selected_post.title=form.cleaned_data['title']
            selected_post.date=str(dt.now().strftime('%B %d, %Y'))
            selected_post.body=form.cleaned_data['body']
            selected_post.author=form.cleaned_data['author']
            selected_post.img_url=form.cleaned_data['img_url']
            selected_post.subtitle=form.cleaned_data['subtitle']
            
            selected_post.save()
            return redirect('show_post',id = selected_post.id)
    else:
        form = CreateBlogPostForm(instance=selected_post)
    return render(request, 'make-post.html', {'form': form,"is_edit":True,'post_id':id})

def delete_post(request,id):
    post = get_object_or_404(BlogPost,pk =id)
    post.delete()
    return redirect('home')

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            
            password = make_password(password=form.cleaned_data.get('password'),salt=str(settings.SALT_LENGTH))
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            user = User.objects.create(username=username,email=email)
            user.set_password(password)
            user.save()
            

            
            return redirect('home')
    return render(request,'register.html',{'form':form})