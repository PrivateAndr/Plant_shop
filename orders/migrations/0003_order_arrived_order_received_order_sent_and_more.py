# Generated by Django 4.1.8 on 2023-05-21 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='arrived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='received',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='sent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='total_cost',
            field=models.IntegerField(default=0),
        ),
    ]
