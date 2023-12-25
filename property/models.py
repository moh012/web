from django.db import models
from accounts.models import Agent,Customer
from .models import Type,Area,Property

# Create your models here.
class Property(models.Model):
    type = models.ForeignKey(Type, on_delete=models.DO_NOTHING)
    area = models.IntegerField(Area, on_delete=models.DO_NOTHING)
    agent = models.IntegerField(Agent, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=50)
    tescription = models.CharField(max_length=100)
    features = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Photo_Property(models.Model):
    property = models.ForeignKey(Property, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=100)
    path = models.CharField(max_length=100)


class Type(models.Model):
    type_Name = models.CharField(max_length=100)


class Comparison(models.Model):
    property = models.ForeignKey(Property, on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


class Favorite(models.Model):
    property = models.ForeignKey(Property, on_delete=models.DO_NOTHING)
    customer = models.OneToOneField(Customer,on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=100)


class ADS(models.Model):
    property = models.ForeignKey(Property, on_delete=models.DO_NOTHING)
    agent = models. ForeignKey(Agent,on_delete=models.DO_NOTHING)


class Photo_ADS(models.Model):
    description = models.CharField(max_length=100)
    path = models.CharField(max_length=100)