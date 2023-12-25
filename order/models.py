from django.db import models
from accounts.models import Customer
from property.models import Property, Area

# Create your models here.


class Order(models.Model):
    area = models.ForeignKey(Area, on_delete=models.DO_NOTHING, null=True)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.DO_NOTHING,
                                 null=True)
    order_date = models.DateField()
    order_type = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    start_price = models.DecimalField(max_digits=10, decimal_places=2)
    end_price = models.DecimalField(max_digits=10, decimal_places=2)
    room_number = models.IntegerField()
    floor = models.CharField(max_length=100)
    details = models.TextField()
    build_year = models.CharField(max_length=100)
    bathrooms = models.CharField(max_length=100)
    hall_room = models.CharField(max_length=100)
    basement = models.CharField(max_length=100)
    pool = models.CharField(max_length=100)
    furnished = models.CharField(max_length=100)
    elevator = models.CharField(max_length=100)
    street_number = models.CharField(max_length=100)
    appendix = models.CharField(max_length=100)
    space = models.IntegerField(null=True)


class Booking(models.Model):
    customer = models.ForeignKey(Customer,
                                 on_delete=models.DO_NOTHING,
                                 null=True)
    property = models.ForeignKey(Property,
                                 on_delete=models.DO_NOTHING,
                                 null=True)
    booking_status = models.BooleanField()
