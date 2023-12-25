from django.db import models
from accounts.models import Customer, Agent 
from order.models import Order
from property.models import ADS

# Create your models here.


class Chat(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.DO_NOTHING, null=True)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.DO_NOTHING,
                                 null=True)
    chat1 = models.TextField(null=True)
    chat2 = models.TextField(null=True)
    date1 = models.DateTimeField()
    date2 = models.DateTimeField()


class Report_Agent(models.Model):
    order = models.ForeignKey(Order , on_delete=models.DO_NOTHING , null=True )
    agent = models.ForeignKey(Agent , on_delete=models.DO_NOTHING )
    report_type = models.CharField(max_length=100)
    report_text = models.CharField(max_length=100)
    report_state = models.CharField(max_length=100)


class Report_Customer(models.Model):
    ads = models.ForeignKey(ADS , on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    report_text = models.CharField(max_length=150)
    report_type = models.CharField(max_length=100)
    report_state = models.CharField(max_length=50)


class Evaluation(models.Model):
    agent = models.ForeignKey(Agent , on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Customer , on_delete=models.DO_NOTHING)
    rating = models.IntegerField()
    review = models.CharField(max_length=50)