# Generated by Django 5.0.1 on 2024-02-02 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backends', '0024_leads_parmas'),
    ]

    operations = [
        migrations.AddField(
            model_name='leads',
            name='date_of_joined',
            field=models.CharField(default='02022024', max_length=20),
        ),
    ]