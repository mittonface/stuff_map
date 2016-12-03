from django.contrib import admin
from .models import Item, Location

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass