from django.db import models

    
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
    duration = models.DurationField()
    total_points = models.IntegerField()

    def __str__(self):
        return f'{self.card_holder} : {self.card}'


class LoyalPoint(models.Model):
    traveler = models.CharField(max_length=50)
    card_points_remain = models.IntegerField()
    earned_points_remain = models.IntegerField()
    points_remain = models.IntegerField()
    points_redeemed = models.IntegerField()
    total_points = models.IntegerField()

    def __str__(self):
        return self.traveler