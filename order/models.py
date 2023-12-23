from django.db import models


# Create your models here.
class Order(models.Model):
    Area_id = models.IntegerField()
    User_ID = models.IntegerField()
    Order_Date = models.DateField()
    Order_Type = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    Start_Price = models.DecimalField(max_digits=10, decimal_places=2)
    End_Price = models.DecimalField(max_digits=10, decimal_places=2)
    Room_Number = models.IntegerField()
    Floor = models.CharField(max_length=100)
    Details = models.TextField()
    Build_Year = models.CharField(max_length=100)
    Bathrooms = models.CharField(max_length=100)
    Hall_Room = models.CharField(max_length=100)
    Basement = models.CharField(max_length=100)
    Pool = models.CharField(max_length=100)
    Furnished = models.CharField(max_length=100)
    Elevator = models.CharField(max_length=100)
    Street_number = models.CharField(max_length=100)
    Appendix = models.CharField(max_length=100)
    Space = models.IntegerField()


class Booking(models.Model):
    Booking_id = models.ImageField()
    Property_id = models.IntegerField()
    User_ID = models.IntegerField()
    Booking_Status = models.BooleanField()


class Area(models.Model):
    Area_id = models.IntegerField()
    City_id = models.IntegerField()
    Area_Name = models.CharField(max_length=100)


class City(models.Model):
    City_id = models.IntegerField()
    City_Name = models.CharField(max_length=100)
