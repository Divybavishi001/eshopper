# Generated by Django 5.0.2 on 2024-03-08 11:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_rename_wishlit_wishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('shipadd_id', models.AutoField(primary_key=True, serialize=False)),
                ('First_Name', models.CharField(max_length=100, null=True)),
                ('Last_Name', models.CharField(max_length=100, null=True)),
                ('Email', models.EmailField(max_length=150, null=True)),
                ('Mobile', models.CharField(max_length=10, null=True)),
                ('Address', models.TextField(max_length=1000, null=True)),
                ('Area_Name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.area')),
                ('lid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.signupuser')),
            ],
        ),
    ]
