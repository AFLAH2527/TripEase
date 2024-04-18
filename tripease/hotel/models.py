from django.db import models

from traveler.models import Destination

class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Hotel(models.Model):
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

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not Destination.objects.filter(name=self.place, district=self.district, state=self.state).exists():
            Destination.objects.create(
                name=self.place,
                district=self.district,
                state=self.state
            )
        super(Hotel, self).save(*args, **kwargs)


class Room(models.Model):
    hotel_name = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=50)
    price = models.IntegerField()
    bathroom_attached = models.BooleanField(blank=True, null=True)
    ac = models.BooleanField(blank=True, null=True)
    count = models.IntegerField()

    def __str__(self):
        return f'{self.room_type}-{self.hotel_name}'


class RoomBooking(models.Model):
    hotel_name = models.CharField(max_length=50)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    traveler_name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    no_of_days = models.IntegerField()
    amount = models.IntegerField()

    def __str__(self):
        return f'{self.traveler_name} - {self.room.room_type}'

    def save(self, *args, **kwargs):
        self.room.count -= 1
        self.room.save()

        super(RoomBooking, self).save(*args, **kwargs)


