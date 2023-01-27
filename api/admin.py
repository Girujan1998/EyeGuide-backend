from django.contrib import admin

from .models import StoreGPSData
from .models import StoreCornerCordsData
from .models import StoreNodeData

class StoreGPSDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'gpsCord')

class StoreCornerCordsDataAdmin(admin.ModelAdmin):
    list_display = ('buildingName', 'cornerCords')

class StoreNodeDataAdmin(admin.ModelAdmin):
    list_display = ('buildingName', 'floorName', 'nodes')

admin.site.register(StoreGPSData, StoreGPSDataAdmin)
admin.site.register(StoreCornerCordsData, StoreCornerCordsDataAdmin)
admin.site.register(StoreNodeData, StoreNodeDataAdmin)
