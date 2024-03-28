# Generated by Django 5.0.2 on 2024-02-27 12:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_category_alter_customer_profile_dp_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('Pro_Name', models.CharField(max_length=100, null=True)),
                ('Pro_Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Pro_Image', models.ImageField(null=True, upload_to='myapp/media')),
                ('Pro_Disc', models.TextField(max_length=500, null=True)),
                ('s_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.subcategory')),
            ],
        ),
    ]