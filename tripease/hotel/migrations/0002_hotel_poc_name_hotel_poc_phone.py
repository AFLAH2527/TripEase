# Generated by Django 5.0.2 on 2024-03-12 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='poc_name',
            field=models.CharField(default='name', max_length=50, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotel',
            name='poc_phone',
            field=models.CharField(default=9999999999, max_length=50),
            preserve_default=False,
        ),
    ]
