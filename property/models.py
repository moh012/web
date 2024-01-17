from django.db import models
from accounts.models import Agent, Customer


# Create your models here.
class Type(models.Model):
    type_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.type_name


class City(models.Model):
    city_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.city_name


class Area(models.Model):
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, null=True)
    area_name = models.CharField(max_length=100)

    def __str__(self):
        return self.area_name


class Property(models.Model):
    type = models.ForeignKey(Type, on_delete=models.DO_NOTHING, null=True)
    area = models.ForeignKey(Area, on_delete=models.DO_NOTHING, null=True)
    agent = models.ForeignKey(Agent, on_delete=models.DO_NOTHING, null=True)
    title = models.CharField(max_length=50)
    tescription = models.CharField(max_length=100)
    features = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class Photo_Property(models.Model):
    property = models.ForeignKey(Property,
                                 on_delete=models.DO_NOTHING,
                                 null=True)
    description = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='propertyPhoto/%Y/%m/%d/', blank=True)


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
    photo = models.ImageField(upload_to='adsPhoto/%Y/%m/%d/', blank=True)
