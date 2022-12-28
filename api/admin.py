from django.contrib import admin

from .models import StoreGPSData

class StoreGPSDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'gpsCord')

admin.site.register(StoreGPSData, StoreGPSDataAdmin)
