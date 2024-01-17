from django.db import models
from django.conf import settings
from accounts.models import Agent, Customer


# Create your models here.
class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             null=True)
    notification_type = models.CharField(max_length=50)
    notification_text = models.CharField(max_length=50)


class Financial_Movement(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             null=True)
    agent = models.ForeignKey(Agent, on_delete=models.DO_NOTHING, null=True)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.DO_NOTHING,
                                 null=True)
    discription = models.TextField()
    method = models.CharField(max_length=100)
    data_time = models.DateTimeField()
    reference = models.CharField(max_length=100)
    admin_configration = models.BooleanField()
    im_port = models.DecimalField(max_digits=5, decimal_places=2)
    export = models.DecimalField(max_digits=5, decimal_places=2)
    img = models.ImageField(upload_to='fmPhoto/%Y/%m/%d/')