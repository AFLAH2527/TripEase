from django.contrib import admin

from .models import Type, Taxi, TaxiBooking

admin.site.register(Type)
admin.site.register(Taxi)
admin.site.register(TaxiBooking)
