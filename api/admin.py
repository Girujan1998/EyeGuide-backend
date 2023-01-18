from django.contrib import admin

from .models import StoreGPSData
from .models import StoreCornerCordsData

class StoreGPSDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'gpsCord')

class StoreCornerCordsDataAdmin(admin.ModelAdmin):
    list_display = ('buildingName', 'cornerCords')

admin.site.register(StoreGPSData, StoreGPSDataAdmin)
admin.site.register(StoreCornerCordsData, StoreCornerCordsDataAdmin)
