from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200,null=False)
    date= models.CharField(max_length=200,null=False)
    body= RichTextField()
    author= models.CharField(max_length=200,null=False)
    img_url= models.CharField(max_length=500,null=False)
    subtitle= models.CharField(max_length=200,null=False)

    class Meta():
        db_table = 'blog_post'