# Generated by Django 5.0.1 on 2024-02-02 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backends', '0022_contact_leads_alter_communitie_date_of_joined_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='leads',
            name='years_of_trading_experience',
            field=models.CharField(default=0, max_length=3),
            preserve_default=False,
        ),
    ]
