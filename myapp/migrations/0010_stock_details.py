# Generated by Django 5.0.2 on 2024-02-28 06:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_cart_items_order_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock_Details',
            fields=[
                ('sto_id', models.AutoField(primary_key=True, serialize=False)),
                ('sto_Quantity', models.IntegerField(null=True)),
                ('p_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
            ],
        ),
    ]
