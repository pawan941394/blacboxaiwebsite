# Generated by Django 5.0.1 on 2024-02-07 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backends', '0036_course_about_company_course_about_instructor'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='whatsapp_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='whatsapp_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]