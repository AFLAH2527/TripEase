# Generated by Django 5.0.2 on 2024-04-18 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0011_roombooking_end_date_roombooking_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='ac',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='room',
            name='bathroom_attached',
            field=models.BooleanField(default=False),
        ),
    ]
