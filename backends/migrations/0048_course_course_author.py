# Generated by Django 5.0.1 on 2024-02-08 05:12

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backends', '0047_courseregisteration_alter_communitie_date_of_joined_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_author',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]