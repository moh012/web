from django.db import models

# Create your models here.


class Chat(models.Model):
    Chat_id = models.IntegerField()
    User_ID = models.IntegerField()
    Cus_user_id = models.IntegerField()
    Chat1 = models.TextField()
    Chat2 = models.TextField()
    Date1 = models.DateTimeField()
    Date2 = models.DateTimeField()


class Order(models.Model):
    Order_id = models.IntegerField()
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


class Type(models.Model):
    Type_id = models.IntegerField()
    Type_Name = models.CharField(max_length=100)


class Report_Agent(models.Model):
    Report_Agent_id = models.IntegerField()
    Order_id = models.IntegerField()
    User_ID = models.IntegerField()
    Report_Type = models.CharField(max_length=100)
    Report_Text = models.CharField(max_length=100)
    Report_State = models.CharField(max_length=100)