# Generated by Django 5.0.2 on 2024-03-25 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0005_room_room_booking'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Room_Booking',
            new_name='RoomBooking',
        ),
    ]