# Generated by Django 5.0.1 on 2024-02-01 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backends', '0018_alter_blog_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='Blog_image',
            field=models.ImageField(null=True, upload_to='Blogs/'),
        ),
    ]
