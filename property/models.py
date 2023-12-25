from django.db import models
from accounts.models import Agent, Customer


# Create your models here.
class Type(models.Model):
    type_Name = models.CharField(max_length=100)


class City(models.Model):
    city_name = models.CharField(max_length=100)


class Area(models.Model):
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, null=True)
    area_name = models.CharField(max_length=100)


class Property(models.Model):
    type = models.ForeignKey(Type, on_delete=models.DO_NOTHING, null=True)
    area = models.ForeignKey(Area, on_delete=models.DO_NOTHING, null=True)
    agent = models.ForeignKey(Agent, on_delete=models.DO_NOTHING, null=True)
    title = models.CharField(max_length=50)
    tescription = models.CharField(max_length=100)
    features = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Photo_Property(models.Model):
    property = models.ForeignKey(Property,
                                 on_delete=models.DO_NOTHING,
                                 null=True)
    description = models.CharField(max_length=100)
    path = models.CharField(max_length=100)


class Comparison(models.Model):
    property = models.ForeignKey(Property,
                                 on_delete=models.DO_NOTHING,
                                 null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


class Favorite(models.Model):
    property = models.ForeignKey(Property,
                                 on_delete=models.DO_NOTHING,
                                 null=True)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.DO_NOTHING,
                                 null=True)
    status = models.CharField(max_length=100)


class ADS(models.Model):
    property = models.ForeignKey(Property,
                                 on_delete=models.DO_NOTHING,
                                 null=True)
    agent = models.ForeignKey(Agent, on_delete=models.DO_NOTHING, null=True)


class Photo_ADS(models.Model):
    description = models.CharField(max_length=100)
    path = models.CharField(max_length=100)