# Generated by Django 5.0.1 on 2024-02-02 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backends', '0021_whatweoffer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('phone_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='leads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('outside_india', models.CharField(max_length=200)),
                ('whatsapp_number', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='communitie',
            name='date_of_joined',
            field=models.CharField(default='02022024', max_length=20),
        ),
        migrations.AlterField(
            model_name='webinarregisteration',
            name='Webinar_time',
            field=models.CharField(default='02022024', max_length=20),
        ),
        migrations.AlterField(
            model_name='webinarregisteration',
            name='date_of_registeration',
            field=models.CharField(default='02022024', max_length=20),
        ),
    ]