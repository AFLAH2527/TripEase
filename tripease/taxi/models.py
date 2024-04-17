from django.db import models
from traveler.models import Destination

class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Taxi(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50)
    poc_name = models.CharField(max_length=50, unique=True)
    poc_phone = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    admin_approved = models.BooleanField(default=False)

    daily_rent = models.IntegerField()
    km_charge = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not Destination.objects.filter(name=self.place, district=self.district, state=self.state).exists():
            Destination.objects.create(
                name=self.place,
                district=self.district,
                state=self.state
            )
        super(Taxi, self).save(*args, **kwargs)


class TaxiBooking(models.Model):
    taxi = models.ForeignKey(Taxi, on_delete=models.CASCADE)
    traveler_name = models.CharField(max_length=50)
    pickup_location = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    total_rent = models.IntegerField()

    def __str__(self):
        return f'{self.traveler_name} - {self.taxi.name}'
