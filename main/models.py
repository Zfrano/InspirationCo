from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=40)
    division = models.IntegerField()
    district_manager = models.CharField(max_length=50)
    city_manager = models.CharField(max_length=50)
    weekday_opening = models.CharField(max_length=10)
    weekday_closing = models.CharField(max_length=10)
    sat_opening = models.CharField(max_length=10)
    sat_closing = models.CharField(max_length=10)
    sun_opening = models.CharField(max_length=10)
    sun_closing = models.CharField(max_length=10)
    def __str__(self) -> str:
        return self.name
