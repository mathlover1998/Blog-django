from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = 'home'),
    path('post/<int:id>/',views.show_post,name = 'show_post'),
    path('about',views.about,name = 'about'),
    path('contact',views.contact,name = 'contact'),
    path('add-post',views.add_post,name = 'add_post'),
    path('edit-post/<int:id>/',views.edit_post,name = 'edit_post'),
    path('<int:id>/delete',views.delete_post,name='delete_post'),
    path('register',views.register,name='register')
]