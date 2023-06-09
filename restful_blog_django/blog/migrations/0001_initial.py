# Generated by Django 4.1 on 2023-03-20 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('author', models.CharField(max_length=200)),
                ('img_url', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'blog_post',
            },
        ),
    ]
