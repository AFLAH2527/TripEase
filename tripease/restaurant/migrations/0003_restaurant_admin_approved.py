# Generated by Django 5.0.2 on 2024-03-14 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_restaurant_poc_name_restaurant_poc_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='admin_approved',
            field=models.BooleanField(default=False),
        ),
    ]
