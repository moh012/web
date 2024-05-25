from django.db import models
from accounts.models import Agent, Customer
from django.utils import timezone
import datetime
import os

# Create your models here.
# class Type(models.Model):
#     search_type = models.CharField(max_length=100, null=True)

#     def __str__(self):
#         return self.type_name


class City(models.Model):
    city_name = models.CharField(max_length=100, null=True)
    phohto = models.ImageField(upload_to='city_photo', null=True, blank=True)

    def __str__(self):
        return self.city_name


class Area(models.Model):
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, null=True)
    area_name = models.CharField(max_length=100)

    def __str__(self):
        return self.area_name


def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)


class Property(models.Model):
    # type = models.ForeignKey(Type, on_delete=models.DO_NOTHING, null=True)
    area = models.ForeignKey(Area, on_delete=models.DO_NOTHING, null=True)
    agent = models.ForeignKey(Agent,
                              on_delete=models.DO_NOTHING,
                              null=True,
                              related_name='properties')
    title = models.CharField(max_length=50, null=True)
    property_type = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
    img = models.ImageField(upload_to=filepath, blank=True)
    details = models.TextField(null=True)
    price = models.IntegerField(null=True)
    room_number = models.CharField(max_length=100, null=True)
    hall_room = models.CharField(max_length=100, null=True)
    bathrooms = models.CharField(max_length=100, null=True)
    floor = models.CharField(max_length=100, null=True)
    street_number = models.CharField(max_length=100, null=True)
    build_year = models.CharField(max_length=100, null=True)
    house_type = models.CharField(max_length=100, null=True)
    space = models.IntegerField(null=True)
    pool = models.BooleanField(default=False, null=True)
    kitchen = models.BooleanField(default=False, null=True)
    roof = models.BooleanField(default=False, null=True)
    modern = models.BooleanField(default=False, null=True)
    appendix = models.BooleanField(default=False, null=True)
    elevator = models.BooleanField(default=False, null=True)
    basement = models.BooleanField(default=False, null=True)
    furnished = models.BooleanField(default=False, null=True)
    property_date = models.DateField(default=timezone.now)
    state = models.BooleanField(default=False, null=True)

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
    status = models.BooleanField(default=False, null=True)


class ADS(models.Model):
    property = models.ForeignKey(Property,
                                 on_delete=models.DO_NOTHING,
                                 null=True)
    agent = models.ForeignKey(Agent, on_delete=models.DO_NOTHING, null=True)


class Photo_ADS(models.Model):
    description = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='adsPhoto/%Y/%m/%d/', blank=True)
