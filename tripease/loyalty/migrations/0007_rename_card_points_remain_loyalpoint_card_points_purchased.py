# Generated by Django 5.0.2 on 2024-04-17 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loyalty', '0006_loyaltycard_current_date_loyaltycard_purchase_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loyalpoint',
            old_name='card_points_remain',
            new_name='card_points_purchased',
        ),
    ]
