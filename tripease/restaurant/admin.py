from django.contrib import admin

from .models import Type, Restaurant, Item, Combo

admin.site.register(Type)
admin.site.register(Restaurant)
admin.site.register(Item)
admin.site.register(Combo)
