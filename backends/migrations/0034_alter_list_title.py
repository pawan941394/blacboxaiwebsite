# Generated by Django 5.0.1 on 2024-02-07 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backends', '0033_remove_course_course_descriptions_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]