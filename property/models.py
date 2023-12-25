from django.db import models


# Create your models here.
class Property(models.Model):
    type_id = models.IntegerField()
    area_id = models.IntegerField()
    user_ID = models.IntegerField()
    title = models.CharField(max_length=50)
    tescription = models.CharField(max_length=100)
    features = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Photo_Property(models.Model):
    property_id = models.IntegerField()
    description = models.CharField(max_length=100)
    path = models.CharField(max_length=100)


class Type(models.Model):
    type_Name = models.CharField(max_length=100)


class Comparison(models.Model):
    property_id = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


class Favorite(models.Model):
    property_id = models.IntegerField()
    user_id = models.IntegerField()
    status = models.CharField(max_length=100)


class ADS(models.Model):
    property_id = models.IntegerField()
    user_id = models.IntegerField()


class Photo_ADS(models.Model):
    description = models.CharField(max_length=100)
    path = models.CharField(max_length=100)