from django.contrib import admin

from .models import Type, Hotel, Room, RoomBooking

admin.site.register(Type)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(RoomBooking)

