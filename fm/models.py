from django.db import models


# Create your models here.
class Notification(models.Model):
    user_id = models.IntegerField()
    notification_type = models.CharField(max_length=50)
    notification_text = models.CharField(max_length=50)


class Financial_Movement(models.Model):
    
    user_id = models.IntegerField()
    use_user_id = models.IntegerField()
    discription = models.TextField()
    method = models.CharField(max_length=100)
    data_time = models.DateTimeField()
    reference = models.CharField(max_length=100)
    admin_configration = models.BooleanField()
    im_port = models.DecimalField(max_digits=5, decimal_places=2)
    export = models.DecimalField(max_digits=5, decimal_places=2)
    img = models.ImageField()