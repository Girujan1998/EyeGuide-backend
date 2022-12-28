from django.db.models import JSONField
from django.db import models

class StoreGPSData(models.Model) :
    name = models.CharField(max_length=100)
    gpsCord = JSONField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'GPS_DATA'