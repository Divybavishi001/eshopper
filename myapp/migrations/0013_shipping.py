# Generated by Django 5.0.2 on 2024-03-07 05:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_subcategory_subcategory_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('Ship_id', models.AutoField(primary_key=True, serialize=False)),
                ('Ship_Charege', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Area_Name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.area')),
            ],
        ),
    ]
