from django.db import models
from accounts.models import Customer
from property.models import Property, Area
from django.utils import timezone

# Create your models here.


class Order(models.Model):
    area = models.ForeignKey(Area, on_delete=models.DO_NOTHING, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100, null=True)
    order_type = models.CharField(max_length=100, null=True)
    order_date = models.DateField(default=timezone.now)
    state = models.BooleanField(default=False)
    start_price = models.IntegerField(null=True)
    end_price = models.IntegerField(null=True)
    room_number = models.IntegerField(null=True)
    floor = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=150, null=True)
    details = models.TextField(null=True)
    build_year = models.CharField(max_length=100, null=True)
    bathrooms = models.CharField(max_length=100, null=True)
    hall_room = models.CharField(max_length=100, null=True)
    floor_room = models.CharField(max_length=100, null=True)
    street_number = models.CharField(max_length=100, null=True)
    housetype = models.CharField(max_length=100, null=True)
    space = models.IntegerField(null=True)
    basement = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)
    kitchen = models.BooleanField(default=False)
    furnished = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
    appendix = models.BooleanField(default=False)
    roof = models.BooleanField(default=False)
    modern = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    property = models.ForeignKey(Property,
                                 on_delete=models.DO_NOTHING,
                                 null=True)
    booking_status = models.BooleanField()
