# Generated by Django 5.0.2 on 2024-02-27 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_customer_profile_lid'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_profile',
            name='dp',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]