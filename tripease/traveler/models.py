from django.db import models


class Destination(models.Model):
    name = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}, {self.district}, {self.state}'


class Traveler(models.Model):
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50)
    native_place = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.name
