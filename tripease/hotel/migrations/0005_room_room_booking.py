# Generated by Django 5.0.2 on 2024-03-25 21:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_hotel_admin_approved_alter_hotel_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=50)),
                ('room_type', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('bathroom_attached', models.BooleanField()),
                ('ac', models.BooleanField()),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Room_Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=50)),
                ('traveler_name', models.CharField(max_length=50)),
                ('no_of_days', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.room')),
            ],
        ),
    ]
