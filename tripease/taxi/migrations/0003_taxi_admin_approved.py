# Generated by Django 5.0.2 on 2024-03-14 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0002_taxi_poc_name_taxi_poc_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxi',
            name='admin_approved',
            field=models.BooleanField(default=False),
        ),
    ]
