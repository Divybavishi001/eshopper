# Generated by Django 5.0.2 on 2024-03-11 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_card_details_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_details',
            name='Payment_Status',
            field=models.CharField(max_length=20, null=True),
        ),
    ]