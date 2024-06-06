
from django.contrib.auth.models import User  

from django.db import models
from django.conf import settings

from accounts.models import Agent, Customer

from django.utils import timezone
# Create your models here.
class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             null=True)
    notification_type = models.CharField(max_length=50)
    notification_text = models.CharField(max_length=50)


class Financial_Movement(models.Model):

    agent = models.ForeignKey(Agent, on_delete=models.DO_NOTHING, null=True , blank=True)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.DO_NOTHING,
                                 null=True , blank=True)
    admin_configration = models.BooleanField(null=True , blank=True, default=False)
    date_time = models.DateTimeField(default=timezone.now , blank=True)
    img = models.ImageField(upload_to='fmPhoto/%Y/%m/%d/')
    reference = models.CharField(max_length=100 , null=True , blank=True)
    
    
    # discription = models.TextField(null=True , blank=True)
    # method = models.CharField(max_length=100 , blank=True)
    # im_port = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    # export = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True )


    class Meta:
            verbose_name = "Financial Movement"
            verbose_name_plural = "Financial Movements"

    def __str__(self):
        return self.reference

