from django.db import models


# Create your models here.
class Property(models.Model):
    Property_id = models.IntegerField()
    Type_id = models.IntegerField()
    Area_id = models.IntegerField()
    User_ID = models.IntegerField()
    Title = models.CharField(max_length=50)
    Description = models.CharField(max_length=100)
    Features = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    Price = models.DecimalField(max_digits=10, decimal_places=2)


class Photo_Property(models.Model):
    Photo_Property_id = models.IntegerField()
    property_id = models.IntegerField()
    description = models.CharField(max_length=100)
    path = models.CharField(max_length=100)


class Type(models.Model):
    Type_id = models.IntegerField()
    Type_Name = models.CharField(max_length=100)


class Comparison(models.Model):
    Comparison_id = models.IntegerField()
    property_id = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


class Favorite(models.Model):
    favorite_id = models.IntegerField()
    property_id = models.IntegerField()
    user_id = models.IntegerField()
    status = models.CharField(max_length=100)


class ADS(models.Model):
    ADS_id = models.IntegerField()
    property_id = models.IntegerField()
    user_id = models.IntegerField()


class Photo_ADS(models.Model):
    Photo_ADS_id = models.IntegerField()
    photADS_id = models.IntegerField()
    description = models.CharField(max_length=100)
    path = models.CharField(max_length=100)