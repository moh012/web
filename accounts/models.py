from django.db import models
from django.conf import settings

# Create your models here.


#extend Agent class form User class
class Agent(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='agentPhoto/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.user.username


#extend Customer class form User class
class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='customerPhoto/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.user.username