from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Taxi(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name