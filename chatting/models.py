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
    Order_Type = models.CharField()
    State = models.CharField()
    Start_Price = models.DecimalField()
    End_Price = models.DecimalField()
    Room_Number = models.DecimalField()
    Floor = models.CharField()
    Details = models.CharField()
    Build_Year = models.CharField()
    Bathrooms = models.CharField()
    Hall_Room = models.CharField()
    Basement = models.CharField()
    Pool = models.CharField()
    Furnished = models.CharField()
    Elevator = models.CharField()
    Street_number = models.CharField()
    Appendix = models.CharField()
    Space = models.IntegerField()


class Booking(models.Model):
    Booking_id = models.ImageField()
    Property_id = models.IntegerField()
    User_ID = models.IntegerField()
    Booking_Status = models.BooleanField()


class Area(models.Model):
    Area_id = models.IntegerField()
    City_id = models.IntegerField()
    Area_Name = models.CharField()


class City(models.Model):
    City_id = models.IntegerField()
    City_Name = models.CharField()


class Property(models.Model):
    Property_id = models.IntegerField()
    Type_id = models.IntegerField()
    Area_id = models.IntegerField()
    User_ID = models.IntegerField()
    Title = models.CharField(max_length=50)
    Description = models.CharField(max_length=100)
    Features = models.CharField()
    Location = models.CharField()
    Price = models.DecimalField()


class Type(models.Model):
    Type_id = models.IntegerField()
    Type_Name = models.CharField()


class Report_Agent(models.Model):
    Report_Agent_id = models.IntegerField()
    Order_id = models.IntegerField()
    User_ID = models.IntegerField()
    Report_Type = models.CharField()
    Report_Text = models.CharField()
    Report_State = models.CharField()