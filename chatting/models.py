from django.db import models
from accounts.models import Customer, Agent

# Create your models here.


class Chat(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    chat1 = models.TextField()
    chat2 = models.TextField()
    date1 = models.DateTimeField()
    date2 = models.DateTimeField()


class Report_Agent(models.Model):
    Report_Agent_id = models.IntegerField()
    Order_id = models.IntegerField()
    User_ID = models.IntegerField()
    Report_Type = models.CharField(max_length=100)
    Report_Text = models.CharField(max_length=100)
    Report_State = models.CharField(max_length=100)


class Report_Customer(models.Model):
    Report_Customer_id = models.IntegerField()
    ADS_id = models.IntegerField()
    user_id = models.IntegerField()
    report_text = models.CharField(max_length=150)
    report_type = models.CharField(max_length=100)
    report_state = models.CharField(max_length=50)


class Evaluation(models.Model):
    evaluation_id = models.IntegerField()
    user_id = models.IntegerField()
    cus_user_id = models.IntegerField()
    rating = models.IntegerField()
    review = models.CharField(max_length=50)