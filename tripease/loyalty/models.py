from django.db import models
from django.utils import timezone

    
class CardType(models.Model):
    name = models.CharField(max_length=20)
    prefix = models.CharField(max_length=10)
    points = models.IntegerField()
    price = models.IntegerField()
    multiple_factor = models.IntegerField()

    def __str__(self):
        return self.name


class LoyaltyCard(models.Model):
    card = models.ForeignKey(CardType, on_delete=models.CASCADE)
    card_holder = models.CharField(max_length=50)
    duration = models.IntegerField()
    total_points = models.IntegerField()
    active = models.BooleanField(default=True)
    purchase_date = models.DateField(null=True, blank=True)
    current_date = models.DateField(null=True, blank=True)
    days_remain = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.card_holder} : {self.card}'

    def save(self, *args, **kwargs):
        # Update current date and days remaining when saving the instance
        if not self.pk:
            # New instance, set purchase date and current date
            self.purchase_date = timezone.now().date()
            self.current_date = self.purchase_date
            self.days_remain = self.duration * 28
        else:
            # Existing instance, update current date
            self.current_date = timezone.now().date()

        # Calculate days remaining
        if self.purchase_date and self.current_date:
            delta = self.current_date - self.purchase_date
            self.days_remain = max(self.duration * 28 - delta.days, 0)

        self.active = self.days_remain > 0

        super().save(*args, **kwargs)


class LoyalPoint(models.Model):
    traveler = models.CharField(max_length=50)
    card_points_purchased = models.IntegerField(null=True)
    earned_points = models.IntegerField(null=True)
    points_remain = models.IntegerField(null=True)
    points_redeemed = models.IntegerField(null=True)
    total_points = models.IntegerField(null=True)

    def __str__(self):
        return self.traveler