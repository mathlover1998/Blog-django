from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200, null=False)
    date = models.CharField(max_length=200, null=False)
    body = RichTextField()
    author = models.CharField(max_length=200, null=False)
    img_url = models.CharField(max_length=500, null=False)
    subtitle = models.CharField(max_length=200, null=False)

    class Meta():
        db_table = 'blog_post'


class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('unknown', 'Unknown'),

    ]

    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return self.user.username

    class Meta():
        db_table = 'user_profile'
