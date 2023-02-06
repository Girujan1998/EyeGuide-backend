from django.db.models import JSONField
from django.db import models

class StoreGPSData(models.Model) :
    name = models.CharField(max_length=100)
    gpsCord = JSONField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'GPS_DATA'

class StoreCornerCordsData(models.Model) :
    buildingName = models.CharField(max_length=100)
    cornerCords = JSONField()

    def __str__(self):
        return self.buildingName

    class Meta:
        db_table = 'GPS_CORNER_CORD'

class StoreNodeData(models.Model) :
    buildingName = models.CharField(max_length=100)
    floorName = models.CharField(max_length=100)
    nodes = JSONField()

    def __str__(self):
        return self.buildingName

    class Meta:
        db_table = 'NODE_DATA'