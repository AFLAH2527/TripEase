from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
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
    

class Item(models.Model):
    restaurant_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} || {self.restaurant_name}"

class Combo(models.Model):
    restaurant_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    items = models.ManyToManyField(Item, related_name='combos')

    def __str__(self):
        return self.name
    

