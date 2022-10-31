from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=40)
    division = models.IntegerField()

    def __str__(self):
        return self.name


class DistrictManager(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    district_manager_name = models.CharField(max_length=50)

    def __str__(self):
        return self.district_manager_name


class StoreManager(models.Model):
    store_manager_name = models.CharField(max_length=50)
    store = models.ForeignKey(Store, max_length=50, on_delete=models.CASCADE)
    district_manager = models.ForeignKey(DistrictManager, on_delete=models.CASCADE)

    def __str__(self):
        return self.store_manager_name
