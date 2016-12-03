from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField()

class Car(models.Model):
    model = models.CharField(max_length=128)
    mpg = models.FloatField()
    fuel_capacity = models.FloatField(max_length=128)

class Location(models.Model):
    latitude = models.CharField(max_length=16)
    longitude = models.CharField(max_length=16)
    home = models.BooleanField(default=False)
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name

    def as_dict(self):
        return {
            "name": self.name,
            "longitude": self.longitude,
            "latitude": self.latitude
        }

